import mysql.connector

# Connect to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Baptiste-2"
)

# Create a database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")