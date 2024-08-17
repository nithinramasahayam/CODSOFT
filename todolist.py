# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

# Function to view tasks
def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your To-Do List is empty.")

# Function to mark a task as done
def complete_task():
    view_tasks()
    task_num = int(input("Enter the number of the task you completed: "))
    if 1 <= task_num <= len(tasks):
        completed_task = tasks.pop(task_num - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
        