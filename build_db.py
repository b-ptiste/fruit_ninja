import mysql.connector

def create_sql_db(host="localhost", user="root", password="Baptiste-2"):
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE fruitdb")
    mydb.commit()
    mydb.close()

def create_sql_table(host="localhost", user="root", password="Baptiste-2", database ="fruitdb"):
    
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password, 
    database=database
    )
    mycursor = mydb.cursor()
    
    mycursor.execute("""
    CREATE TABLE SETTING(
    NAME CHAR(20) NOT NULL,
    RATIO_BONUS INT NOT NULL,
    RATIO_BOMB INT NOT NULL,
    AMOUNT_IT INT NOT NULL
    );""")

    mycursor.execute(add_setting_table("EASY", 40, 10, 4))
    mycursor.execute(add_setting_table("MEDIUM", 30, 20, 4))
    mycursor.execute(add_setting_table("HARD", 10, 40, 4))

    mycursor.execute("""
    CREATE TABLE SCORES(
    NAME CHAR(20) NOT NULL,
    SCORE INT NOT NULL
    );""")
    mydb.commit()
    mydb.close()



def add_setting_table(name, r_bonus, r_bomb, amount_it):
    return f"""
    INSERT INTO SETTING(NAME, RATIO_BONUS, RATIO_BOMB, AMOUNT_IT)
    VALUES ('{name}', {r_bonus}, {r_bomb},  {amount_it});
    ;"""
    

if __name__ == '__main__':
    # Connect to the MySQL server
    
    create_sql_db()
    create_sql_table()


    
    