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
