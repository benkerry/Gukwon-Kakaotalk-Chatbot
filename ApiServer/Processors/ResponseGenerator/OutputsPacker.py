def pack_outputs(lst_outputs):
    dict_result = {}

    dict_result['version'] = 1.0

    dict_result['template'] = {}
    dict_result['template']['outputs'] = []

    for i in lst_outputs:
        dict_result['template']['outputs'].append(i)

    return dict_result