import sqlite3
import os
from Library.student import Student
from Library.teachers import Courses
from Library.courses import Courses


def clear_console():
    os.system('clear')


# def checkPassword(password):
    

def options_screen(loggedInUser: Student):
    clear_console()

    print("Welcome to the USF Course Registration System! ")
    print()

    print("Here are all of your courses: ")

    student_id = loggedInUser.getUID()

    # Execute the SQL query
    courseList = loggedInUser.findCourses(student_id)
  
    for course in courseList:
        print(f"Course ID: {course[0]}, Name: {course[1]}, Classroom: {course[2]}, Building: {course[3]}")


    main()

def login():
    clear_console()
    print("\n\tLogin Screen")

    uid = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = Student(None)
    student = tempUser.findOneByUsername(uid)

    if (student == None or student[2] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()

    else:
        print("\tYou have successfully logged in\n")
        loggedInUser = Student(student[0])
        return loggedInUser
     

def populate_screen():
    return

def main():
    
    print("Press 1 to login")
    print("anything else to populate")
    loginI = int(input())
    if loginI == 1:
        login()
    else:
        populate_screen()


if __name__ == "__main__":
    main()