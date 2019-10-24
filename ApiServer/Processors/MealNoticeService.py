import json
import flask
import traceback

from datetime import datetime, timedelta

from ResponseGenerator.GenerateOutput import SimpleText
from ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, request:flask.Request, logger) -> dict:
    dict_json = None
    str_date = None
    str_mealtime = None

    try:
        dict_json = request.json

        str_date = dict_json['action']['params']['date']
        str_mealtime = dict_json['action']['params']['meal_time']
    except:
        logger.log("[MealNoticeService] Exception Catched")
        logger.log(traceback.format_exc())
        
        return pack_outputs([SimpleText.generate_simpletext("잘못된 요청입니다.")])

    cur_datetime = datetime.now()

    is_strdate_today = str_date == "오늘"
    is_strmealtime_justmeal = str_mealtime == "급식"

    if not is_strdate_today:
        str_date = json.loads(str_date)['date']

    if is_strdate_today and is_strmealtime_justmeal:
        str_time = cur_datetime.strftime("%H%M")

        while str_time[0] == '0':
            str_time = str_time[1:]

        now_time = int(str_time)

        if now_time >= 0 and now_time < 730:
            str_mealtime = "조식"
        elif now_time >= 730 and now_time < 1315:
            str_mealtime = "중식"
        elif now_time >= 1315 and now_time < 1820:
            str_mealtime = "석식"
        else:
            str_mealtime = "조식"
            cur_datetime += timedelta(1)

        str_date = cur_datetime.strftime("%y-%m-%d")
    elif is_strmealtime_justmeal:
        pass
    elif is_strmealtime_justmeal:
        pass
    else