# To-Do List Program

# List to store tasks
tasks = []

while True:
    # Display menu
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add task
    if choice == "1":
        user_task = input("Enter the task you want to add: ")
        tasks.append(user_task)
        print(f"Task '{user_task}' added successfully!")

    # View tasks
    elif choice == "2":
        if not tasks:  # Check if the list is empty
            print("No task in the list.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Delete task
    elif choice == "3":
        if not tasks:
            print("No task in the list.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = input("Enter the number of the task you want to delete: ")

            if task_num.isdigit():  # Ensure input is a number
                task_num = int(task_num)
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    # Exit program
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
