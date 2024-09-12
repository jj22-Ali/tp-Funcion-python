def vuelto(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
            return "Error: El dinero recibido es insuficiente."  

    billetes = [500, 100, 50, 20, 10, 5, 1]

    vuelto = dinero_recibido - total_compra
    resultado = f"El vuelto es de ${vuelto}.\n"

    for billete in billetes:
          cantidad_billetes = vuelto // billete
          if cantidad_billetes > 0 :
                resultado += f"{cantidad_billetes} billete(s) de ${billete}\n"
          vuelto %= billete
    
    return resultado
                
def programa_principal():
      
    total_compra = int(input("Ingresa el total de la compra: "))
    dinero_recibido = int(input("Ingresa el dinero recibido: "))
    print(vuelto(total_compra, dinero_recibido))


programa_principal()