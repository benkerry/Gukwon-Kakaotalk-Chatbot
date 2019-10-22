# DataMiner
* 학사일정, 시간표, 급식 정보는 DataMiner.py를 import하여 얻어올 수 있습니다.
  
  
## main.py
   ### class AutoParser(manager, logger) : 일정 시간마다 파싱을 반복 수행하도록 하는 클래스
   #### 하단에 언급할 DataManager의 인스턴스를 첫 번째 인자로 받습니다.
   #### ServerLogger.Logger의 인스턴스를 두 번째 인자로 받습니다.
     def run()  
     : 기능을 켭니다.  
       
     def stop()  
     : 기능을 끕니다.  

     def parse_10m()  
     : 10분마다 실행되어야 하는 파싱 작업을 수행합니다.  
     객체 외부에서 접근하지 않도록 합니다. 

     def parse_24h()
     : 24시간마다 실행되어야 하는 파싱 작업을 수행합니다.
     객체 외부에서 접근하지 않도록 합니다.
  
   ### class DataManager : 바로 사용 가능한 형태의 데이터를 불러오는 클래스
   #### 생성자에 ServerLogger.Logger의 인스턴스를 넘겨주세요.
     def load_data()
     : 현재 데이터 파일에 저장되어 있는 자료들을 읽어 필드에 저장합니다.

     def get_schedule_by_date(str_date)
     : YYYY-MM Format의 str_date로 해당월의 학사일정을 모두 반환합니다.
     > return format - [날짜(YYYY-MM-DD), 일정명]

     def get_schedule_by_date(schedule_name):
     : 특정 문자열(schedule_name)이 포함된 학사일정을 모두 반환합니다.
     > return format - [[날짜(YYYY-MM-DD) 1, 일정명 1], [날짜 2, 일정명 2] ... ]

     def get_timetable(datetime, grade_class)
     : YYYY-MM-DD Format의 str_date와 '학년-반' 형태의 grade_class를 넘겨주면
     : 해당일의 해당 반 시간표를 반환합니다.
     > return format - [['교사명1', '과목명1'], ['교사명2', '과목명2'] ... ]

     def get_meal(str_date)
     : YYYY-MM-DD Format의 str_date와 '조식', '중식', '석식'이 담긴 str_mealtime을 넘겨주면
     : 해당일의 해당 식단을 리스트로 반환합니다.
     > return format - ["메뉴1", "메뉴2" ... ]

     def get_notice()
     : 현재 등록되어 있는 모든 공지사항을 반환합니다.
     > return format - ["공지 제목1", "공지 링크1", "공지 제목2", "공지 링크2" ... ]
  
## MealServiceParser.py
     def run(logger)
     : 한달 치 급식 데이터 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## NoticeParser.py
     def run(logger)
     : 한달 치 공지사항 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## ScheduleTableParser.py
     def run(logger)
     : 일년 치 학사일정 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## TimeTableParser.py
     def run(logger)
     : 시간표 데이터 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.
