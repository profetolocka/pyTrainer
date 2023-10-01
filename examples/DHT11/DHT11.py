#Lectura del sensor de temperatura y humedad

#Ernesto Tolocka 2021
#www.profetolocka.com.ar/pytrainer

from PyTrainer import *
from time import sleep


while (True):
    
    #Siempre hacer un retardo antes de intentar leer el DHT11
    sleep (1)
    sensorDHT.measure ()
    temp=sensorDHT.temperature ()
    hum=sensorDHT.humidity()
    print ("T={:02d} ºC, H={:02d} %".format (temp,hum))
    
    
    



