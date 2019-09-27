import json
import requests
import datetime
from bs4 import BeautifulSoup

str_datetime = datetime.datetime.now().strftime('%Y%m%d')

response = requests.get("http://school.cbe.go.kr/gukwon-h/M01061201/list?ymd=" + str_datetime)
soup = BeautifulSoup(response.text, 'html.parser')

dict_menu = {}

for i in soup.select('li.tch-lnc-wrap dl'):
    str_key = i.select_one('dt').text[0]
    dict_menu[str_key] = []
    for k in i.select('li'):
        dict_menu[str_key].append(k.text)

with open('data/MenuTable.dat', 'w') as fp:
    json.dump(dict_menu, fp)