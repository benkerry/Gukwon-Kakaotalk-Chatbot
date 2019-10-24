import json
import requests
from dateutil.rrule import rrule, DAILY, MONTHLY
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def run(logger):
    now_datetime = datetime.now() - timedelta(days = 50)
    nextyear_datetime = datetime(int(now_datetime.strftime('%Y')) + 1, 4, 1)

    datetime_iterater = rrule(MONTHLY, dtstart=now_datetime, bymonthday=1)

    left_month = ((nextyear_datetime - now_datetime).days // 30)

    dict_result = {}

    for i in range(left_month):
        lst_next = datetime_iterater[i].strftime('%Y.%m').split('.')
    
        response = requests.get('http://school.cbe.go.kr/gukwon-h/M010607/list?y={0}&m={1}'.format(lst_next[0], lst_next[1]))
        soup = BeautifulSoup(response.text, 'html.parser')

        for k in soup.select('ul.tch-sch-lst li'):
            str_schedule_date = k.select_one('dt').text
            str_key = ''

            if '~' in str_schedule_date:
                lst_datetime_raw = str_schedule_date.split('~')
            
                lst_start = lst_datetime_raw[0].split('.')
                lst_end = lst_datetime_raw[1].split('.')

                start_datetime = datetime(int('20' + lst_start[0]), int(lst_start[1]), int(lst_start[2]))
                end_datetime = datetime(int('20' + lst_end[0]), int(lst_end[1]), int(lst_end[2]) + 1)

                tmp_iterater = rrule(DAILY, dtstart=start_datetime)

                lst_interval_datetimes = []
                foo = 0

                while tmp_iterater[foo] != end_datetime:
                    lst_interval_datetimes.append(tmp_iterater[foo].strftime('%Y-%m-%d'))
                    foo += 1
                del(foo)

                for str_key in lst_interval_datetimes:
                    dict_result[str_key] = []
                    
                    for j in k.select('div.tch-tit-wrap'):
                        dict_result[str_key].append(j.text[3:-6])

            else:    
                lst_datetime = str_schedule_date.split('.')
                str_key = '20' + lst_datetime[0] + '-' + lst_datetime[1] + '-' + lst_datetime[2]
                dict_result[str_key] = []

                for j in k.select('div.tch-tit-wrap'):
                    dict_result[str_key].append(j.text[3:-6])

    with open('data/ScheduleTable.dat', 'w', encoding="UTF-8") as fp:
        json.dump(dict_result, fp, ensure_ascii=False, indent=4)

    logger.log("Schedule Parsing Complete.")