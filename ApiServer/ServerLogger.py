import os
import datetime

log_filename = "Log.txt"

class Logger:
  def __init__(self):
    self.log_fp = open(log_filename, 'a')
    self.lst_logbuf = []

  def log(self, message:str):
    str_log = datetime.datetime.today().strftime("[%y.%m.%d, %X] ") + message + '\n'
    print(str_log)

    self.lst_logbuf.append(str_log)

    if len(self.lst_logbuf) > 5:
      self.write_log()

  def write_log(self):
    for i in self.lst_logbuf:
      self.log_fp.write(i)
    self.lst_logbuf.clear()
  
  def close(self):
    for i in self.lst_logbuf:
      self.log_fp.write(i)

    del(self.lst_logbuf)
    self.log_fp.close() # 파일 스트림을 닫는다.
