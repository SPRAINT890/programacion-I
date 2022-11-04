def registrar_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta, dia, tipo, importe):
    # Eliminar este comentario y colocar el código de la operación
    pass

def calcular_gasto_promedio(gastos):
    # Eliminar este comentario y colocar el código de la operación
    return 0

def obtener_dias_con_gasto_promedio_acumulado_alto(gastos_alimentacion, gastos_transporte, gastos_vestimenta):
    # Eliminar este comentario y colocar el código de la operación
    return []

def obtener_dia_de_semana_con_mayor_gasto(gastos_alimentacion, gastos_transporte, gastos_vestimenta):
    # Eliminar este comentario y colocar el código de la operación
    return 0

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