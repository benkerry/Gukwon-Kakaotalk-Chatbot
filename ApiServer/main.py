import json
import smtplib
import traceback
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
from email.mime.text import MIMEText

from Processors.ResponseGenerator.GenerateOutput import SimpleText
from Processors.ResponseGenerator.OutputsPacker import pack_outputs

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    try:
        global logger
        global data_manager

        dict_json = None
        str_reqtype = None

        dict_json = request.json
        str_reqtype = dict_json['userRequest']['block']['name']

        if str_reqtype == "TestDDay_Query":
            return TestDDay.process(data_manager, logger, dict_json)
        elif str_reqtype == "MealService_Query":
            return MealNotice.process(data_manager, logger, dict_json)
        elif str_reqtype == "TimeTable_Query":
            return TimeTableNotice.process(data_manager, logger, dict_json)
        elif str_reqtype == "Notice_Query":
            return Notice.process(data_manager, logger)
        elif str_reqtype == "SetDefaultClass":
            return SetDefaultClass.process(data_manager, logger, dict_json)
        elif str_reqtype == "SetDefaultName":
            return SetDefaultName.process(data_manager, logger, dict_json)
        elif str_reqtype == "Truncate":
            return Truncate.process(data_manager, logger, dict_json)
        elif str_reqtype == "Newsletter_Query":
            return Newsletter.process(data_manager, logger)
        elif str_reqtype == "ScheduleTable_Query":
            return ScheduleNotice.process(data_manager, logger, dict_json)
        elif str_reqtype == "Authentication_Query":
            return Auth.process(data_manager, logger, dict_json)
        elif str_reqtype == "Suggestion_Query":
            return pack_outputs(SimpleText.generate_simpletext("건의 기능은 아직 테스트 중입니다."))
            #return Suggestion.process(data_manager, logger, dict_json)
        elif str_reqtype == "Suggestion_Show":
            return pack_outputs(SimpleText.generate_simpletext("건의 확인 기능은 아직 테스트 중입니다."))
            #return SuggestionShow.process(data_manager, logger)
        else:
            return pack_outputs(SimpleText.generate_simpletext("잘못된 요청입니다."))
    except Exception as e:
        str_traceback = traceback.format_exc()

        logger.log("[ApiMain] Error Occured.")

        src_email = "developer_kerry@naver.com"
        des_email = "developer_kerry@kakao.com"
        pwd = "temp"

        smtp_name = "smtp.naver.com"
        smtp_port = 587

        msg = MIMEText(traceback.format_exc())
        msg['Subject'] = "[Error Report]: " + str(e)
        msg['From'] = src_email
        msg['To'] = des_email

        smtp = smtplib.SMTP(smtp_name, smtp_port)
        smtp.starttls()
        smtp.login(src_email, pwd)
        smtp.sendmail(src_email, des_email, msg.as_string())
        smtp.close()

        return pack_outputs(SimpleText.generate_simpletext("서버 오류가 발생하였습니다."))

@app.route("/healthcheck")
def healthcheck():
    global logger
    return HealthCheck.process(logger)

app.config['JSON_AS_ASCII'] = False

logger = ServerLogger.Logger()
data_manager = DataManager.Manager(logger)
auto_parser = DataManager.AutoParser(data_manager, logger)

app.run(host="0.0.0.0", port=4444, debug=False)