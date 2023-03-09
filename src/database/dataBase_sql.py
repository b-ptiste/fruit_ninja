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
  mydb.close()

  return(myresult[0])


def add_score(name, score, u_id):
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password, 
    database=database
    )
    mycursor = mydb.cursor()
  

    mycursor.execute(f"""
    INSERT INTO SCORES(ID, NAME, SCORE)
    VALUES ('{u_id}', '{name}', {score});
    
    """
    )

    mydb.commit()
    mydb.close()


def get_best_score():
  
  mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password, 
  database=database)
  
  cursor = mydb.cursor()
  cursor.execute(f"""
  SELECT *
  FROM SCORES
  ORDER BY SCORE DESC LIMIT 5
  """)

  myresult = cursor.fetchall()

  return(myresult)

