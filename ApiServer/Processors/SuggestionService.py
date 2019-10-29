import flask

from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import ListCard, SimpleText

def process(data_manager, logger, dict_json:dict) -> dict:
    str_userval = None
    str_utterance = None

    str_userval = dict_json['userRequest']['user']['id']
    str_utterance = dict_json['userRequest']['utterance']
    
    num_authed = data_manager.mysql_query("SELECT COUNT(*) FROM authed_user WHERE user_val='{0}'".format(str_userval)).fetchone()[0]

    if num_authed == 0:
        pass
    elif num_authed == 1:
        pass
    else:
        return pack_outputs(SimpleText.generate_simpletext("서버 오류가 발생했습니다."))