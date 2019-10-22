# ApiServer
  
## main.py
   이 파일을 실행하면 서버가 시작됩니다.
  
  
## ServerLogger.py
### class Logger : 서버 로그를 남깁니다. 이 클래스의 인스턴스는 하나만 생성해야 합니다.
     def Log(message)  
     : Parameter로 로그 메시지를 남기면, 해당 로그가 콘솔에 출력된 후 파일에 저장됩니다.

     def Close()
     : 로깅을 위해 만들어진 FileStream을 닫습니다.

### DataManager : 챗봇 운용에 필요한 데이터를 관리하는 클래스와 모듈들이 포함되어 있습니다.
  
### Processors : 사용자의 요청을 실질적으로 처리하고 결과를 반환하는 모듈들이 포함되어 있습니다.