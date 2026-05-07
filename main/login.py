import sys

FILENAME = "tasks.txt"

class Login:
    def __init__(self, file_name=FILENAME, key=None):
        if not None:
            print("Extracting Data Record..")
            self.extract(file_name, key)
            self.run_mode(1)
            # sys.exit()
    def run_mode(mode_num=1):
        if mode_num==1:
            # sys run python todo_cli.py
            print("Starting CLI")
        elif mode_num ==2:
            # sys run python todo_tui.py
            print("Starting TUI")
        else:
            raise ValueError("NOT VALID")
    def extract(self, file_name, key):
        # extract encrypted data:
        pass

class Logout:
    def __init__(self, file_name=FILENAME, data="", key=None):
        if not None:
            print("Extracting Data Record..")
            self.encrpyt(file_name, data, key)
            # sys.exit()
    def encrpyt(self, file_name, key):
        # encrypt data:
        pass