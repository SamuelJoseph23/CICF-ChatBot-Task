# Simple Python Command Line ChatBot Task Manager

A beginner-friendly Python chatbot that helps you **add, remove, and list tasks** via a simple menu-driven interface in the command line.

---

## Features

- **Add tasks** interactively
- **Remove tasks** by number
- **List all tasks**
- **Exit** the chatbot gracefully
- Input validation for robust task management

---

## Usage

Run the script in any Python 3 environment:
python chatbot_tasks.py


You'll see an interactive menu:
Menu:

Add Task

Remove Task

List Tasks

Exit
Enter your choice as a number:

---

## Example Interaction

Menu:

Add Task

Remove Task

List Tasks

Exit
Enter your choice as a number: 1
Enter task to add: Write report
Task 'Write report' added.

Menu:

Add Task

Remove Task

List Tasks

Exit
Enter your choice as a number: 3
Your Tasks:

Write report

Menu:

Add Task

Remove Task

List Tasks

Exit
Enter your choice as a number: 2

Write report
Enter task number to remove: 1
Task 'Write report' removed.

Menu:

Add Task

Remove Task

List Tasks

Exit
Enter your choice as a number: 4
ChatBot closed

---

## Code


tasks = []

while True:
print("\nMenu:")
print("1. Add Task")
print("2. Remove Task")
print("3. List Tasks")
print("4. Exit")
choice = input("Enter your choice as a number: ")

if choice == "1":
    task = input("Enter task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
elif choice == "2":
    if not tasks:
        print("No tasks to remove.")
        continue
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
elif choice == "3":
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
elif choice == "4":
    print("ChatBot closed")
    break
else:
    print("Invalid choice. Please try again with a valid number")



---

## Requirements

- Python 3.x

---

## License

This script is open source and free to use for educational purposes.

---

## Contributing

Pull requests, suggestions, and improvements are always welcome!

---

**Enjoy managing your tasks with this simple chatbot!**
