"""
Se desea modelar la realidad de un equipo de basquetbol, para ello se
identifican dos objetos relevantes “Jugador” y “Equipo”. 

Del jugador interesa
información como su cédula, nombre completo, edad, años de experiencia y
posición en la que juega (base, escolta, alero, ala-pivot, pivot). 

Del equipo
interesa conocer su nombre, una lista de jugadores titulares y una lista de
jugadores suplentes. 

En la clase Equipo se debe tener al menos las siguientes
operaciones:
a. agregar_titular(jugador), agrega un jugador como titular dentro del
equipo.
b. agregar_suplente(jugador), agrega un jugador como suplente dentro del
equipo
c. cambiar_suplente_como_titular(cedula), que mueve un jugador del
equipo suplente al equipo titular. En caso de realizar el movimiento con
éxito devuelve true, falso en caso contrario.

Teniendo en cuenta que en un equipo no puede tener más de 30 jugadores, se
deberá controlar que el tamaño de la lista no exceda dicho número.
Cree constructor y metodos get y set que considere necesarios.
Por último, genere un método main que cree un equipo de 2 titulares y 1
suplente, realice el cambio del suplente al titular y muestre en salida estándar
el nombre de los titulares actuales (3 luego del cambio).

jugador (ci, nombre, edad, años exp, posicion(base, escolta, alero, ala-pivot, pivot))
equipo(nombre, lista jugadores titulares, lista jugadores suplentes)
"""