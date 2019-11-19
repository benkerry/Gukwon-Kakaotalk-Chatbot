from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

def process(data_manager, db_manager, logger, dict_json:dict) -> dict:
    str_userval = None
    str_utterance = None

    str_userval = dict_json['userRequest']['user']['id']
    str_utterance = dict_json['userRequest']['utterance']

    if (('[' in str_utterance) and (']' in str_utterance)) and (str_utterance.find('[') < str_utterance.find(']')):
        str_authcode = str_utterance.split('[')[1].split(']')[0].upper()
        
        if len(str_authcode) == 6:
            result_cnt = db_manager.mysql_query("SELECT COUNT(*) AS cnt FROM auth_code WHERE auth_code='{0}'".format(str_authcode)).fetchone()[0]

            if result_cnt == 1:
                lst_sql = [
                    "DELETE FROM auth_code WHERE auth_code='{0}'".format(str_authcode),
                    "INSERT INTO authed_user VALUES('{0}', '')".format(str_userval)
                ]

                db_manager.mysql_query(lst_sql)

                logger.log("[AuthService] Auth Success!")
                return pack_outputs(SimpleText.generate_simpletext("인증 성공!"))
            elif result_cnt == 0:
                logger.log("[AuthService] Auth Fail")
                lst_output = []
                lst_output.append(SimpleText.generate_simpletext("인증 번호가 틀렸거나 입력 형식이 잘못되었습니다."))
                lst_output.append(SimpleText.generate_simpletext("입력 예시: '[123456] 인증해줘.'"))
                return pack_outputs(lst_output)
            else:
                raise
        else:
            logger.log("[AuthService] Auth Fail")
            lst_output = []
            lst_output.append(SimpleText.generate_simpletext("인증 번호가 틀렸거나 입력 형식이 잘못되었습니다."))
            lst_output.append(SimpleText.generate_simpletext("입력 예시: '[123456] 인증해줘.'"))
            return pack_outputs(lst_output)
    else:
        lst_output = []
        lst_output.append(SimpleText.generate_simpletext("인증 번호가 틀렸거나 입력 형식이 잘못되었습니다."))
        lst_output.append(SimpleText.generate_simpletext("입력 예시: '[123456] 인증해줘.'"))
        return pack_outputs(lst_output)