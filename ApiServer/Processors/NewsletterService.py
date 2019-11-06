from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import SimpleImage, SimpleText, ListCard

def process(data_manager, logger) -> dict:
    lst_data = data_manager.get_newsletter()

    logger.log("[NewsletterService] Query Inbounded!")
    
    if len(lst_data) > 0:
        lst_item = []
        
        for i in lst_data:
            lst_item.append(ListCard.generate_listcard_item(i[0], i[1], "https://cataas.com/cat", i[2]))
        
        lst_output = []
        lst_output.append(ListCard.generate_listcard("가정통신문(최근 한달)", "https://source.unsplash.com/random/800x600", lst_item[:5]))
        lst_output.append(SimpleText.generate_simpletext("전체 가정통신문은 다음 링크에서 확인하실 수 있습니다."))
        lst_output.append(SimpleText.generate_simpletext("http://school.cbe.go.kr/gukwon-h/M010606/list"))
        return pack_outputs(lst_output)
    else:
        return pack_outputs(SimpleText.generate_simpletext("최근 한달의 가정통신문이 없습니다."))