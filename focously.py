import json
from datetime import datetime


# List to store tasks (will store each task as a dictionary)
tasks = []

# Function to add a new task
def add_task():
    print("\n--- Add New Task ---")
    task_name = input("Enter task name: ")
    description = input("Enter task description: ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    priority = input("Enter task priority (High, Medium, Low): ")
    
    # Store the task as a dictionary and append to tasks list
    task = {
        "task_name": task_name,
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    print(f"Task '{task_name}' added successfully!")

# Function to view all taks
def view_tasks():
    print("\n--- Task List ---")
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task_name']} - Due: {task['deadline']} - Priority: {task['priority']}")

# Function to delete a task
def delete_task():
    print("\n--- Delete Task ---")
    task_name = input("Enter task name to delete: ")
    global tasks
    tasks = [task for task in tasks if task['task_name'] != task_name]
    print(f"Task '{task_name}' deleted successfully!")

# Main function with menu loop
def main():
    while True:
        print("\n--- Focously ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting Focously. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

