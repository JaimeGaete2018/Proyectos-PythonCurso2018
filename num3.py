#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys

try:
    cantidad = int(input("Ingrese la cantidad de confort a comprar: "))
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error: \n", sys.exc_info()[0]
    raise

try:
    preciounitario = float(input("Ingrese el precio unitario del confort: "))
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error: \n", sys.exc_info()[0]
    raise

OK = "El total a pagar es: "

if cantidad >= 10:
    print( OK , cantidad * (preciounitario - (0.25 * preciounitario)))
elif cantidad >= 5 and cantidad <= 9:
    print(OK , cantidad * (preciounitario - (0.2 * preciounitario)))
elif cantidad >= 1 and cantidad <= 4:
    print(OK , cantidad * (preciounitario - (0.15 * preciounitario)))
elif preciounitario == 0:
    print (OK + "0")
elif preciounitario < 1:
    print "El precio unitario debe ser mayor a 0!!"
elif cantidad < 1:
    print "La cantidad a comprar debe ser mayor a 0!!"

