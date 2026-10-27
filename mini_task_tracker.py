# Mini Task Tracker
# Menu-based task manager that saves tasks in tasks.json

import json

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json. Return an empty list if file is missing."""
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved file found. Starting with an empty task list.")
        return []
    except json.JSONDecodeError:
        print("Saved file is damaged. Starting with an empty task list.")
        return []


def save_tasks(tasks):
    """Save the task list to tasks.json."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Ask for a title and add it as a Pending task."""
    title = input("Task title: ").strip()
    if title == "":
        print("Title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Show a numbered list of tasks with Pending or Done."""
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def ask_task_number(tasks):
    """Ask for a task number. Return its list index, or None if invalid."""
    if len(tasks) == 0:
        print("No tasks available.")
        return None
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Please enter a valid number.")
        return None
    if number < 1 or number > len(tasks):
        print("Task number does not exist.")
        return None
    return number - 1


def complete_task(tasks):
    """Mark the selected task as done."""
    index = ask_task_number(tasks)
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Remove the selected task."""
    index = ask_task_number(tasks)
    if index is None:
        return
    tasks.pop(index)
    save_tasks(tasks)
    print("Task deleted.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add 2. View 3. Complete 4. Delete 5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


main()
