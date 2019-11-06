import json

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, logger, dict_json:dict) -> dict:
    str_class = None
    str_userval = dict_json['userRequest']['user']['id']
    lst_params = dict_json['action']['params'].keys()

    logger.log("[SetDeaultClass] Default Class setting req inbouded.")

    if "grade-class" in lst_params:
        str_class = dict_json['action']['params']['grade-class']
    elif "grade" in lst_params and "class" in lst_params:
        str_class = str(dict_json['action']['params']['grade']) + '-' + str(dict_json['action']['params']['class'])
    else:
        str_output0 = "학년-반 정보가 누락되었어요. 포함해서 다시 요청해주세요."
        str_output1 = "기본 학급을 설정하시려면 '3학년 4반 기본 학급으로 설정해줘'와 같이 말씀해주세요."
        return pack_outputs([SimpleText.generate_simpletext(str_output0), SimpleText.generate_simpletext(str_output1)])

    str_sql = "SELECT COUNT(*) FROM user_info WHERE user_val='{0}'"
    rowcount = data_manager.mysql_query(str_sql.format(str_userval)).fetchone()[0]
    
    if rowcount == 0:
        str_sql = "INSERT INTO user_info(user_val, _class, _name) VALUES(%s, %s, '0')"
        data_manager.mysql_query(str_sql, (str_userval, str_class))
        return pack_outputs(SimpleText.generate_simpletext("등록 완료했습니다."))
    elif rowcount == 1:
        str_sql = "UPDATE user_info SET _class = %s WHERE user_val = %s"
        data_manager.mysql_query(str_sql, (str_class, str_userval))
        return pack_outputs(SimpleText.generate_simpletext("등록 완료했습니다."))
    else:
        raise