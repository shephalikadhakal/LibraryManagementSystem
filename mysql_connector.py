import mysql.connector as ms;

con = ms.connect(
    host="localhost",
    user="root",
    database="library_management",  # name your database here
    passwd="admin"  # enter your mysql passwd here
)


if con.is_connected():
    print("database connected")
else:
    print("connection unsuccessful")
