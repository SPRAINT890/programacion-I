"""
Escriba un programa para eliminar caracteres de una cadena desde cero hasta
n y devolver una nueva cadena. Por ejemplo, remove_chars(‘python’, 2) debe
imprimir ‘hon’.
"""

def remove_chars(cadena, cantidad):
    c = 0
    newcadena = ""
    for letra in cadena:
        if c < cantidad:
            c += 1
        else:
            newcadena += letra
    print(newcadena)


remove_chars(input("ingrese una palabra "), int(input("ingrese un numero: ")))
