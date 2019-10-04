import os
import datetime

log_filename = "Log.txt"

class Logger:
  def __init__(self):
    # 인스턴스 생성과 동시에 Log.txt라는 파일을 만들거나 연다.
    self.log_fp = open(log_filename, 'a')

  def log(self, message):
    str_log = datetime.datetime.today().strftime("[%y.%m.%d, %X] ") + message
    print(str_log) # 콘솔에 출력

    self.log_fp.write(str_log + '\n') # 파일에 출력
    self.log_fp.flush()
  
  def close(self):
    self.log_fp.close() # 파일스트림을 닫는다.
