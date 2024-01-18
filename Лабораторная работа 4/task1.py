# TODO решите задачу
import json

def task():
    with open('input.json', 'r') as file:
        data = json.load(file)
    s = 0
    for i in data:
        s += i['score']*i['weight']
    return s

print(task())
