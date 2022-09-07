"""
Escriba un programa para extraer cada dígito de un número entero en el orden
inverso. Por ejemplo, reverse_number(1267) debe retornar 7621.
"""


def reverse_num(num):
    i = 0
    dig = []
    while num > 9:
        dig.append(num % 10)
        i += 1
        num //= 10
    dig.append(num)
    return dig


numReverseArray = reverse_num(int(input("ingrese un numero ")))
numReverse = ""
for digito in numReverseArray:
    numReverse += str(digito)
print(numReverse)
