import json
import requests

json_0 = {}
json_1 = {}

with open("test_data/Notice/1.json", encoding="UTF-8") as fp:
    json_0 = json.load(fp)

with open("test_data/Notice/2.json", encoding="UTF-8") as fp:
    json_1 = json.load(fp)

rsp_0 = requests.post("http://127.0.0.1:5000/notice-service", json=json_0)
rsp_1 = requests.post("http://127.0.0.1:5000/notice-service", json=json_1)
rsp_2 = requests.post("http://127.0.0.1:5000/notice-service", text="^^7")

print("첫 번째 응답:\n", rsp_0.text())
print("\n\n\n")
print("두 번째 응답:\n", rsp_1.text())
print("\n\n\n")
print("잘못된 요청에 대한 응답:\n", rsp_2.text())