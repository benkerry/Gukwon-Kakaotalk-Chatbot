import sys
import random
import openpyxl
import mysql.connector as mysql

truncate = int(sys.argv[1])
n = int(sys.argv[2])

conn = mysql.connect(
    host="localhost",
    user="root",
    passwd="test",
    database="chatbot_manager_web"
)

cursor = conn.cursor()

lst_authcode = []

str_sql = ""
str_charpool = "abcdefghijklmnopqrstuvwxyz!@#$%^&*+=?~"

if truncate == 1:
    cursor.execute("TRUNCATE auth_code;")

i = 0
while i < n:
    str_authcode = ''
    
    for k in range(6):
        str_authcode += random.choice(str_charpool)

    if not (str_authcode in lst_authcode):
        cursor.execute("INSERT INTO auth_code VALUES(\'{0}\');".format(str_authcode))
        i += 1

conn.commit()

wb = openpyxl.Workbook()
ws = wb.active

cursor.execute("SELECT * FROM auth_code")

for i in range(cursor.rowcount):
    ws.cell(1, i).value = cursor[i][0]

wb.save("authcodes.xlsx")