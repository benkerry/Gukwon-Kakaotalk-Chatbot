import json
import flask
import traceback

from datetime import datetime, timedelta

from ResponseGenerator.GenerateOutput import SimpleText
from ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, request:flask.Request, logger) -> dict:
    dict_json = None
    str_date = None
    str_class = None
    time_column = None

    try:
        dict_json = request.json
        lst_params = dict_json['action']['params'].keys()

        str_date = dict_json['action']['params']['date']

        if "grade-class" in lst_params:
            str_class = dict_json['action']['params']['grade-class']
        elif "grade" in lst_params and "class" in lst_params:
            str_class = dict_json['action']['params']['grade'] + '-' + dict_json['action']['params']['class']
        else:
            return pack_outputs([SimpleText.generate_simpletext("학년-반 정보가 누락되었습니다. 포함하여 다시 질문해주세요.")])
        
        if "timetable_column" in lst_params:
            time_column = dict_json['action']['params']['timetable_column']
    except:
        logger.log("[TimeTableNotice] Exception Catched")
        logger.log(traceback.format_exc())
        
        return pack_outputs([SimpleText.generate_simpletext("잘못된 요청입니다.")])

    if str_date == "오늘":
        today = datetime.today()
        str_time = datetime.now().strftime("%H%M")

        while str_time[0] == '0':
            str_time = str_time[1:]

        now_time = int(str_time)

        if now_time > 1700:
            today += timedelta(1)

        str_date = today.strftime("%y-%m-%d")

    lst_timetable = data_manager.get_timetable(str_date, str_class)
    str_output = "해당일 수업 정보가 없습니다."

    if len(lst_timetable) > 0:
        str_output = "{0} 학급의 시간표는 다음과 같습니다.\n\n".format(str_class)
            
        for i in range(len(lst_timetable)):
            for k in lst_timetable[i]:
                if len(k) == 0:
                    str_output += "{0}교시: 없음".format(i)
                else:
                    str_output += "{0}교시: {1} 선생님의 {2}".format(i, k[0], k[1])

    return pack_outputs([SimpleText.generate_simpletext(str_output)])