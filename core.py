import json
import os
import random
#-
base_dir=os.path.dirname(os.path.abspath(__file__))
data_path=os.path.join(base_dir,'data.json')
#-
class WorkoutConfig:
    def __init__(self,data_path:str):
        with open(data_path,'r',encoding='utf-8') as f:
            data=json.load(f)
        self.exercises:dict={k: v for k, v in data.items() if k!='difficulties'}
        self.difficulties:dict=data['difficulties']
#-
    def get_muscle_groups(self) -> list:
        return list(self.exercises.keys())
#-
    def get_difficulty_levels(self):
        return list(self.difficulties.keys())
#-
class WorkoutGenerator:
    def __init__(self,config:WorkoutConfig):
        self.config=config
    def generate(self,muscle_group:str,difficulty:str,count:int) -> list[dict]:
        exercises=self.config.exercises[muscle_group]
        diff_settings=self.config.difficulties[difficulty]
        pool=list(exercises.values())
        selected=random.sample(pool,min(count,len(pool)))
        return[
            {
                'name':exercise,
                'sets':random.randint(*diff_settings['sets']),
                'reps':random.randint(*diff_settings['reps']),
            }
            for exercise in selected
        ]