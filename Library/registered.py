import sqlite3

db = "aeg_reg.db"
class Registered:
    def addCourse(self, uid,cid):

        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO registered (cid, uid) VALUES (?, ?)",
            (uid,cid ))
        con.commit()


    def dropCourse(self, uid,cid):

        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            "DELETE FROM registered WHERE cid = ? AND uid = ?",
            (uid,cid))
        con.commit()