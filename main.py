import sqlite3
import os
from Library.student import Student
from Library.teachers import Teachers
from Library.courses import Courses
from Library.registered import Registered

db = "aeg_reg.db"
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
    
    userinput = input("Would you like to (a)dd/(d)rop/(l)og off?: ")
    register = Registered()
    if userinput == 'a':
        cid = input("enter class cid: ")
        register.addCourse(loggedInUser.UID, cid)
    elif (userinput.lower() == 'd'):
        cid = input("enter class cid: ")
        register.dropCourse(loggedInUser.UID,cid)
    elif (userinput.lower() == "l"):
        print("Thanks for trying!")
        return
    else:
        print("invalid input!")
    options_screen(loggedInUser)

def login():
    #clear_console()
    print("\n\tLogin Screen")

    uid = input("Enter Username: ")
    password = input("Enter Password: ")

    tempUser = Student(None)
    student = tempUser.findOneByUID(uid)

    if (student == None or student[1] != password):
        print("\tIncorrect username or password!\n\tPlease try again.\n")
        login()

    else:
        print("\tYou have successfully logged in\n")
        loggedInUser = Student(student[0])
        options_screen(loggedInUser)
     

def populate_screen():
    tempUser = Student(None)
    tempClass = Courses(None)
    tempTeachers = Teachers(None)

    print("Press 1 to add student:")
    print("Press 2 to add courses")
    print("Press 3 to add teachers")
    loginI = int(input())
    if loginI == 1:
        for x in range(5):    
            uid = input("Enter uid ")

            user_password = input("Enter user_password: ")

            user_firstname = input("Enter user_firstname: ")
            user_lastname = input("Enter user_lastname: ")
            user_major = input("Enter user_major: ")
            tid = input("Enter tid ")
            tempUser.create(uid, user_password, user_firstname, user_lastname, user_major,tid)

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
def print_database():
    con = sqlite3.connect(db)
    cur = con.cursor()

    # Get the list of all tables in the database
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Iterate through all tables
    for table in tables:
        table_name = table[0]
        print(f"Contents of table {table_name}:")
        
        # Fetch all data from each table
        cur.execute(f"SELECT * FROM {table_name};")
        rows = cur.fetchall()
        
        # Print each row
        for row in rows:
            print(row)

        print("\n")  # Newline for better readability between tables            

def main():

    print_database()
    print("Press 1 to login:")
    print("Press any other num to populate:")
    loginI = int(input())
    if loginI == 1:
        login()
    else:
        populate_screen()


if __name__ == "__main__":
    main()