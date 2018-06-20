#! /usr/bin/python
# -*- coding: utf-8 -*-

def primo(x):
    a = 0
    for i in range(1,x+1):
        if (x%i)==0:
            a = a + 1
    if a>2:
        return False
    else:
        return True


a = int(input("Desde: "))
b = int(input("Hasta: "))
for n in range(a, b+1):
    if primo(n):
        print ("Numero primo: ",n)


