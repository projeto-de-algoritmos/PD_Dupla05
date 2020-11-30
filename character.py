import os 
import random

def select():
    path = 'img/character/'
    files = os.listdir(path)
    random.shuffle(files)
    return files, path
#print(files)

