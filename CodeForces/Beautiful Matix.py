matriz=[[int(x) for x in input().split()],
        [int(x) for x in input().split()],
        [int(x) for x in input().split()],
        [int(x) for x in input().split()],
        [int(x) for x in input().split()]]

for i in range(5):
    for j in range (5):
        if matriz[i][j]==1:
            filaMovimientos = abs(i-2)
            columnaMovimientos = abs(j-2)
print(filaMovimientos + columnaMovimientos)