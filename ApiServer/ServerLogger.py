import os
import datetime

log_filename = "Log.txt"

class Logger:
  def __init__(self):
    # 인스턴스 생성과 동시에 Log.txt라는 파일을 만들거나 연다.
    self.log_fp = open(log_filename, 'a')

  def Log(self, message):
    log_string = datetime.datetime.today().strftime("[%y.%m.%d, %X] ") + message # [19.09.23, 22:20:13] + 메시지가 된다! 
    print(log_string) # 콘솔에 출력

    self.log_fp.write(log_string) # 파일에 출력
    self.log_fp.flush()
  
  def Close(self):
    self.log_fp.close() # 파일스트림을 닫는다.
