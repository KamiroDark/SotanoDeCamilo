n, k = input().split()
n=int(n)
k=int(k)
puntuaciones = list(map(int, input().split()))
puntaje_min = puntuaciones[k-1]
avanzan = 0

for puntaje in puntuaciones:
    if puntaje >= puntaje_min and puntaje > 0:
        avanzan += 1

print(avanzan)
