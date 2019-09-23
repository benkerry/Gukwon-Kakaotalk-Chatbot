# DataMiner
* 학사일정, 시간표, 급식 정보는 DataMiner.py를 import하여 얻어올 수 있습니다.
#
## DataManager.py
   ### class AutoParser : 일정 시간마다 파싱을 반복 수행하도록 하는 클래스
     def Run()  
     : 기능을 켭니다.  
       
     def Stop()  
     : 기능을 끕니다.  

   ### class DataManager : 바로 사용 가능한 형태의 데이터를 불러오는 클래스, 생성자에 ServerLogger.Logger의 인스턴스를 넘겨주세요.
     def GetTimeTableData(week, grade, _class, week_index, time)  
     : Parameter로 어떤 시간표를 얻어올 것인지 지정해주면 ['교사 이름', '과목 이름']을 반환합니다. 접근할 수 없는 위치의 값을 참조하려 시도하면 False를 반환합니다. 수업이 없는 시간이라면 -1을 반환합니다.
       1. week: 0은 이번 주를, 1은 다음 주를 뜻합니다.  
       2. grade: 몇 학년의 시간표를 얻어올 것인지 쓰시면 됩니다.  
       3. _class: 몇 반의 시간표를 얻어올 것인지 쓰시면 됩니다.  
       4. week_index: 1은 월요일, 2는 화요일, 3은 수요일, 4는 목요일, 5는 금요일입니다.  
       5. time: 몇 교시의 시간표를 얻어올 것인지 쓰시면 됩니다.  
## TimeTableParser.py
     def Run(logger)
     : 시간표 데이터 파싱을 수행합니다.
       1. logger: ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.