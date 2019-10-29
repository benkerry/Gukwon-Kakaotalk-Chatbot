import json
import flask

from datetime import datetime, timedelta

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process_student_timetable(data_manager, dict_json:dict, str_class) -> dict:
    time_column = None
    str_date = dict_json['action']['params']['date']
    lst_params = dict_json['action']['params'].keys()
        
    if "timetable_column" in lst_params:
        time_column = dict_json['action']['params']['timetable_column']

    logger.log("[TimeTableNoticeService] Query Inbounded!")

    if str_date == "오늘":
        str_date =  "20" + datetime.today().strftime("%Y-%m-%d")
    else:
        str_date = json.loads(str_date)['date']

    lst_timetable = data_manager.get_timetable_st(str_date, str_class)

    if len(lst_timetable) > 0:
        if time_column == None:
            str_output = []
            str_output[0] = "{0}반의 {1}일 시간표는 다음과 같습니다.\n\n".format(str_class, str_date)
            str_output[1] = ""
            
            for i in range(len(lst_timetable)):
                if len(lst_timetable[i]) == 0:
                    str_output[1] += "{0}교시: 없음\n".format(i + 1)
                else:
                    str_output[1] += "{0}교시: {1} 선생님의 {2}\n".format(i + 1, lst_timetable[i][0], lst_timetable[i][1])
            return pack_outputs([
                SimpleText.generate_simpletext(str_output[0]), 
                SimpleText.generate_simpletext(str_output[1])
                ])
        else:
            str_output = "{0}반의 {1}교시는 {2} 선생님의 {3} 수업입니다.".format(str_class, time_column, lst_timetable[time_column-1][0], lst_timetable[time_column-1][1])
            return pack_outputs(SimpleText.generate_simpletext(str_output))
    else:
        return pack_outputs(SimpleText.generate_simpletext("해당일 수업 정보가 없습니다."))

def process_teacher_timetable(data_manager, dict_json:dict) -> dict:
    str_teachername = dict_json['action']['params']['teacher_name']
    str_date = dict_json['action']['params']['date']

    if str_date == "오늘":
        str_date = datetime.today().strftime("%Y-%m-%d")
    
    lst_timetable = data_manager.get_timetable_tc(str_date, str_teachername)

    len_lst_timetable = len(lst_timetable)

    lst_output = []

    if len_lst_timetable == 0:
        lst_output.append(SimpleText.generate_simpletext("정보가 없습니다."))
    elif len_lst_timetable == 1:
        str_output = "{0} 선생님의 {1}일 시간표는 다음과 같습니다.".format(str_teachername, str_date)
        lst_output.append(SimpleText.generate_simpletext(str_output))

        str_output = ""
        for i in range(len(lst_timetable[0])):
            if len(lst_timetable[i][k]) == 2:
                    str_output += "{0}교시: {1}반 - {2} 수업\n".format(i+1, lst_timetable[i][k][0], lst_timetable[i][k][1])
                else:
                    str_output += "{0}교시: 없음\n".format(i+1)

        lst_output.append(SimpleText.generate_simpletext(str_output))
    elif len_lst_timetable <= 3:
        for i in range(len(lst_timetable)):
            str_output = "{0}을 수업하시는 {1} 선생님의 {2}일 시간표는 다음과 같습니다.\n\n".format(lst_timetable[i][0][1], str_teachername, str_date)
            
            for k in range(len(lst_timetable[i])):
                if len(lst_timetable[i][k]) == 2:
                    str_output += "{0}교시: {1}반 - {2} 수업\n".format(i+1, lst_timetable[i][k][0], lst_timetable[i][k][1])
                else:
                    str_output += "{0}교시: 없음\n".format(i+1)
            
            lst_output.append(SimpleText.generate_simpletext(str_output))
    else:
        str_output = ""
        for i in range(len(lst_timetable)):
            str_output += "{0}을 수업하시는 {1} 선생님의 {2}일 시간표는 다음과 같습니다.\n\n".format(lst_timetable[i][0][1], str_teachername, str_date)
            
            for k in range(len(lst_timetable[i])):
                if len(lst_timetable[i][k]) == 2:
                    str_output += "{0}교시: {1}반 - {2} 수업\n".format(i+1, lst_timetable[i][k][0], lst_timetable[i][k][1])
                else:
                    str_output += "{0}교시: 없음\n".format(i+1)
            
            str_output += "_____\n\n\n"

        lst_output.append(SimpleText.generate_simpletext(str_output))

    return pack_outputs(lst_output)

def process(data_manager, logger, dict_json:dict) -> dict:
    if "grade-class" in lst_params:
        str_class = dict_json['action']['params']['grade-class']
        return process_student_timetable(data_manager, dict_json, str_class)
    elif "grade" in lst_params and "class" in lst_params:
        str_class = dict_json['action']['params']['grade'] + '-' + dict_json['action']['params']['class']
        return process_student_timetable(data_manager, dict_json, str_class)
    elif "teacher_name" in lst_params:
        return process_teacher_timetable(data_manager, dict_json)
    else:
        return pack_outputs(SimpleText.generate_simpletext("학년-반 정보 혹은 성명이 누락되었습니다. 포함하여 다시 질문해주세요."))