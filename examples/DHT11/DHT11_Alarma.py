#Lectura del sensor de temperatura y humedad
#Ernesto Tolocka 2021
#www.profetolocka.com.ar/pytrainer

#Alarma de temperatura
#Se activa si la temperatura sube "delta" grados
#Toma como valor "Normal" el primer valor leido.
 
from PyTrainer import *
from time import sleep

temperatura1 = 0  #Primer valor

delta = 2   #Variación (para arriba) que dispara la alarma

#Empieza en condicion normal, led Rojo apagado y Verde prendido
ledRojo.off ()
ledVerde.on ()


while (True):
    
    #Siempre hacer un retardo antes de intentar leer el DHT11
    sleep (1)
    sensorDHT.measure ()
    temp=sensorDHT.temperature ()
    hum=sensorDHT.humidity()
    
    if (temperatura1 == 0):  #Toma como "normal" el primer valor leído
        temperatura1 = temp
        
    if (temp >= temperatura1 + delta):
        ledRojo.on ()
        ledVerde.off()
    else:
        ledRojo.off ()
        ledVerde.on ()
        
        
    print ("T={:02d} ºC, H={:02d} %".format (temp,hum))
    
    
    



