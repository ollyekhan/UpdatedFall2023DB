import sqlite3

db = "aeg_reg.db"
class Registered:
    def addCourse(self, uid,cid):

        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO registered (uidR, cidR) VALUES (?, ?)",
            (uid,cid ))
        con.commit()


    def dropCourse(self, uid,cid):

        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            "DELETE FROM registered WHERE uidR = ? AND cidR = ?",
            (uid,cid))
        con.commit()

    def deleteCourses(self): #every new semester we need to have a clean slate (it WORKS okay)

        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            "DELETE FROM registered")
        con.commit()    