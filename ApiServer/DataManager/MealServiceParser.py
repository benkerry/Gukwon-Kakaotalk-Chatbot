import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run():

    response = requests.get("http://school.cbe.go.kr/gukwon-h/M01061201/list")
    soup = BeautifulSoup(response.text, 'html.parser')

    str_href = '/gukwon-h/M01061201/list?ymd='
    year_n_month = int(datetime.today().strftime("%Y%m")) * 100

    dict_meal_meun = {}

    for i in range(1,30):
        str_date = str(year_n_month + i)
        lst_raw_meal_data = soup.select_one('a[href="/gukwon-h/M01061201/list?ymd={0}]').format(str_date)

        if type(lst_raw_meal_data) != type(None):

            for k in lst_raw_meal_data('d1'):
                str_key = str_date + '-' + k.select_one('dt').text[0]
                dict_meal_meun[str_key] = []

                for j in k.select('li'):
                    dict_meal_meun[str_key].append(j.text)

    for i in dict_meal_meun.keys():
        for k in range(len(dict_meal_meun[i])):
            for j in range(len(dict_meal_meun[i][k])):
                if dict_meal_meun[i][k][j].isdecimal() and j >2:
                    dict_meal_meun[i][k] = dict_meal_meun[i][k][:j]
                    break   

    with open('data/MenuTable.dat','w')as fp:
        json.dump(dict_meal_meun, fp)
