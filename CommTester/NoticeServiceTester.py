import json
import requests

json_0 = {}
json_1 = {}

# 특별할 거 없는 요청 두 개
with open("test_data/Notice/1.json", encoding="UTF-8") as fp:
    json_0 = json.load(fp)

with open("test_data/Notice/2.json", encoding="UTF-8") as fp:
    json_1 = json.load(fp)

rsp_0 = requests.post("http://127.0.0.1:5000/notice-service", json=json_0)
rsp_1 = requests.post("http://127.0.0.1:5000/notice-service", json=json_1)

# 아무 데이터도 안 넘겨주는 경우도 테스트 해볼 것
rsp_2 = requests.post("http://127.0.0.1:5000/notice-service", text="^^7")

print("첫 번째 응답:\n", rsp_0.text())
print("\n\n\n")
print("두 번째 응답:\n", rsp_1.text())
print("\n\n\n")
print("잘못된 요청에 대한 응답:\n", rsp_2.text())