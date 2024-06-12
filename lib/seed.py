#! /usr/bin/env python3
# lib/seed.py
from models.user import User
from models.task import Task
from models.category import Category

def initialize_database():
    User.drop_table()
    Category.drop_table()
    Task.drop_table()

    User.create_table()
    Category.create_table()
    Task.create_table()

def seed_data():

    user1 = User(None, 'tulleybando', 'Tulley Bando')
    user2 = User(None, 'maithosowavy', 'Brian Maitho')
    user3 = User(None, 'itsiankuria', 'Ian Kuria')
    user4 = User(None, 'valdez', 'Victor Kembei')

    user1.save()
    user2.save()
    user3.save()
    user4.save()

    work_category = Category(None, 'Work')
    personal_category = Category(None, 'Personal')
    school_category = Category(None, 'School')
    music_category = Category(None, 'Music')

    work_category.save()
    personal_category.save()
    school_category.save()
    music_category.save()

    task1 = Task(None, user1.user_id, 'Finish project', 'Finish the project', '2022-12-31', 'High', 'In Progress', school_category.category_id)
    task2 = Task(None, user2.user_id, 'Bird song', 'Finish recording', '2022-11-31', 'High', 'In Progress', music_category.category_id)
    task3 = Task(None, user3.user_id, 'Gym','Leg Day','2024-05-12', 'Low', 'Not Started', personal_category.category_id)
    task4 = Task(None, user4.user_id, 'Interview', 'Submit my application form', '2024-12-31', 'Very High', 'Not Started', work_category.category_id)

    task1.save()
    task2.save()
    task3.save()
    task4.save()

if __name__ == '__main__':
    initialize_database()
    seed_data()
    print("Database seeded successfully.")