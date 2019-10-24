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

    if str_testtype == "시험":
        # 중간/기말 여부 판별
        pass

    if str_testtype == "중간고사":
        pass
    elif str_testtype == "기말고사":
        pass
    elif str_testtype == "영어듣기능력평가":
        pass
    else:
        pass