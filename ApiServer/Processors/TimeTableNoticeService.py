import json
import flask
import traceback

from datetime import datetime, timedelta

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, logger, dict_json:dict) -> dict:
    str_date = None
    str_class = None
    time_column = None

    try:
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

        str_date =  "20" + today.strftime("%y-%m-%d")
    else:
        str_date = json.loads(str_date)['date']

    lst_timetable = data_manager.get_timetable(str_date, str_class)
    str_output = "해당일 수업 정보가 없습니다."

    if len(lst_timetable) > 0:
        str_output = "{0} 학급의 시간표는 다음과 같습니다.\n\n".format(str_class)
            
        for i in range(len(lst_timetable)):
            if len(lst_timetable[i]) == 0:
                str_output += "{0}교시: 없음\n".format(i + 1)
            else:
                str_output += "{0}교시: {1} 선생님의 {2}\n".format(i + 1, lst_timetable[i][0], lst_timetable[i][1])

    return pack_outputs([SimpleText.generate_simpletext(str_output)])