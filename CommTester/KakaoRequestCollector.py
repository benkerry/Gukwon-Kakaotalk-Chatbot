import os
import json
import random
from flask import Flask, request, make_response

str_charpool = "abcdefghijklmnopqrstuwxyz"

app = Flask(__name__)

@app.route("/")
def collector():
    str_fname = ""

    while True:
        for i in range(6):
            str_fname += random.choice(str_charpool)
        
        str_fname += ".json"
        
        if not os.path.isfile(str_fname):
            break

    with open(str_fname, 'w') as fp:
        json.dump(request.get_json(), fp, sort_keys=True, indent=4, ensure_ascii=False)
    
    return make_response({"test":"테스트용 스킬입니다."})

if __name__ == "__main__":
    app.run()