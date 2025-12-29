import json

# Define the to-do data as a Python dictionary
todo_data = {
    "todos": [
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread, butter",
            "completed": False,
            "due_date": "2025-12-30"
        },
        {
            "id": 2,
            "title": "Complete homework",
            "description": "Finish math exercises and history essay",
            "completed": True,
            "due_date": "2025-12-29"
        },
        {
            "id": 3,
            "title": "Clean the room",
            "description": "Vacuum, dust shelves, organize books",
            "completed": False,
            "due_date": "2025-12-31"
        }
    ]
}

tasks = [
    {"task": "Finish homework", "due": "2025-12-30"},
    {"task": "Buy groceries", "due": "2025-12-28"},
]

def Dict_to_Json(Dict_Data: dict, indentation=4) -> str:
    """
    Converts a dictionary to a JSON string with specified indentation.

    Parameters:
    Dict_Data (dict): The dictionary to convert.
    indentation (int): Number of spaces for indentation (default is 4).

    Returns:
    str: A formatted JSON string.
    """
    return json.dumps(Dict_Data, indent=indentation)


def Json_reader(file_name="notes.txt") -> str:
    """
    Reads the contents of a JSON file and returns it as a string.

    :param file_name: The name of the file to read (default is "notes.txt").
    :return: The content of the file as a string.
    :rtype: str
    """
    try:
        with open(file_name, "r") as file:
            return file.load()
    except FileNotFoundError:
        return []



def Json_writer(data_to_write: str, file_name="notes.txt"):
    """
    Writes data to a specified text file.

    Parameters:
    data_to_write (str): Data to write into the file.
    file_name (str): The file name (default is "notes.txt").
    """
    with open(file_name, "w") as file:
        file.write(data_to_write)
    print(f"Data saved to {file_name}")


tasks.append({"task": "Do this thing tommorw", "due":  "2025-12-31"})
Json_writer(Dict_to_Json(tasks))