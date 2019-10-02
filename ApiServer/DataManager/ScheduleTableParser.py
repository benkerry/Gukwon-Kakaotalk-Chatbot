import json
import requests
from dateutil.rrule import *
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

now_datetime = datetime.now() - timedelta(days = 50)
nextyear_datetime = datetime(int(now_datetime.strftime('%Y')) + 1, 4, 1)

# index로 다음 달을 얻어올 수 있는 rrule 인스턴스를 생성
datetime_iterater = rrule(MONTHLY, dtstart=now_datetime, bymonthday=1)

# 몇달 치 데이터를 긁어와야 하는지 구함
left_month = ((nextyear_datetime - now_datetime).days // 30)

dict_result = {}

for i in range(left_month):
    lst_next = datetime_iterater[i].strftime('%Y.%m').split('.')
    
    response = requests.get('http://school.cbe.go.kr/gukwon-h/M010607/list?y={0}&m={1}'.format(lst_next[0], lst_next[1]))
    soup = BeautifulSoup(response.text, 'html.parser')

    # 일정이 들어있는 틀을 긁어옴
    for k in soup.select('ul.tch-sch-lst li'):
        str_schedule_date = k.select_one('dt').text
        str_key = ''

        # 물결표(~)가 있을 때의 처리
        if '~' in str_schedule_date:
            lst_datetime_raw = str_schedule_date.split('~')
            
            lst_start = lst_datetime_raw[0].split('.')
            lst_end = lst_datetime_raw[1].split('.')

            start_datetime = datetime(int('20' + lst_start[0]), int(lst_start[1]), int(lst_start[2]))
            end_datetime = datetime(int('20' + lst_end[0]), int(lst_end[1]), int(lst_end[2]) + 1)

            tmp_iterater = rrule(DAILY, dtstart=start_datetime)

            lst_interval_datetimes = []
            foo = 0

            # 물결표(~) 앞의 날짜와 뒤의 날짜 사이에 무슨 날짜들이 있는지 구해서 lst_ineterval_datetime에 추가
            while tmp_iterater[foo] != end_datetime:
                lst_interval_datetimes.append(tmp_iterater[foo].strftime('%Y%m%d'))
                foo += 1
            del(foo)

            # lst_interval_datetimes의 내용을 key로 하여 Dictionary에 내용을 추가
            for str_key in lst_interval_datetimes:
                dict_result[str_key] = []
                for j in k.select('div.tch-tit-wrap'):
                    dict_result[str_key].append(j.text[3:-6])

        # 물결표가 없을 때의 처리
        else:    
            lst_datetime = str_schedule_date.split('.')
            str_key = lst_datetime[0] + lst_datetime[1] + lst_datetime[2]
            dict_result[str_key] = []

            # 불필요한 문자 제거하여 딕셔너리에 추가
            for j in k.select('div.tch-tit-wrap'):
                dict_result[str_key].append(j.text[3:-6])

# 파일에 저장
with open('data/ScheduleTable.dat', 'w') as fp:
    json.dump(dict_result, fp)