"""
Escriba un programa en Python para encontrar la mediana entre tres números
dados.
"""
numeros = [int(input("ingrese el 1er valor: ")), int(input("ingrese el 2do valor: ")), int(input("ingrese el 3er valor: "))]
mediano = sorted(numeros)
print(mediano[1])
