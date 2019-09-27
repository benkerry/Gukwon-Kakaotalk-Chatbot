import json
import requests
from bs4 import BeautifulSoup

response = requests.get("http://school.cbe.go.kr/gukwon-h/M01061201/list")
soup = BeautifulSoup(response.text, 'html.parser')

dict_menu = {}

for i in soup.select('li.tch-lnc-wrap dl'):
    str_key = i.select_one('dt').text
    dict_menu[str_key] = []
    for k in i.select('li'):
        dict_menu[str_key].append(k.text)

with open('data/MenuTable.dat', 'w') as fp:
    json.dump(dict_menu, fp)