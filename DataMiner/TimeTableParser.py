import requests
import json
import os

class Parser:
    def __init__(self):
        self.file_name['this_week'] = "data/ThisWeekTimeTable.dat"
        self.file_name['next_week'] = "data/NextWeekTimeTable.dat"

        if os.path.isfile(self.file_name['this_week']):
            with open(self.file_name['this_week'], 'r') as fp:
                self.json_data['this_week'] = json.load(fp)

            if os.path.isfile(self.file_name['next_week']):
                with open(self.file_name['next_week'], 'r') as fp:
                    self.json_data['next_week'] = json.load(fp)
            else:
                self.json_data['next_week'] = -1
        else:
            self.json_data['this_week'] = -1


    def getTimeTableFromServer(self):
        response['this_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8x")
        response['this_week'].encoding = 'utf-8'

        response['next_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8y")
        response['next_week'].encoding = 'utf-8'

        self.json_data['this_week'] = json.loads(responsep['this_week'].text.split('\n')[0])
        self.json_data['next_week'] = json.loads(responsep['next_week'].text.split('\n')[0])

        with open(self.file_name['this_week'], 'w') as fp:
            json.dump(self.json_data['this_week'], fp, indent='\t')
        with open(self.file_name['next_week'], 'w') as fp:
            json.dump(self.json_data['next_week'], fp, indent='\t')
    
    def getTimeTableData(self, week, grade, _class, week_index, time):
        try:
            if week == 0:
                tmp_json = self.json_data['this_week']
                n = tmp_json['자료81'][grade][_class][week_index][time]
            else:
                tmp_json = self.json_data['next_week']
                n = tmp_json['자료81'][grade][_class][week_index][time]
        except Exception:
            return False

        teacher_index = n // 100
        subject_index = n % 100

        return [tmp_json['자료46'][teacher_index], self.json_data['긴자료92'][subject_index]]