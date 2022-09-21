from functools import total_ordering


def calcular_consumo_dia_franja(consumo_dia_esp, hora_inicio, hora_fin):
    total_consumo = 0
    for c in range(hora_inicio, hora_fin):
        total_consumo += consumo_dia[c]
    return total_consumo

def calcular_gasto_dia(consumo_dia_esp, tipo_tarifa):
    total_gasto_dia = 0
    if tipo_tarifa == 1:
        total_gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 00, 23) * 6.47
    elif tipo_tarifa == 2:
        total_gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 23, 16) * 3.453
        total_gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 17, 22) * 8.623
    else:
        total_gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 00, 6) * 1.803
        total_gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 7, 16) * 4.676
        total_gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 23, 00) * 4.676
        total_gasto_dia += calcular_consumo_dia_franja(consumo_dia_esp, 17, 22) * 8.623
        
    return total_gasto_dia

def calcular_gasto_mensual(consumo_mensual, tipo_tarifa):
    # Your Code HERE
    return 0

def franja_horario_mayor_consumo_mensual(consumo_mensual):
    # Your Code HERE
    return []

if __name__ == "__main__":
    # Set de pruebas básicos
    # Prueba 1 calcular_consumo_franja
    
    consumo_dia = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 15, 10, 10, 1, 1]
    resultado = calcular_consumo_dia_franja(consumo_dia, 19, 22)
    if resultado == 35:
        print("Prueba 1 OK")
    else:
        print(f"Prueba 1 error esperado 35 se obtuvo {resultado}.")

    # Prueba  2 calcular_gasto_dia
    # tarifa 1
    resultado = calcular_gasto_dia(consumo_dia, 1)
    if resultado == 420.55:
        print("Prueba 2 tarifa 1 OK")
    else:
        print(f"Prueba 2 tarifa 1 error esperado 420.55 se obtuvo {resultado}.")

    # tarifa 2
    resultado = round(calcular_gasto_dia(consumo_dia, 2), 3)
    if resultado == 467.435:
        print("Prueba 2 tarifa 2 OK")
    else:
        print(f"Prueba 2 tarifa 2 error esperado 467.435 se obtuvo {resultado}.")

    # tarifa 3
    resultado = round(calcular_gasto_dia(consumo_dia, 3), 3)
    if resultado == 469.338:
        print("Prueba 2 tarifa 3 OK")
    else:
        print(f"Prueba 2 tarifa 3 error esperado 469.338 se obtuvo {resultado}.")

    # Prueba 3 calcular_gasto_mes
    consumo_mes = [[t for t in consumo_dia] for j in range(31)]  
    resultado = round(calcular_gasto_mensual(consumo_mes, 3), 3)
    if resultado == 14549.478:
        print("Prueba 3 OK")
    else:
        print(f"Prueba 2 error esperado 14549,478 se obtuvo {resultado}.")

    # Prueba 4
    franja = franja_horario_mayor_consumo_mensual(consumo_mes)
    if len(franja) == 2 and franja[0] == 18 and franja[1] == 21:
        print("Prueba 4 OK")
    else:
        print(f"Prueba 4 error esperado [18, 21] se obtuvo {franja}.")
