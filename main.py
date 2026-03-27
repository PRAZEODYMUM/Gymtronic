from core import all_exercises,get_workout,difficulties
import random
#-
while True:
    n=input('What\'s on your mind today? ').lower()
    if n not in all_exercises:
        print('Invalid input, valid inputs:')
        for key in all_exercises.keys():
            print(key)
        continue
    else:
        break
#-
while True:
    diff=input('Difficulty? ').lower()
    if diff not in difficulties:
        print('Invalid input, valid inputs: ')
        for key in difficulties:
            print(key)
        continue
    else:
        break
#-
while True:
    choice=(input('How many exercises? '))
    try:
        choice_int=int(choice)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if choice_int<=0:
            print('Invalid input')
            continue
        if choice_int>len(all_exercises[n]):
            print('Insuficient exercise ammount in the config')
            continue
        else:
            break      
#-
workout=get_workout(all_exercises[n],choice_int)
print(f'\nYour {n} workout ({len(workout)} exercises):')
print('-'*30)
for i,exercise in enumerate(workout,1):
    sets=random.randint(*difficulties[diff]['sets'])
    reps=random.randint(*difficulties[diff]['reps'])
    print(f' {i}.{exercise} - {sets} sets and {reps} reps')
print('-'*30)
