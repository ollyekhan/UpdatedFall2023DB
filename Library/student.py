import sqlite3
import os


class Student:

    def __init__(self, userId):
        self.userId = userId

    def getUserId(self):
        return self.userId

    def isLoggedIn(self):
        return self.userId != None

    def create(self, uid, user_password, user_firstname, user_lastname, user_major):
        
        con = sqlite3.connect("aeg_reg.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO students (uid, user_password, user_firstname, user_lastname, user_major) VALUES (?, ?, ?, ?, ?)",
            (uid, user_password, user_firstname, user_lastname, user_major))
        con.commit()
        self.userId = cur.lastrowid
        return self.userId

    def findOneByUsername(self, uid):
        con = sqlite3.connect("aeg_reg.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT uid WHERE uid = ? LIMIT 1",
            (uid, ))
        user = res.fetchone()
        return user


    def findCourses(self, uid):
        con = sqlite3.connect("aeg_reg.db")
        cur = con.cursor()
        res = cur.execute(
            "SELECT * FROM users WHERE user_id = ? LIMIT 1",
            (userId, ))
        user = res.fetchone()
        return user

    def returnNumStudents(self):
        con = sqlite3.connect("incollege.db")
        cur = con.cursor()
        res = cur.execute("SELECT COUNT() FROM users")
        studentCount = res.fetchone()[0]
        return studentCount


    def updateMajor(self, major: str):
        format = Format()
        major = format.titleCase(major)
        con = sqlite3.connect("aeg_reg.db")
        cur = con.cursor()
        cur.execute(
            "UPDATE users SET user_major = ? WHERE user_id = ?",
            (major, self.userId))
        con.commit()
