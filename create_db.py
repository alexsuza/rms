import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="y",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE market")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)