#! /usr/bin/python
# -*- coding: utf-8 -*-

# 3. Realizar un programa que permita determinar el pago semanal de un trabajador
# considerando los siguientes aspectos: las horas trabajadas, la tarifa por hora y los
# descuentos. Si la cantidad de horas trabajadas es mayor a 40 se le debe pagar un bono
# del 50% adicional.

horas = int(input("Ingrese las horas trabajadas:"))
tarifa = int(input("Ingrese la tarifa por hora:"))
descuentos = int(input("Ingrese los descuentos:"))

pago = (horas * tarifa) - descuentos

if horas > 40:
    pago = pago + (pago * 0.5)

print "El pago semanal es = {0}".format(pago)

