## LIBS FOR TEST
import smtplib
from email.mime.text import MIMEText

import os
import json
import traceback
import threading

import DataManager.ChatbotNoticeParser as ChatbotNoticeParser
import DataManager.MealServiceParser as MealServiceParser
import DataManager.NoticeParser as NoticeParser
import DataManager.ScheduleTableParser as ScheduleTableParser
import DataManager.TimeTableParser as TimeTableParser
import DataManager.NewsletterParser as NewsletterParser

class AutoParser:
    def __init__(self, manager, logger):
        self.manager = manager
        self.logger = logger

        self.tr_10m = None
        self.tr_24h = None

        if os.path.isdir('data') == False:
            os.mkdir('data')

        self.run()

    def run(self):
        self.parse_10m()
        self.parse_24h()

    def stop(self):
        if self.tr_10m.is_alive():
            self.tr_10m.cancel()

        if self.tr_24h.is_alive():
            self.tr_24h.cancel()

    def parse_10m(self):
        if self.tr_10m != None and self.tr_10m.is_alive():
            self.tr_10m.cancel()

        try:
            self.logger.log('[AutoParser] Thread: tr_10m is running.')
            TimeTableParser.run(self.logger)
            NoticeParser.run(self.logger)
            NewsletterParser.run(self.logger)
            ChatbotNoticeParser.run(self.logger)

            self.manager.load_data()

            self.tr_10m = threading.Timer(600, self.parse_10m)
            self.tr_10m.start()
        except:
            self.logger.log('[AutoParser] Exception Catched on parse_10m, DataManager/Main.py')
            self.logger.log(traceback.format_exc())

    def parse_24h(self):
        if self.tr_24h != None and self.tr_24h.is_alive():
            self.tr_24h.cancel()

        try:
            self.logger.log('[AutoParser] Thread: tr_24h is running.')
            MealServiceParser.run(self.logger)
            ScheduleTableParser.run(self.logger)

            self.manager.load_data()
            
            self.tr_24h = threading.Timer(86400, self.parse_24h)
            self.tr_24h.start()
            
        except:
            self.logger.log('[AutoParser] Exception Catched on parse_24h, DataManager/Main.py')
            self.logger.log(traceback.format_exc())

class Manager:
    def __init__(self, logger):
        if os.path.isdir('data') == False:
            os.mkdir('data')

        self.logger = logger

        self.dict_schedule = None
        self.dict_menu = None
        self.lst_notice = None
        self.lst_newsletter = None
        self.lst_chatbotnotice = None
        self.dict_timetable = None

    def load_data(self):
        if os.path.isfile('data/ScheduleTable.dat'):
            with open('data/ScheduleTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_schedule = json.load(fp)

            cnt = 0
            for i in self.dict_schedule.keys():
                for k in range(len(self.dict_schedule[i])):
                    if (("중간고사" in self.dict_schedule[i][k]) or ("기말고사" in self.dict_schedule[i][k])):
                        if not "학기" in self.dict_schedule[i][k]:
                            if cnt == 0 or cnt == 1:
                                self.dict_schedule[i][k] = "1학기 " + self.dict_schedule[i][k]
                            else:
                                self.dict_schedule[i][k] = "2학기 " + self.dict_schedule[i][k]
                    cnt += 1

        if os.path.isfile('data/MenuTable.dat'):
            with open('data/MenuTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_menu = json.load(fp)
        
        if os.path.isfile('data/Notice.dat'):
            self.lst_notice = []

            lst_rdr = []

            with open('data/Notice.dat', 'r', encoding="UTF-8") as fp:
                lst_rdr = fp.readlines()
        
            lst_appender = []

            for i in range(len(lst_rdr)):
                lst_appender.append(lst_rdr[i])

                if (i + 1) % 3 == 0:
                    self.lst_notice.append(lst_appender)
                    lst_appender = []

        if os.path.isfile('data/Newsletter.dat'):
            self.lst_newsletter = []

            lst_rdr = []

            with open('data/Newsletter.dat', 'r', encoding="UTF-8") as fp:
                lst_rdr = fp.readlines()
        
            lst_appender = []

            for i in range(len(lst_rdr)):
                lst_appender.append(lst_rdr[i][:-1])

                if (i + 1) % 3 == 0:
                    self.lst_newsletter.append(lst_appender)
                    lst_appender = []

        if os.path.isfile('data/ChatbotNotice.dat'):
            self.lst_chatbotnotice = []

            lst_rdr = []

            with open('data/ChatbotNotice.dat', 'r', encoding="UTF-8") as fp:
                lst_rdr = fp.readlines()
        
            lst_appender = []

            for i in range(len(lst_rdr)):
                lst_appender.append(lst_rdr[i][:-1])

                if (i + 1) % 3 == 0:
                    self.lst_chatbotnotice.append(lst_appender)
                    lst_appender = []

        if os.path.isfile('data/TimeTable.dat'):
            with open('data/TimeTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_timetable = json.load(fp)

        self.logger.log('[Manager] Data Reloaded.')

        msg = MIMEText(str(self.ScheduleTable))

        msg['Subject'] = "충성^^7"
        msg['From'] = "developer_kerry@naver.com"
        msg['To'] = "developer_kerry@naver.com"

        smtp = smtplib.SMTP("smtp.naver.com", 465)
        smtp.starttls()
        smtp.login("developer_kerry@naver.com", "tmp0")
        smtp.sendmail("developer_kerry@naver.com", "developer_kerry@naver.com", msg.as_string())
        smtp.close()

    # 날짜(str_date, "YYYY-MM-DD") 검색으로 스케줄 하나 얻기
    def get_schedule_daily(self, str_date:str) -> list:
        if str_date in self.dict_schedule.keys():
            return [str_date, self.dict_schedule[str_date]]
        else:
            return []

    # 월간(str_date, "YYYY-MM") 검색으로 스케줄 얻기
    def get_schedule_monthly(self, str_date:str) -> list:
        lst_result = []

        for i in self.dict_schedule.keys():
            if str_date in i:
                lst_result.append([i, self.dict_schedule[i]])

        if len(lst_result) > 0:
            return lst_result
        else:
            return []

    def get_schedule_by_name(self, schedule_name:str) -> list:
        lst_result = []
        lst_schedule = []

        for i in self.dict_schedule.keys():
            for k in self.dict_schedule[i]:
                if schedule_name in k:
                    lst_schedule.append(k)
            if len(lst_schedule) > 0:
                lst_result.append([i, lst_schedule])
                lst_schedule = []
                
        if len(lst_result) > 0:
            return lst_result
        else:
            return []
    
    def get_timetable(self, str_date:str, grade_class:str) -> list:
        if str_date in self.dict_timetable.keys() and grade_class in self.dict_timetable[str_date].keys():
            return self.dict_timetable[str_date][grade_class]
        else:
            return []

    def get_meal(self, str_date:str, str_mealtime:str) -> list:
        str_key = str_date + ':' + str_mealtime

        if not (str_key in self.dict_menu.keys()):
            return []
        else:
            return self.dict_menu[str_key]

    def get_notice(self) -> list:
        return self.lst_notice

    def get_newsletter(self) -> list:
        return self.lst_newsletter

    def get_chatbotnotice(self) -> list:
        return self.lst_chatbotnotice