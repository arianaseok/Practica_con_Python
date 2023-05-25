"""
Escribir funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
's,e,p,a,r,a,r'
b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
debería devolver 'mi_archivo_de_texto.txt'
c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
'X' debería devolver 'su clave es: XXXX'
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
'255.255.255.0'
"""

def agregar_separador(cadena, caracter):
    return caracter.join(cadena)

def agregar_separador1(cadena, caracter):
    return cadena.replace(" ", caracter)

def remplazar_caracter(cadena, caracter):
    cadena_n = ""
    for pos in cadena:
        cadena_n += caracter
    return cadena_n

def agregar_separador3(cadena, caracter):
    cadena_n = ""
    contador = 0
    for n in cadena:
        cadena_n += n 
        contador += 1
        if (contador % 3 == 0):
            cadena_n += caracter
    return cadena_n

print(agregar_separador("separar", ","))
print(agregar_separador1("mi archivo de texto.txt", "_"))
print(remplazar_caracter("1540", "X"))
print(agregar_separador3("2552552550", "."))
