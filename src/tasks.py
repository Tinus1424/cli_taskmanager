import json
import os


def add_task(task, verbose):
    if not os.path.exists("data"):
        os.mkdir("data")

    file_path = os.path.abspath("data/current_tasks.json")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump({}, f)

    with open(file_path, "r") as f:
        tasks = json.load(f)
        
    tasks[task] = "started"

    
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent = 4) 

    if verbose:
        print(f"Succesfully added '{task}'(status: started) to the task list!")

def list_tasks(verbose):
    file_path = os.path.abspath("data/current_tasks.json")
    if not os.path.exists(file_path):
        if verbose:
            return "There are currently no tasks in the list" 
        else:
            return

    with open(file_path, "r") as f:
        tasks = json.load(f)

    for k, v in tasks.items():
        print(f"Task: {k}, status: {v}")

def remove_task(task, verbose):
    file_path = os.path.abspath("data/current_tasks.json")
    if not os.path.exists(file_path):
        return "There are currently no tasks in the list"

    with open(file_path, "r") as f:
        tasks = json.load(f)

    del tasks[task]

    with open(file_path, "w") as f:
        json.dump(tasks, f, indent = 4)

    if verbose:
        print(f"Succesfully removed {task} from the task list!")

def update_status(task, status, verbose):
    file_path = os.path.abspath("data/current_tasks.json")
    if not os.path.exists(file_path):
        return "There are currently no tasks in the list"

    with open(file_path, "r") as f:
        tasks = json.load(f)

    old_status = tasks.get(task)
    tasks[task] = status

    with open(file_path, "w") as f:
        json.dump(tasks, f, indent = 4)

    if verbose: 
        print(f"Succesfully updated the status of {task} from {old_status} to {tasks.get(task)}")