m, n = [int(x) for x in input().split()]
contador = 0
if m % 2 == 0 and n % 2 == 0:
    contador = int((m * n)/2)
elif m % 2 != 0 and n % 2 != 0:
    contador = int(((m*n)-1)/2)
elif m % 2 != 0 or n % 2 != 0:
    contador = int((m*n)/2)

print(contador)