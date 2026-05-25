from model import load_tasks, add_task
from view import display_menu, view_tasks_ui

def main():
    my_tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            task_name = input("\nEnter the task description: ").strip()
            if task_name:
                created_task = add_task(my_tasks, task_name)
                print(f"✅ Task added with Database ID: {created_task['id']}")
            else:
                print("❌ Task description cannot be empty!")
        elif choice == "2":
            view_tasks_ui(my_tasks)
        elif choice == "3":
            print("\nShutting down backend engine. Goodbye!")
            break
        else:
            print("❌ Invalid selection.")

if __name__ == "__main__":
    main()