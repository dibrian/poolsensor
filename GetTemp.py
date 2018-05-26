#!/usr/bin/python
#--------------------------------------
import model

def gettemp(id):
  mytemp = 0
  while int(mytemp) < 1:
      try:
      #  mytemp = ''
        filename = 'w1_slave'
        f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
        line = f.readline() # read 1st line
        crc = line.rsplit(' ',1)
        crc = crc[1].replace('\n', '')
        if crc=='YES':
          line = f.readline() # read 2nd line
          mytemp = line.rsplit('t=',1)
        else:
          mytemp = 0
        f.close()
        return int(mytemp[1])

      except:
        return 0