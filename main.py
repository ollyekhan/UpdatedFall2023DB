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

    student_id = loggedInUser.getStudentId()

    # Execute the SQL query
    query = """SELECT c.cid, c.name, c.classroom, c.bldg
               FROM courses c
               JOIN student_courses sc ON c.cid = sc.course_id
               WHERE sc.student_id = ?"""
    
    # Assuming you have a database connection `conn`
    cursor = conn.execute(query, (student_id,))
    courses = cursor.fetchall()

    for course in courses:
        print(f"Course ID: {course[0]}, Name: {course[1]}, Classroom: {course[2]}, Building: {course[3]}")


    main()

def login():
    clearConsole()
    print("\n\tLogin Screen")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = Student(None)
    student = tempUser.findOneByUsername(username)

    if (user == None or user[2] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()

    else:
        print("\tYou have successfully logged in\n")
        clearConsole()
        loggedInUser = User(user[0])
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