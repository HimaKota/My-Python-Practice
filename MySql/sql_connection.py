import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hima",
  password="1234",
  database="hima_python"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE hima_python")
# mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), department VARCHAR(255))")

# mycursor.execute("SHOW TABLES")
# mycursor.execute("INSERT INTO student (name, department) VALUES ('Hima','ECE'),('Kishore','Mecahnical')")
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)