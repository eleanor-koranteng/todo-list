tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid input.")

while True:
    show_menu()
    choice = input("Choose an option (1–4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid choice.")

