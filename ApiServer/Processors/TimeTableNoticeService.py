import json
import flask

from datetime import datetime, timedelta

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

# False 0 -> Default, True -> using sql data
def process_student_timetable(data_manager, dict_json:dict, str_class:str, use_sql:bool) -> dict:
    time_column = None
    str_date = dict_json['action']['params']['date']

    if str_date == "오늘":
        str_date = datetime.today().strftime("%Y-%m-%d")
    else:
        str_date = json.loads(str_date)['date']

    lst_timetable = data_manager.get_timetable_st(str_date, str_class)

    if len(lst_timetable) > 0:
        str_output = []
        str_output.append("{0}반의 {1}일 시간표는 다음과 같습니다.".format(str_class, str_date))
        str_output.append("")
            
        for i in range(len(lst_timetable)):
            if len(lst_timetable[i]) == 0:
                str_output[1] += "{0}교시: 없음\n".format(i + 1)
            else:
                str_output[1] += "{0}교시: {1} 선생님의 {2}\n".format(i + 1, lst_timetable[i][0], lst_timetable[i][1])
        lst_outputs = [
            SimpleText.generate_simpletext(str_output[0]), 
            SimpleText.generate_simpletext(str_output[1]),
            ]

        if use_sql:
            lst_outputs.append(SimpleText.generate_simpletext("만약 기본값을 초기화하시려면 '초기화'라고 입력하세요."))
        else:
            lst_outputs.append(SimpleText.generate_simpletext("기본 학급을 설정하거나 변경하시려면 '기본 학급 {0}로 설정해줘'와 같이 입력하세요.".format(str_class)))
        return pack_outputs(lst_outputs)
    else:
        return pack_outputs(SimpleText.generate_simpletext("해당일 수업 정보가 없습니다."))

def process_teacher_timetable(data_manager, dict_json:dict, str_teachername:str, use_sql:bool) -> dict:
    str_date = dict_json['action']['params']['date']

    if str_date == "오늘":
        str_date = datetime.today().strftime("%Y-%m-%d")
    else:
        str_date = json.loads(str_date)['date']
    
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
            if len(lst_timetable[0][i]) == 2:
                str_output += "{0}교시: {1}반 - {2} 수업\n".format(i+1, lst_timetable[0][i][0], lst_timetable[0][i][1])
            else:
                str_output += "{0}교시: 없음\n".format(i+1)

        lst_output.append(SimpleText.generate_simpletext(str_output))

        if use_sql:
            lst_output.append(SimpleText.generate_simpletext("만약 기본값을 초기화하시려면 '초기화'라고 입력해주세요."))
        else:
            lst_output.append(SimpleText.generate_simpletext("만약 기본 이름을 설정하거나 변경하시려면 '기본 이름 {0}*으로 설정해줘'와 같이 입력해주세요.".format(str_teachername[:2])))
    elif len_lst_timetable <= 2:
        for i in range(len(lst_timetable)):
            str_subject = None

            k = 0
            while str_subject == None and k < len(lst_timetable[i]):
                if len(lst_timetable[i][k]) != 0:
                    str_subject = lst_timetable[i][k][1]
                k += 1

            str_output = "{0} 과목을 수업하시는 {1} 선생님의 {2}일 시간표는 다음과 같습니다.\n\n".format(str_subject, str_teachername, str_date)
            
            num_blank = 0
            for k in range(len(lst_timetable[i])):
                if len(lst_timetable[i][k]) == 2:
                    str_output += "{0}교시: {1}반 - {2} 수업\n".format(k+1, lst_timetable[i][k][0], lst_timetable[i][k][1])
                else:
                    str_output += "{0}교시: 없음\n".format(k+1)
                    num_blank += 1

            if num_blank == 8:
                continue
            
            lst_output.append(SimpleText.generate_simpletext(str_output))

        if use_sql:
            lst_output.append(SimpleText.generate_simpletext("만약 기본값을 초기화하시려면 '초기화'라고 입력해주세요."))
        else:
            lst_output.append(SimpleText.generate_simpletext("만약 기본 이름을 설정하거나 변경하시려면 '기본 이름 고길*으로 설정해줘'와 같이 입력해주세요."))
    else:
        str_output = ""
        for i in range(len(lst_timetable)):
            str_subject = None

            k = 0
            while str_subject == None and k < len(lst_timetable[i]):
                if len(lst_timetable[i][k]) != 0:
                    str_subject = lst_timetable[i][k][0]
                k += 1

            str_output += "{0}을 수업하시는 {1} 선생님의 {2}일 시간표는 다음과 같습니다.\n\n".format(str_subject, str_teachername, str_date)
            
            num_blank = 0
            for k in range(len(lst_timetable[i])):
                if len(lst_timetable[i][k]) == 2:
                    str_output += "{0}교시: {1}반 - {2} 수업\n".format(k+1, lst_timetable[i][k][0], lst_timetable[i][k][1])
                else:
                    str_output += "{0}교시: 없음\n".format(k+1)
                    num_blank += 1

            if num_blank == 8:
                continue

            str_output += "_____\n\n\n"
        
        if use_sql:
            str_output += "만약 기본값을 초기화하시려면 '초기화'라고 입력해주세요."
        else:
            str_output += "만약 기본 이름을 설정하거나 변경하시려면 '기본 이름 고길*으로 설정해줘'와 같이 입력해주세요."

        lst_output.append(SimpleText.generate_simpletext(str_output))

    return pack_outputs(lst_output)

def process(data_manager, logger, dict_json:dict) -> dict:
    lst_params = dict_json['action']['params'].keys()

    if "grade-class" in lst_params:
        str_class = dict_json['action']['params']['grade-class']
        logger.log("[TimeTableNoticeService] Timetable_st Req Inbounded!")
        return process_student_timetable(data_manager, dict_json, str_class, use_sql=False)
    elif "grade" in lst_params and "class" in lst_params:
        str_class = dict_json['action']['params']['grade'] + '-' + dict_json['action']['params']['class']
        logger.log("[TimeTableNoticeService] Timetable_st Req Inbounded!")
        return process_student_timetable(data_manager, dict_json, str_class, use_sql=False)
    elif "teacher_name" in lst_params:
        logger.log("[TimeTableNoticeService] Timetable_tc Req Inbounded!")
        return process_teacher_timetable(data_manager, dict_json, dict_json['action']['params']['teacher_name'], use_sql=False)
    else:
        str_sql = "SELECT * FROM user_info WHERE user_val='{0}'".format(dict_json['userRequest']['user']['id'])
        cursor = data_manager.mysql_query(str_sql)
        rowcount = cursor.rowcount

        if rowcount == 0:
            logger.log("[TimeTableNoticeService] Timetable Req that invalid inbounded.")
            return pack_outputs(SimpleText.generate_simpletext("학년-반 정보 혹은 성명이 누락되었습니다. 포함하여 다시 질문해주세요."))
        elif rowcount == 1:
            row = cursor.fetchone()
            if row[2] != "0":
                logger.log("[TimeTableNoticeService] Timetable_tc Req Inbounded!")
                return process_teacher_timetable(data_manager, dict_json, row[2], use_sql=False)
            elif row[1] != "0":
                logger.log("[TimeTableNoticeService] Timetable_st Req Inbounded!")
                return process_student_timetable(data_manager, dict_json, row[1], use_sql=True)
        else:
            raise
