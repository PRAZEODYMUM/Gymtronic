from core import all_exercises,get_workout
#-
n=input('What\'s ond your mind today? ')
#-
if n.lower() not in all_exercises:
    print('Invalid input, valid inputs:')
    for key in all_exercises.keys():
        print(key)
    quit()
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
print(get_workout(all_exercises[n.lower()],choice_int))
