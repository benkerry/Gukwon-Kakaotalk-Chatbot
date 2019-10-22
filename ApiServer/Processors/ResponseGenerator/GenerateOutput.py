class ListCard:
    def listcard_item_generator(self, str_title, str_description, str_img_url, str_url):
        dict_item = {}
        dict_item['title'] = str_title
        dict_item['description'] = str_description
        dict_item['imageUrl'] = str_img_url
        dict_item['link'] = {'web':str_url}

        return dict_item

    def generate_listcard(self, str_header_title, str_img_url, lst_items):
        dict_output = {}
        dict_output['listCard'] = {}
        dict_output['listCard']['header'] = {'title':str_header_title, 'imageUrl':str_img_url}
        dict_output['listCard']['items'] = []

        for i in lst_items:
            dict_output['listCard']['items'].append(i)

        return dict_output

class SimpleText:
    def generate_simpletext(self, str_msg):
        dict_output = {}
        dict_output['simpleText'] = {}
        dict_output['simpleText']['text'] = str_msg

        return dict_output