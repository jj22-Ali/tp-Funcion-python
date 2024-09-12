""" Escribir una función para eliminar una subcadena de una cadena de 
caracteres, a partir de una posición y cantidad de caracteres dados, 
devolviendo la cadena resultante. Escribir también un programa para verificar 
el comportamiento de la misma. Escribir una función utilizando rebanadas."""

def eliminar_subcadena(cadena, posicion, cantidad):
    return cadena[:posicion] + cadena[posicion + cantidad:]

cadena = "Hola, este es un ejemplo"
posicion = 5
cantidad = 4
resultado = eliminar_subcadena(cadena, posicion, cantidad)
print("Cadena resultante:", resultado)