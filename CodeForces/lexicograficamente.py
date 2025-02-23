s = str(input())
k = int(input())

n=len(s)
grupos = [[] for _ in range(k)]

for i in range(n):
    grupos[i%k].append(s[i])

for grupo in grupos:
    grupo.sort()

resultado = list(s)
for i in range(n):
    resultado[i] = grupos[i%k].pop(0)

print(''.join(resultado))