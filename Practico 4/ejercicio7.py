def añoBisiesto(año):
    if (año % 4) == 0 and (año % 100) != 0 or (año % 4) == 0 and (año % 100) == 0 and (año % 400) == 0:
        return True
    else:
        return False


año = input("ingrese un año ")
if añoBisiesto(int(año)):
    print("el año " + año + " es biciesto")
else:
    print("el año " + año + " no es biciesto")


"""
1- Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
2- Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
3- Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
4- El año es un año bisiesto (tiene 366 días).
5- El año no es un año bisiesto (tiene 365 días).
"""