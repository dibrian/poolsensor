#!/usr/bin/python
#--------------------------------------
import datetime

def log(msg):
  now = datetime.datetime.now()
  filename = "./log/"+str(now.year)+str(now.month)+str(now.day)+"_main.txt"
  try:
    file = open(filename,"a")
  except:
    file = open(filename,"w")
  msg=msg+"\n"
  file.write(msg)
  
  file.close()
  
def temp(msg):
  now = datetime.datetime.now()
  filename = "./log/"+str(now.year)+str(now.month)+str(now.day)+"_temp.txt"
  try:
    file = open(filename,"a")
  except:
    file = open(filename,"w")
  file.write(msg)
  file.close()
  
def prnt(msg):
  log(msg)
  print(msg)
 
if __name__ == '__main__':
  prnt("teszt")