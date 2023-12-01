import sqlite3
con = sqlite3.connect("aeg_reg.db")
cur = con.cursor()
# Create `students` table

cur.execute("""
CREATE TABLE `students` (
  `uid` INTEGER PRIMARY KEY NOT NULL,
  `user_password` varchar(12) NOT NULL,
  `user_firstname` varchar(32) NOT NULL,
  `user_lastname` varchar(32) NOT NULL,
  `user_major` varchar(64) NOT NULL
)
""")
# Create `courses` table

cur.execute("""

CREATE TABLE courses (
  cid CHAR(5) PRIMARY KEY NOT NULL,
  name varchar(50) NOT NULL,
  classroom varchar(15) NOT NULL,
  bldg CHAR(3) NOT NULL, 
)
""")

# Create `registered` table

cur.execute("""

CREATE TABLE registered (
  uid CHAR(9),
  cid CHAR(5),
  PRIMARY KEY (uid, cid),
  FOREIGN KEY (uid) REFERENCES students (uid),
  FOREIGN KEY (cid) REFERENCES courses (cid)  -- Assuming 'courses' table exists with 'cid' as a primary key
);
""")
# Create `teachers` table

cur.execute("""
CREATE TABLE teachers (
    tid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    dob DATE NOT NULL)
""")