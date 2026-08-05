import mysql.connector
import sys
class DBHelper:

    def __init__(self):

        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hit-db-demo"
            )

            self.cursor = self.conn.cursor()

            print("Connected to database")

        except:
            print("Some error occurred")
            sys.exit(0)
        else:
            print("Connection successful")
    def register(self, name, email, password):
        try:
            self.cursor.execute("""INSERT INTO users (id, name, email, password) VALUES (NULL, '{}', '{}', '{}');""".format(name, email, password))
            self.conn.commit()
        except:
           return -1
        else:
            return 1
    def search(self, email,password):
        self.cursor.execute("""
        SELECT * FROM USERS WHERE email LIKE '{}' AND password LIKE '{}'
                              """.format(email,password))
        data=self.cursor.fetchall()
        return data