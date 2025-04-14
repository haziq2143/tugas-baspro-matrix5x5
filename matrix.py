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

result = [[0 for _ in range(5)] for _ in range(5)]

for a in range(5):
    for b in range(5):
        for k in range(5):
            result[a][b] += matrix[a][k] * matrix[k][b]

for row in result:
    print(row)

