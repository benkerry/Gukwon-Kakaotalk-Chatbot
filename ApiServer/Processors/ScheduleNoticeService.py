import json
import flask
import traceback

from datetime import datetime, timedelta

from ResponseGenerator.GenerateOutput import SimpleText
from ResponseGenerator.OutputsPacker import pack_outputs

# 작성중
def process(data_manager, request:flask.Request, logger) -> dict:
    dict_json = None

    str_major_event = None
    str_period = None

    dict_period = None

    try:
        dict_json = request.json

        str_major_event = dict_json['action']['params']['major_event']
        str_period = dict_json['action']['params']['sys_date_period']
    except:
        logger.log("[SchedultNoticeServicee] Exception Catched")
        logger.log(traceback.format_exc())
        
        return pack_outputs([SimpleText.generate_simpletext("잘못된 요청입니다.")])

    is_thismonth = str_period == "이번 달"

    lst_schedules = []

    if str_major_event != 0:
        pass

    elif is_thismonth:
        str_period = datetime.today().strftime("%y-%m")
        lst_schedules = data_manager.get_schedule_monthly(str_period)
    else:
        dict_tmp = json.loads(str_period)
        dict_period = {}

        lst_token = dict_tmp['from']['date'].split('-')
        dict_period['start'] = datetime(int(lst_token[0]), int(lst_token[1]), int(lst_token[2]))
        
        lst_token = dict_tmp['to']['date'].split('-')
        dict_period['end'] = datetime(int(lst_token[0]), int(lst_token[1]), int(lst_token[2])) + timedelta(1)

        while dict_period['start'] != dict_period['end']:
            lst_schedules.append(data_manager.get_schedule_daily(dict_period['start'].strftime("%y-%m-%d")))
            dict_period['start'] += timedelta(1)

    if len(lst_schedules) > 0:
        str_output = "말씀하신 기간의 학사일정은 다음과 같습니다.\n\n"
        
        for i in lst_schedules:
            str_output += "# {0}일\n".format(i[0])

            for k in i[1]:
                str_output += "- {0}\n".format(k)

            str_output += "\n"

        return pack_outputs(SimpleText.generate_simpletext(str_output))
    else:
        return pack_outputs(SimpleText.generate_simpletext("해당 기간에 등록된 학사일정이 없어요."))
