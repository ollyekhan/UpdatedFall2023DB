import sqlite3
import os
from Library.student import Student
from Library.teachers import Teachers
from Library.courses import Courses


def clear_console():
    os.system('clear')


# def checkPassword(password):
    

def options_screen(loggedInUser: Student):
    #clear_console()

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
    #clear_console()
    print("\n\tLogin Screen")

    uid = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = Student(None)
    student = tempUser.findOneByUID(uid)

    if (student == None or student[2] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()

    else:
        print("\tYou have successfully logged in\n")
        loggedInUser = Student(student[0])
        return loggedInUser
     

def populate_screen():
    tempUser = Student(None)
    tempClass = Courses(None)
    tempTeachers = Teachers(None)

    print("Press 1 to add student:")
    print("Press 2 to add courses")
    print("Press 3 to add courses")
    loginI = int(input())
    if loginI == 1:
        for x in range(5):    
            uid = input("Enter uid ")

            user_password = input("Enter user_password: ")

            user_firstname = input("Enter user_firstname: ")
            user_lastname = input("Enter user_lastname: ")
            user_major = input("Enter user_major: ")
            tempUser.create(uid, user_password, user_firstname, user_lastname, user_major)

    elif loginI == 2:
        for x in range(5):    
            cid = input("Enter cid ")

            name = input("Enter name: ")

            classroom = input("Enter classroom: ")
            bldg = input("Enter bldg: ")
            tid = input("Enter tid: ")

            tempClass.create(cid, name, classroom, bldg, tid)
    elif loginI == 3:
        for x in range(5):    
            tid = input("Enter tid ")
            name = input("Enter name: ")
            department = input("Enter department: ")
            dob = input("Enter dob: ")    
            tempTeachers.create(tid, name, department, dob)

            

def main():
    
    print("Press 1 to login:")
    print("Press anything else to populate:")
    loginI = int(input())
    if loginI == 1:
        login()
    else:
        populate_screen()


if __name__ == "__main__":
    main()