import os
import datetime

log_filename = "Log.txt"

class Logger:
  def __init__(self):
    self.log_fp = open(log_filename, 'a')

  def Log(self, message):
    datetime_string = datetime.datetime.today().strftime("[%y.%m.%d, %X]")
    print(datetime_string + message)
