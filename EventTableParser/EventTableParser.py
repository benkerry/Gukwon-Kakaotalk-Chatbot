import requests
from bs4 import BeautifulSoup

response = requests.get("http://school.cbe.go.kr/gukwon-h/M010607/list")
html = response.text

soup = BeautifulSoup(html, 'html.parser')

for i in soup.select('div class=tch-tit-wrap'):
    print(i.text)
