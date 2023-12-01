import sqlite3
import os

class Courses:
    def __init__(self, cid):
        self.cid = cid

    def getCid(self):
        return self.cid

    def create(self, cid, name, classroom, bldg, tid):
        cid = cid.lower()
        name = name.lower()
        classroom = classroom.lower()
        bldg = bldg.lower()
        tid = tid.lower()

        con = sqlite3.connect("aeg_reg.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO courses (cid, name, classroom, bldg, tid) VALUES (?, ?, ?, ?, ?)",
            (cid, name, classroom, bldg, tid))
        con.commit()

        self.cid = cur.lastrowid
        return self.cid

    def findByCID(self, cid):
        con = sqlite3.connect("aeg_reg.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT * FROM courses WHERE cid = ? LIMIT 1",
            (cid, ))
        course = res.fetchone()
        return course

    def findByName(self, name):
        con = sqlite3.connect("aeg_reg.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT * FROM courses WHERE name = ?",
            (name, ))
        course = res.fetchall()
        return course