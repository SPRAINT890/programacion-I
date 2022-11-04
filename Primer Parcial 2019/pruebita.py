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