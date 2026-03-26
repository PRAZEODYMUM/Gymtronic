import json
import os
import random
#-
base_dir=os.path.dirname(os.path.abspath(__file__))
data_path=os.path.join(base_dir,'data.json')
#-
with open(data_path,'r',encoding='utf-8') as f:
    data=json.load(f)
    all_exercises={k: v for k, v in data.items() if k!='difficulties'}
    difficulties=data['difficulties']
#-
def get_workout(exercises:dict,count):
    if len(exercises)<count:
        return random.sample(list(exercises.values()),len(exercises))
    return random.sample(list(exercises.values()),count)
