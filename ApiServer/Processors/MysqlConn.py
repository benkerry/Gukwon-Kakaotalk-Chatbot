import mysql.connector as mysql

class Conn:
    def __init__(self):
        self.conn = mysql.connect(
            host="localhost",
            user="root",
            passwd="test",
            database="chatbot_manager_web"
        )

        self.cursor = self.conn.cursor()