from Processors.ResponseGenerator.OutputsPacker import pack_outputs
from Processors.ResponseGenerator.GenerateOutput import SimpleImage, SimpleText, ListCard

def process(data_manager, logger) -> dict:
    lst_data = data_manager.get_notice()
    
    if len(lst_data) > 0:
        lst_item = []
        
        for i in lst_data:
            lst_item.append(ListCard.generate_listcard_item(i[0], i[1], "https://cataas.com/cat", i[2]))
        
        return pack_outputs(ListCard.generate_listcard("공지사항", "https://source.unsplash.com/random/800x600", lst_item))
    else:
        lst_output = []
        lst_output.append(SimpleText.generate_simpletext("공지사항이 없습니다.\n오신 김에 고양이 사진이나 보고 가세요."))
        lst_output.append(SimpleImage.generate_simpleimage("https://cataas.com/cat", "CaT as a Service"))
        
        return pack_outputs(lst_output)