import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="web_crawler"
)

mycursor = mydb.cursor()

sql = "INSERT INTO comments (size, color) VALUES (%s, %s)"
val = ("41A", "黑色")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")