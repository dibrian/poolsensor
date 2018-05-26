#!/usr/bin/python
#--------------------------------------
import TimeStamp as TS
import ReleKapcs, GetTemp, log, time, datetime

from model import Sensor
from model import Relay

if __name__ == '__main__':



  time_start=10
  time_stop=18
  sleep_timer = 30
  dif_temp_be = 15000
  dif_temp_ki = 5000


  # Script has been called directly
  
  log.prnt(TS.most(1) + "---------------Rendszerinditas------------------")
  
  #Init sensors
  
  log.prnt(TS.most(1) + ". Szenzorok inicializalasa...")
  
  global sensors=[]

  medence = Sensor()
  medence.id = '28-0417c2d68cff'
  medence.name = "Medence (1)"
  medence.temp = GetTemp.gettemp(medence.id);
   # sensors.append(medence)


  sensor1 = Sensor()
  sensor1.id = '28-0417c3b21dff'
  sensor1.name = "Panel (1)"
#  sensor.temp = GetTemp.gettemp(sensor.id);
  sensor1.temp = "0"
  sensors.append(sensor1)
  
  sensor2 = Sensor()
  sensor2.id = '28-0417c3b93dff'
  sensor2.name = "Panel (2)"
#    sensor.temp = GetTemp.gettemp(sensor.id);
  sensor2.temp = "0"
  sensors.append(sensor2)
  
  sensor3 = Sensor()
  sensor3.id = '28-0417c3b7a4ff'
  sensor3.name = "Panel (3)"
#  sensor.temp = GetTemp.gettemp(sensor.id)
  sensor3.temp = "0"
  sensors.append(sensor3)
     
  avg_temp = 0
  
  count = 0
  while count < len(sensors):
    sensors[count].temp = GetTemp.gettemp(sensors[count].id)
    log.prnt(TS.most(1) + ".. " + sensors[count].name + ", homersekleti erteke: " + "{:.3f}".format(sensors[count].temp/float(1000)))
    avg_temp = avg_temp + sensors[count].temp
    count += 1
  
  avg_temp = (avg_temp / (count))
  
  log.prnt(TS.most(1) + ".. Panelek atlaghomerseklete: %s" %(format(avg_temp/float(1000))))
#  log.prnt(TS.most(1) + "..")
  
  #Init relays
  log.prnt(TS.most(1) + ". Relek inicializalasa...")
  
  relays = []
  
  relay1 = Relay()
  relay1.id=17
  relay1.name="Melegito szivattyu"
  relay1.state=ReleKapcs.mizu(relay1.id)
  relays.append(relay1)
  
  relay2 = Relay()
  relay2.id=18
  relay2.name="Tisztito szivattyu"
  relay2.state=ReleKapcs.mizu(relay2.id)
  relays.append(relay2)
  
  count = 0
  while count < len(relays):
    if relays[count].state == False:  
      log.prnt(TS.most(1) + ".. " + relays[count].name + ", allapota: <<< On >>>")
    else:
      log.prnt(TS.most(1) + ".. " + relays[count].name + ", allapota: <<< Off >>>")
    count += 1
    
  
  log.prnt(TS.most(1) + ". Inditasi ido: %s ora" %(str(time_start)))
  log.prnt(TS.most(1) + ". Kikapcsolasi ido: %s ora" %(str(time_stop)))
  
  log.prnt(TS.most(1) + "--------------Sikeres rendszerinditas-------------")
#BU_logic

def logValues():
    if count == len(sensors) - 1:
        log.temp(str(sensors[count].temp) + ";\n")
    else:
        log.temp(str(sensors[count].temp) + ";")
    log.prnt(TS.most(1) + ". " + sensors[count].name + ", homersekleti erteke: " + "{:.3f}".format(
        sensors[count].temp / float(1000)))


while True:
    #log.prnt(TS.most(1) + "Szenzorok olvasasa...")
    log.prnt(TS.most(1) + "Szenzorok olvasasa...")

    medence_temp = GetTemp.gettemp(medence.id)
    log.prnt(TS.most(1) + ". " + medence.name + ", homersekleti erteke: " + "{:.3f}".format(
        medence_temp / float(1000)))

    avg_temp = 0
    count = 0
    while count < len(sensors):
        sensors[count].temp = GetTemp.gettemp(sensors[count].id);
        if int(sensors[count].temp) > 0:
            logValues()
            avg_temp = avg_temp + int(sensors[count].temp)
            count += 1

    avg_temp = (avg_temp / (count))
    log.prnt(TS.most(1) + ".. Panelek atlaghomerseklete: %s" %(format(avg_temp/float(1000))))
    
    log.prnt(TS.most(1) + "Relek olvasasa...")
    count = 0
    while count < len(relays):
        relays[count].state = ReleKapcs.mizu(relays[count].id);
        if relays[count].state == False:  
          log.prnt(TS.most(1) + ". " + relays[count].name + ", allapota: <<< On >>>")
        else:
          log.prnt(TS.most(1) + ". " + relays[count].name + ", allapota: <<< Off >>>")
        count += 1

    now = datetime.datetime.now()
    #print(now.year, now.month, now.day, "-",now.hour, now.minute, now.second)
#    t=30
    if (now.hour < time_start):
        log.prnt(TS.most(1) + "Koran van meg, nem zajongunk...")
        count = 0
        while count < len(relays):
            if relays[count].state == False:  
              log.prnt(TS.most(1) + ". " + relays[count].name + " <<< Off >>>")
              ReleKapcs.kapcs(relays[count].id,True)
            count += 1
        
        sleep_timer=60
    else:
        if (now.hour > time_stop):
            log.prnt(TS.most(1) + "Keso van mar, nem zajongunk...")
            count = 0
            while count < len(relays):
                if relays[count].state == False:  
                    log.prnt(TS.most(1) + ". " + relays[count].name + " <<< Off >>>")
                    ReleKapcs.kapcs(relays[count].id,True)
                count += 1
            
            sleep_timer=60
        else:
    
            if ((avg_temp-dif_temp_be) > medence_temp):
                
                if relays[0].state == True:
                    log.prnt(TS.most(1) + "<<<< "+ relays[0].name + " ON >>>>")
                    if ReleKapcs.kapcs(relays[0].id,False) == 1:
                     log.prnt(TS.most(1) + "Sikeres kapcsolasi kerelem")
                     relays[0].state = False
                     sleep_timer=10
                     log.prnt(TS.most(1) + "Alvasi periodus beallitva %s masodpercre" % (str(sleep_timer)))
                    else:
                     log.prnt(TS.most(1) + "Nem sikerult kapcsolni")
            else:
                if (avg_temp-dif_temp_ki < medence_temp):
                    
                    if relays[0].state == False:
                        log.prnt(TS.most(1) + "<<<< " + relays[0].name + " OFF >>>>")
                        if ReleKapcs.kapcs(relays[0].id,True) == 1:
                            log.prnt(TS.most(1) + "Sikeres kapcsolasi kerelem")
                            relays[0].state = True
                            sleep_timer=60
                            log.prnt(TS.most(1) + "Alvasi periodus beallitva %s masodpercre" % (str(sleep_timer)))
                        else:
                            log.prnt(TS.most(1) + "Nem sikerult kapcsolni")
    log.prnt(TS.most(1) + "---------------------------")
    log.prnt(TS.most(1) + "Most varunk %s masodpercet..." % (str(sleep_timer)))
    log.prnt(TS.most(1) + "---------------------------")
    time.sleep(sleep_timer)
    
    
     
     