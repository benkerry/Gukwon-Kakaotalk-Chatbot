import flask
from datetime import datetime

from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import ListCard, SimpleText

def process(data_manager, logger, dict_json:dict) -> dict:
    str_userval = None
    str_utterance = None

    str_userval = dict_json['userRequest']['user']['id']
    str_utterance = dict_json['userRequest']['utterance']

    logger.log("[SuggestionService] Suggestion Request Inbounded.")
    
    cursor = data_manager.mysql_query("SELECT * FROM authed_user WHERE user_val='{0}'".format(str_userval))

    if cursor.rowcount == 0:
        lst_output = []
        lst_output.append(SimpleText.generate_simpletext("아직 구성원 인증을 하지 않았습니다."))
        lst_output.append(SimpleText.generate_simpletext("구성원 인증을 하시려면 '[6자리 인증번호] 인증해줘'와 같이 말씀하세요."))
        return pack_outputs(lst_output)
    elif cursor.rowcount == 1:
        if ('(' in str_utterance and ')' in str_utterance) and (str_utterance.find('(') < str_utterance.find(')')):
            lst_temp = str_utterance.split(")")
            str_temp = ""

            for i in range(len(lst_temp) - 1):
                str_temp += lst_temp[i]
            
            lst_temp = str_temp.split("(")
            str_description = ""
            for i in range(1, len(lst_temp)):
                str_description += lst_temp[i]
            
            str_sql = "INSERT INTO suggestion(user_val, description, status, num_signs, open_datetime) VALUES(%s, %s, %d, %d, %s)"
            tup_sql = (str_userval, str_utterance, 0, 0, datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
            data_manager.mysql_query(str_sql, tup_sql)
            
            str_sql = "SELECT idx FROM suggestion WHERE user_val='{0}' AND description = '{1}' AND status = 0".format(str_userval, str_description)
            issue_number = data_manager.mysql_query(str_sql).fetchone()[0]

            return pack_outputs(SimpleText.generate_simpletext("#{0}번 이슈로 등록되었습니다! 관리자의 승인을 기다리고 있습니다.".format(issue_number)))
        elif '#' in str_utterance:
            str_sug_idx = str_utterance.split('#')[1]
            numeric_idx_end = 1
            
            for i in str_sug_idx:
                if i.isdecimal():
                    numeric_idx_end += 1
                else:
                    break

            if numeric_idx_end == 0:
                lst_output = []
                lst_output.append(SimpleText.generate_simpletext("입력 형식이 잘못되었습니다."))
                lst_output.append(SimpleText.generate_simpletext("발화 예시: #31번 건의 동의합니다."))
                return pack_outputs(lst_output)
            else:
                str_sug_idx = str_sug_idx[:numeric_idx_end]

                str_sql = "SELECT status FROM suggestion WHERE idx = '{0}'".format(str_sug_idx)
                cursor = data_manager.mysql_query(str_sql)
                
                if not cursor.fetchone()[0] == 1:
                    return pack_outputs(SimpleText.generate_simpletext("닫힌 건의입니다."))

                str_sql = "SELECT signed_suggestion FROM authed_user WHERE user_val='{0}'".format(str_userval)
                cursor = data_manager.mysql_query(str_sql)
                lst_signed = cursor.fetchone()[0].split(':')

                if str_sug_idx in lst_signed:
                    return pack_outputs(SimpleText.generate_simpletext("이미 해당 건의에 동의하셨습니다."))
                else:
                    str_signed = ""
                    
                    for i in lst_signed:
                        str_signed += i + ":"
                    str_signed = str_signed[:-1]

                    lst_sql = []
                    lst_sql.append("UPDATE suggestion SET num_signs = num_signs + 1 WHERE idx = {0}".format(str_sug_idx))
                    lst_sql.append("UPDATE user_info SET signed_suggestion='{0}' WHERE user_val = '{1}'".format(str_signed, str_userval))
                    data_manager.mysql_query(lst_sql)

                    return pack_outputs(SimpleText.generate_simpletext("#{0}번 건의에 동의하셨습니다!".format(str_sug_idx)))
        else:
            lst_output = []
            lst_output.append(SimpleText.generate_simpletext("필수 기호('(', ')')가 누락되었거나 입력 형식이 잘못되었습니다. 필수 기호로 건의 내용을 감싸서 다시 제보해주세요."))
            str_output = "# 건의 방법\n"
            str_output += "발화 예시: (국밥 사주세요.)라고 건의해줘!\n"
            str_output += "#건의 추천 방법\n"
            str_output += "발화 예시: #31번 건의에 동의합니다.\n\n"
            str_output += "건의 열람은 누구나 가능하지만 건의 등록, 건의 추천은 구성원 인증이 완료된 사용자만 가능합니다."
            lst_output.append(SimpleText.generate_simpletext(str_output))
            return pack_outputs(lst_output)
    else:
        raise