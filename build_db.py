import argparse
import mysql.connector


def create_sql_db(host, user, password):
    mydb = mysql.connector.connect(host=host, user=user, password=password)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE fruitdb")
    mydb.commit()
    mydb.close()


def create_sql_table(host, user, password, database):
    mydb = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    mycursor = mydb.cursor()

    mycursor.execute(
        """
    CREATE TABLE SETTING(
    NAME CHAR(20) NOT NULL,
    RATIO_BONUS INT NOT NULL,
    RATIO_BOMB INT NOT NULL,
    AMOUNT_IT INT NOT NULL
    );"""
    )

    mycursor.execute(add_setting_table("EASY", 20, 40, 2))
    mycursor.execute(add_setting_table("MEDIUM", 30, 20, 3))
    mycursor.execute(add_setting_table("HARD", 50, 20, 6))

    mycursor.execute(
        """
    CREATE TABLE SCORES(
    ID CHAR(36) NOT NULL,
    NAME CHAR(20) NOT NULL,
    SCORE INT NOT NULL
    );"""
    )
    mydb.commit()
    mydb.close()


def add_setting_table(name, r_bonus, r_bomb, amount_it):
    return f"""
    INSERT INTO SETTING(NAME, RATIO_BONUS, RATIO_BOMB, AMOUNT_IT)
    VALUES ('{name}', {r_bonus}, {r_bomb},  {amount_it});
    ;"""


def parse_args():
    parser = argparse.ArgumentParser(description="Testing")

    parser.add_argument(
        "--host", required=False, type=str, help="host of your mysql DB"
    )

    parser.add_argument("--user", required=True, type=str, help="root of your mysql DB")

    parser.add_argument(
        "--password", required=True, type=str, help="password of your mysql DB"
    )

    parser.add_argument(
        "--database", required=True, type=str, help="name to store the results"
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    # Connect to the MySQL server
    args = parse_args()
    host = args.host
    user = args.user
    password = args.password
    database = args.database
    create_sql_db(host, user, password)
    create_sql_table(host, user, password, database)
