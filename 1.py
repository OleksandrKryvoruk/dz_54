import mysql.connector # type: ignore

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="11111111"
)
my_cursor = my_db.cursor()
my_cursor.execute("CREATE DATABASE my_first_db")
