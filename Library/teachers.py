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
            """INSERT INTO teachers (tid, name, department, dob) VALUES (?, ?, ?, ?)""",
            (tid, name, department, dob))
        con.commit()
        self.tid = cur.lastrowid
        return self.tid

    def list_teachers(self):
        # """List all teachers"""
        con = sqlite3.connect(db)
        query = 'SELECT * FROM teachers'
        cursor = con.execute(query)
        return cursor.fetchall()

