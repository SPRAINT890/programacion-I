def factorial(valor):
    if valor <= 0:
        return 1
    else:
        fact = 1
        while valor > 0:
            fact = fact * valor
            valor = valor - 1
        return fact


numero = input("ingrese un numero ")
print("el valor factorial de " + numero + " es " + str(factorial(int(numero))))
