#! /usr/bin/python
# -*- coding: utf-8 -*-

# 2. Escribir un programa que permita calcular la suma, la resta, el producto y la
# división de dos números dados por el ususario e imprima el resultado. Tomando en
# cuenta cada caso, si el resultado es menor que 20 debe mostrar un mensaje que diga
# AZUL, si es menor que 40 debe decir ROJO, y si es menor que 60 debe decir NEGRO.

def color(valor):
    if valor < 20:
        msg="AZUL"
    elif valor >= 20 and valor < 40:
        msg="ROJO"
    elif valor >= 40 and valor < 60:
        msg="NEGRO"
    else:
        msg = "OTRO COLOR"
    return msg


num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

suma = num1+num2
resta = num1-num2
multi = num1*num2
divi = num1/num2

print "Resultado de la suma = {0}".format(suma)
print(color(suma))
print "Resultado de la resta = {0}".format(resta)
print(color(resta))
print "Resultado de la multiplicacion = {0}".format(multi)
print(color(multi))
print "Resultado de la division = {0}".format(divi)
print(color(divi))



