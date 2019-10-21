import json
import requests

json_0 = {}
json_1 = {}

with open("test_data/Notice/1.json", encoding="UTF-8") as fp:
    json_0 = json.load(fp)

with open("test_data/Notice/2.json", encoding="UTF-8") as fp:
    json_1 = json.load(fp)

rsp_0 = requests.post("0.0.0.0:5000/NoticeService", json=json_0)
rsp_1 = requests.post("0.0.0.0:5000/NoticeService", json=json_1)

print("첫 번째 응답:\n", rsp_0.text())
print("\n\n\n")
print("두 번째 응답:\n", rsp_1.text())