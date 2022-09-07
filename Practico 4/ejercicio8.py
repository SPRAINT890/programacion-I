"""
Defina un archivo que permita representar una serie aritmética.
Una serie aritmética viene caracterizada por el primer elemento de la serie y el
incremento o diferencia entre dos elementos sucesivos de la serie.
Implemente un método que permita calcular la suma de los n primeros
elementos de la serie (utilice un bucle para realizar esta operación)
"""


def seriearitmetica(inicio, diferencia, fin):
    resultado = 0
    out = [inicio]
    while resultado < fin-1:
        out.append(inicio + diferencia)
        inicio = inicio + diferencia
        resultado += 1
    return out


inicio = input("Indique el inicio de la serie aritmetica: ")
diferencia = input("indique la diferencia entre cada numero: ")
fin = input("indique la cantidad de veces de la serie aritmetica: ")

print(seriearitmetica(int(inicio), int(diferencia), int(fin)))
