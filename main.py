from data import *
from core import get_workout
n=input('Чем сегодня займёмся? ')
choice=(input('Сколько упражнений? '))
try:
    choice_int=int(choice)
except ValueError:
    print(f'Неверный ввод количества')
    quit()
choice_dict={
'back':get_workout(exercices_back,int(choice)),
'cardio':get_workout(exercices_cardio,int(choice)),
'chest':get_workout(exercices_chest,int(choice)),
'core':get_workout(exercices_core,int(choice)),
'legs':get_workout(exercices_legs,int(choice)),
'shoulders':get_workout(exercices_shoulders,int(choice))
}
if n.lower() in choice_dict:
    print(choice_dict[n.lower()])
else:
    keys=choice_dict.keys()
    print('Неверный ввод упражнения, правильные вводы: ')
    for n in keys:
        print(n)
    quit()