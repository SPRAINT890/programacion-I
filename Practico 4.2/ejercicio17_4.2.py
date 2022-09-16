"""
Escriba un programa Python que reciba una fecha e imprima el día de la fecha.
Por ejemplo, si se recibe 02/08/2022, se debe imprimir 02 de Agosto del 2022.
"""


def separador_fecha(fecha):
    dia = []
    mes = []
    año = []
    diagonales = 0
    for c in fecha:
        if c != "/":
            if diagonales == 0:
                dia.append(c)
            elif diagonales == 1:
                mes.append(c)
            elif diagonales == 2:
                año.append(c)
        else:
            diagonales += 1
    return dia, mes, año

def juntar_numeros_de_array(array):
    num = ""
    for c in array:
        num += str(c)
    return num

def comprobar_mes(num):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "nomviembre", "diciembre"]
    return str(meses[int(num) - 1])

def devolver_fecha(array):
    dia, mes, año = separador_fecha(array)
    dia = juntar_numeros_de_array(dia)
    mes = juntar_numeros_de_array(mes)
    mes = comprobar_mes(mes)
    año = juntar_numeros_de_array(año)

    print(dia + " de " + mes + " del " + año)

devolver_fecha(input("fecha: "))



