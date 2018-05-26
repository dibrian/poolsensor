#!/usr/bin/python
#--------------------------------------

import RPi.GPIO as GPIO
import time
import TimeStamp as TS

def kapcs(id,state):
 try:
#   GPIO.setwarnings(False);
#   GPIO.setmode(GPIO.BCM);
#   GPIO.setup(id,GPIO.OUT);
#   GPIO.output(id,state)
# #  GPIO.output(id,False);
#  time.sleep(2)
#  GPIO.output(id,True)
  return True
 except:
  return False

def mizu(id):
 try:
  # GPIO.setwarnings(False);
  # GPIO.setmode(GPIO.BCM);
  # GPIO.setup(id,GPIO.OUT);
  # state = GPIO.input(id)
  return True
 except:
  return str("lofasz")


if __name__ == '__main__':
 #time.sleep(5)
 id=17
 
 if kapcs(id,True) == 1:
  print(TS.most(1) +"Rele kikapcsolva")
 else:
  print(TS.most(1) +"Gaz van, relet nem sikerult kikapcsolni, pedig megprobaltam");

