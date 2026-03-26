import random
#-
def get_workout(exercises:dict,count):
    if len(exercises)<count:
        print(f'Недостаточно упражнений в конфиге, беру {len(exercises)}')
        return random.sample(sorted(exercises.values()),len(exercises))
    return random.sample(sorted(exercises.values()),count)
