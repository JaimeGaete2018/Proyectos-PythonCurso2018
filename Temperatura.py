#! /usr/bin/python
# -*- coding: utf-8 -*-

salida = False
while not salida:
    print("1. Convertir F a C")
    print("2. Convertir C a F")
    print("3. Salir")
    op = input("Eliga una opcion: ")
    if op == 1:
        f = int(input("Ingrese grados Farenheit: "))
        c = (f-32) * 5/9
        print " Celcius = {0}".format(c)
    elif op == 2:
        c = int(input("Ingrese grados Celcius: "))
        f = (9/5) * (c+32)
        print " Farenheit = {0}".format(f)
    elif op == 3:
        print("Bye")
        salida = True
        #break
