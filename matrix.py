matrix = [
    [6,7,8,9,10],
    [1,2,3,4,5],
    [11,12,13,14,15],
    [21,32,43,54,65],
    [12,65,76,86,43]
]
matrix2 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [21,32,43,54,65],
    [12,65,76,86,43]
]

result = []

for k in range(5):
    baris = []
    for j in range(5):
        total = 0
        for z in range(5):
            total += matrix[k][z] * matrix2[z][j]
        baris.append(total)
    result.append(baris)

for row in result:
    print(row)

