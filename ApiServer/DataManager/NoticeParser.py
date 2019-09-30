import requests
from bs4 import BeautifulSoup
#주소 따고
response = requests.get("http://school.cbe.go.kr/gukwon-h/M010301/")
html = response.text
#담아 와서
soup = BeautifulSoup(html, 'html.parser')
#이렇게 한다면?...
for i in soup.select('tbody td.tch-tit'):
    print(i.text.strip())
    for k in soup.select('tbody td.tch-nme'):
        print(k.text)
        
#으악 이게뭐야...