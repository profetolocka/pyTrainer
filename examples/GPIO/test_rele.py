from pyTrainer import *
from time import sleep

#Interruptor crepuscular
#Se debe conectar un modulo rele a la salida ledRojo, controlando una lampara
#conectada a la red de corriente alterna
#La lampara se prende cuando se detecta oscuridad, caso contrario se apaga

while (True):
    
    #Leer el sensor de luz
    if (sensorLDR.read ()<100):
        ledRojo.on ()
    else:
        ledRojo.off ()
        
    
   