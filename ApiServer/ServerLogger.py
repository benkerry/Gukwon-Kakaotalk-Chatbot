import os
import datetime

log_filename = "Log.txt"

class Logger:
  def __init__(self):
    self.log_fp = open(log_filename, 'a')

  def log(self, message:str):
    str_log = datetime.datetime.today().strftime("[%y.%m.%d, %X] ") + message + '\n'
    print(str_log)

    self.log_fp.write(str_log)
  
  def close(self):
    self.log_fp.close() # 파일 스트림을 닫는다.
