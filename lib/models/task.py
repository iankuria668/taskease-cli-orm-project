#! /usr/bin/env python
# lib/models/task.py

from models.__init__ import CONN, CURSOR
class Task:
    all = {}

    def __init__(self, task_id, user_id, title, description, due_date, priority, status, category_id):
        self.task_id = task_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.category_id = category_id

        Task.all[self.task_id] = self

    def __repr__(self):
        return f"<Task {self.title}>"
    
    @property
    def task_title(self):
        return self.title
    
    @task_title.setter
    def task_title(self, title):
        if isinstance(title, str) and len(title):
            self.title = title
        else:
            raise ValueError("Title must be a string and not empty.")
    
    @property
    def task_description(self):
        return self.description
    
    @task_description.setter
    def task_description(self, description):
        if isinstance(description, str) and len(description):
            self.description = description
        else:
            raise ValueError("Description must be a string and not empty.")
    
    @classmethod
    def create_table(cls):
        """Created the task table in the database."""
        sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL,
            priority INTEGER NOT NULL,
            status INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drops the task table in the database. """
        sql = "DROP TABLE IF EXISTS tasks;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Inserts a new row with the task's information into the database."""
        sql = "INSERT INTO tasks (user_id, title, description, due_date, priority, status, category_id) VALUES (?, ?, ?, ?, ?, ?, ?);"
        CURSOR.execute(sql, (self.user_id, self.title, self.description, self.due_date, self.priority, self.status, self.category_id))
        CONN.commit()

        self.task_id = CURSOR.lastrowid
        type(self).all[self.task_id] = self

    def update(self):
        """Updates the task's information in the database."""
        sql = "UPDATE tasks SET title = ?, description = ?, due_date = ?, priority = ?, status = ?, category_id = ? WHERE task_id = ?"
        CURSOR.execute(sql, (self.title, self.description, self.due_date, self.priority, self.status, self.category_id, self.task_id))
        CONN.commit()

    def delete(self):
        """Deletes the task from the database."""
        sql = "DELETE FROM tasks WHERE task_id = ?"
        CURSOR.execute(sql, (self.task_id,))
        CONN.commit()

        self.task_id = None
        self.user_id = None
        self.title = None
        self.description = None
        self.due_date = None
        self.priority = None
        self.status = None
        self.category_id = None

    @classmethod
    def instance_from_db(cls, row):
        """Returns a task object from a database row  having the task's information."""
        task = cls.all.get(row[0])
        if task:
            task.user_id = row[1]
            task.title = row[2]
            task.description = row[3]
            task.due_date = row[4]
            task.priority = row[5]
            task.status = row[6]
            task.category_id = row[7]
            return task
        else:
            task = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            cls.all[row[0]] = task
            return task
        
    @classmethod
    def get_all(cls):
        """Returns a list of all tasks in the database."""
        sql = "SELECT * FROM tasks;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return rows
    
    @classmethod
    def find_by_id(cls, task_id):
        """Returns a task object from the database having the task's ID."""
        sql = "SELECT * FROM tasks WHERE task_id = ?;"
        row = CURSOR.execute(sql, (task_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name_and_user_id(cls, task_name, user_id):
        sql = "SELECT * FROM tasks WHERE title = ? AND user_id = ?;"
        CURSOR.execute(sql, (task_name, user_id))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_ser_id(cls, user_id):
        sql = "SELECT * FROM tasks WHERE user_id = ?;"
        CURSOR.execute(sql, (user_id,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None


    

