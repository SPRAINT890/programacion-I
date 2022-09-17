'''Escriba un programa en Python para calcular el número de días entre dos
fechas. Por ejemplo, si se ingresan 30/08/2022 y 08/09/2022, debe retornar 9
días.
'''

def fecha_a_tres_variables(fecha):
    dia = fecha[0:2]
    mes = fecha[3:5]
    año = fecha[6:]

    return int(dia), int(mes), int(año)

def añoBisiesto(año):
    if (año % 4) == 0 and (año % 100) != 0 or (año % 4) == 0 and (año % 100) == 0 and (año % 400) == 0:
        return True
    else:
        return False

def cont_año_bisiesto(num2, dif_num):
    cant_año_bisiesto = 0
    cant_año_natural = 0
    for año in range(dif_num):
        if añoBisiesto(num2 + año) == False:
            cant_año_bisiesto += 1
        else:
            cant_año_natural += 1
    print(str(cant_año_natural) + " " + str(cant_año_bisiesto))
    return cant_año_natural, cant_año_bisiesto

def cont_meses(mes2, mes_año2, dif_mes):
    dias = 0
    for x in range(dif_mes):
        if mes2 % 2 != 0 and mes2 != 1:
            dias += 30
        elif mes2 % 2 == 0:
            dias += 31
        else:
            if añoBisiesto(mes_año2 + x):
                dias += 29
            else:
                dias += 28
    return dias

def diferencia_num_dia(num1, num2, mes_año1, mes_año2, tipo):
    if tipo == 0:
        if num1 > num2:
            dif_num = num1 - num2
            año_natural, año_bisiesto = cont_año_bisiesto(num2, dif_num)
            return año_natural * 365 + año_bisiesto * 366      
        else:
            dif_num = num2 - num1
            año_natural, año_bisiesto = cont_año_bisiesto(num1, dif_num)
            return año_natural * 365 + año_bisiesto * 366

    elif mes_año1 and mes_año2 and tipo == 1:
        if num1 > num2:
            dif_num = num1 - num2
            if mes_año1 > mes_año2:
                dif_mes_año = mes_año1 - mes_año2
                dias_mes = cont_meses(num2, mes_año2, dif_num)
                return dias_mes
            else:
                dif_mes_año = mes_año2 - mes_año1
                dias_mes = cont_meses(num2, mes_año1, dif_num)
                return dias_mes
        else:
            dif_num = num2 - num1
            if mes_año1 > mes_año2:
                dif_mes_año = mes_año1 - mes_año2
                dias_mes = cont_meses(num1, mes_año2, dif_num)
                return dias_mes
            else:
                dif_mes_año = mes_año2 - mes_año1
                dias_mes = cont_meses(num1, mes_año1, dif_num)
                return dias_mes

    else:
        if num1 > num2:
            dif_num = num1 - num2
        else:
            dif_num = num2 - num1
        return dif_num

def mostrar_diferencia_entre_fechas(fecha1, fecha2):
    dia1, mes1, año1 = fecha_a_tres_variables(fecha1)
    dia2, mes2, año2 = fecha_a_tres_variables(fecha2)

    dif_año = diferencia_num_dia(año1, año2, False, False, 0)
    dif_mes = diferencia_num_dia(mes1, mes2, año1, año2, 1)
    dif_dia = diferencia_num_dia(dia1, dia2, False, False, 2)
    
    print("La diferencia de dias es: " + str(dif_año + dif_mes - dif_dia))
    

mostrar_diferencia_entre_fechas("08/09/2024", "08/09/2023")
#mostrar_diferencia_entre_fechas(input("Fecha 1: "), input("Fecha 2: "))