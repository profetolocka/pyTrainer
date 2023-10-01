#Interruptor crepuscular
#Se debe conectar un modulo LDR a la entrada A0
#Se debe conectar un modulo rele a la salida ledRojo, controlando una lampara
#conectada a la red de corriente alterna
#La lampara se prende cuando se detecta oscuridad, caso contrario se apaga
#Luego de la primera detección, se espera 1 segundo y se vuelve a medir el nivel de luz,
#para evitar falsos disparos (ej, relampagos, luces de autos)

#Ernesto Tolocka 2023
#www.profetolocka.com.ar/pytrainer


from pyTrainer import *
from time import sleep

umbral = 100

while (True):
    
    #Leer el sensor de luz
    if (A0.read ()<umbral):
        sleep (1)
        #Confirmar lectura
        if (A0.read()<umbral):
            ledRojo.on ()
    else:
        sleep (1)
        #Confirmar lectura
        if (A0.read ()>=umbral):
            ledRojo.off ()
        
    
   