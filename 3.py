import mysql.connector  # type: ignore

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="11111111",
    database="my_first_db"
)
my_cursor = my_db.cursor()
my_cursor.execute("CREATE TABLE employee("
                  "id INT AUTO_INCREMENT PRIMARY KEY, "
                  "name VARCHAR(255),"
                  "salary INT(6))")
