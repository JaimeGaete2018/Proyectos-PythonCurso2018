#! /usr/bin/python
# -*- coding: utf-8 -*-

n = int(input("Ingrese la cantidad de cauchos a comprar: "))

p = float(input("Ingrese el precio unitario: "))

if n > 6:
    x = 0.15 * p
else:
    x = 0.1 * p

total = n * (p - x)

print("El total a pagar es: " , total)