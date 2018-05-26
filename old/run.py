#!/usr/bin/python
#--------------------------------------
import TimeStamp as TS
import ReleKapcs, GetTemp, log

from model import Sensor

if __name__ == '__main__':

  # Script has been called directly
  
  sensors=[]

  sensor = Sensor()
  sensor.id = '28-0417c2d68cff'
  sensor.name = "Medence (1)"
  sensor.temp = GetTemp.gettemp(sensor.id);
  sensors.append(sensor)
  
  sensor = Sensor()
  sensor.id = '28-0417c3b93dff'
  sensor.name = "Panel (1)"
  sensor.temp = GetTemp.gettemp(sensor.id);
  sensors.append(sensor)
  
  
  count = 0
  while count < len(sensors):
    log.prnt(TS.most(1) + sensors[count].name + " szenzor inicializálva, hőmérsékleti értéke: " + "{:.3f}".format(sensors[count].temp/float(1000)))
    count += 1

#  count = 0
#  while count < 2:
#      id = "28-0417c2d68cff"
#      sensor_new = Sensor(id,"ciklusbol_generalt %s" %(count),GetTemp.gettemp(id))
#      sensors.append(sensor_new)
#      count += 1
  
  #print(sensor[0]name)
  
  
#  id = '28-0417c2d68cff'
#  mytemp_1 = GetTemp.gettemp(id);
#  log.prnt(TS.most(1) + "1. szenzor: " + "{:.3f}".format(mytemp_1/float(1000)))
#  log.temp(TS.most(1) + str(mytemp_1)+";")
  

#  log.prnt(TS.most(1) + sensor2.name + " szenzor: " + "{:.3f}".format(sensor2.temp/float(1000)))
#  log.temp(TS.most(1) + str(sensor2.temp)+";")

#  id =  '28-0417c3b93dff'
#  mytemp_2 = GetTemp.gettemp(id);
#  log.prnt(TS.most(1) + "2. szenzor: "  + '{:.3f}'.format(mytemp_2/float(1000)))
#  log.temp(str(mytemp_2)+";\n")
  
if (sensors[1].temp > sensors[0].temp):
    log.prnt(TS.most(1) + "A %s szenzor értéke a kisebb, ezért bekapcsolom" %(sensors[0].name))
    id=17
    
    if ReleKapcs.releon(id) == 1:
     log.prnt(TS.most(1) + "Sikeres kapcsolási kérelem")
    else:
     log.prnt(TS.most(1) + "Nem sikerült kapcsolni")
else:
    log.prnt(TS.most(1) + "Az %s szenzor értéke a kisebb, ezért kikapcsolom" %(sensors[1].name))
    id=17
    
    if ReleKapcs.releoff(id) == 1:
     log.prnt(TS.most(1) + "Sikeres kapcsolási kérelem")
    else:
     log.prnt(TS.most(1) + "Nem sikerült kapcsolni")

 
msg=TS.most(1) + "----------------------------------------------------"    
log.log(msg)
     
     