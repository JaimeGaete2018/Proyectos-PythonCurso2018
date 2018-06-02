#! /usr/bin/python
# -*- coding: utf-8 -*-

from random import *

x = 0
i = 0
while True:
    x = randint(1,999)
    i += 1
    print(x)
    if x == 5:
        break
    x = 0

print "En {0} intentos salio del ciclo".format(i)
