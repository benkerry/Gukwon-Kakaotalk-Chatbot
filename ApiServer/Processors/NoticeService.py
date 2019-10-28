from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import SimpleImage, SimpleText, ListCard

def process(data_manager, logger) -> dict:
    lst_data = data_manager.get_notice()
    
    logger.log("[NoticeService] Query Inbounded!")
    
    if len(lst_data) > 0:
        lst_item = []
        
        for i in lst_data:
            lst_item.append(ListCard.generate_listcard_item(i[0], i[1], "https://cataas.com/cat", i[2]))
        
        return pack_outputs([ListCard.generate_listcard("공지사항(최근 한달)", "https://source.unsplash.com/random/800x600", lst_item)])
    else:
        return pack_outputs([SimpleText.generate_simpletext("최근 한달의 공지사항이 없습니다.")])