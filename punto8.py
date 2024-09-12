"""Eliminar de una lista de palabras que se encuentren en una segunda lista. 
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante."""

lista_original = ["manzana", "pera", "banana", "naranja", "uva"]
palabras_a_eliminar = ["pera", "uva"]

# la "palabra" que aparece primero, es el item uno de la lista original que quiero asignar
lista_resultante = [palabra for palabra in lista_original if palabra not in palabras_a_eliminar]

print("Lista original:", lista_original)
print("Palabras a eliminar:", palabras_a_eliminar)
print("Lista resultante:", lista_resultante)