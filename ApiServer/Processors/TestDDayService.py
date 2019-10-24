import json
import flask
import traceback

from datetime import datetime, timedelta

from ResponseGenerator.GenerateOutput import SimpleText
from ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, request:flask.Request, logger) -> dict:
    dict_json = None

    str_testtype = None
    str_semester = None

    try:
        dict_json = request.json
        
        str_testtype = dict_json['action']['params']['date']
        
        if '1학기' in dict_json['userRequest']['utterance']:
            str_semester = "1학기"
        elif '2학기' in dict_json['userRequest']['urrerance']:
            str_semester = "2학기"
    except:
        logger.log("[TestDDayService] Exception Catched")
        logger.log(traceback.format_exc())
        
        return pack_outputs([SimpleText.generate_simpletext("잘못된 요청입니다.")])

    today = datetime.today()

    if str_semester == "1학기":
        today.month = 1
        today.day = 1
    elif str_semester == "2학기":
        today.month = 9
        today.day = 1

    dict_test = {}

    if str_testtype == "시험":
        dict_test = data_manager.get_schedule_by_name("고사")
    elif "고사" in str_testtype:
        dict_test = data_manager.get_schedule_by_name(str_testtype)      
    elif str_testtype == "영어듣기능력평가":
        dict_test = data_manager.get_schedule_by_name("영어듣기")
    elif str_testtype == "대학수학능력시험":
        dict_test = data_manager.get_schedule_by_name("수능")
    else:
        dict_test = data_manager.get_schedule_by_name("학력평가")

    str_testname = None
    str_testdate = None
    schedule_day = None
    left_days = None

    lst_test_keys = dict_test.keys().sort()

    for i in lst_test_keys:
        lst_token = i.split('-')
        schedule_day = datetime(int(lst_token[0]), int(lst_token[1]), int(lst_token[2]))
        left_days = (schedule_day - today).day

        if left_days > 0:
            str_testdate = i
            str_testname = dict_test[i][0]
            break

    if str_testname == None:
        return pack_outputs([SimpleText.generate_simpletext("아직 시험 일정이 없어요.")])
    else:
        left_days = (schedule_day - today).days
        str_output = "{0}: {1}일에 시행되며, {2}일 남았습니다.".format(str_testname, str_testdate, left_days)
        return pack_outputs([SimpleText.generate_simpletext(str_output)])