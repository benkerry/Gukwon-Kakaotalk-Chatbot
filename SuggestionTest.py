import mysql.connector as mysql

conn = mysql.connect(
    host="localhost",
    user="root",
    passwd="test",
    datebase="chatbot_manager_web"
)

cursor = conn.cursor()

i = 0
while i == 0:
## DB에 건의사항 추가하는 코드 테스트 할 것