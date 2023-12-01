import sqlite3

class TeacherDatabase:
    def __init__(self, db_file):
        # """Initialize db class variables"""
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        # """Create teachers table if it doesn't exist already"""
        query = '''CREATE TABLE IF NOT EXISTS teachers (
                    tid INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    dob DATE NOT NULL)'''
        self.conn.execute(query)

    def get_teacher(self, name):
        # """Retrieve a teacher's details by their ID"""
        query = 'SELECT * FROM teachers WHERE tid = ?'
        cursor = self.conn.execute(query, (name))
        return cursor.fetchone()

    def list_teachers(self):
        # """List all teachers"""
        query = 'SELECT * FROM teachers'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def __del__(self):
        # """Close the database connection when the object is destroyed"""
        self.conn.close()

