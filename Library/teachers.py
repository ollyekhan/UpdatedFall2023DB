import sqlite3

class TeacherDatabase:
    def __init__(self, db_file):
        """Initialize db class variables"""
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        """Create teachers table if it doesn't exist already"""
        query = '''CREATE TABLE IF NOT EXISTS teachers (
                    tid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    dob DATE NOT NULL UNIQUE)'''
        self.conn.execute(query)

    def add_teacher(self, name, department, dob):
        """Add a new teacher to the database"""
        query = 'INSERT INTO teachers (name, department, dob) VALUES (?, ?, ?)'
        self.conn.execute(query, (name, department, dob))
        self.conn.commit()

    def get_teacher(self, teacher_id):
        """Retrieve a teacher's details by their ID"""
        query = 'SELECT * FROM teachers WHERE tid = ?'
        cursor = self.conn.execute(query, (teacher_id,))
        return cursor.fetchone()

    def update_teacher(self, tid, name, department, dob):
        """Update a teacher's details"""
        query = 'UPDATE teachers SET name = ?, department = ?, dob = ? WHERE tid = ?'
        self.conn.execute(query, (name, department, dob, tid))
        self.conn.commit()

    def delete_teacher(self, teacher_id):
        """Delete a teacher from the database"""
        query = 'DELETE FROM teachers WHERE tid = ?'
        self.conn.execute(query, (teacher_id,))
        self.conn.commit()

    def list_teachers(self):
        """List all teachers"""
        query = 'SELECT * FROM teachers'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def __del__(self):
        """Close the database connection when the object is destroyed"""
        self.conn.close()

