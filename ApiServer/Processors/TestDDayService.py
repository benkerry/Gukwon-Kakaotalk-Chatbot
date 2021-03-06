import json
import flask

from datetime import datetime, timedelta

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, logger, dict_json:dict) -> dict:
    str_testtype = None
    str_semester = None

    str_testtype = dict_json['action']['params']['test_type']
        
    if '1학기' in dict_json['userRequest']['utterance']:
        str_semester = "1학기"
    elif '2학기' in dict_json['userRequest']['utterance']:
        str_semester = "2학기"

    logger.log("[TestDDayService] Query Inbounded!")

    cur_date = None

    if str_semester == "1학기":
        cur_date = datetime(2000 + int(datetime.today().strftime("%y")), 1, 1)
    elif str_semester == "2학기":
        cur_date = datetime(2000 + int(datetime.today().strftime("%y")), 9, 1)
    else:
        cur_date = datetime.today()
        

    lst_test = []

    if str_testtype == "시험":
        lst_test = data_manager.get_schedule_by_name("고사")
    elif "고사" in str_testtype:
        lst_test = data_manager.get_schedule_by_name(str_testtype)      
    elif str_testtype == "영어듣기능력평가":
        if "1학년" in dict_json['userRequest']['utterance']:
            lst_test = data_manager.get_schedule_by_name("1학년 영어듣기")
        elif "2학년" in dict_json['userRequest']['utterance']:
            lst_test = data_manager.get_schedule_by_name("2학년 영어듣기")
        elif "3학년" in dict_json['userRequest']['utterance']:
            lst_test = data_manager.get_schedule_by_name("3학년 영어듣기")
        else:
            lst_test = data_manager.get_schedule_by_name("영어듣기")
    elif str_testtype == "대학수학능력시험":
        lst_test = data_manager.get_schedule_by_name("수능")
    else:
        lst_test = data_manager.get_schedule_by_name("학력평가")

    str_testname = None
    str_testdate = None
    schedule_day = None
    left_days = None

    lst_test.sort(key=lambda x:x[0])

    for i in lst_test:
        lst_token = i[0].split('-')
        schedule_day = datetime(int(lst_token[0]), int(lst_token[1]), int(lst_token[2]))
        left_days = (schedule_day - cur_date).days + 1

        if left_days >= 0:
            str_testdate = i[0]
            str_testname = i[1][0]
            break

    if str_testname == None:
        return pack_outputs(SimpleText.generate_simpletext("아직 시험 일정이 없어요."))
    else:
        if left_days > 0:
            str_output = "{0}: {1}일에 시행되며, {2}일 남았습니다.".format(str_testname, str_testdate, left_days)
        else:
            str_output = "{0}: {1}일에 시행되었습니다.".format(str_testname, str_testdate)
        return pack_outputs(SimpleText.generate_simpletext(str_output))