#!/usr/bin/env python3
# lib/models/user.py
from models.__init__ import CONN, CURSOR

class User:
    all = {}

    def __init__(self, user_id, username, full_name):
        self._user_id = user_id
        self.username = username
        self.full_name = full_name

        if self._user_id:
            User.all[self._user_id] = self

    def __repr__(self):
        return f"<User {self.username}>"
    
    @property
    def name(self):
        return self.full_name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self.full_name = name
        else:
            raise ValueError("Name must be a string and not empty.")
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username):
            self._username = username.lower()
        else:
            raise ValueError("Username must be a string and not empty.")
    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username UNIQUE NOT NULL,
            full_name TEXT NOT NULL
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS users;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO users (username, full_name) VALUES (?, ?);"
        CURSOR.execute(sql, (self.username, self.full_name))
        CONN.commit()

        self._user_id = CURSOR.lastrowid
        User.all[self._user_id] = self

    def update(self):
        sql = "UPDATE users SET username = ?, full_name = ? WHERE user_id = ?;"
        CURSOR.execute(sql, (self.username, self.full_name, self._user_id))
        CONN.commit()
    
    def delete(self):
        sql = "DELETE FROM users WHERE user_id = ?;"
        CURSOR.execute(sql, (self._user_id,))
        CONN.commit()

        del User.all[self._user_id]

        self._user_id = None
        self._username = None
        self.full_name = None

    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            user._username = row[1]
            user.full_name = row[2]
            return user
        else:
            user = cls(row[0], row[1], row[2])
            user_id = row[0]
            cls.all[user_id] = user
            return user
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM users;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, user_id):
        sql = "SELECT * FROM users WHERE user_id = ?;"
        row = CURSOR.execute(sql, (user_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_username(cls, username):
        sql = "SELECT * FROM users WHERE username = ?;"
        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None
