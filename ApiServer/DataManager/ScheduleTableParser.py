import json
import requests
from dateutil.rrule import *
from datetime import datetime
from bs4 import BeautifulSoup

now_datetime = datetime.now()
nextyear_datetime = datetime(int(now_datetime.strftime('%Y')) + 1, 4, 1)

datetime_iterater = rrule(MONTHLY, dtstart=now_datetime, bymonthday=1)

left_month = (nextyear_datetime - now_datetime).month + 1

dict_result = {}

for i in range(left_month):
    lst_next = datetime_iterater[0].strftime('%Y.%m').split('.')
    
    response = requests.get('http://school.cbe.go.kr/gukwon-h/M010607/list?y={0}&m={1}'.format(lst_next[0], lst_next[1]))
    soup = BeautifulSoup(response.text, 'html.parser')

    for k in soup.select('ul.tch-sch-lst li'):
        lst_datetime = k.select_one('dt').text.split('.')
        str_key = lst_datetime[0] + lst_datetime[1] + lst_datetime[2]
        
        dict_result[str_key] = []

        for j in soup.select('div.tch-tit-wrap'):
            dict_result[str_key].append(j.text[1:])