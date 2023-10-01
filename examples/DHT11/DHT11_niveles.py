#Sensor de nivel de humedad con alarma
#El nivel de humedad del aire dentro de una vivienda no debe ser muy elevado
#ya que es perjudicial para personas con afecciones respiratorias.
#Un valor de 55% se considera aceptable, uno mayor es desaconsejable.
#Este programa monitorea el nivel de humedad y alerta usando los leds de colores
#Si es menor a 50%, prende verde
#Si esta entre 50 y 55, prende el amarillo
#Si es 55 o superior prende rojo

#Ernesto Tolocka 2021
#www.profetolocka.com.ar/pytrainer


from pyTrainer import *
from time import sleep

nivelVerde = 50
nivelAmarillo = 55


while (True): 
    
    #Leer el sensor de humedad
    #Siempre un retardo antes
    sleep (1)
    sensorDHT.measure ()
    humedad = sensorDHT.humidity ()
    #humedad=55  #Fijar valor si no se logran las medidas adecuadas
    print (humedad)
    
    if (humedad < nivelVerde):
        ledVerde.on ()
        ledAmarillo.off ()
        ledRojo.off ()
        
    elif (humedad < nivelAmarillo):
        ledVerde.off ()
        ledAmarillo.on ()
        ledRojo.off ()
        
    else:
        ledVerde.off ()
        ledAmarillo.off ()
        ledRojo.on ()
   
        