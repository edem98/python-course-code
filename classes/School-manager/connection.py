import mysql.connector as conn

db = conn.connect(host="127.0.0.1",user="devuser",password="sergedem",
                  port=3306,auth_plugin='mysql_native_password',autocommit=True)

cursor = db.cursor()

cursor.execute("use school;")