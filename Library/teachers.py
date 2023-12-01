import sqlite3
db = "aeg_reg.db"

class Teachers:
    def __init__(self, tid):
       self.tid = tid
        
    def getTID(self):
        return self.tid
    
    def create(self, tid, name, department, dob):
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute(
            """INSERT INTO students (tid, name, department, dob) VALUES (?, ?, ?,?)""",
            (tid, name, department, dob))
        con.commit()
        self.UID = cur.lastrowid
        return self.userId

    def list_teachers(self):
        # """List all teachers"""
        con = sqlite3.connect(db)
        query = 'SELECT * FROM teachers'
        cursor = con.execute(query)
        return cursor.fetchall()

    def __del__(self):
        # """Close the database connection when the object is destroyed"""
        self.conn.close()

