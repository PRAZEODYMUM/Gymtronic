import json
from core import all_exercises,get_workout
#-
n=input('Чем сегодня займёмся? ')
#-
if n.lower() not in all_exercises:
    print('Неверный ввод, правильные вводы:')
    for key in all_exercises.keys():
        print(key)
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
print(get_workout(all_exercises[n.lower()],choice_int))
