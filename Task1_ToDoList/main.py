# CodSoft Internship Task 1
# To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully.")

def remove_task():
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num-1)
        print("Removed:", removed)
    except:
        print("Invalid task number.")

while True:

    print("\n===== TO DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        break

    else:
        print("Invalid choice")
