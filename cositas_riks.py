print("Transpuesta de una matriz")
"""
Transpuesta de matriz

Matriz normal
[[1, 2, 3, 2],
[4, 3, 4, 3],
[8, 2, 13, 4]]

Matriz Transpuesta
[[1, 4, 8],
[2, 3, 2],
[3, 4, 13], 
[2, 3, 4]]
"""
matrix = [[1, 2, 3, 2],
          [4, 3, 4, 3],
          [8, 2, 13, 4]]

matrix_t = []
for x in range(4):
    matrix_x = []
    for y in range(3):
        matrix_x.append(matrix[y][x])
    matrix_t.append(matrix_x)
print(matrix)
print(matrix_t)


"""
Reordenar una lista de menor a mayor
a = [4, 2, 8, 20]
a_reordenado = sorted(a)

Reordenar una lista de mayor a menor}
a = [4, 2, 8, 20]
a_reordenado_reverse = sorted(a, reverse = True)
"""
print("\nReordenar una lista de menor a mayor Y de mayor a menor")
a = [4, 2, 8, 20]
a_reordenado = sorted(a)
a_reordenado_reverse = sorted(a, reverse = True)

print(a_reordenado)
print(a_reordenado_reverse)


"""
reformatear una letra o palabra en minuscula

a="A"
a.lower()
"""
print("\nreformatear una letra o palabra en minuscula")
a = "AyuDa"
print(a)
print(a.lower())

"""
Separar un string
a = "ayuda mi ksa esta sucia"
a.split()

separar en base a un caracter
a = "ayuda#mi#ksa#esta#sucia"
a.split("#")

separar una sola vez
a.split("#", 1)
"""

print("\nSeparar un string en una lista ")
a = "ayuda mi ksa esta sucia"
x = a.split()
print(x)

print("\nseparar en base a un caracter")
a = "ayuda#mi#ksa#esta#sucia"
print(a.split("#"))

print("\nseparar una sola vez")
print(a.split("#", 1))

"""
contar un elemento en una lista
a = [1, 2, 5, 7, 5, 3, 87, 9, 2]
a.count(87)
"""
print("\ncontar un elemento en una lista")
a = [1, 2, 5, 7, 5, 3, 87, 9, 2,]
print(a)
print(a.count(87))