"""Crear una función lambda para comprobar si un número es par o impar. 
Desarrollar además un programa para verificar el comportamiento de la 
función."""

paridad = lambda x: x % 2 == 0

numero = int(input("Ingresa un número: "))

if paridad(numero):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")