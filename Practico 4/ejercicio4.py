"""
Escriba un archivo que tenga un método que calcule la distancia recorrida por
un móvil que se mueve a velocidad constante de 3.2 m/s en un tiempo de t
segundos. El valor de t se introducirá como argumento en la llamada del
método.
"""


def distRecorrida(tiempo):
    velocidad = 3.2
    return velocidad * int(tiempo)


tiempoUsuario = input("tiempo transcurrido ")
print("La distancia recorrida es de " + str(distRecorrida(tiempoUsuario)))
