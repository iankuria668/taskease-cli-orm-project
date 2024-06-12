#!/usr/bin/env python3
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
    # Create users
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
    health_category = Category(None, 'Health')
    travel_category = Category(None, 'Travel')

    work_category.save()
    personal_category.save()
    school_category.save()
    music_category.save()
    health_category.save()
    travel_category.save()

    task1 = Task(None, user1._user_id, 'Finish project', 'Finish the project report', '2022-12-31', 'High', 'In Progress', work_category._category_id)
    task2 = Task(None, user1._user_id, 'Prepare presentation', 'Prepare slides for the presentation', '2023-02-28', 'Medium', 'Not Started', work_category._category_id)
    task3 = Task(None, user1._user_id, 'Book flight tickets', 'Book tickets for summer vacation', '2023-06-30', 'Low', 'Not Started', travel_category._category_id)
    task4 = Task(None, user1._user_id, 'Update portfolio', 'Update and polish my portfolio', '2023-04-15', 'High', 'Not Started', work_category._category_id)
    task5 = Task(None, user1._user_id, 'Attend conference', 'Participate in the annual conference', '2023-08-15', 'Medium', 'Not Started', work_category._category_id)
    task6 = Task(None, user2._user_id, 'Write new song lyrics', 'Compose lyrics for a new song', '2023-04-15', 'High', 'Not Started', music_category._category_id)
    task7 = Task(None, user2._user_id, 'Practice guitar', 'Practice guitar for 2 hours daily', '2023-03-31', 'Medium', 'Not Started', music_category._category_id)
    task8 = Task(None, user2._user_id, 'Record music video', 'Shoot and edit a new music video', '2023-05-30', 'High', 'Not Started', music_category._category_id)
    task9 = Task(None, user2._user_id, 'Promote new single', 'Plan and execute marketing campaign', '2023-06-15', 'Medium', 'Not Started', music_category._category_id)
    task10 = Task(None, user2._user_id, 'Collaborate with artist', 'Work on a collaboration project', '2023-07-31', 'High', 'Not Started', music_category._category_id)
    task11 = Task(None, user3._user_id, 'Morning run', 'Run 5 kilometers in the morning', '2024-06-15', 'Medium', 'Not Started', health_category._category_id)
    task12 = Task(None, user3._user_id, 'Plan healthy meals', 'Create meal plan for the week', '2024-05-15', 'Low', 'Not Started', health_category._category_id)
    task13 = Task(None, user3._user_id, 'Learn meditation', 'Practice meditation daily', '2024-04-30', 'Low', 'Not Started', health_category._category_id)
    task14 = Task(None, user3._user_id, 'Attend yoga class', 'Join yoga classes twice a week', '2024-06-30', 'Medium', 'Not Started', health_category._category_id)
    task15 = Task(None, user3._user_id, 'Research fitness trackers', 'Compare and buy a fitness tracker', '2024-07-15', 'Low', 'Not Started', health_category._category_id)
    task16 = Task(None, user4._user_id, 'Interview preparation', 'Prepare for upcoming interviews', '2024-05-30', 'High', 'Not Started', work_category._category_id)
    task17 = Task(None, user4._user_id, 'Update resume', 'Update and refine my resume', '2024-04-30', 'High', 'Not Started', work_category._category_id)
    task18 = Task(None, user4._user_id, 'Apply to job openings', 'Apply to 5 job openings per week', '2024-06-30', 'Medium', 'Not Started', work_category._category_id)
    task19 = Task(None, user4._user_id, 'Network with professionals', 'Attend networking events', '2024-07-15', 'Low', 'Not Started', work_category._category_id)
    task20 = Task(None, user4._user_id, 'Research industry trends', 'Stay updated on industry trends', '2024-08-31', 'Medium', 'Not Started', work_category._category_id)


    
    task1.save()
    task2.save()
    task3.save()
    task4.save()
    task5.save()
    task6.save()
    task7.save()
    task8.save()
    task9.save()
    task10.save()
    task11.save()
    task12.save()
    task13.save()
    task14.save()
    task15.save()
    task16.save()
    task17.save()
    task18.save()
    task19.save()
    task20.save()

if __name__ == '__main__':
    initialize_database()
    seed_data()
    print("Database seeded successfully.")
