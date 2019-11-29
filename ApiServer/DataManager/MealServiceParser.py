import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def run():
    response = requests.get("http://school.cbe.go.kr/gukwon-h/M01061201/list")
    soup = BeautifulSoup(response.text, 'html.parser')
    str_href = '/gukwon-h/M01061201/list?ymd='
    
    year_n_month = int(datetime.today().strftime("%Y%m")) * 100

    dict_meal_menu = {}

    for i in range(1, 32):
        str_date = str(year_n_month + i)
        lst_raw_meal_data = soup.select_one('a[href=\"{0}\"]'.format(str_href + str_date))

        if type(lst_raw_meal_data) != type(None):
            for k in lst_raw_meal_data('dl'):
                str_key = str_date[:4] + '-' + str_date[4:6] + '-' + str_date[6:8] + ':' + k.select_one('dt').text[:2]
                dict_meal_menu[str_key] = []

                for j in k.select('li'):
                    dict_meal_menu[str_key].append(j.text)

    nextmonth_delta = timedelta(1)

    if (year_n_month + 100) % 10000 > 1200:
        year_n_month += 8800
    else:
         year_n_month += 100

    year_n_month -= (year_n_month % 100)

    response = requests.get("http://school.cbe.go.kr/gukwon-h/M01061201/list?ymd={0}".format(year_n_month + 1))
    soup = BeautifulSoup(response.text, 'html.parser')

    for i in range(1, 32):
        str_date = str(year_n_month + i)
        lst_raw_meal_data = soup.select_one('a[href=\"{0}\"]'.format(str_href + str_date))

        if type(lst_raw_meal_data) != type(None):
            for k in lst_raw_meal_data('dl'):
                str_key = str_date[:4] + '-' + str_date[4:6] + '-' + str_date[6:8] + ':' + k.select_one('dt').text[:2]
                dict_meal_menu[str_key] = []

                for j in k.select('li'):
                    dict_meal_menu[str_key].append(j.text)

    for i in dict_meal_menu.keys():
        for k in range(len(dict_meal_menu[i])):
            for j in range(len(dict_meal_menu[i][k])):
                if dict_meal_menu[i][k][j].isdecimal() and j > 1:
                    dict_meal_menu[i][k] = dict_meal_menu[i][k][:j]
                    break   

    with open('data/MenuTable.dat','w', encoding="UTF-8") as fp:
        json.dump(dict_meal_menu, fp, ensure_ascii=False, indent=4)
