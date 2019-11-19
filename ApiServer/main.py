import json
import traceback

import config
import ServerLogger
import DataManager.main as DataManager 

import Processors.AuthService as Auth
import Processors.Truncate as Truncate
import Processors.NoticeService as Notice
import Processors.HealthCheck as HealthCheck
import Processors.TestDDayService as TestDDay
import Processors.NewsletterService as Newsletter
import Processors.SuggestionService as Suggestion
import Processors.MealNoticeService as MealNotice
import Processors.SuggestionShow as SuggestionShow
import Processors.SetDefaultName as SetDefaultName
import Processors.SetDefaultClass as SetDefaultClass
import Processors.ScheduleNoticeService as ScheduleNotice
import Processors.TimeTableNoticeService as TimeTableNotice

from flask import Flask, request
from threading import Thread

from Mailer import Mailer
from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

app = Flask(__name__)

@app.route("/healthcheck")
def healthcheck():
    global logger
    return HealthCheck.process(logger)

@app.route("/", methods=["POST"])
def main():
    try:
        global lst_thread

        global mailer
        global logger
        global db_manager
        global data_manager

        dict_json = request.json
        str_reqtype = dict_json['userRequest']['block']['name']

        if str_reqtype == "TestDDay_Query":
            return TestDDay.process(data_manager, logger, dict_json)
        elif str_reqtype == "MealService_Query":
            return MealNotice.process(data_manager, logger, dict_json)
        elif str_reqtype == "TimeTable_Query":
            return TimeTableNotice.process(data_manager, db_manager, logger, dict_json)
        elif str_reqtype == "Notice_Query":
            return Notice.process(data_manager, logger)
        elif str_reqtype == "SetDefaultClass":
            return SetDefaultClass.process(data_manager, db_manager, logger, dict_json)
        elif str_reqtype == "SetDefaultName":
            return SetDefaultName.process(data_manager, db_manager, logger, dict_json)
        elif str_reqtype == "Truncate":
            return Truncate.process(db_manager, logger, dict_json)
        elif str_reqtype == "Newsletter_Query":
            return Newsletter.process(data_manager, logger)
        elif str_reqtype == "ScheduleTable_Query":
            return ScheduleNotice.process(data_manager, logger, dict_json)
        elif str_reqtype == "Authentication_Query":
            return Auth.process(data_manager, db_manager, logger, dict_json)
        elif str_reqtype == "Suggestion_Query":
            return Suggestion.process(db_manager, logger, dict_json)
        elif str_reqtype == "Suggestion_Show":
            return SuggestionShow.process(db_manager, logger)
        else:
            return pack_outputs(SimpleText.generate_simpletext("잘못된 요청입니다."))
    except Exception as e:
        logger.log("[ApiMain] Error Occured.\nThread Count: {0}\nIP Addr: {1}".format(len(lst_thread), request.remote_addr))
        lst_del = []

        for i in range(len(lst_thread)):
            if not lst_thread[i].is_alive():
                lst_del.append(i)

        lst_del.reverse()

        for i in lst_del:
            del(lst_thread[i])

        tr = Thread(target=mailer.send_error_message, args=(e, traceback.format_exc() + '\n\n\n' + str(dict_json)))
        tr.start()
        lst_thread.append(tr)

        return pack_outputs(SimpleText.generate_simpletext("서버 오류가 발생하였습니다.\n\n버그 리포트가 개발자에게 전송되었습니다. 불편을 드려 죄송합니다.\n\n버그와 관련한 세부 정보를 developer_kerry@kakao.com으로 보내주시면 문제 개선에 큰 도움이 됩니다."))

app.config['JSON_AS_ASCII'] = False

mailer = Mailer(
    str_email = config.str_email,
    str_password = config.str_password,
    str_smtp_name = "smtp.naver.com",
    smtp_port = 587
)

lst_thread = []

logger = ServerLogger.Logger()
db_manager = DataManager.DBManager(logger, mailer, str_db_addr, str_db_username, str_db_pwd, str_db_name)
data_manager = DataManager.Manager(logger)
auto_parser = DataManager.AutoParser(data_manager, logger)

app.run(host="0.0.0.0", port=4444, debug=False)