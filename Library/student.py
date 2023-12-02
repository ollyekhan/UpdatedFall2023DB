import sqlite3

db = "aeg_reg.db"


class Student:

    def __init__(self, uid):
        self.uid = uid

    def get_uid(self):
        return self.uid

    def isLoggedIn(self): #returns false if student is not logged in
        return self.uid != None

    def create(self, uid, user_password, user_firstname, user_lastname, user_major,tid):
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            """INSERT INTO students (uid, user_password, user_firstname, user_lastname, user_major, tid) VALUES (?, ?, ?, ?, ?, ?)""",
            (uid, user_password, user_firstname, user_lastname, user_major,tid))
        con.commit()
        self.uid = cur.lastrowid
        return self.uid

    def findOneByuid(self, uid):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute("""SELECT uid,user_password FROM students WHERE uid = ? LIMIT 1""",(uid, ))
        user = res.fetchone()
        return user

    def findCourses(self, uid):
        con = sqlite3.connect(db)  # Replace with your actual database name
        cur = con.cursor()
        res = cur.execute(""" 
                SELECT courses.cid, classroom, courses.name, bldg, tidClass
                FROM courses 
                JOIN registered ON courses.cid = cidR
                JOIN students ON uidR = students.uid
                WHERE students.uid = ?
            """, (uid, ))
        courses = res.fetchall()
        return courses
    
    def returnNumStudents(self):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute("""SELECT COUNT() FROM students""")
        studentCount = res.fetchone()[0]
        return studentCount

