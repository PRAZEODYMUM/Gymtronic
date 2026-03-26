from data import *
import random
def get_workout(exercices:dict,count):
    if len(exercices)<count:
        print(f'Недостаточно упражнений в конфиге, беру {len(exercices)}')
        return random.sample(sorted(exercices.values()),len(exercices))
    return random.sample(sorted(exercices.values()),count)