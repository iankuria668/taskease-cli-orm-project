# lib/cli.py

from helpers import (
    exit_program, list_tasks_by_username,
    find_task_by_name_and_username, find_task_by_id, 
    create_task,update_task, delete_task, 
    list_categories, find_category_by_name,
    find_category_by_id, create_category, 
    update_category, delete_category, 
    find_user_by_id, find_user_by_username
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_tasks_by_username()
        elif choice == "2":
            find_task_by_name_and_username()
        elif choice == "3":
            find_task_by_id()
        elif choice == "4":
            create_task()
        elif choice == "5":
            update_task()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            list_categories()
        elif choice == "8":
            find_category_by_name()
        elif choice == "9":
            find_category_by_id()
        elif choice == "10":
            create_category()
        elif choice == "11":
            update_category()
        elif choice == "12":
            delete_category()
        elif choice == "13":
            find_user_by_id()
        elif choice == "14":
            find_user_by_username()
        else:
            print("Invalid choice")





def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List tasks")
    print("2. Find task by name")
    print("3. Find task by ID")
    print("4. Create task")
    print("5. Update task")
    print("6. Delete task")
    print("7. List categories")
    print("8. Find category by name")
    print("9. Find category by ID")
    print("10. Create category")
    print("11. Update category")
    print("12. Delete category")
    print("13. Find user by ID")
    print("14. Find user by username")


if __name__ == "__main__":
    main()
