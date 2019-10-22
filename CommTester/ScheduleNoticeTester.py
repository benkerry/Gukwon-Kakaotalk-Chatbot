import json
import requests

lst_json = []
lst_rsp = []

with open("test_data/Schedule/JobExp.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

with open("test_data/Schedule/JustVacation.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

with open("test_data/Schedule/NextMonthSchedule_Query.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

with open("test_data/Schedule/SemesterOpen.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

with open("test_data/Schedule/SummerVacation.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

for i in lst_json:
    lst_rsp.append(requests.post("http://127.0.0.1:5000/schedule-notice-service", json=i).text)

# 아무 데이터도 안 넘겨주는 경우도 테스트 해볼 것
lst_rsp.append(requests.post("http://127.0.0.1:5000/schedule-notice-service", text="^^7").text)

num_rsp = len(lst_rsp)

for i in range(num_rsp):
    if i < (num_rsp - 1):
        print(i, "번째 응답:\n", lst_rsp[i])
        print("\n\n\n")
    else:
        print("잘못된 요청에 대한 응답:\n", lst_rsp[i])