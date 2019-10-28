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
        
        lst_output.append(ListCard.generate_listcard("국원고 공지사항(최근 한달)", "https://source.unsplash.com/random/800x600", lst_item))

    if len(lst_chatbotnotice) > 0:
        lst_item = []
        for i in lst_chatbotnotice:
            lst_item.append(ListCard.generate_listcard_item(i[0], i[1], "https://cataas.com/cat", i[2]))
        
        lst_output.append(ListCard.generate_listcard("학생회 공지사항(최근 한달)", "https://source.unsplash.com/random/800x600", lst_item))

    if len(lst_notice) and len(lst_chatbotnotice):
        return pack_outputs([SimpleText.generate_simpletext("최근 한달간의 공지사항이 없습니다.")])
    else:
        return pack_outputs(lst_output)