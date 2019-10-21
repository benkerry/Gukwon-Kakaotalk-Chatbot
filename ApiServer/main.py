import json
import ServerLogger
import DataManager.main as DataManager

from flask import Flask, request

class ApiServer:
    app = Flask(__name__)

    def __init__(self):
        self.app.config['JSON_AS_ASCII'] = False

        self.logger = ServerLogger.Logger()
        self.data_manager = DataManager.Manager(self.logger)
        self.auto_parser = DataManager.AutoParser(self.data_manager, self.logger)

    @app.route("/")
    def healthcheck(self):
        # HealthCheck 응답
        return ""

    @app.route("/NoticeService", methods=["POST"])
    def notice_service(self):
        # 공지사항 요청을 처리
        return ""

    @app.route("/MealNoticeService", methods=["POST"])
    def meal_notice_service(self):
        # 급식 알림 요청을 처리
        return ""

    @app.route("/TimeTableNoticeService", methods=["POST"])
    def timetable_notice_service(self):
        # 시간표 알림 요청을 처리
        return ""

    @app.route("/ScheduleNoticeService", methods=["POST"])
    def schedule_notice_service(self):
        # 학사일정 알림 요청을 처리
        return ""

    @app.route("/SuggestionService", methods=["POST"])
    def suggestion_service(self):
        # 건의 요청을 처리(박형진 담당)
        return ""

if __name__ == "__main__":
    server = ApiServer()
    server.app.run()