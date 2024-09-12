def imprimir_asterico(z, x):
    for i in range(z):
        for j in range(x):
            print("*", end="")
        print(" ")

def imprimir_astericos_2(z,x):
    for i in range(z):
        for j in range(x):
            print("*", end="")
        x += 2
        print(" ")

            

z = int(input("Ingresar filas: "))
x = int(input("Ingresar columnas: "))

imprimir_asterico(z,x)

imprimir_astericos_2(z, 2)