import sqlite3
import os
from Library.student import Student


def clearConsole():
    os.system('clear')


# def checkPassword(password):
    

def optionsScreen(loggedInUser: User):
    clearConsole()

    print("Welcome to the USF Course Registration System! ")
    print()

    print("Here are all of your courses: ")

    student_id = loggedInUser.getUId()

    # Execute the SQL query
    courseList = loggedInUser.findCourses(student_id)
  
    for course in courseList:
        print(f"Course ID: {course[0]}, Name: {course[1]}, Classroom: {course[2]}, Building: {course[3]}")


    main()

def login():
    clearConsole()
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
        clearConsole()
        loggedInUser = Student(student[0])
        optionsScreen(loggedInUser)


def checkUsername(username):
    if (not checkStrUtils.checkIfStrIsCorrectLength(username, 1, 32)):
        print(
            "\tUsername must be between 1 and 32 characters!\n\tPlease try again.\n"
        )
        return False
    if (not checkIfUsernameIsUniqueInDB(username)):
        print("\tUsername must be unique!\n\tPlease try again.\n")
        return False
    return True


def main():
    
    print("Press any key to login")
    input()
    login()

if __name__ == "__main__":
    main()