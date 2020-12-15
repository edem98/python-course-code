import sqlite3

conn = sqlite3.connect('school.db')
# create cursor
cur = conn.cursor()
#create a table


#commit and close connection
conn.commit()
conn.close()