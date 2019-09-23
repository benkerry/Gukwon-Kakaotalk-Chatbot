import os
import datetime

log_filename = "Log.txt"

class Logger:
  def __init__(self):
    self.log_fp = open(log_filename, 'a')

  def Log(self, message):
    log_string = datetime.datetime.today().strftime("[%y.%m.%d, %X] ") + message
    print(log_string)
    self.log_fp.write(log_string)
    self.log_fp.flush()
  
  def Close(self):
    self.log_fp.close()
