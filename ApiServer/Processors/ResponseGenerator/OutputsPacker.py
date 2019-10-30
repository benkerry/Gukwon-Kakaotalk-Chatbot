from flask import jsonify

def pack_outputs(output) -> dict:
    dict_result = {
        "version": "2.0",
        "template": {
            "outputs": [
            ]
        }
    }

    if str(type(output)) == "<class 'list'>":
        dict_result['template']['outputs'] = output
    else:
        dict_result['template']['outputs'].append(output)

    return jsonify(dict_result)