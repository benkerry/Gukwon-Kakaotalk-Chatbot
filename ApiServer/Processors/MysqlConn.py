import mysql.connector as mysql

class Conn:
    def __init__(self):
        self.conn = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="test",
            database="chatbot_manager_web"
        )

        self.cursor = self.conn.cursor()