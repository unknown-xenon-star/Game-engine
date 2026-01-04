import json
from typing import List, Dict

JSON_FILE_NAME = "todo.json" 

# For Future devlopment DATATYPE = DATACLASS Tasks
class Task:
    id: int
    task: str
    due: str
    mark: bool
    
    # def __init__(self, id, task, due, mark):
    # function(a,b,c) = args = (a,b,c)
    # args -> tuple
    # function(A=a,B=b,C=c) = kwargs = {A:a,B:b,C:c}
    # kwargs -> dict
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], dict):
            self.task = list(args[0])
        elif len(args) == 4:
            self.task = {
                "id": args[0],
                "task": args[1],
                "due": args[2],
                "mark": args[3]
            }
        elif len(kwargs)==4:
            self.task = kwargs
        else:
            raise ValueError("Invalid arguments")

    def __repr__(self):

        return f"{self.task!r}"
    
    def __getitem__(self, key):
        return self.task[key]
    
    def __setitem__(self, key, value):
        self.task[key] = value
    
    def keys(self):
        return self.task.keys()

    def items(self):
        return self.task.items()

    def values(self):
        return self.task.values()

    def get_task(self) -> Dict[str, str]:
        return self.task
    
    def To_Dict(self) -> Dict[str, str]:
        return self.task
# Task Data in Json
class JsonData:
    def __init__(self, *args):
        if args:
            if len(args)==1 and isinstance(args, (list, tuple)):
                self.tasks = args[0]
            else:
                raise TypeError("Exaclty One *args Nedded")
        else:
            self.tasks = []
    def append(self,task: Task):
        self.tasks.append(task)
    def get_tasks(self, index=None):
        if index is not None:
            if index<=len(self.tasks) and index>=1:
                return self.tasks[index-1]
            else:
                raise IndexError("Index out of range. should be >0 and <len(tasks)")
        return self.tasks
    def remove_task(self, id: int):
        for i, data in enumerate(self.tasks):
            if data["id"] == id:
                self.tasks.pop(i)
                break
    

    def add_list_task(self, data):
        if len(data) == 4:
            self.tasks.append(Task({
                "id": data[0],
                "task": data[1],
                "due": data[2],
                "mark": data[3]
            }))
    def add_task(self, data: Task):
        if not isinstance(data, Task):
            raise TypeError(f"Expected a Task object, got {type(data).__name__}")
        self.tasks.append(data)
    
    def add_dict_task(self, data):
        if len(data)==4:
            self.tasks.append(Task(data))
        else:
            raise ValueError("Invalid arguments")

class JsonManager:
    """
    # MANAGER = help manage Json
    """
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
            if any(isinstance(obj, Task) for obj in Data):
                Data = [task.To_Dict() for task in Data]
            with open(self.file_name, "w") as file:
                json.dump(Data, file, indent=4)
                print(f"Data Saved to {self.file_name}")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    con = {
            "id": 12456,
            "task": "Nesw task",
            "due": "27-12-2025",
            "mark": "False"
        }

    con1 = {
            "id": 12456,
            "task": "Nesw task",
            "due": "27-12-2025",
            "mark": "False"
        }
    manager = JsonManager()
    context = manager.Load_Json()
    print(type(context, "\n", context))
