import sqlite3

db = "aeg_reg.db"
class Courses:
    def __init__(self, cid =None):
        self.cid = cid

    def getCID(self):
        return self.cid

    def create(self, cid, name, classroom, bldg, tid):
        name = name.lower()
        classroom = classroom.lower()
        bldg = bldg.lower()

        
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO courses (cid, name, classroom, bldg, tidClass) VALUES (?, ?, ?, ?, ?)",
            (cid, name, classroom, bldg, tid))
        con.commit()

        self.cid = cur.lastrowid
        return self.cid

    def findByCID(self, cid):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute(
            "SELECT * FROM courses WHERE cid = ? LIMIT 1",
            (cid, ))
        course = res.fetchone()
        return course

    def findByName(self, name):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute(
            "SELECT * FROM courses WHERE name = ?",
            (name, ))
        course = res.fetchall()
        return course
    @staticmethod
    def displayAllCourses():
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute("SELECT * FROM courses")
        course = res.fetchall()
        return course
