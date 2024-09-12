def validar_fecha(dia, mes, año):
    if año < 1 :
        return False
    
    if mes < 1 or mes > 12: 
        return False

    max_dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (año % 4 == 0 and año % 100 != 0):
        max_dias_por_mes[1]=29

    if dia < 1 or dia > max_dias_por_mes[mes - 1]:
        return False
    
    return True

def programa_principal():

    dia = int(input("Ingresa el dia: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))

    if validar_fecha(dia, mes, año):
        print("La fecha", dia,"-",mes,"-",año, " es valida")
    else:
        print("La fecha", dia,"-",mes,"-",año, " no es valida")

programa_principal()