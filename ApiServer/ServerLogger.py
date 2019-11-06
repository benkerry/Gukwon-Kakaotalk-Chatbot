import os
import datetime

log_filename = "Log.txt"

class Logger:
  def __init__(self):
    self.log_fp = open(log_filename, 'a', encoding="UTF-8")

  def log(self, message:str):
    str_log = (datetime.datetime.today().strftime("[%y.%m.%d, %X] ") + message + '\n').encode("utf-8")
    print(str_log)

    self.log_fp.write(str_log.decode('utf-8'))
  
  def close(self):
    self.log_fp.close()
