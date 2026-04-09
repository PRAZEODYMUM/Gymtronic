from core import WorkoutConfig,WorkoutGenerator
import os
#-
base_dir=os.path.dirname(os.path.abspath(__file__))
config=WorkoutConfig(os.path.join(base_dir,'data.json'))
generator=WorkoutGenerator(config)
#-
def prompt(question:str,valid_options:list) -> str:
    while True:
        answer=input(question).lower()
        if answer in valid_options:
            return answer
        print(f'Invalid input. Valid options: {", ".join(valid_options)}')
#-
def prompt_count(question:str,max_count:int) -> int:
    while True:
        try:
            value=int(input(question))
            if 1<=value<=max_count:
                return value
            print(f'Enter a number between 1 and {max_count}.')
        except ValueError:
            print('Invalid input, enter a number.')
#-
muscle_group=prompt('What\'s on your mind today? ',config.get_muscle_groups())
difficulty=prompt('Difficulty? ',config.get_difficulty_levels())
count=prompt_count('How many exercises? ',len(config.exercises[muscle_group]))
#-
workout=generator.generate(muscle_group,difficulty,count)
#-
print(f'\nYour {muscle_group} workout ({len(workout)} exercises):')
print('-'*30)
for i, exercise in enumerate(workout,1):
    print(f' {i}. {exercise["name"]} - {exercise["sets"]} sets and {exercise["reps"]} reps')  
print('-'*30)
