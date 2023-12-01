import sqlite3

db = "aeg_reg.db"


class Student:

    def __init__(self, UID):
        self.UID = UID

    def getUID(self):
        return self.UID

    def isLoggedIn(self):
        return self.UID != None

    def create(self, uid, user_password, user_firstname, user_lastname, user_major, tid):
        
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            """INSERT INTO students (uid, user_password, user_firstname, user_lastname, user_major, tid) VALUES (?, ?, ?, ?, ?,?)""",
            (uid, user_password, user_firstname, user_lastname, user_major))
        con.commit()
        self.UID = cur.lastrowid
        return self.userId

    def findOneByUID(self, uid):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute("""SELECT uid,user_password FROM students WHERE uid = ? LIMIT 1""",(uid, ))
        user = res.fetchone()
        return user

    def findCourses(self, uid):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute( """ SELECT courses.cid,courses.classroom,courses.name,courses.bldg 
                          FROM courses JOIN registered ON courses.cid = registered.cid JOIN students ON registered.uid = students.uid
                          WHERE students.uid = ?""", (uid, ))
        courses = res.fetchall()
        return courses

    def returnNumStudents(self):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute("""SELECT COUNT() FROM students""")
        studentCount = res.fetchone()[0]
        return studentCount

