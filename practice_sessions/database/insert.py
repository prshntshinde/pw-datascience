import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO test1.test_table values(1234,'Pras',45,35.34,'Shin');")
mydb.commit()
mydb.close()
