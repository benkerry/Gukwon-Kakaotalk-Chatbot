import json
import os
import TimeTableParser

class AutoParser:
    # 일정 시간마다 파싱 반복하는 클래스
    def __init__(self):
        self.Enabled = False

    def Run(self, timetable_interval):
        # 시작!
        self.Enabled = True
        return 1

    def Stop(self):
        # 정지!
        self.Enabled = False

class DataManager:    
    def GetTimeTableData(self, week, grade, _class, week_index, time):
        file_name = {'this_week':'data/ThisWeekTimeTable.dat', 'next_week':'data/NextWeekTimeTable.dat'}
        json_data = {'this_week':'', 'next_week':''}

        if os.path.isfile(file_name['this_week']):
            TimeTableParser.Run()

        with open(file_name['this_week'], 'r') as fp:
            json_data['this_week'] = json.load(fp)

        with open(file_name['next_week'], 'r') as fp:
            json_data['next_week'] = json.load(fp)

        try:
            if week == 0:
                n = json_data['this_week']['자료81'][grade][_class][week_index][time]
            else:
                n = json_data['next_week']['자료81'][grade][_class][week_index][time]
        except Exception:
            return False

        if len(json_data['this_week']) < 50:
            return False

        teacher_index = n // 100
        subject_index = n % 100

        if week == 0:
            return [json_data['this_week']['자료46'][teacher_index], json_data['this_week']['긴자료92'][subject_index]]
        else:
            return [json_data['next_week']['자료46'][teacher_index], json_data['next_week']['긴자료92'][subject_index]]
