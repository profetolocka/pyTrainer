#Lectura de valores analogicos
#Ernesto Tolocka 2023
#www.profetolocka.com.ar/pytrainer

#Muestra como leer valores analogicos desde la entrada A0

from pyTrainer import *
from time import sleep

while (1):

    print (A0.read ())
    sleep (1)
    