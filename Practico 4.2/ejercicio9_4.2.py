"""
Escriba un programa para aceptar una cadena del usuario y mostrar los
caracteres que están presentes en un número de índice par. Por ejemplo,
show_even(‘python’) debe imprimir caracteres ‘p’, ‘t’, ‘o’.
"""


def show_even(cadena):
    c = 0
    for caracter in cadena:
        if not c % 2:
            print(caracter)
        c += 1


show_even(input("Ingrese una palabra "))
