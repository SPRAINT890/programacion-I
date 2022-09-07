"""
Escriba un programa para iterar los primeros 10 números y en cada iteración,
imprima la suma del número actual y anterior. Puede servir función range().
"""
anterior = 0
for actual in range(10):
    if actual == 0:
        print(actual)
    else:
        print(actual + anterior)
    anterior += actual
