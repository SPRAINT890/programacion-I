"""
Escriba un programa en Python para calcular e imprimir la suma de dos enteros
dados (mayores o iguales a cero). Si se dan enteros o la suma tiene más de 10
dígitos, imprimir "overflow".
"""


numa, numb = int(input("ingrese un numero mayor o igual a cero: ")), int(input("ingrese otro numero mayor o igual a cero: "))

if numa >= 0 and numb >= 0:
    resultado = numa + numb
    count = 0
    for num in str(resultado):
        count += 1
    if count > 10:
        print("overflow")
else:
    print("numeros invalidos")
