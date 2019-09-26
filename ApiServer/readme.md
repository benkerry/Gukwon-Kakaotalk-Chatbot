# ApiServer
  
## main.py
   이 파일을 실행하면 서버가 시작됩니다.
  
  
## ServerLogger.py
### class Logger : 서버 로그를 남깁니다. 이 클래스의 인스턴스는 하나만 생성할 수 있습니다.
     def Log(message)  
     : Parameter로 로그 메시지를 남기면, 해당 로그가 콘솔에 출력된 후 파일에 저장됩니다.

     def Close()
     : 로깅을 위해 만들어진 FileStream을 닫습니다.
  
  
## JSON Return Format 정의
#### TestDDay_Query에 대한 Return Format
      {
          version: [현재 스킬서버의 버전]
          data: {
              test_type: [어떤 시험인지(ex. 중간고사, 수능)]
              datetime: [시험의 날짜(ex. 2019. 09. 19.)]
              left_days: [남은 날짜]
          }
      }
  
  
#### MealService_Query에 대한 Return Format
      {
          "version": "[현재 스킬서버의 버전(ex. 2.0)]",
          "data": {
              "meal_time": "[어떤 급식인지(ex. 아침, 점심, 저녁)]",
              "result_string": "[메뉴 리스트(Escape Sequence 포함)(ex. '밥\n요구르트...')]"
          }
      }
  
  
#### TimeTable_Query에 대한 Return Format
      {
          "version": "[현재 스킬서버의 버전(ex. 2.0)]",
          "data": {
              "date": "[언제의 시간표인지(ex. 오늘, 내일, 모레, 이번 주 x요일)]",
              "grade_class": "[몇학년 몇반의 시간표인지(ex. 3-4, 2-5)]",
              "result_string": "[시간표 리스트(Escape Sequence 포함)(ex. '1교시: 국어\n...')]"        
          }
      }
  
  
#### Notice_Query에 대한 Return Format
      {
          "version": "[현재 스킬서버의 버전(ex. 2.0)]",
          "template": {
              "listcard": {
                  "header": {
                      "title": "공지사항",
                      "imageurl": "http://school.cbe.go.kr/hosts/gukwon-h/M01/logo.png" 
                  },
                  "items": [
                     {
                         "title": "[공지사항 Title]",     
                          "decription": "[내용 일부]",
                          "imageUrl": "[관련 이미지 링크]",
                          "link": {
                              "web": "[해당 게시물 링크]"
                          }
                      }
                  .
                  .
                  .
                  .
                  .
                  ]
              }
          }
      }
  
  
#### ScheduleTable_Query에 대한 Return Format
      {
         "version": "[현재 스킬서버의 버전(ex. 2.0)]",
          "template": {
              "outputs":[
                  {
                      "simpleText":{
                          "text": "[(ex. '이번 주의 학사일정을 문의하셨군요!\n\n00월 00일 방학.....')]"
                      }
                  }
              ]
          }
      }
  
  
##### 이외의 블록에 대한 Format은 추후 결정하여 커밋하겠음.