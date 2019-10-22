def listcard_item_generator(str_title, str_uploaddate, str_img_url, str_url):
    dict_item = {}
    dict_item['title'] = str_title
    dict_item['description'] = str_uploaddate
    dict_item['imageUrl'] = str_img_url
    dict_item['link'] = {'web':str_url}

    return dict_item

def listcard(str_header_title, str_img_url, lst_items):
    dict_output = {}
    dict_output['listCard'] = {}
    dict_output['listCard']['header'] = {'title':str_header_title, 'imageUrl':str_img_url}
    dict_output['listCard']['items'] = []

    for i in lst_items:
        dict_output['listCard']['items'].append(i)

    return dict_output

def simpletext(str_msg):
    dict_output = {}
    dict_output['simpleText'] = {}
    dict_output['simpleText']['text'] = str_msg

    return dict_output

def pack_outputs(lst_outputs):
    dict_result = {}

    dict_result['version'] = 1.0

    dict_result['template'] = {}
    dict_result['template']['outputs'] = []

    for i in lst_outputs:
        dict_result['template']['outputs'].append(i)

    return dict_result