#Interruptor crepuscular
#Se debe conectar un modulo LDR a la entrada A0
#Se debe conectar un modulo rele a la salida ledRojo, controlando una lampara
#conectada a la red de corriente alterna
#La lampara se prende cuando se detecta oscuridad, caso contrario se apaga

#Ernesto Tolocka 2023
#www.profetolocka.com.ar/pytrainer


from pyTrainer import *

umbral = 100

while (True):   
    #Leer el sensor de luz
    if (A0.read ()<umbral):
        ledRojo.on ()
    else:
        ledRojo.off ()
         
   