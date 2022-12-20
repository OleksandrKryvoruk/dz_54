import mysql.connector  # type: ignore

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="11111111",
    database="my_first_db"
)
my_cursor = my_db.cursor()
my_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
