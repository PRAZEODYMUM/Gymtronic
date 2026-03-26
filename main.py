from core import all_exercises,get_workout,difficulties
import random
#-
n=input('What\'s on your mind today? ').lower()
#-
if n not in all_exercises:
    print('Invalid input, valid inputs:')
    for key in all_exercises.keys():
        print(key)
    quit()
#-
diff=input('Difficulty? ').lower()
#-
if diff not in difficulties:
    raise Exception('Invalid input')
#-
choice=(input('How many exercises? '))    
#-
try:
    choice_int=int(choice)
except ValueError:
    raise Exception('Invalid input')
#-
if choice_int<=0:
    raise Exception('Invalid input')
#-
if choice_int>len(all_exercises[n]):
    raise Exception('Insuficient exercise ammount in config')      
#-
workout=get_workout(all_exercises[n],choice_int)
print(f'\nYour {n} workout ({len(workout)} exercises):')
print('-'*30)
for i,exercise in enumerate(workout,1):
    sets=random.randint(*difficulties[diff]['sets'])
    reps=random.randint(*difficulties[diff]['reps'])
    print(f' {i}.{exercise} - {sets} sets and {reps} reps')
print('-'*30)
