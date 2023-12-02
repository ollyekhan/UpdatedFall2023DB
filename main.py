import sqlite3
import os
from Library.student import Student
from Library.teachers import Teachers
from Library.courses import Courses
from Library.registered import Registered
import Library.strCheck as strCheck

db = "aeg_reg.db"
def clear_console():
    os.system('clear')


# def checkPassword(password):
    
def options_screen_teacher(loggedInUser: Teachers):
    #clear_console()

    print("\nWelcome to the USF Course Registration System! ")
    print()
    print("Here are all of your courses: ")

    teacher_id = loggedInUser.get_tid()

    # Execute the SQL query
    courseList = loggedInUser.findCourses(teacher_id)
  
    for course in courseList:
        print(f"Course Name: {course[2]}")

def options_screen(loggedInUser: Student):
    #clear_console()

    print("\nWelcome to the USF Course Registration System! ")
    print()

    print("Here are all of your courses: ")

    student_id = loggedInUser.get_uid()

    # Execute the SQL query
    courseList = loggedInUser.findCourses(student_id)
  
    for course in courseList:
        print(f"Name: {course[2]}, Classroom: {course[1]}, Building: {course[3]},Course ID: {course[0]} ")

    print("Here are all courses offered by the University\n")

    
    
    userinput = input("Would you like to (a)dd/(d)rop/(l)og off?: ")
    register = Registered()
    if userinput == 'a':
        cid = int(input("enter class cid: "))
        register.addCourse(loggedInUser.uid, cid)
    elif (userinput.lower() == 'd'):
        cid = int(input("enter class cid: "))
        register.dropCourse(loggedInUser.uid,cid)
    elif (userinput.lower() == "l"):
        print("Thanks for trying!")
        return
    else:
        print("invalid input!")
    options_screen(loggedInUser)

def login():
    #clear_console()
    print("\n\tLogin Screen")

    uid = input("Enter uid: ")
    password = input("Enter Password: ")

    tempUser = Student(None)
    student = tempUser.findOneByuid(uid)

    if (student == None or student[1] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()

    else:
        print("\tYou have successfully logged in\n")
        loggedInUser = Student(student[0])
        options_screen(loggedInUser)

def log_in_teacher():
    #clear_console()
    print("\n\tLogin Screen")

    tid = input("Enter TID: ")
    password = input("Enter Password: ")

    tempUser = Teachers(None)
    student = tempUser.findOneBytid(tid)

    if (student == None or student[1] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        log_in_teacher()

    else:
        print("\tYou have successfully logged in\n")
        loggedInUser = Teachers(student[0])
        options_screen_teacher(loggedInUser)     

def populate_screen():
    tempUser = Student(None)
    tempClass = Courses(None)
    tempTeachers = Teachers(None)

    print("\nPress 1 to add student: ")
    print("Press 2 to add courses: ")
    print("Press 3 to add teachers: ")
    loginI = int(input())
    if loginI == 1:
        for x in range(5):    
            uid = int(input("Enter uid: "))
            while True:
                user_password = input("Enter user_password: ")
                if strCheck.pwValidation(user_password) == True:
                    break
            user_firstname = input("Enter user_firstname: ")
            user_lastname = input("Enter user_lastname: ")
            user_major = input("Enter user_major: ")
            tid = int(input("Enter tid "))
            tempUser.create(uid, user_password, user_firstname, user_lastname, user_major,tid)

    elif loginI == 2:
        for x in range(5):    
            cid = int(input("Enter cid: "))
            name = input("Enter name: ")
            classroom = input("Enter classroom: ")
            bldg = input("Enter bldg: ")
            tid = int(input("Enter tid: "))
            tempClass.create(cid, name, classroom, bldg, tid)

    elif loginI == 3:
        for x in range(5):    
            tid = int(input("Enter tid "))
            while True:
                user_password = input("Enter user_password: ")
                if strCheck.pwValidation(user_password) == True:
                    break
            name = input("Enter name: ")
            department = input("Enter department: ")
            dob = input("Enter dob: ")    
            tempTeachers.create(tid,user_password, name, department, dob)

def print_database():
    con = sqlite3.connect(db)
    cur = con.cursor()

    # Get the list of all tables in the database
    cur.execute("\nSELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"Contents of table {table_name}:")
        cur.execute(f"SELECT * FROM {table_name};")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("\n")  # Newline for better readability 

def main():

    print_database()
    print("Press \"1\" to login as a student:")
    print("Press \"2\" to login as a teacher:")
    print("Press \"9\" to end application:")
    print("Press any other num to populate:")
    loginI = int(input())
    if loginI == 1:
        login()
    elif loginI == 2:
        log_in_teacher()
    elif loginI == 9:
        return
    else:
        populate_screen()

if __name__ == "__main__":
    main()