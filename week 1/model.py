import json
import os

DB_FILE = "todo_database.json"

def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def add_task(tasks, task_name):
    next_id = max([task["id"] for task in tasks], default=0) + 1
    new_task = {"id": next_id, "task": task_name}
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task 
.
