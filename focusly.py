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
