import sqlite3

conn = sqlite3.connect('school.db')
# create cursor
cur = conn.cursor()
#create a table
cur.execute("""
    CREATE TABLE careers(
    careerid integer primary key,
    name text
    )
""")

cur.execute("""
    CREATE TABLE courses(
    courseid integer primary key,
    name text,
    duration integer,
    complexity integer,
    career integer,
    FOREIGN KEY(career) REFERENCES career(careerid)
    )
""")


cur.execute("""
    CREATE TABLE students(
    firstname text,
    lastname text,
    age integer,
    career integer,
    FOREIGN KEY(career) REFERENCES career(careerid)
    )
""")

cur.execute("""
    CREATE TABLE teachers(
    firstname text,
    lastname text,
    age integer,
    career integer ,
    FOREIGN KEY(career) REFERENCES career(careerid)
    )
""")

#commit and close connection
conn.commit()
conn.close()