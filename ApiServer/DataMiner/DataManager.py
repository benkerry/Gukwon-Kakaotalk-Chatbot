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
    def __init__(self, logger):
        self.logger = logger
    def GetTimeTableData(self, week, grade, _class, week_index, time):
        # 변수 초기화!
        file_name = {'this_week':'data/ThisWeekTimeTable.dat', 'next_week':'data/NextWeekTimeTable.dat'}
        json_data = {'this_week':'', 'next_week':''}

        # 한 번도 데이터를 파싱한 적이 없을 때 실행
        if os.path.isfile(file_name['this_week']) == False:
            TimeTableParser.Run(self.logger)

        # 저장된 JSON 파일을 읽는다.
        with open(file_name['this_week'], 'r') as fp:
            json_data['this_week'] = json.load(fp)

        with open(file_name['next_week'], 'r') as fp:
            json_data['next_week'] = json.load(fp)

        # JSON에서 (교사 번호)*100 + 과목코드로 되어있는 시간표 한 칸에 해당하는 값을 가져온다.
        try:
            if week == 0:
                n = json_data['this_week']['자료81'][grade][_class][week_index][time]
            else:
                n = json_data['next_week']['자료81'][grade][_class][week_index][time]
        except Exception:
            return False

        # 다음 주 시간표를 읽으려는데, 다음 주 시간표가 아직 안 나온 경우
        if len(json_data['next_week']) < 50 and week = 1:
            return False

        # 선생님 코드와 과목 코드를 구한다.
        teacher_index = n // 100
        subject_index = n % 100

        if week == 0:
            return [json_data['this_week']['자료46'][teacher_index], json_data['this_week']['긴자료92'][subject_index]]
        else:
            return [json_data['next_week']['자료46'][teacher_index], json_data['next_week']['긴자료92'][subject_index]]
