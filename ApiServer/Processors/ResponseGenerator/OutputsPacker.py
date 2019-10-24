from flask import jsonify

def pack_outputs(lst_outputs:list) -> dict:
    dict_result = {
        "version": "2.0",
        "template": {
            "outputs": [
            ]
        }
    }

    for i in lst_outputs:
        dict_result['template']['outputs'].append(i)

    return jsonify(dict_result)