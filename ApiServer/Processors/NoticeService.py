from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import SimpleImage, SimpleText, ListCard

def process(data_manager, logger) -> dict:
    lst_notice = data_manager.get_notice()
    lst_chatbotnotice = data_manager.get_chatbotnotice()
    lst_output = []

    logger.log("[NoticeService] Query Inbounded!")
    
    if len(lst_notice) > 0:
        lst_item = []
        for i in lst_notice:
            lst_item.append(ListCard.generate_listcard_item(i[0], i[1], "https://cataas.com/cat", i[2]))
        
        lst_output.append(ListCard.generate_listcard("국원고 공지사항(최근 한달)", "https://source.unsplash.com/random/800x600", lst_item[:5]))

    if len(lst_chatbotnotice) > 0:
        lst_item = []
        for i in lst_chatbotnotice:
            lst_item.append(ListCard.generate_listcard_item(i[0], i[1], "https://cataas.com/cat", i[2]))
        
        lst_output.append(ListCard.generate_listcard("학생회 공지사항(최근 한달)", "https://source.unsplash.com/random/800x600", lst_item[:5]))

    str_output = "전체 공지사항은 다음 링크에서 확인하실 수 있습니다.\n\n"
    str_output += "국원고 공지사항: http://school.cbe.go.kr/gukwon-h/M010301/list\n\n"
    str_output += "학생회 공지사항: http://school.cbe.go.kr/gukwon-h/M010406/list"
    lst_output.append(SimpleText.generate_simpletext(str_output))

    if len(lst_notice) == 0 and len(lst_chatbotnotice) == 0:
        return pack_outputs(SimpleText.generate_simpletext("최근 한달간의 공지사항이 없습니다."))
    else:
        return pack_outputs(lst_output)