from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input

from task_manager import load_tasks


class HelloWorld(App):
    """A professional terminal app."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("r", "refresh", "Refresh tasks"),
        ("a", "add_task", "Add task"),
        ("x", "delete_task", "Delete task by number"),
    ]

    def compose(self) -> ComposeResult:
        

        yield Header()
        self.task_display = Static()
        yield self.task_display
        yield Footer()
    
    def update_header(self, tasks: list) -> None:
        task_count = len(tasks)
        self.title = f"{task_count} task's Found" if task_count else f"NO Task Found"  
        self.sub_title = f"You Have {task_count} tasks." if task_count else "Add tasks to start."
        
    
    def on_mount(self) -> None:
        self.refresh_tasks()

    def refresh_tasks(self) -> None:
        tasks = load_tasks()

        self.update_header(tasks)

        if not tasks:
            text = "No tasks found."
        else:
            text = "\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks))
        
        self.task_display.update(text)
    

    def action_refresh(self) -> None:
        self.refresh_tasks()

    
    def action_add_task(self) -> None:
        self.task_input = Input(
            placeholder = "Type a task and press Enter...",
            id="task_input"
        )
        self.mount(self.task_input)
        self.task_input.focus()

    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    
    def action_delete_task(self) -> None:
        """ Delete An Task """
        tasks = load_tasks()

        if not tasks:
            self.task_display.update("⚠️ No tasks to delete.")
            return

        self.delete_input = Input(
            placeholder="Enter task number to delete and press Enter...",
            id="delete_input"
        )
        self.mount(self.delete_input)
        self.delete_input.focus()
    
    def handle_delete_by_number(self, value: str, input_widget: Input) -> None:
        tasks = load_tasks()

        if not value.isdigit():
            self.task_display.update("⚠️ Please enter a valid number.")
            input_widget.remove()
            return

        index = int(value) - 1

        if index < 0 or index >= len(tasks):
            self.task_display.update("⚠️ Task number out of range.")
            input_widget.remove()
            return

        deleted_task = tasks.pop(index)

        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

        input_widget.remove()
        self.task_display.update(f"🗑️ Deleted: {deleted_task}")
        self.refresh_tasks()


    def on_input_submitted(self, event: Input.Submitted) -> None:
        task_text = event.value.strip()

        if hasattr(self, "delete_input") and event.input.id == "delete_input":
            self.handle_delete_by_number(task_text, event.input)
            return

        if not task_text:
            self.task_display.update("⚠️ Task cannot be empty. Press \"r\" to Load Context.")
            event.input.remove()
            return
        
        tasks = load_tasks()
        tasks.append(task_text)

        # save tasks
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        
        event.input.remove()
        self.refresh_tasks()
    
    def on_key(self, event) -> None:
        if event.key == "escape" and hasattr(self, "task_input"):
            self.task_input.remove()
            del self.task_input
            self.task_display.update("⚠️ Task input cancelled. Press \"r\" to Load Context.")




    

if __name__ == "__main__":
    app = HelloWorld()
    app.run()