def paroimpar(valor):
    return valor % 2


numero = input("ingrese un numero ")

print(str(paroimpar(int(numero))))

if paroimpar(int(numero)) != 1:
    print("es par")
else:
    print("es impar")
