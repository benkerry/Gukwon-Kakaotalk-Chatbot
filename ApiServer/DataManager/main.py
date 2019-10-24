import json
import os
import traceback
import threading

import DataManager.MealServiceParser as MealServiceParser
import DataManager.NoticeParser as NoticeParser
import DataManager.ScheduleTableParser as ScheduleTableParser
import DataManager.TimeTableParser as TimeTableParser

class AutoParser:
    # 일정 시간마다 파싱 반복하는 클래스: Thread에 물려줘야 함
    def __init__(self, manager, logger):
        self.manager = manager
        self.logger = logger

        self.tr_10m = None
        self.tr_24h = None

        # 읽어온 데이터를 저장할 디렉터리가 없을 때 실행
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
            TimeTableParser.run(self.logger)
            NoticeParser.run(self.logger)

            self.manager.load_data()

            self.tr_10m = threading.Timer(600, self.parse_10m)
            self.tr_10m.start()
            self.logger.log('[AutoParser] Thread: tr_10m Started.')
        except:
            self.logger.log('[AutoParser] Exception Catched on parse_10m, DataManager/Main.py')
            self.logger.log(traceback.format_exc())

    def parse_24h(self):
        if self.tr_24h != None and self.tr_24h.is_alive():
            self.tr_24h.cancel()

        try:
            MealServiceParser.run(self.logger)
            ScheduleTableParser.run(self.logger)

            self.manager.load_data()
            
            self.tr_24h = threading.Timer(86400, self.parse_24h)
            self.tr_24h.start()
            self.logger.log('[AutoParser] Thread: tr_24h Started.')
        except:
            self.logger.log('[AutoParser] Exception Catched on parse_24h, DataManager/Main.py')
            self.logger.log(traceback.format_exc())

class Manager:
    def __init__(self, logger):
        # 읽어온 데이터를 저장할 디렉터리가 없을 때 실행
        if os.path.isdir('data') == False:
            os.mkdir('data')

        self.logger = logger

        self.dict_schedule = {}
        self.dict_menu = {}
        self.lst_notice = []
        self.dict_timetable = {}

    def load_data(self):
        # 학사일정 꺼내오기
        if os.path.isfile('data/ScheduleTable.dat'):
            with open('data/ScheduleTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_schedule = json.load(fp)

        cnt = 0
        for i in self.dict_schedule.keys():
            for k in len(self.dict_schedule[i][1]):
                if (("중간고사" in self.dict_schedule[i][1][k]) or ("기말고사" in self.dict_schedule[i][1][k])):
                    if not "학기" in self.dict_schedule[i][1][k]:
                        if cnt == 0 or cnt == 1:
                            self.dict_schedule[i][1][k] = "1학기 " + self.dict_schedule[i][1][k]
                        else:
                            self.dict_schedule[i][1][k] = "2학기 " + self.dict_schedule[i][1][k]
                    cnt += 1

        # 급식 꺼내오기
        if os.path.isfile('data/MenuTable.dat'):
            with open('data/MenuTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_menu = json.load(fp)
        
        # 공지사항 파일에서 꺼내오기
        if os.path.isfile('date/Notice.dat'):
            self.lst_notice = []

            with open('date/Notice.dat', 'r', encoding="UTF-8") as fp:
                lst_rdr = fp.readlines()

                if len(lst_rdr) % 2 != 0 or len(lst_rdr) == 0:
                    return []
        
            lst_appender = []

            for i in range(len(lst_rdr)):
                lst_appender.append(lst_rdr[i])

                if i % 2 == 1:
                    self.lst_notice.append(lst_appender)
                    lst_appender = []

        # 시간표 꺼내오기
        if os.path.isfile('data/TimeTable.dat'):
            with open('data/TimeTable.dat', 'r', encoding="UTF-8") as fp:
                self.dict_timetable = json.load(fp)

        self.logger.log('[Manager] Data Reloaded.')

    # 날짜(str_date, "YYYY-MM-DD") 검색으로 스케줄 하나 얻기
    def get_schedule_daily(self, str_date:str) -> list:
        if str_date in self.dict_schedule.keys():
            return [str_date, self.dict_schedule[str_date]]
        else:
            return []

    # 월간(str_date, "YYYY-MM") 검색으로 스케줄 얻기
    def get_schedult_monthly(self, str_date:str) -> list:
        lst_result = []

        for i in self.dict_schedule.keys():
            if str_date in i:
                lst_sub = []
                
                for k in self.dict_schedule[i]:
                    lst_sub.append(k)
                
                lst_result.append([i, lst_sub])

        if len(lst_result) > 0:
            return lst_result
        else:
            return []

    # 스케줄명 검색으로 스케줄 얻기
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
    
    # 날짜(str_date, "YYYY-MM-DD"), 소속(grade_class, "GRADE-CLASS")
    def get_timetable(self, str_date:str, grade_class:str):
        # 해당일/해당 반의 하루치 시간표를 가져온다.
        return self.dict_timetable[str_date][grade_class]

    # 날짜(str_date, "YYYY-MM-DD"), 식사 선택(str_mealtime, '조식' or '중식' or '석식')으로 식단 얻기
    def get_meal(self, str_date:str, str_mealtime:str) -> list:
        str_key = str_date + ':' + str_mealtime

        # Key에 해당하는 메뉴의 List를 반환
        if not (str_key in self.dict_menu.keys()):
            return []
        else:
            return self.dict_menu[str_key]

    def get_notice(self) -> list:
        return self.lst_notice