import flask

from Processors.MysqlConn import Conn
from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import ListCard, SimpleText

def process(logger, dict_json:dict) -> dict:
    str_userval = None
    str_utterance = None

    str_userval = dict_json['userRequest']['user']['id']
    str_utterance = dict_json['userRequest']['utterance']

    if ('[' in str_utterance) and (']' in str_utterance):
        str_authcode = str_utterance.split('[')[1].split(']')[0]
        
        if len(str_authcode) == 6:
            connector = Conn()

            connector.cursor.execute("SELECT COUNT(*) AS cnt FROM auth_code WHERE auth_code='{0}'".format(str_authcode))
            result_cnt = connector.cursor.fetchone()[0]

            if result_cnt == 1:
                connector.cursor.execute("DELETE FROM auth_code WHERE auth_code='{0}'".format(str_authcode))
                connector.cursor.execute("INSERT INTO authed_user VALUES('{0}', '')".format(str_userval))
                connector.conn.commit()
                connector.conn.close()

                logger.log("[AuthService] Auth Success!")
                return pack_outputs([SimpleText.generate_simpletext("인증 성공!")])
            else:
                logger.log("[AuthService] Auth Fail")
                str_error = "인증 번호가 틀렸거나 입력 형식이 잘못되었습니다.\n\n(입력 예시: \"[123456] 인증해줘.\")"
                return pack_outputs([SimpleText.generate_simpletext(str_error)])
        else:
            logger.log("[AuthService] Auth Fail")
            str_error = "인증 번호가 틀렸거나 입력 형식이 잘못되었습니다.\n\n(입력 예시: \"[123456] 인증해줘.\")"
            return pack_outputs([SimpleText.generate_simpletext(str_error)])
    else:
        logger.log("[AuthService] Auth Fail")
        str_error = "입력 형식이 잘못되었습니다.\n\n(입력 예시: \"[123456] 인증해줘.\")"
        return pack_outputs([SimpleText.generate_simpletext(str_error)])