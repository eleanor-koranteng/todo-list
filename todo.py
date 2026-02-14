import os

FILENAME = "tasks.txt"
tasks = []

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                tasks.append(line.strip())

def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks()
        print("Task added.")
    else:
        print("Task cannot be empty.")

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
            save_tasks()
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid input.")

load_tasks()

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

