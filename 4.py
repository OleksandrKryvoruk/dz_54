import mysql.connector  # type: ignore

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="11111111",
    database="my_first_db"
)
my_cursor = my_db.cursor()
my_cursor.execute("ALTER TABLE student CHANGE id PRIMARY_KEY VARCHAR(255)")

my_db.commit()
