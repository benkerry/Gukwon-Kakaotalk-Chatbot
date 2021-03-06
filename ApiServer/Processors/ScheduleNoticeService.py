import json
import flask

from datetime import datetime, timedelta

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

# 작성중
def process(data_manager, logger, dict_json:dict) -> dict:
    str_major_event = None
    str_period = None

    dict_period = None

    str_major_event = dict_json['action']['params']['major_event']
    str_period = dict_json['action']['params']['sys_date_period']

    logger.log("[ScheduleNoticeService] Query Inbounded!")

    is_thismonth = str_period == "이번 달"

    lst_schedules = []

    if str_major_event != "0":
        if str_major_event == "봉인해제":
            today = datetime.today()
            thrid = datetime(today.year + 1, 1, 1)
            second = datetime(today.year + 2, 1, 1)
            freshman = datetime(today.year + 3, 1, 1)

            str_output = "여러분들의 봉인해제는\n\n"
            str_output += "3학년 기준 {0}일\n".format((thrid - today).days)
            str_output += "2학년 기준 {0}일\n".format((second - today).days)
            str_output += "1학년 기준 {0}일 ".format((freshman - today).days)
            str_output += "남았습니다."

            return pack_outputs(SimpleText.generate_simpletext(str_output))
        else:
            lst_schedules = data_manager.get_schedule_by_name(str_major_event)
    elif is_thismonth:
        str_period = datetime.today().strftime("%y-%m")
        lst_schedules = data_manager.get_schedule_monthly(str_period)
    else:
        dict_tmp = json.loads(str_period)
        lst_token = dict_tmp['from']['date'].split('-')
        lst_schedules = data_manager.get_schedule_monthly(lst_token[0] + '-' + lst_token[1])

    if len(lst_schedules) > 0:
        lst_schedules.sort(key=lambda x:x[0])
        str_output = "학사일정 검색 결과는 다음과 같습니다.\n\n"

        for i in lst_schedules:
            str_output += "# {0}일\n".format(i[0])

            for k in i[1]:
                str_output += "- {0}\n".format(k)

            str_output += "\n"

        return pack_outputs(SimpleText.generate_simpletext(str_output))
    else:
        return pack_outputs(SimpleText.generate_simpletext("해당 기간에 등록된 학사일정이 없어요."))
