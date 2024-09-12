"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que 
la misma tiene 80 columnas."""

def imprimir_centrada(cadena):
    columnas = 80
    espacios = (columnas - len(cadena)) // 2  # Calcular cuántos espacios poner a la izquierda
    print(' ' * espacios + cadena)  # Imprimir con los espacios a la izquierda

# Programa para probar
cadena = input("Ingresa una cadena: ")
imprimir_centrada(cadena)