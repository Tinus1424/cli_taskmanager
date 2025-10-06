import json
import os


def add_task(task):
    file_path = os.path.abspath("data/current_tasks.json")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump({}, f)

    with open(file_path, "r") as f:
        tasks = json.load(f)
    
    tasks[task] = 0

    with open(file_path, "w") as f:
        json.dump(tasks, f, indent = 4) 

def list_tasks():
    file_path = os.path.abspath("data/current_tasks.json")
    if not os.path.exists(file_path):
        return "There are currently no tasks in the list" 

    with open(file_path, "r") as f:
        tasks = json.load(f)

    print(tasks)