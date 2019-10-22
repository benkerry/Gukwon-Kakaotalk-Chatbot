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
        return "Fine Working!"

    @app.route("/notice-service", methods=["POST"])
    def notice_service(self):
        # 공지사항 요청을 처리
        return "공지사항 요청을 처리"

    @app.route("/meal-notice-service", methods=["POST"])
    def meal_notice_service(self):
        # 급식 알림 요청을 처리
        return "급식 알림 요청을 처리"

    @app.route("/timetable-notice-service", methods=["POST"])
    def timetable_notice_service(self):
        # 시간표 알림 요청을 처리
        return "시간표 알림 요청을 처리"

    @app.route("/schedule-notice-service", methods=["POST"])
    def schedule_notice_service(self):
        # 학사일정 알림 요청을 처리
        return "학사일정 알림 요청을 처리"

    @app.route("/suggestion-service", methods=["POST"])
    def suggestion_service(self):
        # 건의 요청을 처리(박형진 담당)
        return "건의 요청을 처리"

if __name__ == "__main__":
    server = ApiServer()
    server.app.run(host="0.0.0.0", debug=False)