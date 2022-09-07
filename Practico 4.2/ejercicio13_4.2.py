"""
Escriba un programa en Python que acepte cuatro números como entrada y los
clasifique en orden descendente.
"""
numeros = [int(input("Ingrese un numero: ")), int(input("Ingrese otro numero: ")), int(input("Ingrese otro numero: ")), int(input("Ingrese otro numero: "))]
print((sorted(numeros, reverse = True)))
