
import sys
from task_manager import load_tasks, save_tasks, add_task, remove_task

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- SIMPLE TASK MANAGER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("List is empty.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")

        elif choice == '2':
            new_task = input("Enter the task description: ")
            add_task(tasks, new_task)

        elif choice == '3':
            if not tasks:
                print("Nothing to delete.")
                continue
            
            else:
                try:
                    task_num = int(input("Enter task number to remove: "))
                except ValueError:
                    print("Please Enter a Valis Number.")
                    continue

                if task_num < 1 or task_num > len(tasks):
                    print("Task Number out of range.")
                    continue
                
                task_to_delete = tasks[task_num -1]
                confirm = input(f"Delete task '{task_to_delete}'? (y/n): ").lower()
                
                if confirm != 'y':
                    print("Deletion Cancelled.")
                    continue
                
                remove_task(tasks, task_num)
                
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()