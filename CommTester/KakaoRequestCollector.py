import os
import json
import random
from flask import Flask, request, jsonify

str_charpool = "abcdefghijklmnopqrstuwxyz"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = True

@app.route("/", methods=["POST", "GET"])
def collector():
    str_fname = "data/"

    while True:
        for i in range(6):
            str_fname += random.choice(str_charpool)
        
        str_fname += ".json"
        
        if not os.path.isfile(str_fname):
            break

    with open(str_fname, 'w', encoding="UTF-8") as fp:
        json.dump(request.get_json(), fp, ensure_ascii=False, sort_keys=True, indent=4)
    
    return jsonify("{'hi':'안뇽'}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)