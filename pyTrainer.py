#Definiciones de entradas y salidas de la placa PyTrainer
#Ernesto Tolocka 2023
#www.profetolocka.com.ar/pytrainer

from hcsr04 import HCSR04

#Mapeo Dx a GPIOx
D0 = 16       
D1 = 5
D2 = 4
D3 = 0
D4 = 2
D5 = 14
D6 = 12
D7 = 13
D8 = 15


from machine import Pin, ADC

#Entrada analogica
A0 = ADC (0)

#Medidor de distancias
medidor = HCSR04 (trigger_pin=D2 , echo_pin=D1)

def distancia_cm ():
    return medidor.distance_cm ()

def distancia_mm ():
    return medidor.distance_mm ()


#Leds
ledVerde = Pin (D6, Pin.OUT, value=0)
ledAmarillo = Pin (D8, Pin.OUT, value=0)
ledRojo = Pin (D0, Pin.OUT, value=0)

LED0 = Pin (D6, Pin.OUT, value=0)
LED1 = Pin (D8, Pin.OUT, value=0)
LED2 = Pin (D0, Pin.OUT, value=0)

#Salidas
S0 = Pin (D6, Pin.OUT, value=0)
S1 = Pin (D8, Pin.OUT, value=0)
S2 = Pin (D0, Pin.OUT, value=0)

#Buzzer
buzzer = Pin (D7, Pin.OUT, value=0)

#Teclas
SW0 = Pin (D4, Pin.IN, Pin.PULL_UP)
SW1 = Pin (D3, Pin.IN, Pin.PULL_UP)

#Entradas
E0 = Pin (D4, Pin.IN, Pin.PULL_UP)
E1 = Pin (D3, Pin.IN, Pin.PULL_UP)
E2 = Pin (D5, Pin.IN)


