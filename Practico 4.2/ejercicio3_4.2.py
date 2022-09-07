"""
Escriba un programa en Python que acepte el nombre y apellido del usuario y
los imprima en orden inverso con una coma y espacio entre ellos. Usar input().
"""


nombre = [input("Ingrese su nombre: "), input("Ingrese su apellido: ")]
print(nombre[1] + ", " + nombre[0])
