import json
import flask

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, logger, dict_json:dict) -> dict:
    str_sql = "DELETE FROM user_info WHERE user_val = '{0}'".format(dict_json['userRequest']['user']['id'])
    data_manager.mysql_query(str_sql)

    logger.log("[Truncate] Req Inbounded.")

    return pack_outputs(SimpleText.generate_simpletext("초기화 완료"))