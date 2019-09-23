# ApiServer

## main.py
   이 파일을 실행하면 서버가 시작됩니다.
 
## ServerLogger.py
### class Logger : 서버 로그를 남깁니다. 이 클래스의 인스턴스는 하나만 생성할 수 있습니다.
     def Log(message)  
     : Parameter로 로그 메시지를 남기면, 해당 로그가 콘솔에 출력된 후 파일에 저장됩니다.

     def Close()
     : 로깅을 위해 만들어진 FileStream을 닫습니다.