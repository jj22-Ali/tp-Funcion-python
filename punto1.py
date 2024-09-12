#Declaración  de funciones 

def numeros():
    numero = []
    for i in range(3):
        x = int(input("ingresar un numero: "))
        numero.append(x)
    return numero 

def programaPrincipal():
    numerosV = numeros()
    mayor = max(numerosV)
    rep = numerosV.count(mayor)
    if rep > 1:
        
        return -1
    else:
        return numerosV, mayor
    
#Programa principal

x = programaPrincipal()

if x == -1:
    print("no ingresaste ningun numero estrictamente  mayor")
else:
    z , v = x
    print("los numeros ingresados fueron: ", z)
    print("El mayor es: ", v)