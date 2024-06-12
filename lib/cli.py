# lib/cli.py

from helpers import (
    exit_program,
    list_tasks_by_username_and_category,
    list_tasks_by_username,
    find_tasks_by_name_and_username,
    find_task_by_id,
    create_task,
    update_task,
    delete_task,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    create_category,
    update_category,
    delete_category,
    list_users,
    find_user_by_id,
    find_user_by_username,
    create_user,
    update_user,
    delete_user,
    
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_tasks_by_username_and_category()
        elif choice == "2":
            list_tasks_by_username()
        elif choice == "3":
            find_tasks_by_name_and_username()
        elif choice == "4":
            find_task_by_id()
        elif choice == "5":
            create_task()
        elif choice == "6":
            update_task()
        elif choice == "7":
            delete_task()
        elif choice == "8":
            list_categories()
        elif choice == "9":
            find_category_by_name()
        elif choice == "10":
            find_category_by_id()
        elif choice == "11":
            create_category()
        elif choice == "12":
            update_category()
        elif choice == "13":
            delete_category()
        elif choice == "14":
            list_users()
        elif choice == "15":
            find_user_by_id()
        elif choice == "16":
            find_user_by_username()
        elif choice == "17":
            create_user()
        elif choice == "18":
            update_user()
        elif choice == "19":
            delete_user()
        else:
            print("Invalid choice. Please try again.")





def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Filter tasks by category")
    print("2. List tasks")
    print("3. Find tasks by name")
    print("4. Find task by ID")
    print("5. Create task")
    print("6. Update task")
    print("7. Delete task")
    print("8. List categories")
    print("9. Find category by name")
    print("10. Find category by ID")
    print("11. Create category")
    print("12. Update category")
    print("13. Delete category")
    print("14. List users")
    print("15. Find user by ID")
    print("16. Find user by username")
    print("17. Create user")
    print("18. Update user")
    print("19. Delete user")
    


if __name__ == "__main__":
    main()
