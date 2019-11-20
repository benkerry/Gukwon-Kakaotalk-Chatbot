from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import ListCard, SimpleText

def process(db_manager, logger) -> dict:
    str_sql = "SELECT idx, description, status, num_signs FROM suggestion WHERE status > 0 ORDER BY idx ASC"
    cursor = db_manager.mysql_query(str_sql)

    lst_open = []
    lst_close = []
    for i in cursor:
        lst_appender = []
        lst_appender.append('#{0}번 건의(동의: {1}개)'.format(i[0], i[3]))
        lst_appender.append(i[1][:30])
        lst_appender.append("https://cataas.com/cat")
        lst_appender.append("https://web.gukwonchatbot.ml/SuggestionViewer/SuggestionViewer.php?idx={0}".format(i[0]))
        
        if i[2] == 1:
            lst_open.append(lst_appender) 
        elif i[2] == 2:
            lst_close.append(lst_appender)

    lst_output = []
    
    if len(lst_open) > 0:
        lst_carditem_open = []
        for i in lst_open:
            lst_carditem_open.append(ListCard.generate_listcard_item(i[0], i[1], i[2], i[3]))
        lst_output.append(ListCard.generate_listcard("열린 건의", "https://source.unsplash.com/random/800x600", lst_carditem_open[:5]))
    else:
        lst_output.append(SimpleText.generate_simpletext("열린 건의가 없습니다."))

    if len(lst_close) > 0:
        lst_carditem_close = []
        for i in lst_close:
            lst_carditem_close.append(ListCard.generate_listcard_item(i[0], i[1], i[2], i[3]))
        lst_output.append(ListCard.generate_listcard("닫힌 건의", "https://source.unsplash.com/random/800x600", lst_carditem_close[:5]))
    else:
        lst_output.append(SimpleText.generate_simpletext("닫힌 건의가 없습니다."))

    str_output = "전체 건의 리스트는 다음 링크에서 확인하실 수 있습니다.\n\n"
    str_output += ">> https://web.gukwonchatbot.ml/SuggestionViewer/index.php\n\n"
    str_output += "# 건의 방법\n"
    str_output += "발화 예시: (국밥 사주세요.)라고 건의해줘!\n\n"
    str_output += "#건의 추천 방법\n"
    str_output += "발화 예시: #31번 건의에 동의합니다.\n\n"
    str_output += "건의 열람은 누구나 가능하지만 건의 등록, 건의 추천은 구성원 인증이 완료된 사용자만 가능합니다."
    lst_output.append(SimpleText.generate_simpletext(str_output))
    return pack_outputs(lst_output)