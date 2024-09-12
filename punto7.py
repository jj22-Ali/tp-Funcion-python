"""Crear una lista con los cuadrados de los números entre 1 y N (ambos 
incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los 
últimos 10 valores de la lista."""

N = int(input("Ingresa el valor de N: "))
cuadrados = [x ** 2 for x in range(1, N + 1)]
print(cuadrados)
print("Los ultimos 10 cuadrados son: ", cuadrados[-10:])