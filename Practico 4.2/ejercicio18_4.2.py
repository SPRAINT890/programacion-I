'''Escriba un programa en Python para calcular el número de días entre dos
fechas. Por ejemplo, si se ingresan 30/08/2022 y 08/09/2022, debe retornar 9
días.
'''

def fecha_a_tres_variables(fecha):
    dia = fecha[0:2]
    mes = fecha[3:5]
    año = fecha[6:]

    return int(dia), int(mes), int(año)

def diferencia_num(num1, num2):
    if num1 < num2:
        dif_num = num1 - num2
    else:
        dif_num = num2 - num1
    return dif_num

def mostrar_diferencia_entre_fechas(fecha1, fecha2):
    dia1, mes1, año1 = fecha_a_tres_variables(fecha1)
    dia2, mes2, año2 = fecha_a_tres_variables(fecha2)

    dif_año = diferencia_num(año1, año2)
    dif_mes = diferencia_num(mes1, mes2)
    dif_dia = diferencia_num(dia1, dia2)
    


    

mostrar_diferencia_entre_fechas(input("Fecha 1: "), input("Fecha 2: "))