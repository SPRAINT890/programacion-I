from __future__ import barry_as_FLUFL


def poner_alimento_heladera(heladera, alimento, cantidad):
    existe_alimento_en_heladera = False
    for alimento_en_heladera in heladera:
        if alimento_en_heladera[0] == alimento:
            existe_alimento_en_heladera = True
            alimento_en_heladera[1] += cantidad
    if not existe_alimento_en_heladera:
        alimento_a_agregar = [alimento, cantidad]
        heladera.append(alimento_a_agregar)
    pass

def sacar_alimento_heladera(heladera, alimento, cantidad):
    for alimento_en_heladera in heladera:
        if alimento_en_heladera[0] == alimento and alimento_en_heladera[1] >= cantidad:
            alimento_en_heladera[1] -= cantidad
            return True
    return False

def sacar_alimentos_para_receta(heladera, receta):
    hay_stock = False
    for alimento_en_receta in receta:
        for alimento_en_heladera in heladera:
            if alimento_en_receta[0] == alimento_en_heladera[0] and alimento_en_heladera[1] >= alimento_en_receta[1]:
                hay_stock = True
                break
        if not hay_stock:
            return False
        else:
            hay_stock = False
    for alimento_en_receta in receta:
        sacar_alimento_heladera(heladera, alimento_en_receta[0], alimento_en_receta[1])
    return True

def alimentos_a_comprar_para_receta (heladera, receta, tabla_conversion_unidad):
    requerido = []
    for alimento_receta in receta:
        hay_stock = False
        for alimento_heladera in heladera:
            if alimento_receta[0] == alimento_heladera[0]:
                hay_stock = True
                if alimento_receta[1] > alimento_heladera[1]:
                    alimento_faltante = [alimento_receta[0], alimento_receta[1] - alimento_heladera[1]]
                    requerido.append(alimento_faltante)
                    break
        if not hay_stock:
            requerido.append(alimento_receta)
    requerido_formateado = []
    for alimento_tabla_conv_und in tabla_conversion_unidad:
        for alimento_requerido in requerido:
            if alimento_tabla_conv_und[0] == alimento_requerido[0]:
                if alimento_tabla_conv_und[1] > alimento_requerido[1]:
                    requerido_formateado.append([alimento_requerido[0],1])
                else:
                    if alimento_tabla_conv_und[1] % alimento_requerido[1] == 0:
                        requerido_formateado.append([alimento_requerido[0], alimento_requerido[1] // alimento_tabla_conv_und[1]])
                    else:
                        requerido_formateado.append([alimento_requerido[0], (alimento_requerido[1] // alimento_tabla_conv_und[1]) + 1 ])
    return requerido_formateado

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