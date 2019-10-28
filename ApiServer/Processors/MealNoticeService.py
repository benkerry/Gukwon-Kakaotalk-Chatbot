import json
import flask

from datetime import datetime, timedelta

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, logger, dict_json:dict) -> dict:
    str_date = None
    str_mealtime = None

    str_date = dict_json['action']['params']['date']
    str_mealtime = dict_json['action']['params']['meal_time']

    logger.log("[MealNoticeService] MealService Query Inbounded")

    cur_datetime = datetime.now()

    is_strdate_today = str_date == "오늘"
    is_date_setted = not is_strdate_today
    is_strmealtime_justmeal = str_mealtime == "급식"

    if is_date_setted:
        dict_tmp = json.loads(str_date)
        
        str_date = dict_tmp['date']
        lst_date_elements = str_date.split('-')

        req_datetime = datetime(int(lst_date_elements[0]), int(lst_date_elements[1]), int(lst_date_elements[2]))

        is_strdate_today = (cur_datetime - req_datetime).days == 0    

    if is_strdate_today and is_strmealtime_justmeal: # 급식 알려줘 or 오늘 급식 알려줘
        str_time = cur_datetime.strftime("%H%M")

        while str_time[0] == '0':
            str_time = str_time[1:]

        now_time = int(str_time)

        if now_time >= 0 and now_time < 730:
            str_mealtime = "조식"
        elif now_time >= 730 and now_time < 1315:
            str_mealtime = "중식"
        elif now_time >= 1315 and now_time < 1830:
            str_mealtime = "석식"
        else:
            return pack_outputs([SimpleText.generate_simpletext("오늘 배식은 종료되었어요.")])

        str_date = "20" + cur_datetime.strftime("%y-%m-%d")
    elif is_strdate_today: # 오늘 (조식, 중식, 석식) 알려줘 or (조식, 중식, 석식) 알려줘
        if not is_date_setted:
            str_date = "20" + cur_datetime.strftime("%y-%m-%d")
    elif is_strmealtime_justmeal: # 언제언제 급식 알려줘
        str_mealtime = "중식"

    lst_meal = data_manager.get_meal(str_date, str_mealtime)
    str_output = None

    if len(lst_meal) == 0:
        str_output = "해당일의 급식 정보가 없어요."
    else:
        str_output = "{0}일 {1} 메뉴는 다음과 같아요.\n\n".format(str_date, str_mealtime)
        for i in lst_meal:
            str_output += "- {0}\n".format(i)

    return pack_outputs([SimpleText.generate_simpletext(str_output)])