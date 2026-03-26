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
    raise Exception('Неверный ввод')
#-
if choice_int<=0:
    raise Exception('Неверный ввод количества')
#-
if choise_int>len(all_exercises):
    raise Exception('Недостаточно занятий в конфиге')
#-
print(get_workout(all_exercises[n.lower()],choice_int))
