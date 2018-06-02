#! /usr/bin/python
# -*- coding: utf-8 -*-

print "Hola mundo";

# Comillas simples 
cadenaa = 'Texto entre comillas simples'
print cadenaa 
print type(cadenaa)

# Comillas dobles 
cadenab = "Texto entre comillas dobles" 
print cadenab 
print type(cadenab)


# Cadena con codigo escapes 
cadenaesc = 'Texto entre \n\tcomillas simples' 
print cadenaesc 
print type(cadenaesc)

a = 21 
b = 10

if ( a != b ): 
    print "Comparacion != | a no es igual a b" 
else: 
    print "Comparacion != | a es igual a b" 
    
if ( a <> b ): 
      print "Comparacion <> | a no es igual a b" 
else: 
    print "Comparacion <> | a es igual a b"
