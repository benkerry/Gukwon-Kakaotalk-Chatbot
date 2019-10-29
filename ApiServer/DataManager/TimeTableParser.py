import os
import json
import requests
import traceback
from dateutil.rrule import rrule, DAILY
from datetime import datetime, timedelta

def run(logger):
    dict_json = {}
    dict_response = {}

    dict_response['this_week'] = requests.get("http://112.186.146.81:4080/5813_31154_1_1")
    dict_response['this_week'].encoding = 'utf-8'

    dict_response['next_week'] = requests.get("http://112.186.146.81:4080/5813_31154_2_1")
    dict_response['next_week'].encoding = 'utf-8'

    dict_json['this_week'] = json.loads(('{' + dict_response['this_week'].text.split('{')[1]).split('\n')[0])
    dict_json['next_week'] = json.loads(('{' + dict_response['next_week'].text.split('{')[1]).split('\n')[0])

    datetime_cur = datetime.now()
    
    for i in range(7):
        if not datetime_cur.weekday() == 0:
            datetime_cur -= timedelta(1)
        else:
            break

    datetime_iterater = rrule(DAILY, dtstart=datetime_cur)
    
    dict_result = {}
    dict_teachertimetable = {}
    str_key = {}

    for week_index in range(1, 8):
        str_key['datetime'] = datetime_iterater[week_index-1].strftime("%Y-%m-%d")
        dict_result[str_key['datetime']] = {}
        
        for grade in range(1, 4):
            for _class in range(1, 13):
                str_key['grade-class'] = str(grade) + '-' + str(_class)
                dict_result[str_key['datetime']][str_key['grade-class']] = []
                try:
                    for i in range(1, len(dict_json['this_week'][''][grade][_class][week_index])):
                        teacher_index = (dict_json['this_week']['학급시간표'][grade][_class][week_index][i] // 100)
                        subject_index = (dict_json['this_week']['학급시간표'][grade][_class][week_index][i] % 100)

                        if not teacher_index and not subject_index:
                            dict_result[str_key['datetime']][str_key['grade-class']].append([])
                            continue

                        dict_result[str_key['datetime']][str_key['grade-class']].append(
                            [dict_json['this_week']['성명'][teacher_index], dict_json['this_week']['긴과목명'][subject_index]])
                except:
                    pass
        
        dict_teachertimetable[str_key['datetime']] = {}

        for teacher in range(1, len(dict_json['this_week']['교사시간표'][0])):
            str_tname = dict_json['this_week']['성명'][teacher]
            lst_buf = []

            if dict_teachertimetable[str_key['datetime']][str_tname] == None:
                dict_teachertimetable[str_key['datetime']][str_tname] = []

            for week_idx in range(1, len(dict_json['this_week']['교사시간표'][0][teacher])):
                for time in range(1, len(dict_json['this_week']['교사시간표'][0][teacher][week_idx])):
                    if dict_json['this_week']['교사시간표'][0][teacher][week_idx][time] == 0:
                        lst_buf.append([])
                    else:
                        str_class = str(dict_json['this_week']['교사시간표'][0][teacher][week_idx][time] % 100)
                        
                        if str_class[1] == '0':
                            str_class[1] = '-'
                        else:
                            str_class = str_class[0] + '-' + str_class[1:3]

                        subject_idx = dict_json['this_week']['교사시간표'][0][teacher][week_idx][time] // 100
                        str_subject = dict_json['this_week']['긴과목명'][subject_idx]

                        lst_buf.append([str_class, str_subject])
            
            dict_teachertimetable[str_key['datetime']][str_tname].append(lst_buf)

    for week_index in range(1, 8):
        str_key['datetime'] = datetime_iterater[week_index + 6].strftime("%Y-%m-%d")
        dict_result[str_key['datetime']] = {}
        
        for grade in range(1, 4):
            for _class in range(1, 13):
                str_key['grade-class'] = str(grade) + '-' + str(_class)
                dict_result[str_key['datetime']][str_key['grade-class']] = []
                try:
                    for i in range(1, len(dict_json['next_week']['학급시간표'][grade][_class][week_index])):
                        teacher_index = dict_json['next_week']['학급시간표'][grade][_class][week_index][i] // 100
                        subject_index = dict_json['next_week']['학급시간표'][grade][_class][week_index][i] % 100

                        if not teacher_index and not subject_index:
                            dict_result[str_key['datetime']][str_key['grade-class']].append([])
                            continue
                        
                        dict_result[str_key['datetime']][str_key['grade-class']].append(
                            [dict_json['next_week']['성명'][teacher_index], dict_json['next_week']['긴과목명'][subject_index]])
                except:
                    pass

        dict_teachertimetable[str_key['datetime']] = {}

        for teacher in range(1, len(dict_json['next_week']['교사시간표'][0])):
            str_tname = dict_json['next_week']['성명'][teacher]
            lst_buf = []

            if dict_teachertimetable[str_key['datetime']][str_tname] == None:
                dict_teachertimetable[str_key['datetime']][str_tname] = []

            for week_idx in range(1, len(dict_json['next_week']['교사시간표'][0][teacher])):
                for time in range(1, len(dict_json['next_week']['교사시간표'][0][teacher][week_idx])):
                    if dict_json['next_week']['교사시간표'][0][teacher][week_idx][time] == 0:
                        lst_buf.append([])
                    else:
                        str_class = str(dict_json['next_week']['교사시간표'][0][teacher][week_idx][time] % 100)
                        
                        if str_class[1] == '0':
                            str_class[1] = '-'
                        else:
                            str_class = str_class[0] + '-' + str_class[1:3]

                        subject_idx = dict_json['next_week']['교사시간표'][0][teacher][week_idx][time] // 100
                        str_subject = dict_json['next_week']['긴과목명'][subject_idx]

                        lst_buf.append([str_class, str_subject])
            
            dict_teachertimetable[str_key['datetime']][str_tname].append(lst_buf)

    with open("data/StudentTimeTable.dat", "w", encoding="UTF-8") as fp:
        json.dump(dict_result, fp, ensure_ascii=False, indent=4)

    with open("data/TeacherTimeTable.dat", "w", encoding="UTF-8") as fp:
        json.dump(dict_teachertimetable, fp, ensure_ascii=False, indent=4)

    logger.log("Timetable Parsing Completed.")