import sqlite3
db = "aeg_reg.db"

class Teachers:
    def __init__(self, tid):
       self.tid = tid
        
    def getTID(self):
        return self.tid
    
    def get_teacher(self, tid):
        # """Get a teacher's details by their ID"""
        con = sqlite3.connect(db)
        query = 'SELECT * FROM teachers WHERE tid = ?'
        cursor = con.execute(query, (tid))
        return cursor.fetchone()

    def list_teachers(self):
        # """List all teachers"""
        con = sqlite3.connect(db)
        query = 'SELECT * FROM teachers'
        cursor = con.execute(query)
        return cursor.fetchall()

    def __del__(self):
        # """Close the database connection when the object is destroyed"""
        self.conn.close()

