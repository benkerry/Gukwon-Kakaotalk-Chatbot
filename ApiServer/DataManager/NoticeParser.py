import requests
from bs4 import BeautifulSoup
from datetime import datetime

def run():
    str_url = "http://school.cbe.go.kr/gukwon-h/M010301/list?s_idx="
    year = int(datetime.now().strftime('%Y')[1:])
    month = int(datetime.now().strftime('%m'))
    day = int(datetime.now().strftime('%d'))

    lst_result = []
    is_break = False

    for i in range(1, 10):
        response = requests.get(str_url + str(i))
        soup = BeautifulSoup(response.text, 'html.parser')

        lst_post = soup.select('table.usm-brd-lst tbody tr')
        
        for k in lst_post:
            lst_datetime = k.select_one('td.tch-dte').text.split('.')
            lst_element = []

            diff_day = ((int(lst_datetime[0])  * 365) + (int(lst_datetime[1]) * 30) + int(lst_datetime[2])) - ((year * 365) + (month * 30) + day)

            if diff_day <= 30:
                last_tag = k.select_one('td.tch-tit a')
                lst_element.append(last_tag.text)
                lst_element.append(last_tag['href'])

                lst_result.append(lst_element)
            else:
                is_break = True
                break

        if is_break:
            break

    with open("data/Notice.dat", 'w', encoding='utf-8') as fp:
        fp.write(str(len(lst_result)))
        
       for i in lst_result:
            fp.write(i[0] + '\n')
            fp.write(i[1] + '\n')