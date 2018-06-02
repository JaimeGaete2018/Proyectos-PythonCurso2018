#! /usr/bin/python
# -*- coding: utf-8 -*-

valormaximo = int(input("Ingrese valor maximo: "))
valorinicial = int(input("Ingrese valor inicial: "))

dia = 0
i = 1

while dia < valormaximo:
    dia += valorinicial * 2
    i += 1

print "En {0} dias se alcanzo el valor maximo".format(i)



