# ApiServer

## config.py
   git에 업로드할 수 없는 민감한 정보들(메일 패스워드, DB 패스워드)을 여기에 설정합니다.
      
      str_email: Email
      str_password: Mail Application Password
      str_smtp_name: SMTP Server Name
      tls_port: SMTP Server's TLS Port Number

      str_db_addr: MySQL Database Addr
      str_db_username: MySQL Database Username
      str_db_pwd: MySQL Database Password
      str_db_name: MySQL Database Name
  
## main.py
   이 파일을 실행하면 서버가 시작됩니다.
  
## ServerLogger.py
### class Logger : 서버 로그를 남깁니다. 이 클래스의 인스턴스는 하나만 생성해야 합니다.
      def log(message)  
      : Parameter로 로그 메시지를 남기면, 해당 로그가 콘솔에 출력된 후 파일에 저장됩니다.

      def close()
      : 로깅을 위해 만들어진 FileStream을 닫습니다.

## Mailer.py
### class Mailer : 메일을 전송하는 데 필요한 클래스입니다.
      def __init__(str_email:str, str_password:str, str_smtp_name:str, smtp_port:int)
      : str_email에 본인의 네이버 이메일을, str_password에 네이버 메일 비밀번호를, str_smtp_name에 smtp Server Name을, smtp_port에 smtp SSL Port 번호를 넘겨주십시오.

      def send(str_title:str, str_description:str, lst_to:list)
      : str_title에는 메일 제목을, str_description에 메일 내용을, lst_to에 수신자 목록을 넘겨주면 lst_to의 수신자들에게 메일이 전송됩니다.

      def send_passed_issues(db_manager, lst_passed:list)
      : db_manager에 DBManager의 인스턴스를, lst_passed에 [건의 번호, 건의 내용]을 Element로 갖는 리스트를 넘겨주면 DB의 sign_info 내 이메일이 등록된 모든 관리자들에게 해당 건의가 메일로 전송됩니다.

      def send_error_message(e:Exception, str_error:str)
      : 예외 객체 e와 예외 정보 string(Traceback 권장)을 넘겨주면 해당 정보가 Mailer.py 내부에 하드코딩된 개발자의 이메일로 전송됩니다.  

### DataManager : 챗봇 운용에 필요한 데이터를 관리하는 클래스와 모듈들이 포함되어 있습니다.
  
### Processors : 사용자의 요청을 실질적으로 처리하고 결과를 반환하는 모듈들이 포함되어 있습니다.

### Processors/ResponseGenerator : 카카오톡 응답 메시지를 Format에 맞춰 생성하는 패키지입니다.