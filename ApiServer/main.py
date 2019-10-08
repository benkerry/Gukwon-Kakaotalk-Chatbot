import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def healthcheck():
    # 서버의 상태를 표시
    return ""

@app.route("/NoticeService", methods=["POST"])
def notice_service():
    # 공지사항 요청을 처리
    return ""

@app.route("/MealNoticeService", methods=["POST"])
def meal_notice_service():
    # 급식 알림 요청을 처리
    return ""

@app.route("/TimeTableNoticeService", methods=["POST"])
def timetable_notice_service():
    # 시간표 알림 요청을 처리
    retun ""

@app.route("/ScheduleNoticeService", methods=["POST"])
def schedule_notice_service():
    # 학사일정 알림 요청을 처리
    return ""