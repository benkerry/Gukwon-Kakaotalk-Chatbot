import json
import os
import threading

import TimeTableParser
import NoticeParser
import MealServiceParser
import ScheduleTableParser

class AutoParser:
    # 일정 시간마다 파싱 반복하는 클래스: Thread에 물려줘야 함
    def __init__(self, logger):
        self.logger = logger

        self.tr_10m = threading.Timer(600, self.parse_10m)
        self.tr_24h = threading.Timer(86400, self.parse_24h)

        # 읽어온 데이터를 저장할 디렉터리가 없을 때 실행
        if os.path.isdir('data') == False:
            os.mkdir('data')

    def parse_10m(self):
        try:
            TimeTableParser.run(self.logger)
            NoticeParser.run(self.logger)
        except:
            pass

    def parse_24h(self):
        try:
            MealServiceParser.run(self.logger)
            ScheduleTableParser.run(self.logger)
        except:
            pass

    def run(self):
        if not self.tr_10m.is_alive():
            self.tr_10m.start()
            
        if not self.tr_24h.is_alive():
            self.tr_24h.start()

    def stop(self):
        if self.tr_10m.is_alive():
            self.tr_10m.cancel()

        if self.tr_24h.is_alive():
            self.tr_24h.cancel()

class DataManager:
    def __init__(self, logger):
        self.logger = logger

    # 날짜(YYYYMMDD)로 스케줄 얻기
    def get_schedule_by_date(self, str_date):
        dict_data = {}
        lst_result = []

        with open('data/ScheduleTable.dat', 'r') as fp:
            dict_data = json.load(fp)

        for i in dict_data.keys():
            if i == str_date:
                for k in dict_data[i]:
                    lst_result.append(k)

        # [YYYYMMDD, [Schedules]] 형태로 반환
        if len(lst_result) > 0:
            return [str_date, lst_result]
        else:
            return []

    # 스케줄명 검색으로 스케줄 얻기
    def get_schedule_by_name(self, schedule_name):
        dict_data = {}

        str_result_date = ''
        str_result_schedule = ''
        
        with open('data/ScheduleTable.dat', 'r') as fp:
            dict_data = json.load(fp)

        for i in dict_data.keys():
            for k in dict_data[i]:
                if schedule_name in k:
                    str_result_date = i
                    str_result_schedule = k

                    # [YYYYMMDD, [Schedules]] 형태 반환
                    return [str_result_date, [str_result_schedule]]

        return []

    def get_meal(self, str_date, str_mealtime):
        dict_data = {}
        lst_result = []

        with open('data/MenuTable.dat', 'r') as fp:
            dict_data = json.load(fp)

        # 메뉴 List를 반환
        return dict_data[str_date + str_mealtime]

    def get_notice(self):
        lst_rdr = []
        lst_result = []

        with open("date/Notice.dat", 'r') as fp:
            lst_rdr = fp.readlines()

            if len(lst_rdr) % 2 != 0 or len(lst_rdr) == 0:
                return []
        
        lst_appender = []

        for i in range(len(lst_rdr)):
            lst_appender.append(lst_rdr[i])

            if i % 2 == 1:
                lst_result.append(lst_appender)
                lst_appender = []

        return lst_result


    def get_timetable(self, week, grade, _class, week_index, time):
        # 변수 초기화!
        dict_filename = {'this_week':'data/ThisWeekTimeTable.dat', 'next_week':'data/NextWeekTimeTable.dat'}
        dict_json = {'this_week':'', 'next_week':''}

        # 한 번도 데이터를 파싱한 적이 없을 때 실행
        if os.path.isfile(dict_filename['this_week']) == False:
            TimeTableParser.run(self.logger)

        # 저장된 JSON 파일을 읽는다.
        with open(dict_filename['this_week'], 'r') as fp:
            dict_json['this_week'] = json.load(fp)

        with open(dict_filename['next_week'], 'r') as fp:
            dict_json['next_week'] = json.load(fp)

        # JSON에서 (교사 번호)*100 + 과목코드로 되어있는 시간표 한 칸에 해당하는 값을 가져온다.
        try:
            if week == 0:
                n = dict_json['this_week']['자료81'][grade][_class][week_index][time]
            else:
                n = dict_json['next_week']['자료81'][grade][_class][week_index][time]
        except Exception:
            return False

        # 다음 주 시간표를 읽으려는데, 다음 주 시간표가 아직 안 나온 경우
        if len(dict_json['next_week']) < 50 and week == 1:
            return False
        
        # 수업이 없는 경우
        if n == 0:
            return -1

        # 선생님 코드와 과목 코드를 구한다.
        teacher_index = n // 100
        subject_index = n % 100

        if week == 0:
            return [dict_json['this_week']['자료46'][teacher_index], dict_json['this_week']['긴자료92'][subject_index]]
        else:
            return [dict_json['next_week']['자료46'][teacher_index], dict_json['next_week']['긴자료92'][subject_index]]
