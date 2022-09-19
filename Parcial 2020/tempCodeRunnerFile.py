for alimento_en_receta in receta:
        for alimento_en_heladera in heladera:
            if alimento_en_receta[0] == alimento_en_heladera[0] and alimento_en_heladera[1] >= alimento_en_receta[1]:
                hay_stock = True
                break
        if not hay_stock:
            return False
        else:
            hay_stock = False
    if hay_stock:
        for alimento_en_receta in receta:
            sacar_alimento_heladera(heladera, alimento_en_receta[0], alimento_en_receta[1])