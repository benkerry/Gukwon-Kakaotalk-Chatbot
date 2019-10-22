# Processors
* 요청을 실제로 처리하는 코드들이 포함되어 있습니다.
* data_manager : DataManager.Manager 객체를 넘겨줍니다.
* request : Flask.request를 그대로 넘겨줍니다.
  
## AuthService.py
      def process(requests)
      : 구성원 인증 요청을 처리하고 처리 결과 응답 메시지를 생성해 반환합니다.
  
## HealthCheck.py
      def process()
      : HealthCheck 결과를 응답 메시지로 생성해 반환합니다.
  
## MealNoticeService.py
      def process(data_manager, request)
      : 급식 알림 요청을 처리하고 처리 결과 응답 메시지를 생성해 반환합니다.
  
## NoticeService.py
      def process(data_manager)
      : 공지사항 알림 요청을 처리하고 처리 결과 응답 메시지를 생성해 반환합니다.
  
## ScheduleNoticeService.py
      def process(data_manager, request)
      : 학사일정 알림 요청을 처리하고 처리 결과 응답 메시지를 생성해 반환합니다.
  
## SuggestionService.py
      def process(reqeust)
      : 건의사항 요청을 처리하고 처리 결과 응답 메시지를 생성해 반환합니다.
  
## TestDDayService.py
      def process(data_manager, request)
      : 시험 디데이 요청을 처리하고 처리 결과 응답 메시지를 생성해 반환합니다.
  
## TimeTableNoticeService.py
      def process()
      : 시간표 요청을 처리하고 처리 결과 응답 메시지를 생성해 반환합니다.