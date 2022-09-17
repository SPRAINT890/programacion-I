def listaHabitaciones(array):
    for x in array:
        for y in x:
            print(y, end=" ")
        print()


def mostrarHabitacion(numeroPuerta, array):
    try:
        print(array[numeroPuerta][1] + " camas, " + array[numeroPuerta][2] + " planta")
    except:
        print("error el " + str(numeroPuerta) + " no esta asociado a ninguna habitacion")


casaRural = [["Habitacion", "Camas", "Planta"], ["1. Azul", "2", "Primera"], ["2. Roja", "1", "Primera"],
            ["3. Verde", "3", "Segunda"], ["4. Rosa", "2", "Segunda"], ["5. Gris", "1", "Tercera"]]

usuario = input("1 - Listar Habitaciones \n2 - elegir habitacion \n3 - exit\n")
while int(usuario) != 3:
    match int(usuario):
        case 1:
            print("\n" * 130)
            print(listaHabitaciones(casaRural))
            usuario = input("\n1 - Listar Habitaciones \n2 - elegir habitacion \n3 - exit\n")
        case 2:
            print("\n" * 130)
            habitacion = input("numero de habitacion: ")
            mostrarHabitacion(int(habitacion), casaRural)
            usuario = input("\n1 - Listar Habitaciones \n2 - elegir habitacion \n3 - exit\n")
