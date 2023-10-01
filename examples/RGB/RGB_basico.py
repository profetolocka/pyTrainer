#Control de led RGB
#Ernesto Tolocka 2023
#www.profetolocka.com.ar/pytrainer

#Control basico de un led RGB conectado a una salida
#Conectar un modulo de led RGB en salida S0

from pyTrainer import *
import neopixel

LedRGB = neopixel.NeoPixel(LED0, 1)

LedRGB[0] = (200, 0, 100)

LedRGB.write ()
