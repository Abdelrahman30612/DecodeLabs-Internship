def display_menu():
    print("\n" + "="*30)
    print("      DECODELABS TO-DO ENGINE      ")
    print("="*30)
    print("1. Add a New Task ➕")
    print("2. View All Tasks 📋")
    print("3. Exit Program 🚪")
    print("="*30)

def view_tasks_ui(tasks):
    if not tasks:
        print("\n⚠️ Your to-do list is empty.")
        return
    print("\n📋 CURRENT TASKS IN MEMORY:")
    print("-" * 35)
    for index, task_item in enumerate(tasks, start=1):
        print(f"[{index}] ID: {task_item['id']} | Task: {task_item['task']}")
    print("-" * 35)