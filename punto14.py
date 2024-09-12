"""Desarrollar una función eliminar_claves() que reciba como parámetros un 
diccionario y una lista de claves. La función debe eliminar del diccionario todas 
las claves contenidas en la lista, devolviendo el diccionario modificado y un 
valor de verdad que indique si la operación fue exitosa. Desarrollar también un 
programa para verificar su comportamiento."""

def eliminar_claves(diccionario, claves):
    exito = False
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            exito = True
    return diccionario, exito

diccionario ={'a': 1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18, "s":19, "t":20,"u":21,"v":22,"w":23,"y":24, "x":25, "z":26}
claves_para_elimnar = ["a","c","m","d","p"]
diccionario_modificado, exito = eliminar_claves(diccionario,claves_para_elimnar)
print("Diccionario modificado", diccionario_modificado)
print("Operación exitosa:", exito)