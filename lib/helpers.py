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
            print(task)
    else:
        print(f"User {username} not found.")

def find_tasks_by_name_and_username():
    username = input("Enter username: ")
    user = User.find_by_username(username)
    if user:
        task_name = input("Enter task name: ")
        task = Task.find_by_name_and_user_id(task_name, user.user_id)
        if task:
            for task in task:
                print(task)
        else:
            print(f"No tasks found for user {username} and task name {task_name}.")
    else:
        print(f"User {username} not found.")

def find_task_by_id():
    task_id = input("Enter task ID: ")
    task = Task.find_by_id(task_id)
    if task:
        print(task)
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
        if not category:
            create_category =  input(f'Category {category_name} does not exist. Do you want to create it? (y/n): ').strip().lower()
            if create_category == 'y':
                category = Category(None, category_name)
                category.save()

            else:
                print('Task Creation Aborted')
                return

        task = Task(None, user.user_id, task_name, task_description, task_due_date, task_priority, task_status, category.category_id)
        task.save()
        print(f"Task {task_name} created successfully.")
    else:
        print(f"User {username} not found.")

def update_task():
    task_id = int(input("Enter task ID: "))
    task = Task.find_by_id(task_id)
    if task:
        task_name = input("Enter new task name: ")
        task_description = input("Enter new task description: ")
        task_due_date = input("Enter new task due date: ")
        task_priority = input("Enter new task priority: ")
        task_status = input("Enter new task status: ")
        category_name = input("Enter new category name: ")

        category = Category.find_by_name(category_name)
        if not category:
            create_category =  input(f'Category {category_name} does not exist. Do you want to create it? (y/n): ').strip().lower()
            if create_category == 'y':
                category = Category(None, category_name)
                category.save()

            else:
                print('Task Creation Aborted')
                return
            
        task.title = task_name
        task.description = task_description
        task.due_date = task_due_date
        task.priority = task_priority
        task.status = task_status
        task.category_id = category.category_id
        task.update()
        print(f"Task {task_name} updated successfully.")
    else:
        print(f"Task {task_id} not found.")
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
    category_id = int(input("Enter category ID: "))
    category = Category.find_by_id(category_id)
    if category:
        category_name = input("Enter new category name: ")
        category.category_name = category_name
        category.update()
        print(f"Category {category_name} updated successfully.")
    else:
        print(f"Category {category_id} not found.")

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
        print(user)

def find_user_by_username():
    username = input('Enter username: ')
    user = User.find_by_username(username)
    if user:
        print(user)
    else:
        print(f"User {username} not found.")

def find_user_by_id():
    user_id = int(input('Enter user ID: '))
    user = User.find_by_id(user_id)
    if user:
        print(user)
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















