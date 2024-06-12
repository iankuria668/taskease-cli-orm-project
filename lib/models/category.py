#!/usr/bin/env python3
# lib/models/category.py
from models.__init__ import CONN, CURSOR

class Category:
    all = {}

    def __init__(self, category_id, category_name):
        self._category_id = category_id
        self.category_name = category_name

        if self._category_id:
            Category.all[self._category_id] = self

    def __repr__(self):
        return f"<Category {self.category_name}>"
    
    @property
    def category_name(self):
        return self._category_name
    
    @category_name.setter
    def category_name(self, category_name):
        if isinstance(category_name, str) and len(category_name):
            self._category_name = category_name
        else:
            raise ValueError("Category name must be a string and not empty.")
    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL
        );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS categories;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO categories (category_name) VALUES (?);"
        CURSOR.execute(sql, (self.category_name,))
        CONN.commit()

        self._category_id = CURSOR.lastrowid
        Category.all[self._category_id] = self

    def update(self):
        """Updates the category's information in the database."""
        sql = "UPDATE categories SET category_name = ? WHERE category_id = ?;"
        CURSOR.execute(sql, (self.category_name, self._category_id))  # Corrected attribute name
        CONN.commit()

    
    def delete(self):
        """Deletes the category from the database."""
        sql = "DELETE FROM categories WHERE category_id = ?;"
        CURSOR.execute(sql, (self._category_id,))  # Corrected attribute name
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        category = cls.all.get(row[0])
        if category:
            category._category_name = row[1]
            return category
        else:
            category = cls(row[0], row[1])
            category_id = row[0]
            cls.all[category_id] = category
            return category
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM categories;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, category_id):
        sql = "SELECT * FROM categories WHERE category_id = ?;"
        row = CURSOR.execute(sql, (category_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, category_name):
        sql = "SELECT * FROM categories WHERE category_name = ?;"
        row = CURSOR.execute(sql, (category_name,)).fetchone()
        return cls.instance_from_db(row) if row else None
