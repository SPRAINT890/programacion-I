def registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, dia, tipo, importe):
    if tipo == 1:
        gastos_alimentacion[dia - 1] = gastos_alimentacion[dia - 1] + importe
        
    elif tipo == 2:
        gastos_transporte[dia - 1] =gastos_transporte[dia - 1] + importe
    
    elif tipo == 3:
        gastos_vestimenta[dia - 1] = gastos_vestimenta[dia - 1] + importe
    pass

def calcular_gasto_promedio(gastos):
    contador = 0
    suma = 0   
    for i in gastos:
        if i > 0:
            contador += 1
            suma = suma + i

    return suma/contador

def obtener_dias_con_gasto_promedio_acumulado_alto(gastos_alimentacion, gastos_transporte, gastos_vestimenta):
    gasto_prom_alimentacion = calcular_gasto_promedio(gastos_alimentacion)
    gasto_prom_transporte = calcular_gasto_promedio(gastos_transporte)
    gasto_prom_vestimenta = calcular_gasto_promedio(gastos_vestimenta)
    gastos_prom_aculado_alto = []
    for i in range (30):
        if gastos_alimentacion[i] > gasto_prom_alimentacion and gastos_transporte[i] > gasto_prom_transporte and gastos_vestimenta[i] > gasto_prom_vestimenta:
            gastos_prom_aculado_alto.append(i + 1)
    
    return gastos_prom_aculado_alto

def obtener_dia_de_semana_con_mayor_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta):
    mayor_gasto = 0
    dia = 0
    for i in range (30):
        gasto = 0
        gasto = gastos_alimentacion[i] + gastos_transporte[i] + gastos_vestimenta[i]
        if mayor_gasto < gasto:
            mayor_gasto = gasto
            dia_mayor = dia
        dia += 1
        if dia > 6:
            dia = 0
    return dia_mayor

if __name__ == "__main__":

    gastos_alimentacion = [0, 230, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 100]

    gastos_transporte = [0, 230, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 100]

    gastos_vestimenta = [0, 230, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 10, 0, 23, 0, 50, 0, 0, 0, 0, 0, 100]

    registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, 1, 1, 50)
    registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, 2, 1, 100)
    registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, 30, 3, 100)

    if gastos_alimentacion[0] == 50 and gastos_alimentacion[1] == 330 and gastos_vestimenta[29] == 200:
        print("Prueba 1 Ok")
    else: 
        print("Prueba 1 Error")

    gasto_promedio = 69.6

    if calcular_gasto_promedio(gastos_alimentacion) == gasto_promedio:
        print("Prueba 2 Ok")
    else:
        print("Prueba 2 Error")

    dias_gasto_promedio_alto = obtener_dias_con_gasto_promedio_acumulado_alto(gastos_alimentacion, gastos_transporte, gastos_vestimenta)

    if len(dias_gasto_promedio_alto) == 2 and dias_gasto_promedio_alto[0] == 2 and dias_gasto_promedio_alto[1] == 30:
        print("Prueba 3 Ok")
    else:
        print("Prueba 3 Error", dias_gasto_promedio_alto)

    dia_mayor_gasto = obtener_dia_de_semana_con_mayor_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta)

    if dia_mayor_gasto == 1:
        print("Prueba 4 Ok")
    else:
        print("Prueba 4 Error")