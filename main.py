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
'back':get_workout(exercices_back,choice_int),
'cardio':get_workout(exercices_cardio,choice_int),
'chest':get_workout(exercices_chest,choice_int),
'core':get_workout(exercices_core,choice_int),
'legs':get_workout(exercices_legs,choice_int),
'shoulders':get_workout(exercices_shoulders,choice_int)
}
if n.lower() in choice_dict:
    print(choice_dict[n.lower()])
else:
    keys=choice_dict.keys()
    print('Неверный ввод упражнения, правильные вводы: ')
    for n in keys:
        print(n)
    quit()
