import sqlite3

db = "aeg_reg.db"

def addCourse(uid):
    course = input("Enter CID to add: ")
    con = sqlite3.connect(db)
    cur = con.cursor()
    print(cur.execute("SELECT * FROM courses"))
    cur.execute(
        "INSERT INTO registered (cid, uid) VALUES (?, ?)",
        (course, uid))
    con.commit()


def dropCourse(uid):
    course = input("Enter CID to drop: ")
    con = sqlite3.connect(db)
    cur = con.cursor()
    print(cur.execute("SELECT * FROM registered"))
    cur.execute(
        "DELETE FROM registered WHERE cid = ?",
        (course))
    con.commit()