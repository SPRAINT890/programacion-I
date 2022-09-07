altura = int(input("ingrese la altura de la piramide: "))

h = 0

for i in range(1, altura + 1):
    for espacio in range(1, (altura - i) + 1):
        print(end="  ")

    while h != (2 * i - 1):
        print("* ", end="")
        h += 1

    h = 0
    print()
