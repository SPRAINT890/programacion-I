"""
Escriba un programa en Python para encontrar divisores comunes entre dos
números en un par dado.
"""

def get_divisores(mayor, menor):
    c = 1
    divisoresDelChico = [] 
    divisores = []
    while c <= menor:
        if not menor % c:
            divisoresDelChico.append(c)
        c += 1
    for numeros in divisoresDelChico:
        if not mayor % numeros:
            divisores.append(numeros)
    return divisores



numeros = [int(input("Ingrese un numero: ")), int(input("Ingrese otro numero: "))]

if numeros[0] > numeros[1]:
    print(get_divisores(numeros[0], numeros[1]))
elif numeros[1] > numeros[0]:
    print(get_divisores(numeros[1], numeros[0]))
else:
    print(get_divisores(numeros[0], numeros[1]))