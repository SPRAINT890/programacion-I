#####################################################
#  PRIMER PARCIAL - Programacion 1 [s2 2022]        #
#                                                   #
#  Nombre y Apellido:  Gaspar Morales               #
#####################################################

# Funciones de EJERCICIO A


from operator import truediv


def asignar_actores_a_peliculas(mat_peliculas, mat_actores, names_peliculas, names_actores, edades_actores):
    """
    Los contadores funcionan, pero en algun lugar no cambia bien las matrices
    """
    
    #matriz con toda la info de los actores a agregar para facilitarme
    actores_y_peliculas = []
    actores_agregados = 0
    for x in range(len(names_actores)):
        nombre = names_actores[x].split(" ", 1)
        actores_y_peliculas.append([nombre[0], nombre[1], edades_actores[x], names_peliculas[x]]) 
    
    for actor_a_agregar in actores_y_peliculas:
        existe_actor = False
        for dic_actores in mat_actores:
            if dic_actores[0] == actor_a_agregar[0]:
                existe_actor = True
        if not existe_actor:
            mat_actores.append([actor_a_agregar[0], actor_a_agregar[1], actor_a_agregar[2], 0, True])
            actores_agregados += 1

    posicion = []
    for actor_a_agregar in actores_y_peliculas:
        contador = 1
        for dic_actores in mat_actores:
            if actor_a_agregar[0] == dic_actores[0] and actor_a_agregar[1] == dic_actores[1]:
                posicion.append(contador)
            else:
                contador += 1
    contador = 0
    existe_pelicula = False
    for actor_a_agregar in actores_y_peliculas:
        for pelicula in mat_peliculas:
            if pelicula[0] == actor_a_agregar[3]:
                pelicula.append(posicion[contador])
                existe_pelicula = True
                break
        if existe_pelicula:
            existe_pelicula = False
        else:
            return -1
        contador += 1
    return actores_agregados

# Funciones de EJERCICIO B
def restringir_peliculas_en_years(mat_peliculas, year_comienzo, year_final):
    peliculas_eliminadas = 0
    for pelicula in mat_peliculas:
        if not pelicula[1] < year_comienzo and not pelicula[1] > year_final:
            True
        else:
            mat_peliculas.remove(pelicula)
            peliculas_eliminadas += 1
    if len(mat_peliculas) == 1:
        for pelicula in mat_peliculas:
            mat_peliculas.remove(pelicula)
    if len(mat_peliculas) == 0:
        return -1
    else:
        return peliculas_eliminadas

# Funciones de EJERCICIO C
def registrar_premios_a_actores_vivos(mat_actores, names_actores, awards_actores):
    actores_y_premios = []
    exitosos = 0
    error = 0
    for x in range(len(names_actores)):
        nombre = names_actores[x].split(" ", 1)
        actores_y_premios.append([nombre[0], awards_actores[x]])

    for actor in actores_y_premios:
        for lista_actores in mat_actores:
            if actor[0] == lista_actores[0] and lista_actores[4] == True:
                lista_actores[3] += actor[1]
                exitosos += 1
            elif actor[0] == lista_actores[0] and lista_actores[4] == False:
                error -= 1
    if error*-1 == len(names_actores):
        return error
    else:
        return exitosos

# Funciones de EJERCICIO D
def desvincular_actores(mat_peliculas, mat_actores, apellidos_actores):
    # Your Code HERE
    # no me dio tiemp
    pass


