print("ToDo List Menu:" \
    "\n1. View Tasks" \
    "\n2. Add Task" \
    "\n3. Remove Task" \
    "\n4. Exit")

tasks = []

while True:
    choice = input("Choose an option (1-4): ")

    match choice:
        case "1":
            if not tasks:
                print("No tasks available.")
            else:
                print("Tasks:")
                for id , task in enumerate(tasks, start=1):
                    print(f"{id}. {task}")
        case "2":
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"{task} added.")
        case "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                print("Tasks:")
                for id , task in enumerate(tasks, start=1):
                    print(f"{id}. {task}")
                try:
                    task_id = int(input("Enter the task number to remove: "))
                    if 1 <= task_id <= len(tasks):
                        removed_task = tasks.pop(task_id -1)
                        print(f"{removed_task} removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        case "4":
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please choose a valid option.")

