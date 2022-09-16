'''Escriba un programa en Python para calcular el número de días entre dos
fechas. Por ejemplo, si se ingresan 30/08/2022 y 08/09/2022, debe retornar 9
días.
'''

def fecha_a_tres_variables(fecha):
    dia = fecha[0:2]
    mes = fecha[3:5]
    año = fecha[6:]

    return dia, mes, año