import json
import flask

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, logger, dict_json:dict) -> dict:
    str_name = None
    str_userval = dict_json['userRequest']['user']['id']
    lst_params = dict_json['action']['params'].keys()

    logger.log("[SetDeaultName] Default Name setting req inbouded.")

    if not "teacher_name" in lst_params:
        str_output0 = "이름이 누락되었거나, 등록되어 있지 않은 이름입니다. 이름을 포함하여 다시 요청하시거나, 개발자에게 문의해주세요."
        str_output1 = "기본 이름을 등록하시려면 '홍길* 기본 이름으로 설정'과 같이 말씀해주세요."
        return pack_outputs([SimpleText.generate_simpletext(str_output0), SimpleText.generate_simpletext(str_output1)])
    else:
        str_name = dict_json['action']['params']['teacher_name']

    str_sql = "SELECT COUNT(*) FROM user_info WHERE user_val='{0}'"
    rowcount = data_manager.mysql_query(str_sql.format(str_userval)).fetchone()[0]

    if rowcount == 0:
        str_sql = "INSERT INTO user_info(user_val, _class, _name) VALUES(%s, '0', %s)"
        data_manager.mysql_query(str_sql, (str_userval, str_name))
        return pack_outputs(SimpleText.generate_simpletext("등록 완료했습니다."))
    elif rowcount == 1:
        str_sql = "UPDATE user_info SET _name = %s WHERE user_val = %s"
        data_manager.mysql_query(str_sql, (str_name, str_userval))
        return pack_outputs(SimpleText.generate_simpletext("등록 완료되었습니다."))
    else:
        raise