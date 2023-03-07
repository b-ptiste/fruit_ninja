import mysql.connector

host="localhost"
user="root"
password="Baptiste-2"
database ="fruitdb"

def find_setting(name):
  assert name in ["EASY", "MEDIUM", "HARD"], f"name must be in EASY, MEDIUM, HARD"
  mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password, 
  database=database)
  
  cursor = mydb.cursor()
  cursor.execute(f"""
  SELECT *
  FROM SETTING
  WHERE NAME='{name}'
  """)

  myresult = cursor.fetchall()

  return(myresult[0])


def add_setting_score(name, score):
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password, 
    database=database
    )
    mycursor = mydb.cursor()
  

    mycursor.execute(add_setting_score(name, score))

    mydb.commit()
    


def get_best_score(database):
  
  mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password, 
  database=database)
  
  cursor = mydb.cursor()
  cursor.execute(f"""
  SELECT *
  FROM SCORES
  ORDER BY SCORE DESC LIMIT 10
  """)

  myresult = cursor.fetchall()

  return(myresult[0])

