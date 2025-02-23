k, n, w = map(int, input().split())
precio = 0
dolaresFaltantes = 0
for i in range(1, w + 1):
    precio +=i * k

if precio > n:
    dolaresFaltantes = abs(n-precio)
    print(dolaresFaltantes)
else:
    print(0)