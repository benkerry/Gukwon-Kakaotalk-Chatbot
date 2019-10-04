import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run(logger):
    # [이달의 식단 관리] 페이지 Get & Soup Instance 생성
    response = requests.get("http://school.cbe.go.kr/gukwon-h/M01061201/list")
    soup = BeautifulSoup(response.text, 'html.parser')
    str_href = '/gukwon-h/M01061201/list?ymd='
    
    # YYMM00 형태의 숫자열 생성됨
    year_n_month = int(datetime.today().strftime("%Y%m")) * 100

    dict_meal_menu = {}

    # 한달 치 식단 데이터를 dict_meal_menu에 저장
    for i in range(1,30):
        str_date = str(year_n_month + i)
        lst_raw_meal_data = soup.select_one('a[href=\"{0}\"]'.format(str_href + str_date))

        if type(lst_raw_meal_data) != type(None):

            for k in lst_raw_meal_data('d1'):
                str_key = str_date + '-' + k.select_one('dt').text[0]
                dict_meal_menu[str_key] = []

                for j in k.select('li'):
                    dict_meal_menu[str_key].append(j.text)

    # 메뉴명의 3번째 자리 뒤에 오는 숫자(알레르기 유발식품 번호) 제거
    for i in dict_meal_menu.keys():
        for k in range(len(dict_meal_menu[i])):
            for j in range(len(dict_meal_menu[i][k])):
                if dict_meal_menu[i][k][j].isdecimal() and j > 1:
                    dict_meal_menu[i][k] = dict_meal_menu[i][k][:j]
                    break   

    # 파일에 저장
    with open('data/MenuTable.dat','w')as fp:
        json.dump(dict_meal_menu, fp)

    logger.log("Meal Menu Parsing Complete.")