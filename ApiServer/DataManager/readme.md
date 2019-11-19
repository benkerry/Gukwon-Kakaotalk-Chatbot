# DataManager
* 학사일정, 시간표, 급식 정보는 main.py를 import하여 얻어올 수 있습니다.
  
  
## main.py
### class AutoParser : 일정 시간마다 파싱을 반복 수행하도록 하는 클래스, 
      def __init__(manager, logger)
      : 생성시 DataManager 객체와 ServerLogger.Logger 객체를 받습니다.

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

### class DBManager : MySQL Database 이용 전반에 관련한 동작을 수행합니다.
      def __init__(logger, mailer, str_db_addr, str_db_username, str_db_pwd, str_db_name)
      : ServerLogger.Logger, Mailer, MySQL 주소, MySQL Username, Password, Database Name을 인자로 받아 connection을 생성합니다.

      def suggestion_manager()
      : 24시간 주기로 건의사항들을 검사하여 삭제 플래그 세트 후 15일이 지난 건의사항을 삭제하고, 통과 조건이 만족된 건의를 관리자들에게 메일로 보냅니다.

      def refresh_mysql_connection()
      : 일정 시간마다 MySQL에 쿼리를 전송하여 Connection이 끊기지 않도록 합니다.

      def mysql_query(sql, tuple_params:tuple = None) -> mysql.cursor.MySQLCursor
      : MySQL 쿼리를 수행합니다. sql에는 string 형태의 SQL문, 혹은 SQL문 리스트가 올 수 있습니다. tuple_params에는 아무 것도 넘겨주지 않으면 쿼리 실행시 넘겨줄 Parameter가 없다고 간주합니다. 만약 여러 쿼리문에 대한 Parameters를 넘겨주려면 2D Tuple을 이용하십시오.

### class DataManager : 바로 사용 가능한 형태의 데이터를 불러오는 클래스
      def __init__(logger)
      : ServerLogger.Logger의 객체를 인자로 받습니다.

      def load_data()
      : 현재 데이터 파일에 저장되어 있는 자료들을 모두 읽어 메모리에 적재합니다.

      def get_schedule_daily(str_date:str) -> list
      : YYYY-MM-DD Format의 str_date를 넘겨주면, 해당일의 학사일정을 검색/반환합니다.
      > return format - [날짜(YYYY-MM-DD), [일정1, 일정2, ...]]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

      def get_schedule_monthly(str_month:str) -> list:
      : YYYY-MM Format의 str_month를 넘겨주면, 해당월의 학사일정을 모두 검색/반환합니다.
      > return format - [[날짜(YYYY-MM-DD) 1, [일정명 1-1, 일정명 1-2, ...]], [날짜 2, [일정명 2-1, 일정명 2-2, ...]], ... ]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

      def get_schedule_by_name(schedule_name:str) -> list
      : schedule_name이 일정명에 포함된 모든 일정을 검색하여 반환합니다.
      > return format - [[날짜(YYYY-MM-DD) 1, [일정명 1-1, 일정명 1-2, ...]], [날짜 2, [일정명 2-1, 일정명 2-2, ...]], ... ]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

      def get_timetable_st(str_date:str, grade_class:str) -> list
      : YYYY-MM-DD Format의 str_date와 '학년-반' 형태의 grade_class를 넘겨주면 해당일 해당 반의 시간표를 반환합니다.
      > return format - [['교사명1', '과목명1'], ['교사명2', '과목명2'] ... ]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

      def get_timetable_tc(str_date:str, str_tname:str) -> list
      : YYYY-MM-DD Format의 str_date와 'O*O'(ex. '박*진') 형태의 str_tname을 넘겨주면 해당일 해당 교사의 사간표를 반환합니다.
      > return format - [[반1, 과목명1], [반2, 과목명2], ...]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

      def get_meal(str_date:str, str_mealtime:str)) -> list
      : YYYY-MM-DD Format의 str_date와 '조식', '중식', '석식'중 하나가 담긴 str_mealtime을 넘겨주면 해당일의 해당 식단을 반환합니다.
      > return format - ["메뉴1", "메뉴2" ... ]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

      def get_notice()
      : 현재 등록되어 있는 모든 공지사항을 반환합니다.
      > return format - [[공지 제목 1, 공지 등록일 1, 공지 링크 1], [공지 제목 2, 공지 등록일 2, 공지 링크 2], ...]
      > 찾는 데이터가 없는 경우 빈 리스트 반환
      
      def get_newsletter()
      : 현재 등록되어 있는 모든 가정통신문을 반환합니다.
      > return format - [[가정통신문 제목 1, 가정통신문 등록일 1, 가정통신문 링크 1], [가정통신문 제목 2, 가정통신문 등록일 2, 가정통신문 링크 2], ...]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

      def get_chatbotnotice()
      : 현재 등록되어 있는 모든 학생회 공지사항을 반환합니다.
      > return format - [[학생회 공지 제목 1, 학생회 공지 등록일 1, 학생회 공지 링크 1],  [학생회 공지 제목 2, 학생회 공지 등록일 2, 학생회 공지 링크 2], ...]
      > 찾는 데이터가 없는 경우 빈 리스트 반환

## ChatbotNoticeParser.py
      def run(logger)
      : 한달 치 챗봇 공지사항 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## MealServiceParser.py
      def run(logger)
      : 한달 치 급식 데이터 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## NewsletterParser.py
      def run(logger)
      : 한달 치 가정통신문 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## NoticeParser.py
      def run(logger)
      : 한달 치 공지사항 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## ScheduleTableParser.py
      def run(logger)
      : 일년 치 학사일정 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.

## TimeTableParser.py
      def run(logger)
      : 시간표 데이터 파싱을 수행합니다. ServerLogger.Logger 형식의 인스턴스를 넘겨주십시오.
