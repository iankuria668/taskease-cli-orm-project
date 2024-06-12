#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
class User:
    # Users are stored in a dictionary with the user's ID as the key.
    all = []

    def __init__(self, user_id, username, full_name):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name

        User.all[self.user_id] = self

    def __repr__(self):
        return f"<User {self.username}>"
    
    @property
    def name(self):
        return self.full_name
    
    @name.setter
    def name(self, name):
        # Input validation
        if isinstance(name, str) and len(name):
            self.full_name = name
        else:
            raise ValueError("Name must be a string and not empty.")
        
    @property
    def username(self):
        return self.username
    
    @username.setter
    def username(self, username):
        #  Input validation
        if isinstance(username, str) and len(username):
            # Changing username to lowercase
            self.username = username.lower()
        else:
            raise ValueError("Username must be a string and not empty.")
    
    @classmethod
    def create_table(cls):
        """ Creates the user table in the database. """
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
        """ Drops the user table in the database. """
        sql = "DROP TABLE IF EXISTS users;"
        CURSOR.execute(sql)
        CONN.commit()

    def save (self):
        """Inserts a new row with the user's information into the database."""
        sql = "INSERT INTO users (username, full_name) VALUES (?, ?);"
        CURSOR.execute(sql, (self.username, self.full_name))
        CONN.commit()

        self.user_id = CURSOR.lastrowid
        type(self).all[self.user_id] = self

    def update (self):
        """Updates the user's information in the database."""
        sql = "UPDATE users SET username = ?, full_name = ? WHERE user_id = ?;"
        CURSOR.execute(sql, (self.username, self.full_name, self.user_id))
        CONN.commit()
    
    def delete (self):
        """Deletes the user from the database."""
        sql = "DELETE FROM users WHERE user_id = ?;"
        CURSOR.execute(sql, (self.user_id,))
        CONN.commit()

        del type(self).all[self.user_id]

        self.user_id = None
        self.username = None
        self.full_name = None

    @classmethod
    def instance_from_db(cls, row):
        """Returns a user object from a database row  having the user's information."""
        user = cls.all.get(row[0])
        if user:
            # ensuring the user's information is up to date
            user.username = row[1]
            user.full_name = row[2]
            return user
        else:
            # Creting a new insatance if the user is not in the database
            user = cls(row[0], row[1], row[2])
            user_id = row[0]
            cls.all[user_id] = user
            return user
    
    @classmethod
    def get_all(cls):
        """Returns a list of all users in the database."""
        sql = "SELECT * FROM users;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, user_id):
        """Returns a user object from the database having the user's ID."""
        sql = "SELECT * FROM users WHERE user_id = ?;"
        row = CURSOR.execute(sql, (user_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_username(cls, username):
        """Returns a user object from the database having the user's username."""
        sql = "SELECT * FROM users WHERE username = ?;"
        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def users(self):
        """Returns a list of all users in the database."""
        sql = "SELECT * FROM users;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return rows

    