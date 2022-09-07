"""
Escriba un programa en Python para encontrar si el número de divisores de un
número entero es par o impar.
"""


def divisores(n):
    x = len([i for i in range(1,n+1) if not n % i])
    return x


if not divisores(int(input("ingrese un numero "))) % 2:
    print("el numero de divisores es par")
else:
    print("el numero de divisores es impar")
