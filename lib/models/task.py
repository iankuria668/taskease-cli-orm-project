#!/usr/bin/env python3
# lib/models/task.py
from models.__init__ import CONN, CURSOR

class Task:
    all = {}

    def __init__(self, task_id, user_id, task_name, task_description, task_due_date, task_priority, task_status, category_id):
        self._task_id = task_id
        self._user_id = user_id
        self.task_name = task_name
        self.task_description = task_description
        self.task_due_date = task_due_date
        self.task_priority = task_priority
        self.task_status = task_status
        self._category_id = category_id

        if self._task_id:
            Task.all[self._task_id] = self

    def __repr__(self):
        return f"<Task {self.task_name}>"

    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        if isinstance(task_name, str) and len(task_name):
            self._task_name = task_name
        else:
            raise ValueError("Task name must be a string and not empty.")

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task_name TEXT NOT NULL,
            task_description TEXT,
            task_due_date TEXT,
            task_priority TEXT,
            task_status TEXT,
            category_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(category_id) REFERENCES categories(category_id)
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS tasks;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO tasks (user_id, task_name, task_description, task_due_date, task_priority, task_status, category_id)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self._user_id, self.task_name, self.task_description, self.task_due_date, self.task_priority, self.task_status, self._category_id))
        CONN.commit()

        self._task_id = CURSOR.lastrowid
        Task.all[self._task_id] = self

    def update(self):
        sql = """
        UPDATE tasks SET user_id = ?, task_name = ?, task_description = ?, task_due_date = ?, task_priority = ?, task_status = ?, category_id = ?
        WHERE task_id = ?;
        """
        CURSOR.execute(sql, (self._user_id, self.task_name, self.task_description, self.task_due_date, self.task_priority, self.task_status, self._category_id, self._task_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM tasks WHERE task_id = ?;"
        CURSOR.execute(sql, (self._task_id,))
        CONN.commit()

        del Task.all[self._task_id]

        self._task_id = None
        self._user_id = None
        self._category_id = None
        self._task_name = None
        self._task_description = None
        self._task_due_date = None
        self._task_priority = None
        self._task_status = None

    @classmethod
    def instance_from_db(cls, row):
        task = cls.all.get(row[0])
        if task:
            task._user_id = row[1]
            task._task_name = row[2]
            task._task_description = row[3]
            task._task_due_date = row[4]
            task._task_priority = row[5]
            task._task_status = row[6]
            task._category_id = row[7]
            return task
        else:
            task = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            task_id = row[0]
            cls.all[task_id] = task
            return task

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM tasks;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, task_id):
        sql = "SELECT * FROM tasks WHERE task_id = ?;"
        row = CURSOR.execute(sql, (task_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_user_id(cls, user_id):
        sql = "SELECT * FROM tasks WHERE user_id = ?;"
        CURSOR.execute(sql, (user_id,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name_and_user_id(cls, task_name, user_id):
        """Returns a task object from the database having the given name and user ID."""
        sql = "SELECT * FROM tasks WHERE task_name = ? AND user_id = ?;"
        CURSOR.execute(sql, (task_name, user_id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
    
    @staticmethod
    def find_by_username_and_category(username, category_id):
        sql = """
            SELECT * FROM tasks 
            WHERE user_id = (SELECT user_id FROM users WHERE username = ?)
            AND category_id = ?;
        """
        CURSOR.execute(sql, (username, category_id))
        rows = CURSOR.fetchall()
        tasks = []
        for row in rows:
            task = Task(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
            )  # Assuming Task constructor order matches the SQL query result
            tasks.append(task)
        return tasks