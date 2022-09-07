"""
Escriba un programa para encontrar cuántas veces aparece un substring dado
en el String de referencia. Por ejemplo, how_many(‘Montevideo’, ‘Universidad de
Montevideo ubicada en Montevideo’) devuelve 2 (dado que hay 2 repeticiones
de ‘Montevideo’ en String de referencia). Puede servir método count() y split().
"""

def how_many(palabra_a_buscar, frase):
    palabra_a_buscar = palabra_a_buscar.lower()
    frase = frase.lower()
    frase = frase.split()
    print(frase.count(palabra_a_buscar))


how_many(input("ingrese la palabra a buscar: "), input("ingrese la frase donde buscar: "))
