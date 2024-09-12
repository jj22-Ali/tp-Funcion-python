"""Desarrollar una función que determine si una cadena de caracteres es capicúa, 
sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que 
permita verificar su funcionamiento. """

def capicua(Cadena_texto_o_numero):
    longitud = len(Cadena_texto_o_numero)
    for i in range(longitud // 2):
        if Cadena_texto_o_numero[i] != Cadena_texto_o_numero[longitud - 1 - i]:
            return False
    return True

Cadena_texto_o_numero = input("Ingresa una cadena: ")
if capicua(Cadena_texto_o_numero):
    print("los caracteres o los numeros son capicúa.")
else:
    print("los caracteres o numeros no son capicúa.")