if __name__ == "__main__":

    resultados = [False, False, False, False, False, False, False, False, False, False, False, False]

    # EJERCICIO A ===================================================================

    peliculas = [ [ "Godfather I and II", 1974, 1, 2, 3],
                  [ "Star Wars A New Hope", 1977, 4, 5, 6],
                  [ "Star Trek Motion Picture", 1979, 7, 8], 
                  [ "The Irishman", 2019, 2, 3] ]

    actores = [ [ "Marlon", "Brando", 80, 12, False ],
                [ "Al", "Pacino", 82, 7, True ],
                [ "Robert", "DeNiro", 79, 9, True ], 
                [ "Mark", "Hamill", 70, 5, True ],
                [ "Harrison", "Ford", 80, 10, True ],
                [ "Carrie", "Fisher", 60, 4, False ],
                [ "William", "Shatner", 91, 7, True ],
                [ "Leonard", "Nimoy", 84, 11, False ] ]

    respuesta_1a = asignar_actores_a_peliculas(peliculas, actores, ["Star Wars Empire Strikes Back", "Star Trek Wrath of Khan"], ["Billy Dee Williams", "Walter Koenig"], [85, 85])
    
    if(len(peliculas) == 4 and len(actores) == 8 and respuesta_1a == -1):
        print("Ejercicio A (Pelicula No Registrada): OK")
        resultados[0] = True
    else:
        print("Ejercicio A (Pelicula No Registrada): WRONG - Retorno "+str(respuesta_1a)+", Esperado -1")

    respuesta_1b = asignar_actores_a_peliculas(peliculas, actores, ["Godfather I and II", "Star Trek Motion Picture"], ["Marlon Brando", "Leonard Nimoy"], [80, 84])
    
    if(len(peliculas) == 4 and len(actores) == 8 and respuesta_1b == 0):
        print("Ejercicio A (Actores Repetidos): OK")
        resultados[1] = True
    else:
        print("Ejercicio A (Actores Repetidos): WRONG - Retorno "+str(respuesta_1b)+", Esperado 0")

    respuesta_1c = asignar_actores_a_peliculas(peliculas, actores, ["Godfather I and II", "Star Trek Motion Picture"], ["Diane Keaton", "George Takei"], [76, 85])

    if(len(actores) == 10 and len(peliculas[0]) == 6 and len(peliculas[2]) == 5 and respuesta_1c == 2):
        verificacion_asignados_1 = peliculas[0] == ["Godfather I and II", 1974, 1, 2, 3, 9] and peliculas[2] == ["Star Trek Motion Picture", 1979, 7, 8, 10]
        verificacion_asignados_2 = ["Diane", "Keaton", 76, 0, True] in actores and ["George", "Takei", 85, 0, True] in actores
        if(verificacion_asignados_1 and verificacion_asignados_2):
            #print("Actores asignados:", respuesta_1c)
            print("Ejercicio A (Principal): OK")
            resultados[2] = True
        else:
            print("Ejercicio A (Principal): WRONG (Bad Verification)")
    else:
        print("Ejercicio A (Principal): WRONG (Bad Function Return) - Retorno "+str(respuesta_1c)+", Esperado 2")

    print(" ==================================================================================== ")

    # EJERCICIO B ===================================================================

    peliculas = [ [ "Godfather I and II", 1974, 1, 2, 3],
                  [ "Star Wars A New Hope", 1977, 4, 5, 6],
                  [ "Star Trek Motion Picture", 1979, 7, 8], 
                  [ "The Irishman", 2019, 2, 3] ]

    actores = [ [ "Marlon", "Brando", 80, 12, False ],
                [ "Al", "Pacino", 82, 7, True ],
                [ "Robert", "DeNiro", 79, 9, True ], 
                [ "Mark", "Hamill", 70, 5, True ],
                [ "Harrison", "Ford", 80, 10, True ],
                [ "Carrie", "Fisher", 60, 4, False ],
                [ "William", "Shatner", 91, 7, True ],
                [ "Leonard", "Nimoy", 84, 11, False ] ]

    respuesta_2a = restringir_peliculas_en_years(peliculas, 1970, 2020)

    if(len(peliculas) == 4 and len(actores) == 8 and respuesta_2a == 0):
        print("Ejercicio B (Sin Eliminaciones): OK")
        resultados[3] = True
    else:
        print("Ejercicio B (Sin Eliminaciones): WRONG - Retorno "+str(respuesta_2a)+", Esperado 0")

    respuesta_2b = restringir_peliculas_en_years(peliculas, 1975, 1979)
    
    if(len(peliculas) == 2 and len(actores) == 8 and respuesta_2b == 2):
        verificacion_eliminados_1 = [ "Godfather I and II", 1974, 1, 2, 3 ] not in peliculas
        verificacion_eliminados_2 = [ "The Irishman", 2019, 2, 3 ] not in peliculas
        if(verificacion_eliminados_1 and verificacion_eliminados_2):
            #print("Peliculas eliminadas:", respuesta_2b)
            print("Ejercicio B (Principal): OK")
            resultados[4] = True
        else:
            print("Ejercicio B (Principal): WRONG (Bad Verification)")
    else:
        print("Ejercicio B (Principal): WRONG (Bad Function Return) - Retorno "+str(respuesta_2b)+", Esperado 2")

    respuesta_2c = restringir_peliculas_en_years(peliculas, 1990, 2000)
    if(len(peliculas) == 0 and len(actores) == 8 and respuesta_2c == -1):
        print("Ejercicio B (Todas Eliminadas): OK")
        resultados[5] = True
    else:
        print("Ejercicio B (Todas Eliminadas): WRONG (Bad Function Return) - Retorno "+str(respuesta_2c)+", Esperado -1")

    print(" ==================================================================================== ")

    # EJERCICIO C ===================================================================

    peliculas = [ [ "Godfather I and II", 1974, 1, 2, 3],
                  [ "Star Wars A New Hope", 1977, 4, 5, 6],
                  [ "Star Trek Motion Picture", 1979, 7, 8], 
                  [ "The Irishman", 2019, 2, 3] ]

    actores = [ [ "Marlon", "Brando", 80, 12, False ],
                [ "Al", "Pacino", 82, 7, True ],
                [ "Robert", "DeNiro", 79, 9, True ], 
                [ "Mark", "Hamill", 70, 5, True ],
                [ "Harrison", "Ford", 80, 10, True ],
                [ "Carrie", "Fisher", 60, 4, False ],
                [ "William", "Shatner", 91, 7, True ],
                [ "Leonard", "Nimoy", 84, 11, False ] ]

    respuesta_3a = registrar_premios_a_actores_vivos(actores, ['Diane Keaton', 'DeForrest Kelley'], [3, 8])

    if(respuesta_3a == 0):
        print("Ejercicio C (Actores NO Registrados): OK")
        resultados[6] = True
    else:
        print("Ejercicio C (Actores NO Registrados): WRONG - Retorno "+str(respuesta_3a)+", Esperado 0")

    respuesta_3b = registrar_premios_a_actores_vivos(actores, ['Marlon Brando', 'Leonard Nimoy'], [3, 8])
    if(respuesta_3b == -2):
        verificacion_premios = actores[0][3] == 12 and actores[7][3] == 11
        if(verificacion_premios):
            #print("Actores vivos premiados:", respuesta_3b)
            print("Ejercicio C (Actores NO Vivos): OK")
            resultados[7] = True
        else:
            print("Ejercicio C (Actores NO Vivos): WRONG (Bad Verification)")
    else:
        print("Ejercicio C (Actores NO Vivos): WRONG (Bad Function Return) - Retorno "+str(respuesta_3b)+", Esperado -2")

    respuesta_3c = registrar_premios_a_actores_vivos(actores, ['Al Pacino', 'Carrie Fisher', 'William Shatner'], [5, 3, 4])
    if(respuesta_3c == 2):
        verificacion_premios = actores[1][3] == 12 and actores[5][3] == 4 and actores[6][3] == 11
        if(verificacion_premios):
            #print("Actores vivos premiados:", respuesta_3c)
            print("Ejercicio C (Principal): OK")
            resultados[8] = True
        else:
            print("Ejercicio C (Principal): WRONG (Bad Verification)")
    else:
        print("Ejercicio C (Principal): WRONG (Bad Function Return) - Retorno "+str(respuesta_3c)+", Esperado 2")

    print(" ==================================================================================== ")

    # EJERCICIO D ===================================================================

    peliculas = [ [ "Godfather I and II", 1974, 1, 2, 3],
                  [ "Star Wars A New Hope", 1977, 4, 5, 6],
                  [ "Star Trek Motion Picture", 1979, 7, 8], 
                  [ "The Irishman", 2019, 2, 3] ]

    actores = [ [ "Marlon", "Brando", 80, 12, False ],
                [ "Al", "Pacino", 82, 7, True ],
                [ "Robert", "DeNiro", 79, 9, True ], 
                [ "Mark", "Hamill", 70, 5, True ],
                [ "Harrison", "Ford", 80, 10, True ],
                [ "Carrie", "Fisher", 60, 4, False ],
                [ "William", "Shatner", 91, 7, True ],
                [ "Leonard", "Nimoy", 84, 11, False ] ]

    respuesta_4a = desvincular_actores(peliculas, actores, ['Kelley', 'Stiller', 'Downey'])

    if(respuesta_4a == -1):
        print("Ejercicio D (Actores NO Registrados): OK")
        resultados[9] = True
    else:
        print("Ejercicio D (Actores NO Registrados): WRONG - Retorno "+str(respuesta_4a)+", Esperado -1")

    respuesta_4b = desvincular_actores(peliculas, actores, ['Shatner', 'Nimoy'])

    if(respuesta_4b == 8):
        verificacion_desvinculo_1 = [ "William", "Shatner", 91, 7, True ] not in actores
        verificacion_desvinculo_2 = [ "Leonard", "Nimoy", 84, 11, False ] not in actores
        verificacion_desvinculo_3 = len(peliculas) == 4 and len(actores) == 6
        verificacion_desvinculo_4 = peliculas[2] == [ "Star Trek Motion Picture", 1979 ] 
        if(verificacion_desvinculo_1 and verificacion_desvinculo_2 and verificacion_desvinculo_3 and verificacion_desvinculo_4):
            #print("Actor Mas Desvinculado:", respuesta_4b)
            print("Ejercicio D (Pelicula Sin Actores): OK")
            resultados[10] = True
        else:
            print("Ejercicio D (Pelicula Sin Actores): WRONG (Bad Verification)")
    else:
        print("Ejercicio D (Pelicula Sin Actores): WRONG (Bad Function Return) - Retorno "+str(respuesta_4b)+", Esperado 8")

    respuesta_4c = desvincular_actores(peliculas, actores, ['Pacino', 'Ford'])

    if(respuesta_4c == 2):
        verificacion_desvinculo_1 = [ "Al", "Pacino", 82, 7, True ] not in actores
        verificacion_desvinculo_2 = [ "Harrison", "Ford", 80, 10, True ] not in actores
        verificacion_desvinculo_3 = len(peliculas) == 4 and len(actores) == 4
        verificacion_desvinculo_4 = ([ "Godfather I and II", 1974, 1, 2] in peliculas) and ([ "Star Wars A New Hope", 1977, 3, 4] in peliculas)
        if(verificacion_desvinculo_1 and verificacion_desvinculo_2 and verificacion_desvinculo_3 and verificacion_desvinculo_4):
            #print("Actor Mas Desvinculado:", respuesta_4c)
            print("Ejercicio D (Principal): OK")
            resultados[11] = True
        else:
            print("Ejercicio D (Principal): WRONG (Bad Verification)")
    else:
        print("Ejercicio D (Principal): WRONG (Bad Function Return) - Retorno "+str(respuesta_4c)+", Esperado 2")
    
    print(" ==================================================================================== ")

    print("CANTIDAD CASOS DE USO CORRECTOS: "+str(resultados.count(True))+" en 12")

    # FIN PARCIAL ===================================================================