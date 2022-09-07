"""
Escriba un archivo donde, dados dos números enteros, devuelva su producto
solo si el producto es igual o menor que 1000, de lo contrario, devuelve su suma.
"""

numeros = [int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo numero: "))]

producto = numeros[0] * numeros[1]
if producto > 1000:
    print("la suma es " + str(numeros[0] + numeros[1]))
else:
    print("el producto es " + str(producto))
