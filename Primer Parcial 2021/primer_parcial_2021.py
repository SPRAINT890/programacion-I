def buscar_actividad_por_nombre(mat_actividades, nombre):
    salida = []

    # FIXME colocar algoritmo de operacion

    return salida

def crear_actividad(mat_actividades, nombre, hora_apertura, cantidad_horas, cant_personas_por_hora):
    salida = False

    # FIXME colocar algoritmo de operacion

    return salida

def consultar_aforo_disponible(mat_actividades, mat_reservas, nombre_actividad, dia , hora):
    aforo_disponible = -1

    # FIXME colocar algoritmo de operacion

    return aforo_disponible

def reservar_actividad(mat_actividades, mat_reservas, nombre_actividad, dia, hora, cant_personas):
    reserva_actividad = False

    # FIXME colocar algoritmo de operacion

    return reserva_actividad

# Conjunto de pruebas para validar el correcto funcionamiento de los algoritmos

if __name__ == "__main__":
    mat_actividades = []
    mat_reservas = []

    # Crear dos actividades validas

    salida_1 = crear_actividad(mat_actividades, "Parque Rodo", 14, 8, 50)

    salida_2 = crear_actividad(mat_actividades, "Jardín Japones", 12, 5, 20)

    if (salida_1 and salida_2):
        print("Ok Prueba 1 crear actividades")
    else:
        print("Error Prueba 1 crear actividades")

    # buscar una actividad existente

    actividad_1 = buscar_actividad_por_nombre(mat_actividades, "Parque Rodo")

    if (actividad_1 != [] and  actividad_1[0] == "Parque Rodo" and actividad_1[1] == 14 and actividad_1[2] == 8 and actividad_1[3] == 50):
        print("Ok Prueba 2 buscar actividades")
    else:
        print("Error Prueba 2 buscar actividades")

    # buscar una actividad no existente

    actividad_2 = buscar_actividad_por_nombre(mat_actividades, "Parque Roosevelt")  

    if len(actividad_2) == 0:
        print("Ok Prueba 3 buscar actividades")
    else:
        print("Error Prueba 3 buscar actividades")

    aforo = consultar_aforo_disponible(mat_actividades, mat_reservas, "Parque Salus", 12, 15)

    if aforo == -1 :
        print("Ok Prueba 4 consultar aforo sin actividad existente")
    else:
        print("Error Prueba 4 consultar aforo sin actividad existente")

    aforo = consultar_aforo_disponible(mat_actividades, mat_reservas, "Parque Rodo", 12, 15)
    
    if aforo == 50:
          print("Ok Prueba 4.5 consultar aforo actividad existente")
    else:
        print("Error Prueba 4.5 consultar aforo actividad existente")

    resultado = reservar_actividad(mat_actividades, mat_reservas, "Parque Salus", 12, 15, 50)

    if resultado:
        print("Error Prueba 5 consultar reserva sin actividad existente")
    else:
        print("Ok Prueba 5 consultar reserva sin actividad existente")
    
    resultado = reservar_actividad(mat_actividades, mat_reservas, "Parque Rodo", 12, 15, 10)
    resultado2 = reservar_actividad(mat_actividades, mat_reservas, "Parque Rodo", 12, 15, 15)
    
    if resultado and resultado2:
        print("Ok Prueba 6 consultar reserva con actividad existente")
    else:
        print("Error Prueba 6 consultar reserva con actividad existente")

    aforo = consultar_aforo_disponible(mat_actividades, mat_reservas, "Parque Rodo", 12, 15)

    if aforo == 25:
        print("Ok Prueba 7 aforo disponible post reserva")  
    else:
        print("Error Prueba 7 aforo disponible post reserva")