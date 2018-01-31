import random
import json
import os


PROJECT_ROOT = 'T:/Users/a.mondelin/python'
PROJECT_NAME = 'SportTraining'
EXERCICES_FOLDER = 'exercices'
EXERCICE_TYPE_FILE = '.json'


EXERCICES_TYPE = ['one', 'two', 'three']
EXERCICES_DONE = []
exercice_count = 0


def exercice_root(exercice_type):
    file_name = exercice_type + EXERCICE_TYPE_FILE
    exercice_path = os.path.join(PROJECT_ROOT, PROJECT_NAME, EXERCICES_FOLDER, file_name)

    if os.path.isfile(exercice_path):
        return exercice_path


def get_random_exercice(exercice_type):
    exercice_path = exercice_root(exercice_type)
    with open(exercice_path, 'r') as read_file:
        exercices_array = json.load(read_file)

        new_exercice = random.choice(exercices_array)

        while (new_exercice in EXERCICES_DONE):
            new_exercice = random.choice(exercices_array)

        EXERCICES_DONE.append(new_exercice)
        global exercice_count += 1

        return new_exercice


for trys in range(0, 2):
    print get_random_exercice('bras')

