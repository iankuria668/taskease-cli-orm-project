#! /usr/bin/env python3
# lib/models/category.py
from models.__init__ import CONN, CURSOR

class Category:
    all = {}

    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

        Category.all[self.category_id] = self

    def __repr__(self):
        return f"<Category {self.category_name}>"
    
    @property
    def name(self):
        return self.category_name
    
    @name.setter
    def name(self, name):
        # Input validation
        if isinstance(name, str) and len(name):
            self.category_name = name
        else:
            raise ValueError("Name must be a string and not empty.")

    @classmethod
    def create_table(cls):
        """Creates the category table in the database."""
        sql = """
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name UNIQUE NOT NULL
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drops the category table in the database. """
        sql = "DROP TABLE IF EXISTS categories;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Inserts a new row with the category's information into the database."""
        sql = "INSERT INTO categories (category_name) VALUES (?)"
        CURSOR.execute(sql, (self.category_name,))
        CONN.commit()

        self.category_id = CURSOR.lastrowid
        type(self).all[self.category_id] = self

    def update(self):
        """Updates the category's information in the database."""
        sql = "UPDATE categories SET category_name = ? WHERE category_id = ?"
        CURSOR.execute(sql, (self.category_name, self.category_id))
        CONN.commit()

    def delete(self):
        """Deletes the category from the database."""
        sql = "DELETE FROM categories WHERE category_id = ?"
        CURSOR.execute(sql, (self.category_id,))
        CONN.commit()

        del type(self).all[self.category_id]

        self.category_id = None
        self.category_name = None

    @classmethod
    def instance_from_db(cls, row):
        """Returns a category object from a database row  having the category's information."""
        category = cls.all.get(row[0])
        if category:
            # ensuring the category's information is up to date
            category.category_name = row[0]
            return category
        else:
            # Creting a new insatance if the category is not in the database
            category = cls(row[0], row[1])
            category_id = row[0]
            cls.all[category_id] = category
            return category
        
    @classmethod
    def get_all(cls):
        """Returns a list of all categories in the database."""
        sql = "SELECT * FROM categories;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, category_id):
        """Returns a category object from the database having the category's ID."""
        sql = "SELECT * FROM categories WHERE category_id = ?;"
        row = CURSOR.execute(sql, (category_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def find_by_name(cls, category_name):
        """Returns a category object from the database having the category's name."""
        sql = "SELECT * FROM categories WHERE category_name = ?;"
        row = CURSOR.execute(sql, (category_name,)).fetchone()
        return cls.instance_from_db(row) if row else None