""" Ingresar una frase desde el teclado y usar un conjunto para eliminar las 
palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar 
las palabras ordenadas según su longitud"""

def elminar_palabras_repetidas_y_ordernar(frase):
    palabras = set(frase.split())
    ord_palabras = sorted(palabras, key=len)
    return ord_palabras

frase = input("Ingrese una frase: ")
resultado = elminar_palabras_repetidas_y_ordernar(frase)
print("Frase inicial: ", frase)
print("Palabras ordenadas por longitud:", resultado)





"""sorted(palabras, key=len):
Se usa la función sorted() para ordenar las palabras por su longitud. El parámetro key=len indica que la clave de ordenación es la longitud de cada palabra."""

"""set(frase.split()):

Luego, se convierte la lista de palabras en un conjunto con set(). Los conjuntos en Python eliminan automáticamente los elementos duplicados. El resultado será un conjunto de palabras únicas:"""
