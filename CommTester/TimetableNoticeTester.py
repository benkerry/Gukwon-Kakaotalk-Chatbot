import json
import requests

lst_json = []
lst_rsp = []

# '학년-반' 형태의 반 정보와 함께, 해당 반의 2교시를 요청
with open("test_data/TimeTable/ReqWithNotSplitedGradeClass_2Time.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

# '학년-반' 형태의 반 정보와 함께, 해당 반의 전체 시간표를 요청
with open("test_data/TimeTable/ReqWithNotSplitedGradeClass_All.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

# 학년, 반 정보를 별도로 전달하며 해당 반의 전체 시간표를 요청
with open("test_data/TimeTable/ReqWithSplitedGradeClass_All.json", encoding="UTF-8") as fp:
    lst_json.append(json.load(fp))

for i in lst_json:
    lst_rsp.append(requests.post("http://127.0.0.1:5000/timetable-notice-service", json=i).text)

# 아무 데이터도 안 넘겨주는 경우도 테스트 해볼 것
lst_rsp.append(requests.post("http://127.0.0.1:5000/timetable-notice-service", text="^^7").text)

num_rsp = len(lst_rsp)

for i in range(num_rsp):
    if i < (num_rsp - 1):
        print(i, "번째 응답:\n", lst_rsp[i])
        print("\n\n\n")
    else:
        print("잘못된 요청에 대한 응답:\n", lst_rsp[i])