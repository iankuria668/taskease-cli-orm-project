#! usr/bin/env python3
# lib/helpers.py
from models.user import User
from models.task import Task
from models.category import Category
def exit_program():
    print("Goodbye!")
    exit()

def list_tasks_by_username():
    username = input("Enter username: ")
    user = User.find_by_username(username)
    if user:
        tasks = Task.find_by_user_id(user._user_id)
        for task in tasks:
            # printing all info about tasks
            print(f"Task found: ID: {task._task_id}, Title: {task.task_name}, Description: {task.task_description}, Due Date: {task.task_due_date}, Priority: {task.task_priority}, Status: {task.task_status}")
    else:
        print(f"User {username} not found.")

def find_tasks_by_name_and_username():
    username = input("Enter username: ")
    user = User.find_by_username(username)
    if user:
        task_name = input("Enter task name: ")
        task = Task.find_by_name_and_user_id(task_name, user._user_id)  # Corrected user ID attribute name
        if task:

            print(f"Task found: ID: {task._task_id}, Title: {task.task_name}, Description: {task.task_description}, Due Date: {task.task_due_date}, Priority: {task.task_priority}, Status: {task.task_status}")
        else:
            print("Task not found.")
    else:
        print(f"User {username} not found.")

def find_task_by_id():
    task_id = input("Enter task ID: ")
    task = Task.find_by_id(task_id)
    if task:
        print(f'Task found: Title: {task.task_name}, Description: {task.task_description}, Due Date: {task.task_due_date}, Priority: {task.task_priority}, Status: {task.task_status}')
    else:
        print(f"Task {task_id} not found.")

def create_task():
    username = input("Enter username: ")
    user = User.find_by_username(username)
    if user:
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_due_date = input("Enter task due date: ")
        task_priority = input("Enter task priority: ")
        task_status = input("Enter task status: ")
        category_name = input("Enter category name: ")
        category = Category.find_by_name(category_name)
        if category:
            task = Task(None, user._user_id, task_name, task_description, task_due_date, task_priority, task_status, category._category_id)  # Corrected attribute names
            task.save()
            print(f"Task '{task_name}' created successfully.")
        else:
            print(f"Category '{category_name}' not found.")
    else:
        print(f"User '{username}' not found.")

def update_task():
    task_id = input("Enter task ID: ")
    task = Task.find_by_id(task_id)
    if task:
        task_name = input("Enter new task name: ")
        task_description = input("Enter new task description: ")
        task_due_date = input("Enter new task due date: ")
        task_priority = input("Enter new task priority: ")
        task_status = input("Enter new task status: ")
        category_name = input("Enter new category name: ")

        # Find the category by name
        category = Category.find_by_name(category_name)
        if category:
            # Update task attributes
            task.task_name = task_name
            task.task_description = task_description
            task.task_due_date = task_due_date
            task.task_priority = task_priority
            task.task_status = task_status
            task.category_id = category._category_id  # Use correct attribute name
            task.update()
            print("Task updated successfully.")
        else:
            print(f"Category {category_name} not found.")
    else:
        print(f"Task with ID {task_id} not found.")
def delete_task():
    task_id = int(input("Enter task ID: "))
    task = Task.find_by_id(task_id)
    if task:
        task.delete()
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task {task_id} not found.")

def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(category)

def find_category_by_name():
    category_name = input(('Enter category name: '))
    category = Category.find_by_name(category_name)
    if category:
        print(category)
    else:
        print(f"Category {category_name} not found.")

def find_category_by_id():
    category_id = int(input("Enter category ID: "))
    category = Category.find_by_id(category_id)
    if category:
        print(category)
    else:
        print(f"Category {category_id} not found.")

def create_category():
    category_name = input("Enter category name: ")
    category = Category(None, category_name)
    category.save()
    print(f"Category {category_name} created successfully.")

def update_category():
    category_id = input("Enter category ID: ")
    category = Category.find_by_id(category_id)
    if category:
        new_category_name = input("Enter new category name: ")
        category.category_name = new_category_name
        category.update()
        print("Category updated successfully.")
    else:
        print(f"Category with ID {category_id} not found.")


def delete_category():
    category_id = int(input("Enter category ID: "))
    category = Category.find_by_id(category_id)
    if category:
        category.delete()
        print(f"Category {category_id} deleted successfully.")
    else:
        print(f"Category {category_id} not found.")

def list_users():
    users = User.get_all()
    for user in users:
        print(f"User ID: {user._user_id}, Username: {user.username}, Full Name: {user.full_name}")

def find_user_by_username():
    username = input('Enter username: ')
    user = User.find_by_username(username)
    if user:
        print(f"User ID: {user._user_id}, Username: {user.username}, Full Name: {user.full_name}")
    else:
        print(f"User {username} not found.")

def find_user_by_id():
    user_id = int(input('Enter user ID: '))
    user = User.find_by_id(user_id)
    if user:
        print(f"User ID: {user._user_id}, Username: {user.username}, Full Name: {user.full_name}")
    else:
        print(f"User {user_id} not found.")

def create_user():
    username = input('Enter username: ')
    full_name = input('Enter full name: ')
    user = User(None, username, full_name)
    user.save()
    print(f"User {username} created successfully.")

def update_user():
    user_id = int(input('Enter user ID: '))
    user = User.find_by_id(user_id)
    if user:
        username = input('Enter new username: ')
        full_name = input('Enter new full name: ')
        user.username = username
        user.full_name = full_name
        user.update()
        print(f"User {username} updated successfully.")
    else:
        print(f"User {user_id} not found.")

def delete_user():
    user_id = int(input("Enter user ID: "))
    user = User.find_by_id(user_id)
    if user:
        user.delete()
        print(f"User {user_id} deleted successfully.")
    else:
        print(f"User {user_id} not found.")















