import json
import ServerLogger
import DataManager.main as DataManager

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def healthcheck():
    # HealthCheck 응답
    return "Fine Working!"

@app.route("/notice-service", methods=["POST"])
def notice_service():
    # 공지사항 요청을 처리
    global data_manager
    return "공지사항 요청을 처리"

@app.route("/meal-notice-service", methods=["POST"])
def meal_notice_service():
    # 급식 알림 요청을 처리
    global data_manager
    return "급식 알림 요청을 처리"

@app.route("/test-dday-service", methods=["POST"])
def test_dday_service():
    # 시험 디데이 요청을 처리
    global data_manager
    return "시험 디데이 요청을 처리"

@app.route("/timetable-notice-service", methods=["POST"])
def timetable_notice_service():
    # 시간표 알림 요청을 처리
    global data_manager
    return "시간표 알림 요청을 처리"

@app.route("/schedule-notice-service", methods=["POST"])
def schedule_notice_service():
    # 학사일정 알림 요청을 처리
    global data_manager
    return "학사일정 알림 요청을 처리"

@app.route("/suggestion-service", methods=["POST"])
def suggestion_service():
    # 건의 요청을 처리(박형진 담당)
    global data_manager
    return "건의 요청을 처리"

app.config['JSON_AS_ASCII'] = False

logger = ServerLogger.Logger()
data_manager = DataManager.Manager(logger)
auto_parser = DataManager.AutoParser(data_manager, logger)

app.run(host="0.0.0.0", debug=False)