import mysql.connector as mysql
import random

n = 100
str_charpool = "abcdefghijklmnopqrstuvwxyz!@#$%^&*+=?~"

lst_authcode = []
i = 0

while i < n:
    str_authcode = ''
    
    for k in range(6):
        str_authcode += random.choice(str_charpool)

    if not (str_authcode in lst_authcode):
        lst_authcode.append(str_authcode)
        i += 1

print(lst_authcode)