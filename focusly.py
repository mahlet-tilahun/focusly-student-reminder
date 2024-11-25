import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

# Task class to store task details
class Task:
    def __init__(self, name, description, deadline, priority, tags, completed=False):
        self.name = name
        self.description = description
        self.deadline = deadline  # stored as a string in 'YYYY-MM-DD' format
        self.priority = priority
        self.tags = tags
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return (f"Task: {self.name}\nDescription: {self.description}\n"
                f"Deadline: {self.deadline}\nPriority: {self.priority}\n"
                f"Tags: {', '.join(self.tags)}\nStatus: {status}\n")


# Focusly App class
class FocuslyApp:
    def __init__(self):
        self.tasks = []
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # Replace with your MySQL username
                password='1234',  # Replace with your MySQL password
                database='focusly_db'
            )
            if connection.is_connected():
                self.initialize_database(connection)
                print("Connected to the database successfully!\n")
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def initialize_database(self, connection):
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                deadline DATE,
                priority ENUM('1', '2', '3') NOT NULL,
                tags TEXT,
                completed BOOLEAN DEFAULT FALSE
            )
        """)
        connection.commit()

    def add_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        
        # Validate deadline input
        while True:
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            try:
                datetime.strptime(deadline, "%Y-%m-%d")  # Check if input is a valid date
                break  # Exit loop if valid
            except ValueError:
                print("Invalid date format. Please insert correct value (YYYY-MM-DD).")
        
        # Validate priority input
        while True:
            priority = input("Enter priority (1-High, 2-Medium, 3-Low): ")
            if priority in ['1', '2', '3']:
                break  # Exit loop if valid
            else:
                print("Invalid priority. Please insert correct value (1, 2, or 3).")
      
        tags_input = input("Enter tags (comma-separated): ")
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        task = Task(name, description, deadline, priority, tags)
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO tasks (name, description, deadline, priority, tags, completed)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (task.name, task.description, task.deadline, task.priority, ",".join(task.tags), task.completed))
            self.connection.commit()
            print("Task added successfully!\n")

    def list_tasks(self):
        print("Choose an option to list tasks:")
        print("1. View All Tasks")
        print("2. View Incomplete Tasks")
        print("3. View Tasks Due This Week")
        print("4. View Tasks by Tag")
        choice = input("Enter your choice: ")

        cursor = self.connection.cursor()
        if choice == '1':
            cursor.execute("SELECT name, description, deadline, priority, tags, completed FROM tasks ORDER BY priority, deadline")
            tasks = cursor.fetchall()
            print("\n{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format("ID", "Name", "Description", "Deadline", "Priority", "Status"))
            print("-" * 110)
            for idx, row in enumerate(tasks, start=1):
                tags = row[4].split(",") if row[4] else []  # Split tags into a list
                task = Task(row[0], row[1], row[2], row[3], tags, completed=row[5])
                deadline = task.deadline if isinstance(task.deadline, str) else task.deadline.strftime('%Y-%m-%d')
                print("{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format(idx, task.name, task.description, deadline, task.priority, "Completed" if task.completed else "Pending"))

        elif choice == '2':
            cursor.execute("SELECT name, description, deadline, priority, tags, completed FROM tasks WHERE completed = FALSE ORDER BY priority, deadline")
            tasks = cursor.fetchall()
            print("\n{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format("ID", "Name", "Description", "Deadline", "Priority", "Status"))
            print("-" * 110)
            for idx, row in enumerate(tasks, start=1):
                tags = row[4].split(",") if row[4] else []  # Split tags into a list
                task = Task(row[0], row[1], row[2], row[3], tags, completed=row[5])
                deadline = task.deadline if isinstance(task.deadline, str) else task.deadline.strftime('%Y-%m-%d')
                print("{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format(idx, task.name, task.description, deadline, task.priority, "Completed" if task.completed else "Pending"))

        elif choice == '3':
            today = datetime.today()
            week_later = today + timedelta(days=7)
            cursor.execute("SELECT name, description, deadline, priority, tags, completed FROM tasks WHERE completed = FALSE AND deadline BETWEEN %s AND %s ORDER BY priority, deadline", (today, week_later))
            tasks = cursor.fetchall()
            print("\n{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format("ID", "Name", "Description", "Deadline", "Priority", "Status"))
            print("-" * 110)
            for idx, row in enumerate(tasks, start=1):
                tags = row[4].split(",") if row[4] else []  # Split tags into a list
                task = Task(row[0], row[1], row[2], row[3], tags, completed=row[5])
                deadline = task.deadline if isinstance(task.deadline, str) else task.deadline.strftime('%Y-%m-%d')
                print("{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format(idx, task.name, task.description, deadline, task.priority, "Completed" if task.completed else "Pending"))

        elif choice == '4':
            tag = input("Enter the tag to filter by: ")
            cursor.execute("SELECT name, description, deadline, priority, tags, completed FROM tasks WHERE tags LIKE %s ORDER BY priority, deadline", ('%' + tag + '%',))
            tasks = cursor.fetchall()
            print("\n{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format("ID", "Name", "Description", "Deadline", "Priority", "Status"))
            print("-" * 110)
            for idx, row in enumerate(tasks, start=1):
                tags = row[4].split(",") if row[4] else []  # Split tags into a list
                task = Task(row[0], row[1], row[2], row[3], tags, completed=row[5])
                deadline = task.deadline if isinstance(task.deadline, str) else task.deadline.strftime('%Y-%m-%d')
                print("{:<5} {:<25} {:<40} {:<15} {:<10} {:<10}".format(idx, task.name, task.description, deadline, task.priority, "Completed" if task.completed else "Pending"))

        else:
            print("Invalid choice. Please try again.\n")

    def reminder(self):
        print("High-Priority Tasks and Tasks Near Deadline:")
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, description, deadline, priority, tags, completed FROM tasks WHERE completed = FALSE AND priority = '1'")
        tasks = cursor.fetchall()
        for row in tasks:
            tags = row[4].split(",") if row[4] else []  # Split tags into a list
            task = Task(row[0], row[1], row[2], row[3], tags, completed=row[5])
            print(task)

    def delete_task(self):
        task_name = input("Enter the name of the task to delete: ")
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE name = %s", (task_name,))
        self.connection.commit()
        print(f"Task '{task_name}' deleted!\n")

    def mark_task_complete(self):
        task_name = input("Enter the name of the task to mark as complete: ")
        cursor = self.connection.cursor()
        cursor.execute("UPDATE tasks SET completed = TRUE WHERE name = %s", (task_name,))
        self.connection.commit()
        print(f"Task '{task_name}' marked as complete!\n")

    def start_screen(self):
        print("Options:\n1. Add Task\n2. List Tasks\n3. Mark Task as Complete\n"
              "4. Delete Task\n5. View Reminders\n6. Exit")

    def run(self):
        print("Welcome to Focusly!")
        while True:
            self.start_screen()
            option = input("Enter your choice: ")
            if option == '1':
                self.add_task()
            elif option == '2':
                self.list_tasks()
            elif option == '3':
                self.mark_task_complete()
            elif option == '4':
                self.delete_task()
            elif option == '5':
                self.reminder()
            elif option == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


# Run the app
if __name__ == "__main__":
    app = FocuslyApp()
    app.run()

