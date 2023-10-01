#Semáforo peatonal
#Ernesto Tolocka 2021
#www.profetolocka.com.ar/pytrainer

#Normalmente está en verde hasta que un peatón pulsa teclaVerde, entonces cambia a Amarillo y luego Rojo.
#Después de un tiempo en rojo, vuelve a la condición inicial

from pyTrainer import *
from time import sleep

#Comienza con verde encendido y el resto apagado
ledVerde.on ()
ledRojo.off ()
ledAmarillo.off ()

#Tiempo de encendido de cada led
tiempoRojo = 4
tiempoVerde = 2
tiempoAmarillo = 0.5


#Repite por siempre
while (True):
    
    if (SW0.value () == False):

        ledVerde.off ()
        
        #Hace un "bip"
        buzzer.on ()
        sleep (0.1)
        buzzer.off ()
        
        #Prende led amarillo
        ledAmarillo.on ()
        sleep (tiempoAmarillo)
        ledAmarillo.off ()
        
        #Prende led Rojo
        ledRojo.on ()
        sleep (tiempoRojo)
        ledRojo.off ()
        
        #Vuelve al modo normal
        ledVerde.on ()
        
  