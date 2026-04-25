import os
import customtkinter as ctk
from core import WorkoutConfig, WorkoutGenerator

# Nastavenie vzhľadu
ctk.set_appearance_mode("System")  # Režim podľa systému (Dark/Light)
ctk.set_default_color_theme("blue")  # Farebná téma

class GymtronicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Nastavenie hlavného okna
        self.title("Gymtronic - Workout Generator")
        self.geometry("500x650")
        self.minsize(400, 600)

        # Načítanie tvojej core logiky
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_dir, 'data.json')
        self.config = WorkoutConfig(data_path)
        self.generator = WorkoutGenerator(self.config)

        # Vytvorenie UI prvkov
        self.create_widgets()

    def create_widgets(self):
        # Nadpis
        self.title_label = ctk.CTkLabel(self, text="Gymtronic", font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.pack(pady=(30, 20))

        # Výber svalovej partie
        self.muscle_label = ctk.CTkLabel(self, text="Svalová partia:", font=ctk.CTkFont(size=14))
        self.muscle_label.pack(pady=(10, 0))
        
        self.muscle_var = ctk.StringVar(value=self.config.get_muscle_groups()[0])
        self.muscle_dropdown = ctk.CTkOptionMenu(
            self, 
            variable=self.muscle_var, 
            values=self.config.get_muscle_groups(),
            command=self.update_count_slider # Pri zmene partie upravíme maximum cvikov
        )
        self.muscle_dropdown.pack(pady=(5, 10))

        # Výber náročnosti
        self.diff_label = ctk.CTkLabel(self, text="Náročnosť:", font=ctk.CTkFont(size=14))
        self.diff_label.pack(pady=(10, 0))
        
        self.diff_var = ctk.StringVar(value=self.config.get_difficulty_levels()[0])
        self.diff_dropdown = ctk.CTkOptionMenu(
            self, 
            variable=self.diff_var, 
            values=self.config.get_difficulty_levels()
        )
        self.diff_dropdown.pack(pady=(5, 10))

        # Posuvník pre počet cvikov
        self.count_label = ctk.CTkLabel(self, text="Počet cvikov: 1", font=ctk.CTkFont(size=14))
        self.count_label.pack(pady=(10, 0))
        
        self.count_slider = ctk.CTkSlider(
            self, 
            from_=1, 
            to=10, # Bude sa dynamicky meniť
            command=self.slider_event
        )
        self.count_slider.set(1)
        self.count_slider.pack(pady=(5, 20))
        
        # Inicializácia správnej hodnoty slidera podľa prvej vybranej partie
        self.update_count_slider(self.muscle_var.get())

        # Tlačidlo na generovanie
        self.generate_btn = ctk.CTkButton(
            self, 
            text="Vygenerovať tréning", 
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            command=self.generate_workout
        )
        self.generate_btn.pack(pady=(10, 20))

        # Textové pole pre zobrazenie výsledku
        self.result_textbox = ctk.CTkTextbox(self, width=400, height=200, font=ctk.CTkFont(size=14))
        self.result_textbox.pack(pady=(0, 20), padx=20, fill="both", expand=True)

    def slider_event(self, value):
        # Aktualizuje text nad sliderom počas posúvania
        self.count_label.configure(text=f"Počet cvikov: {int(value)}")

    def update_count_slider(self, muscle_group):
        # Nastaví maximálnu hodnotu slidera podľa počtu cvikov v danej kategórii v data.json
        max_exercises = len(self.config.exercises[muscle_group])
        self.count_slider.configure(to=max_exercises, number_of_steps=max_exercises-1)
        
        # Ak je aktuálna hodnota vyššia ako nové maximum, znížime ju
        if self.count_slider.get() > max_exercises:
            self.count_slider.set(max_exercises)
            self.slider_event(max_exercises)

    def generate_workout(self):
        # Získanie hodnôt z UI
        muscle = self.muscle_var.get()
        diff = self.diff_var.get()
        count = int(self.count_slider.get())

        # Vygenerovanie tréningu cez tvoju triedu WorkoutGenerator
        workout = self.generator.generate(muscle, diff, count)

        # Vymazanie starého textu vo výstupe
        self.result_textbox.delete("1.0", "end")
        
        # Vypísanie nového tréningu
        self.result_textbox.insert("end", f"Tvoj '{muscle}' tréning ({len(workout)} cvikov):\n")
        self.result_textbox.insert("end", "-" * 40 + "\n\n")
        
        for i, exercise in enumerate(workout, 1):
            self.result_textbox.insert("end", f"{i}. {exercise['name']}\n")
            self.result_textbox.insert("end", f"   Série: {exercise['sets']} | Opakovania: {exercise['reps']}\n\n")

if __name__ == "__main__":
    app = GymtronicApp()
    app.mainloop()
