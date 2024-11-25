# Focusly - Task and Time Management App

Focusly is a task and time management application designed to help users organize their tasks efficiently. This app connects to a MySQL database to store, retrieve, and manage tasks with features such as priority setting, due dates, task tags, and completion tracking.

---

## Features

- **Add Task**: Users can add tasks with a name, description, deadline, priority (high, medium, low), and tags.
- **List Tasks**: View tasks in various formats:
  - View all tasks, sorted by priority and deadline.
  - View incomplete tasks, sorted by priority and deadline.
  - View tasks due in the next week, sorted by priority and deadline.
  - View tasks filtered by tags.
- **Task Reminders**: Displays high-priority tasks and tasks nearing their deadline.
- **Delete Task**: Delete tasks by their name.
- **Mark Task as Complete**: Mark tasks as complete after finishing them.

---

## Prerequisites

- Python 3.x
- MySQL (or a compatible database)
- MySQL Connector for Python

---

## Installation

1. Clone the repository or copy the script.
2. Install dependencies:
   ```bash
   pip install mysql-connector-python
   ```
3. Set up the MySQL database:
   Create a database named focusly_db.
   Update the host, user, and password fields in the connect_to_db method to match your MySQL credentials.
   The app will automatically create the necessary table if it doesn't exist.

## Usage

Run the script:

```bash
python focusly.py
```

Choose from the menu options:

1. Add Task: Add a new task.
2. List Tasks: View tasks based on different filters.
3. Mark Task as Complete: Update the status of a task to completed.
4. Delete Task: Permanently delete a task.
5. View Reminders: View high-priority or urgent tasks.
6. Exit: Quit the app.

