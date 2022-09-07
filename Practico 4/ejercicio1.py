# celsius 0 = 32 fahrenheit
def convaFahrenheit(celsius):
    return (int(celsius) * 9 / 5) + 32


temperatura = input("ingrese la temperatura en celsius: ")
print(convaFahrenheit(temperatura))
