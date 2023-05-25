"""
Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.
b) Imprima los tres últimos caracteres.
c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
'reflejoojelfer'.
"""

def imprimir_palabra(palabra):
    print(palabra[:2])

def imprimir_palabra1(palabra):
    print(palabra[-3:])

def imprimir_palabra2(palabra):
    print(palabra[::2])

def imprimir_palabra3(palabra):
    print(palabra[::-1])

def imprimir_palabra4(palabra):
    print(palabra+palabra[::-1])


imprimir_palabra("recta")
imprimir_palabra1("recta")
imprimir_palabra2("recta")
imprimir_palabra3("Hola mundo")
imprimir_palabra4("reflejo")
