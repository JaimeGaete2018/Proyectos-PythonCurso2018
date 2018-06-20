#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from random import *

try:
    lanzamientos = int(input("Ingrese cantidad de lanzamientos: "))
except IOError as e:
    print "Error I/O ( {0} ): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Error de conversión a int"
except:
    print "Error inesperado: \n", sys.exc_info()[0]
    raise

if lanzamientos < 1:
    print("Debe ingresar un numero mayor a cero")
    sys.exit()

dados = 0
gana = 0
for i in range(lanzamientos):
    dados = randint(1,6)
    #print(dados)
    if dados == 6:
        gana = gana + 600
    elif dados == 3:
        gana = gana + 300 
    elif dados == 1:
        continue
    elif dados in(2,4,5):
        gana = gana - 50

if gana < 0:
    print " Perdio = {0}".format(gana)
elif gana > 0:
    print " Gano = {0}".format(gana)



