#Definiciones de entradas y salidas de la placa PyTrainer
#Ernesto Tolocka 2023-2025
#www.profetolocka.com.ar/pytrainer

from hcsr04 import HCSR04
import network, time, dht

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


from machine import Pin, ADC, PWM

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

#Buzzer activo
buzzer = Pin (D7, Pin.OUT, value=0)  

#buzzer pasivo
def bip (duracion):
    zumbador = PWM (Pin(D7), freq=5000, duty=512)
    time.sleep (duracion)
    zumbador.deinit ()

#Teclas
SW0 = Pin (D4, Pin.IN, Pin.PULL_UP)
SW1 = Pin (D3, Pin.IN, Pin.PULL_UP)

#Entradas
E0 = Pin (D4, Pin.IN, Pin.PULL_UP) 
E1 = Pin (D3, Pin.IN, Pin.PULL_UP) 
E2 = Pin (D5, Pin.IN)

#Wifi
def conectaWifi (red, password):
    global miRed
    miRed = network.WLAN(network.STA_IF)     
    if not miRed.isconnected():              #Si no está conectado…
        miRed.active(True)                   #activa la interface
        miRed.connect(red, password)         #Intenta conectar con la red
        print('Conectando a la red', red +"…")
        timeout = time.time ()
        while not miRed.isconnected():           #Mientras no se conecte..
            if (time.ticks_diff (time.time (), timeout) > 10):
                return False
    
    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    return True

## Sensor DHT11
sensorTH = dht.DHT11 (Pin(D5))

