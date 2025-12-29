import json
from typing import List, Dict

JSON_FILE_NAME = "todo.json" 

class Tasks:
    id: int
    task: str
    due: str
    mark: bool
    # def __init__(self, id, task, due, mark):
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], dict):
            self.tasks = [args[0]]

        elif len(args) == 4:
            self.tasks = [{
                "id": args[0],
                "task": args[1],
                "due": args[2],
                "mark": args[3]
            }]

        elif kwargs:
            self.tasks = [kwargs]

        else:
            raise ValueError("Invalid arguments")
    
    def add_dict_task(self, data):
        if len(data)==4:
            self.tasks.append(data)
        else:
            raise ValueError("Invalid arguments")
    
    def remove_task(self, id: int):
        for i, data in enumerate(self.tasks):
            if data["id"] == id:
                self.tasks.pop(i)
                break

    def get_tasks(self):
        return self.tasks
    

class JsonManager:
    def __init__(self, file_name=JSON_FILE_NAME):
        self.file_name = file_name
    
    def Load_Json(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []
    
    def Save_Json(self, Data):
        try:
            with open(self.file_name, "w") as file:
                json.dump(Data, file, indent=4)
                print(f"Data Saved to {self.file_name}")
        except Exception as e:
            print(e)

con = {
        "id": 12456,
        "task": "Nesw task",
        "due": "27-12-2025",
        "mark": "False"
    }
if __name__ == "__main__":
    manager = JsonManager()
    context = manager.Load_Json()

    # print(type(context), "\n"+f"{context}")
    
    # print(context[0])
    tasks = Tasks(**context[0])
    tasks.add_dict_task(con)
    manager.Save_Json(tasks.get_tasks())
    print(tasks.get_tasks())
    # print("WRITING NEW CONTEXT")
    # manager.Save_Json(con)
    # context = manager.Load_Json()
    # print(type(context), "\n"+f"{context}")
    