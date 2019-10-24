import json
import flask
import traceback

from datetime import datetime

from ResponseGenerator.GenerateOutput import SimpleText
from ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, request:flask.Request, logger) -> dict:
    dict_json = None
    str_class = None
    time_column = None

    try:
        dict_json = request.json
        lst_params = dict_json['action']['params'].keys()

        if "grade-class" in lst_params:
            str_class = dict_json['action']['params']['grade-class']
        elif "grade" in lst_params and "class" in lst_params:
            str_class = dict_json['action']['params']['grade'] + '-' + dict_json['action']['params']['class']
        else:
            return pack_outputs([SimpleText.generate_simpletext("학년-반 정보가 누락되었습니다. 포함하여 다시 질문해주세요.")])
        
        if "timetable_column" in lst_params:
            time_column = dict_json['action']['params']['timetable_column']
    except:
        logger.log("[TestDDayService] Exception Catched")
        logger.log(traceback.format_exc())
        
        return pack_outputs([SimpleText.generate_simpletext("잘못된 요청입니다.")])