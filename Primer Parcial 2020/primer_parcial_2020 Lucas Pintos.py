def poner_alimento_heladera(heladera, alimento, cantidad):
    nuevo_alimento = [alimento, cantidad]
    heladera.append(nuevo_alimento)

def sacar_alimento_heladera(heladera, alimento, cantidad):
    for i in heladera:
        if i[0] == alimento and i[1] > cantidad:
            i[1] -= cantidad
            return True
    return False

def sacar_alimentos_para_receta(heladera, receta):
    for alimento in receta:
        resultado = sacar_alimento_heladera(heladera, alimento[0], alimento[1])
        if not resultado:
            return False
    return True

def alimentos_faltantes(heladera, receta):
    faltantes = []
    for alimento_receta in receta:
        for alimento_heladera in heladera:
            if alimento_receta[0] == alimento_heladera[0] and alimento_receta[1] > alimento_heladera[1] and alimento_receta not in faltantes:
                alimento_faltante = alimento_receta.copy()
                alimento_faltante[1] = alimento_receta[1] - alimento_heladera[1]
                faltantes.append(alimento_faltante)
                break
    return faltantes

def alimentos_a_comprar_para_receta(heladera, receta, tabla_conversion_unidad):
    faltantes = alimentos_faltantes(heladera, receta)
    print(faltantes)
    return []

if __name__ == "__main__":
    # Pruebas
    
    # Prueba 1, agregar alimentos
    heladera = []
    poner_alimento_heladera(heladera, "Leche", 1000)
    poner_alimento_heladera(heladera, "Manteca", 400)
    poner_alimento_heladera(heladera, "Huevos", 12)

    if len(heladera) == 3:
        if (heladera[0][0] == "Leche" and heladera[0][1] == 1000 and 
                heladera[1][0] == "Manteca" and heladera[1][1] == 400 and
                heladera[2][0] == "Huevos" and heladera[2][1] == 12):
                print("Prueba 1 ok")
        else:
            print("Prueba 1 incorrecta")
    else:
        print("Prueba 1 incorrecta")

    # Prueba 2, sacar alimentos
    temp_resu = sacar_alimento_heladera(heladera, "Leche", 400)
    temp_resu2 = sacar_alimento_heladera(heladera, "Leche", 200)
    temp_resu3 = sacar_alimento_heladera(heladera, "Tomate", 1000)

    if temp_resu and temp_resu2 and not temp_resu3:
        if len(heladera) == 3:
            if (heladera[0][0] == "Leche" and heladera[0][1] == 400 and 
                    heladera[1][0] == "Manteca" and heladera[1][1] == 400 and
                    heladera[2][0] == "Huevos" and heladera[2][1] == 12):
                    print("Prueba 2 ok")
            else:
                print("Prueba 2 incorrecta")
        else:
            print("Prueba 2 incorrecta")
    else:
        print("Prueba 2 incorrecta")
    
    # prueba 3, sacar alimentos para receta

    receta = [["Leche", 300], ["Huevos", 6], ["Manteca", 200]]
    receta2 = [["Leche", 300], ["Huevos", 2], ["Tomates", 300]]

    temp_resu = sacar_alimentos_para_receta(heladera, receta)
    temp_resu2 = sacar_alimentos_para_receta(heladera, receta2)

    if temp_resu and not temp_resu2:
        if len(heladera) == 3:
            if (heladera[0][0] == "Leche" and heladera[0][1] == 100 and 
                    heladera[1][0] == "Manteca" and heladera[1][1] == 200 and
                    heladera[2][0] == "Huevos" and heladera[2][1] == 6):
                    print("Prueba 3 ok")
            else:
                print("Prueba 3 incorrecta")
        else:
            print("Prueba 3 incorrecta")
    else: 
        print("Prueba 3 incorrecta")

    # prueba 4, sacar alimentos para comprar de una receta
    receta = [["Leche", 300], ["Huevos", 2], ["Tomates", 300]]
    tabla_conversion_unidad = [["Leche", 1000], ["Huevos", 1], ["Tomates", 200]]

    compras = alimentos_a_comprar_para_receta(heladera, receta, tabla_conversion_unidad)
    
    if (len(compras) == 2 and compras[0][0] == "Leche" and compras[0][1] == 1 and 
            compras[1][0] == "Tomates" and compras[1][1] == 2):
        print("Prueba 4 ok")
    else:
        print("Prueba 4 incorrecta")