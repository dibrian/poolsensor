#!/usr/bin/python
#--------------------------------------

import datetime

def most(id):
  now = datetime.datetime.now()
  #print(now.year, now.month, now.day, "-",now.hour, now.minute, now.second)
  time = "["+str(now.year)+"."

  #Month
  if now.month < 10 :
    time = time+"0"+str(now.month)+"."
  else:
    time = time+str(now.month)+"."
  
  #Day
  if now.day < 10 :
    time = time+"0"+str(now.day)+" "
  else:
    time = time+str(now.day)+" "
  
  #Hour
  if now.hour < 10 :
    time = time+"0"+str(now.hour)+":"
  else:
    time = time+str(now.hour)+":"

  #Minute
  if now.minute < 10 :
    time = time+"0"+str(now.minute)+":"
  else:
    time = time+str(now.minute)+":"

  #Second
  if now.second < 10 :
    time = time+"0"+str(now.second)+"] "
  else:
    time = time+str(now.second)+"] "

  return(time)

if __name__ == '__main__':
    print(most(1))