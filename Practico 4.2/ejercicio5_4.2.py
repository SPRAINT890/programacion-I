"""
Escriba un programa en Python que acepte un número positivo y reste de este
número la suma de sus dígitos y así sucesivamente. Continuar esta operación
hasta que el número sea negativo y mostrar el resultado.
"""


def get_digitos(num):
    i = 0
    dig = []
    while num > 9:
        dig.append(num % 10)
        i += 1
        num //= 10
    dig.append(num)
    return dig


def sum_digitos(dig):
    num = 0
    for i in dig:
        num += i
    return num


def resta(num):
    suma = sum_digitos(get_digitos(num))
    while num >= 0:
        num -= suma
    print(num)


numero = int(input("Ingrese un numero "))
resta(numero)
