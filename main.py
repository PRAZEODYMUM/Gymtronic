from data import *
from core import get_workout

n=input('Чем сегодня займёмся? ')
choice=(input('Сколько упражнений? '))

choice_dict={
'back':exercices_back,
'cardio':exercices_cardio,
'chest':exercices_chest,
'core':exercices_core,
'legs':exercices_legs,
'shoulders':exercices_shoulders
}

if n.lower() not in choice_dict:
    print('Неверный ввод, правильные вводы:')
    for n in choice_dict.keys():
        print(n)
    quit()

try:
    choice_int=int(choice)
except ValueError:
    print(f'Неверный ввод количества')
    quit()    

print(get_workout(choice_dict[n.lower()],choice_int))
