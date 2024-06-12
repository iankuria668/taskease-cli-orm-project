# lib/cli.py

from helpers import (
    exit_program,
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_tasks()
        elif choice == "2":
            find_task_by_name()
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
        else:
            print("Invalid choice")





def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
