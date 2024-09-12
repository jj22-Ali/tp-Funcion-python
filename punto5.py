"""Crear una función lambda que devuelva el cuadrado de un valor recibido cómo 
parámetro. Desarrollar además un programa para verificar el comportamiento 
de la función."""

cuadrado = lambda x: x ** 2

numero = int(input("Ingresa un número: "))
print("El cuadrado de", numero, "es:", cuadrado(numero))