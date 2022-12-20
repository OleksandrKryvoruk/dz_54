import mysql.connector  # type: ignore

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="11111111",
    database="my_first_db"
)
my_cursor = my_db.cursor()
sql_1 = "INSERT INTO student (PRIMARY_KEY, NAME) VALUES (%s, %s)"
val_1 = (1, "John")
my_cursor.execute(sql_1, val_1)
sql_2 = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val_2 = (1, "John", 10000)
my_cursor.execute(sql_2, val_2)
my_db.commit()
