"""
Escriba un programa en Python para probar si un carácter o letra dada
(mayúscula o minúscula) es una vocal o no.
"""

letra = input("Ingrese una letra o caracter: ")

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print("es vocal")
else:
    print("no es vocal")
