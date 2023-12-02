import sqlite3
db = "aeg_reg.db"

class Teachers:
    def __init__(self, tid):
       self.tid = tid
        
    def get_tid(self):
        return self.tid
    
    def isLoggedIn(self): #returns false if student is not logged in
        return self.tid != None
    def create(self, tid, name, department, dob):
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            """INSERT INTO students (tid, name, department, dob) VALUES (?, ?, ?,?)""",
            (tid, name, department, dob))
        con.commit()
        self.tid = cur.lastrowid
        return self.tid
    
    def findOneBytid(self, tid):
        con = sqlite3.connect(db)
        cur = con.cursor()
        res = cur.execute("""SELECT tid,user_password FROM teachers WHERE tid = ? LIMIT 1""",(tid, ))
        user = res.fetchone()
        return user

    def list_teachers(self):
        # """List all teachers"""
        con = sqlite3.connect(db)
        query = 'SELECT * FROM teachers'
        cursor = con.execute(query)
        return cursor.fetchall()
    
    def findCourses(self, tid):
        con = sqlite3.connect(db) 
        cur = con.cursor()
        res = cur.execute(""" 
                SELECT courses.cid, courses.classroom, courses.name, courses.bldg 
                FROM courses 
                JOIN teachers ON courses.tidClass = teachers.tid
                WHERE teachers.tid = ?
            """, (tid, ))
        courses = res.fetchall()
        return courses

