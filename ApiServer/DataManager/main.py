import os
import json
import traceback
import threading
import mysql.connector as mysql

from datetime import datetime

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
            TimeTableParser.run()
            NoticeParser.run()
            NewsletterParser.run()
            ChatbotNoticeParser.run()

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
            MealServiceParser.run()
            ScheduleTableParser.run()

            self.manager.load_data()
            
            self.tr_24h = threading.Timer(86400, self.parse_24h)
            self.tr_24h.start()
        except:
            self.logger.log('[AutoParser] Exception Catched on parse_24h, DataManager/Main.py')
            self.logger.log(traceback.format_exc())

class DBManager:
    def __init__(self, logger, mailer, str_db_addr, str_db_username, str_db_pwd, str_db_name):
        self.logger = logger
        self.mailer = mailer

        self.conn = mysql.connect(
            host=str_db_addr,
            user=str_db_username,
            passwd=str_db_pwd,
            database=str_db_name,
            use_unicode=True,
            charset='utf8'
        )
        self.cursor = self.conn.cursor(buffered=True)
        
        self.suggestion_manager()
        self.refresh_mysql_connection()

    def suggestion_manager(self):
        cursor = self.mysql_query("SELECT status, idx, num_signs, open_datetime, description FROM suggestion")
        num_authed_users = self.mysql_query("SELECT COUNT(*) FROM authed_user").fetchone()[0]
        boundary = int(num_authed_users * 0.15)

        lst_passed = []
        lst_closed = []
        lst_delete = []

        lst_passed_mail = []

        for i in cursor:
            if i[0] == 1:
                if i[2] > boundary:
                    lst_passed.append(i[1])
                    lst_passed_mail.append([i[1], i[4]])
                else:
                    lst_datetime_token = i[3].split("-")
                    today_datetime = datetime.today() 
                    open_datetime = datetime(lst_datetime_token[0], lst_datetime_token[1], lst_datetime_token[2])

                    passed_days = (today_datetime - open_datetime).day

                    if passed_days > 28:
                        lst_closed.append(i[1])
            elif i[0] == 3:
                lst_datetime_token = i[3].split("-")
                today_datetime = datetime.today() 
                open_datetime = datetime(lst_datetime_token[0], lst_datetime_token[1], lst_datetime_token[2])

                passed_days = (today_datetime - open_datetime).day

                if passed_days > 28:
                    lst_delete.append(i[1])

        lst_sql = []

        str_sql = "UPDATE suggestion SET status = 4 WHERE"

        for i in lst_passed:
            str_sql += " idx = {0} OR".format(i)

        if num_authed_users > 50 and len(lst_passed) > 0:
            lst_sql.append(str_sql[:-3])

        str_sql = "UPDATE suggestion SET status = 2 WHERE"
        for i in lst_closed:
            str_sql += " idx = {0} OR".format(i)

        if len(lst_closed) > 0:
            lst_sql.append(str_sql[:-3])

        str_sql = "DELETE FROM suggestion WHERE"
        for i in lst_delete:
            str_sql += " idx = {0} OR".format(i)

        if len(lst_delete) > 0:
            lst_sql.append(str_sql[:-3])

        self.mysql_query(lst_sql)
        self.mailer.send_passed_issues(self, lst_passed_mail)
        self.logger.log("Suggestion Arrangement Complete!")
        
        self.tr_suggestion_manager = threading.Timer(86400, self.suggestion_manager)
        self.tr_suggestion_manager.start()

    def refresh_mysql_connection(self):
        self.mysql_query("SHOW TABLES")
        self.logger.log("MySQL Connection Refreshed!")

        self.mysql_refresher = threading.Timer(28000, self.refresh_mysql_connection)
        self.mysql_refresher.start()

    def mysql_query(self, sql, tuple_params:tuple = None) -> mysql.cursor.MySQLCursor:
        if tuple_params == None:
            if str(type(sql)) == "<class 'str'>":
                self.cursor.execute(sql)
                self.conn.commit()
            else:
                for i in sql:
                    self.cursor.execute(i)
                self.conn.commit()
        else:
            if str(type(sql)) == "<class 'str'>":
                self.cursor.execute(sql, tuple_params)
                self.conn.commit()
            elif len(sql) == len(tuple_params):
                for i in range(len(sql)):
                    self.cursor.execute(sql[i], tuple_params[i])
                self.conn.commit()
            
        self.logger.log("MySQL Queried!")
        return self.cursor

class Manager:
    def __init__(self, logger):
        if os.path.isdir('data') == False:
            os.mkdir('data')

        self.logger = logger
        self.tr_3h = None

        self.dict_schedule = None
        self.dict_menu = None
        self.lst_notice = None
        self.lst_newsletter = None
        self.lst_chatbotnotice = None
        self.dict_timetable_st = None
        self.dict_timetable_tc = None

        self.load_data()

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

        if os.path.isfile('data/StudentTimeTable.dat'):
            with open('data/StudentTimeTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_timetable_st = json.load(fp)

        if os.path.isfile('data/TeacherTimeTable.dat'):
            with open('data/TeacherTimeTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_timetable_tc = json.load(fp)

        self.logger.log('[Manager] Data Reloaded.')

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
    
    def get_timetable_st(self, str_date:str, grade_class:str) -> list:
        if str_date in self.dict_timetable_st.keys() and grade_class in self.dict_timetable_st[str_date].keys():
            return self.dict_timetable_st[str_date][grade_class]
        else:
            return []

    def get_timetable_tc(self, str_date:str, str_tname:str) -> list:
        if str_date in self.dict_timetable_tc.keys() and str_tname in self.dict_timetable_tc[str_date].keys():
            return self.dict_timetable_tc[str_date][str_tname]
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