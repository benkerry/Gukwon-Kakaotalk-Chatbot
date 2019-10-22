import json
import requests

def run_test():
    json_0 = {}
    json_1 = {}
    json_2 = {}
    json_3 = {}
    json_4 = {}

    with open("test_data/MealNotice/Breakfast.json", encoding="UTF-8") as fp:
        json_0 = json.load(fp)

    with open("test_data/MealNotice/Dinner.json", encoding="UTF-8") as fp:
        json_1 = json.load(fp)

    with open("test_data/MealNotice/JustMeal.json", encoding="UTF-8") as fp:
        json_2 = json.load(fp)

    with open("test_data/MealNotice/Lunch.json", encoding="UTF-8") as fp:
        json_3 = json.load(fp)

    with open("test_data/MealNotice/Invalid.json", encoding="UTF-8") as fp:
        json_4 = json.load(fp)

    rsp_0 = requests.post("http://127.0.0.1:5000/meal-notice-service", json=json_0)
    rsp_1 = requests.post("http://127.0.0.1:5000/meal-notice-service", json=json_1)
    rsp_2 = requests.post("http://127.0.0.1:5000/meal-notice-service", json=json_2)
    rsp_3 = requests.post("http://127.0.0.1:5000/meal-notice-service", json=json_3)
    rsp_4 = requests.post("http://127.0.0.1:5000/meal-notice-service", json=json_4)
    rsp_5 = requests.post("http://127.0.0.1:5000/meal-notice-service", text="^^7")

    print("10월 25일 조식 요청에 대한 응답:\n", rsp_0.text)
    print("\n\n\n")
    print("9월 3일 석식 요청에 대한 응답:\n", rsp_1.text)
    print("\n\n\n")
    print("그냥 밥 알려달라고 했을 때의 응답:\n", rsp_2.text)
    print("\n\n\n")
    print("11월 18일 점심 요청에 대한 응답:\n", rsp_3.text)
    print("\n\n\n")
    print("일부 원소가 누락된 요청에 대한 응답:\n", rsp_4.text)
    print("\n\n\n")
    print("여러모로 맛이 간 요청에 대한 응답:\n", rsp_5.text)

def custom_test():
    month = input("월 입력(format:MM)>> ")
    day = input("일 입력(format:DD)>> ")

    str_date = "2019" + month + day
    mealtime = input("조식/중식/석식 입력>> ")

    dict_json = {}

    with open("test_data/MealNotice/Lunch.json", encoding="UTF-8") as fp:
        dict_json = json.load(fp)

    dict_json['params']['date']['date'] = str_date
    dict_json['params']['meal_time'] = mealtime

    rsp = requests.post("http://127.0.0.1:5000/meal-notice-service", json=dict_json)

    print("응답:\n", rsp.text)


print("1. 일반 모드\n")
print("2. 요청 커스텀\n\n")
mode = input("모드 선택>> ")

if mode == "1":
    run_test()
elif mode == "2":
    custom_test()
else:
    print("잘못 선택함!")