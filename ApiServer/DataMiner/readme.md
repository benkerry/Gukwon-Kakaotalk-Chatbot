# DataMiner
>* 학사일정, 시간표, 급식 정보는 DataMiner.py를 import하여 얻어올 수 있습니다.
#
>## DataMiner.py
>>def GetTimeTableData(self, week, grade, _class, week_index, time)
>>: Parameter로 어떤 시간표를 얻어올 것인지 지정해주면 ['교사 이름', '과목 이름']을 반환합니다.  
>>>*week: 0은 이번 주를, 1은 다음 주를 뜻합니다.  
>>>*grade: 몇 학년의 시간표를 얻어올 것인지 쓰시면 됩니다.  
>>>*_class: 몇 반의 시간표를 얻어올 것인지 쓰시면 됩니다.  
>>>*time: 몇 교시의 시간표를 얻어올 것인지 쓰시면 됩니다.  
#
>* TimeTableParser를 Cronjob에 물려 일정 시간마다 실행시켜 주십시오.