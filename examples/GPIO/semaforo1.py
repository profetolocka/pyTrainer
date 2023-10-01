#Semáforo simple
#Ernesto Tolocka 2021
#www.profetolocka.com.ar/pytrainer

#Lasluces prenden secuencialmente
#El tiempo de encendido de cada luz está definido por una variable

from pyTrainer import *
from time import sleep

#Comienza con todos apagados
ledVerde.off ()
ledRojo.off ()
ledAmarillo.off ()

#Tiempo de encendido de cada led
tiempoRojo = 1
tiempoVerde = 1
tiempoAmarillo = 0.2

#Repite por siempre
while (True):
    
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
