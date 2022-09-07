"""
Sabiendo que tiene
12000 cilindros,
16 pistas,
8 sectores por pista y
sectores de 512 bytes.
Exprese su tamaño en bytes, kilobytes, megabytes y gigabytes.

El tamaño del disco se calcula de acuerdo con la siguiente fórmula:
capacidad = cilindros * pistas * sectores * bytes
Un kilobyte son 1024 bytes. Un megabyte son (kilobyte * 1024) bytes. Un
gigabyte es (megabyte * 1024) bytes.
"""


def capacidadDisco ():
    return 12000 * 16 * (16*8) * 512

#print (str(capacidadDisco()))


kilobyte = capacidadDisco() / 1024
megabyte = kilobyte / 1024
gigabyte = megabyte / 1024

print("capacidad en bytes " + str(capacidadDisco()) + "\ncapacidad en kilobytes " + str(kilobyte) + "\ncapacidad en megabytes " + str(megabyte) + "\ncapacidad en gigabytes " + str(gigabyte))