import json
import ServerLogger
import DataManager.main as DataManager 

import Processors.AuthService as Auth
import Processors.NoticeService as Notice
import Processors.HealthCheck as HealthCheck
import Processors.TestDDayService as TestDDay
import Processors.SuggestionService as Suggestion
import Processors.MealNoticeService as MealNotice
import Processors.ScheduleNoticeService as ScheduleNotice
import Processors.TimeTableNoticeService as TimeTableNotice

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def healthcheck():
    global logger
    return HealthCheck.process(logger)

@app.route("/notice-service", methods=["POST"])
def notice_service():
    global logger
    global data_manager
    return Notice.process(data_manager, logger)

@app.route("/meal-notice-service", methods=["POST"])
def meal_notice_service():
    global logger
    global data_manager
    return MealNotice.process(data_manager, request, logger)

@app.route("/test-dday-service", methods=["POST"])
def test_dday_service():
    global logger
    global data_manager
    return TestDDay.process(data_manager, request, logger)

@app.route("/timetable-notice-service", methods=["POST"])
def timetable_notice_service():
    global logger
    global data_manager
    return TimeTableNotice.process(data_manager, request, logger)

@app.route("/schedule-notice-service", methods=["POST"])
def schedule_notice_service():
    global logger
    global data_manager
    return ScheduleNotice.process(data_manager, request, logger)

@app.route("/auth-service", methods=["POST"])
def auth_service():
    # 구성원 인증 요청을 처리(박형진 담당)
    # 오류 발생시 오류 메시지 보낼 것
    global logger
    return Auth.process(request, logger)

@app.route("/suggestion-service", methods=["POST"])
def suggestion_service():
    # 건의 요청을 처리(박형진 담당)
    # 오류 발생시 오류 메시지 보낼 것
    global logger
    return Suggestion.process(request, logger)

app.config['JSON_AS_ASCII'] = False

logger = ServerLogger.Logger()
data_manager = DataManager.Manager(logger)
auto_parser = DataManager.AutoParser(data_manager, logger)

app.run(host="0.0.0.0", debug=False)