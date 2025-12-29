import os
from json_handler import Json_reader
from json_handler import Json_writer

FILE_NAME = "tasks.txt"

def load_tasks():
    """
    Load tasks from a file if it exists. Returns an empty list if the file doesn't exist.
    """
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as F:
            return [line.strip() for line in F.readlines()]
    return []

def get_task(tasks, task_num):
    """
    Return a task by its number without modifying the list.
    """
    try:
        return tasks[task_num - 1]
    except IndexError:
        return None

def save_tasks(tasks):
    """
    Save the list of tasks to a file.
    """
    with open(FILE_NAME, "w") as F:
        for task in tasks:
            F.write(task + "\n")

def add_task(tasks, task_description):
    """
    Add a new task to the task list.
    """
    tasks.append(task_description)
    save_tasks(tasks)
    print("Task added!")


def remove_task(tasks, task_num):
    """
    Remove a task from the list by its number.
    """
    try:
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid number.")


def load_json_tasks():
    """
    Call Json_reader from json_handler
    """
    return Json_reader(FILE_NAME)



def write_json_tasks(Data):
    """
    Call Json_writer form json_handler
    """
    Json_writer(Data, FILE_NAME)