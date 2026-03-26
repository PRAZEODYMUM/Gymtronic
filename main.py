from data import *
from core import get_workout
#-
n=input('Чем сегодня займёмся? ')
#-
choice_dict={
'back':exercises_back,
'cardio':exercises_cardio,
'chest':exercises_chest,
'core':exercises_core,
'legs':exercises_legs,
'shoulders':exercises_shoulders
}
#-
if n.lower() not in choice_dict:
    print('Неверный ввод, правильные вводы:')
    for n in choice_dict.keys():
        print(n)
    quit()
#-
choice=(input('Сколько упражнений? '))
#-
try:
    choice_int=int(choice)
except ValueError:
    print(f'Неверный ввод количества')
    quit()
#-
if choice_int<=0:
    print('Неверный ввод количества')
    quit()
#-
print(get_workout(choice_dict[n.lower()],choice_int))
