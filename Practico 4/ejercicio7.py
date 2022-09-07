def añoBisiesti(año):
    if (año % 4) == 0 and (año % 100) == 0 and (año % 400) == 0:
        return True
    else:
        return False


año = input("ingrese un año ")
if añoBisiesti(int(año)):
    print("el año " + año + " es biciesto")
else:
    print("el año " + año + " no es biciesto")
