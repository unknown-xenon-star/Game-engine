import json
from typing import List, Dict










# tasks.append({"task": "Do this thing tommorw", "due":  "2025-12-31"})
# Json_writer(Dict_to_Json(tasks))


class JsonManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
    
    def load_Json(self) -> List[Dict]:
        """"
        Loads tasks from a JSON file and returns them as a list of dictionaries.
        If the file doesn't exist, an empty list is returned.
        """
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            return []   # Return an empty list if the file doesn't exist
    

    def save_Json(self, tasks: List[Dict]) -> None:
        """
        Saves a list of tasks (as dictionaries) to a JSON file.
        """
        with open(self.file_name, "w") as file:
            json.dump({"tasks": tasks}, file, indent=4)
        print(f"Data saved to {self.file_name}")
    
    def add_task(self, task: Dict) -> None:
        """
        Docstring for add_task
        
        :param self: Description
        :param task: Description
        :type task: Dict
        """
        tasks = self.load_Json()
        tasks.append(task)
        self.save_Json(tasks)
    
    def remove_task(self, task_id: int) -> None:
        """
        Docstring for remove_task
        
        :param self: Description
        :param task_id: Description
        :type task_id: int
        """
        tasks =self.load_Json()
        tasks = [task for task in tasks if task["id"]!=task_id]
        self.save_Json(tasks)

    def get_task_by_id(self, task_id: int) -> Dict:
        """
        Docstring for get_task_by_id
        
        :param self: Description
        :param task_id: Description
        :type task_id: int
        :return: Description
        :rtype: Dict
        """
        tasks = json_to_dict(self.load_Json())
        for task in tasks:
            if task["id"] == task_id:
                return task
        return None



def dict_to_json(data: dict) -> str:
    """
    Converts a dictionary to a formatted JSON string.
    """
    return json.dumps(data, indent=4)

def json_to_dict(json_str: str) -> dict:
    """
    Converts a JSON string into a dictionary.
    """
    return json.loads(json_str)


if __name__ == "__main__":
    task_manager = JsonManager("todo.json")
    # Add a task
    new_task = [{
        "id": 4,
        "title": "Read book",
        "description": "Finish reading the Python book",
        "completed": False,
        "due_date": "2026-01-10"
    }]
    task_manager.add_task(new_task)

    # View all tasks
    tasks = task_manager.load_Json()
    print("All tasks:", tasks)

    # Get a specific task by ID
    task = task_manager.get_task_by_id(4)
    print("Task with ID 4:", task)

    # Remove a task by ID
    task_manager.remove_task(4)