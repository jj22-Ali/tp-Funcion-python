"""Escribir una función que reciba como parámetro una tupla conteniendo una 
fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha 
expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de 
Octubre de 2017”. Escribir también un programa para verificar su 
comportamiento"""

def fecha_detallada(fecha):
    dias = fecha[0]
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo", 
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",    
        12: "Diciembre"
    }
    mes = meses[fecha[1]]
    anio = fecha[2]
    return f"{dias} de {mes} de {anio}"

fecha = (20, 8, 1998)
print(fecha_detallada(fecha))