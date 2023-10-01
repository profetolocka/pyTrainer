#Variables booleanas
#Ernesto Tolocka 2023
#www.profetolocka.com.ar/pytrainer

#Lectura de entradas y control de salidas como variables booleanas

from pyTrainer import *

while (1):
    
    LED0.value (not(SW0.value()))

    LED1.value (not(SW1.value()))

       
    
    