"""Escribir una función que reciba una lista como parámetro y devuelva True si la 
lista está ordenada en forma ascendente o False en caso contrario. Por 
ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. 
Desarrollar además un programa para verificar el comportamiento de la 
función. """

def Ord_list(lista):
    return lista == sorted(lista)

lista =input("Ingresa un numero/caracter separados por espacio: ").split()
if Ord_list(lista):
    print("La lista está ordenada en forma ascendente.")
else:
    print("La lista no está ordenada en forma ascendente.")