import json, io

class Sensor(object):
    def __init__(self, sensor_id_number = None, name_of_the_sensor = None, sensor_temperature_value = None):
        self.id = sensor_id_number
        self.name = name_of_the_sensor
        self.temp = sensor_temperature_value
    def name(self):
        return (" %s %s %s" % (self.id, self.name, self.temp))
    
    @classmethod
    def getALL(self):
        database = open('./db/db_sensor.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            sensor = Sensor(item['sensor_id_number'], item['name_of_the_sensor'], item['sensor_temperature_value'])
            result.append(sensor)
        return result

class Relay(object):
    def __init__(self, relay_id_number = None, name_of_the_connected_device = None, actual_status_of_operation = None):
        self.id = relay_id_number
        self.name = name_of_the_connected_device
        self.state = actual_status_of_operation
    def name(self):
        return (" %s %s %s" % (self.id, self.name, self.temp))
    @classmethod
    def getALL(self):
        database = open('./db/db_relay.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            relay = Relay(item['relay_id_number'], item['name_of_the_connected_device'], item['actual_status_of_operation'])
            result.append(relay)
        return(result)
    def setALL(self):
        database = open('./db/db_relay.txt', 'w', encoding='ut8')
        
        
        
    