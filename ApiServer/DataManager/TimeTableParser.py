import os
import json
import requests
from dateutil.rrule import rrule, DAILY
from datetime import datetime, timedelta

def run(logger):
    # 변수 초기화
    dict_json = {}
    dict_response = {}

    # 서버에 이번 주 시간표 데이터를 요청한다.
    dict_response['this_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8x")
    dict_response['this_week'].encoding = 'utf-8'

    # 서버에 다음 주 시간표 데이터를 요청한다.
    dict_response['next_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8y")
    dict_response['next_week'].encoding = 'utf-8'

    # 이번 주 시간표 데이터, 다음 주 시간표 데이터를 Dictionary로 변환한다.
    dict_json['this_week'] = json.loads(dict_response['this_week'].text.split('\n')[0])
    dict_json['next_week'] = json.loads(dict_response['next_week'].text.split('\n')[0])

    # YYYY-MM-DD:Class-Grade 형식 키로 데이터 탐색 가능하도록 처리
    datetime_cur = datetime.now()
    timedelta_oneday = timedelta(1)
    
    for i in range(7):
        if not datetime_cur.weekday() == 0:
            datetime_cur -= timedelta_oneday - timedelta(1)
        else:
            break

    datetime_iterater = rrule(DAILY, dtstart=datetime_cur)
    
    dict_result = {}
    str_key = {}

    for week_index in range(1, 15):
        str_key['datetime'] = datetime_iterater[week_index-1].strftime("%Y-%m-%d")
        dict_result[str_key['datetime']] = {}
        
        for grade in range(1, 4):
            for _class in range(1, 13):
                str_key['grade-class'] = str(grade) + '-' + str(_class)
                dict_result[str_key['datetime']][str_key['grade-class']] = []
                try:
                    if week_index < 8:
                        for i in range(1, len(dict_json['this_week']['자료81'][grade][_class][week_index])):
                            teacher_index = dict_json['this_week']['자료81'][grade][_class][week_index][i] // 100
                            subject_index = dict_json['this_week']['자료81'][grade][_class][week_index][i] % 100

                            if not teacher_index and not subject_index:
                                dict_result[str_key['datetime']][str_key['grade-class']].append([])
                                continue

                            dict_result[str_key['datetime']][str_key['grade-class']].append(
                                [dict_json['this_week']['자료46'][teacher_index], dict_json['this_week']['긴자료92'][subject_index]])
                    else:
                        for i in range(1, len(dict_json['next_week']['자료81'][grade][_class][week_index])):
                            teacher_index = dict_json['next_week']['자료81'][grade][_class][week_index][i] // 100
                            subject_index = dict_json['next_week']['자료81'][grade][_class][week_index][i] % 100

                            if not teacher_index and not subject_index:
                                dict_result[str_key['datetime']][str_key['grade-class']].append([])
                                continue

                            dict_result[str_key['datetime']][str_key['grade-class']].append(
                                [dict_json['next_week']['자료46'][teacher_index], dict_json['next_week']['긴자료92'][subject_index]])
                except:
                    pass

    # 처리 완료된 데이터 저장
    with open("TimeTable.dat", "w", encoding="UTF-8") as fp:
        json.dump(dict_result, fp, ensure_ascii=False, sort_keys=True, indent=4)
    
    # 로그 남기기
    logger.log("Data Parsing Completed.")