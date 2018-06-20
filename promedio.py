#! /usr/bin/python
# -*- coding: utf-8 -*-

n = int(input("Ingrese la cantidad de datos: "))

suma = 0

for i in range(n):
    num = float(input("Ingrese el numero: "))
    suma = suma + num
    prom = suma / n
    print("Promedio = ", prom)
