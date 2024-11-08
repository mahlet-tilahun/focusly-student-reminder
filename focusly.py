# Task class to store task details
class Task:
    def __init__(self, name, description, deadline, priority, tags):
        self.name = name
        self.description = description
        self.deadline = deadline  # stored as a string in 'YYYY-MM-DD' format
        self.priority = priority
        self.tags = tags
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return (f"Task: {self.name}\nDescription: {self.description}\n"
                f"Deadline: {self.deadline}\nPriority: {self.priority}\n"
                f"Tags: {', '.join(self.tags)}\nStatus: {status}\n")


class FocuslyApp:
    def __init__(self):
        self.tasks = []

    # TaskInserter Functionality
    def add_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        priority = input("Enter priority (1-High, 2-Medium, 3-Low): ")
        tags = input("Enter tags (comma-separated): ").split(",")
        task = Task(name, description, deadline, priority, tags)
        self.tasks.append(task)
        print("Task added successfully!\n")


         # Reminder Mechanism (prints tasks with priority '1' or nearing deadlines)
    def reminder(self):
        print("High-Priority Tasks and Tasks Near Deadline:")
        for task in self.tasks:
            if not task.completed and task.priority == '1':
                print(task)

    # TaskDeletion Functionality
    def delete_task(self):
        self.list_tasks()
        task_name = input("Enter the name of the task to delete: ")
        self.tasks = [task for task in self.tasks if task.name != task_name]
        print(f"Task '{task_name}' deleted!\n")

    # TaskListing Display
        def list_tasks(self):
            print("All Tasks (sorted by priority and deadline):")
            sorted_tasks = sorted(self.tasks, key=lambda x: (x.priority, x.deadline))
            for task in sorted_tasks:
                print(task)

    # Tracker for Completions
    def mark_task_complete(self):
        self.list_tasks()
        task_name = input("Enter the name of the task to mark as complete: ")
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                print(f"Task '{task_name}' marked as complete!\n")
                return
        print("Task not found.\n")
