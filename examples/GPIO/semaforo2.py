#Semáforo con modo noche
#Ernesto Tolocka 2021
#www.profetolocka.com.ar/pytrainer

#Mide el nivel de luz a través del sensor LDR
#Si es de noche, cambia a modo intermitente

from PyTrainer import *
from time import sleep

#Comienza con todos apagados
ledVerde.off ()
ledRojo.off ()
ledAmarillo.off ()

#Tiempo de encendido de cada led
tiempoRojo = 1
tiempoVerde = 1
tiempoAmarillo = 0.2

ModoNoche = False

TiempoNoche = 0.5

#Valor del ADC umbral para determinar que no hay luz
#Modificar según el nivel de iluminación
UmbralNoche = 300

#Repite por siempre
while (True):
    
    print (sensorLDR.read ())
   
    #Según la cantidad de luz, definir el modo de funcionamiento
    if (sensorLDR.read () < UmbralNoche):
        ModoNoche = True
    else:
        ModoNoche = False
   
    if (ModoNoche == False):
        #Modo Normal
        #Prende led verde
        ledVerde.on ()
        sleep (tiempoVerde)
        ledVerde.off ()
    
        #Prende led Amarillo
        ledAmarillo.on ()
        sleep (tiempoAmarillo)
        ledAmarillo.off ()
    
        #Prende led Rojo
        ledRojo.on ()
        sleep (tiempoRojo)
        ledRojo.off ()
    else:
        #Modo Noche
        ledVerde.off ()
        ledRojo.off ()
        
        ledAmarillo.on ()
        sleep (TiempoNoche)
        ledAmarillo.off ()
        sleep (TiempoNoche)
    