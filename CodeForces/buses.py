n, k, l = [int(x) for x in input().split()]

ultimosD = 10**6

combinaciones = [0]*(n+1)
combinaciones[0]=1

for i in range(1, n + 1):
    if i >= 5:
        combinaciones[i] += combinaciones[i-5] * k
    if i >= 10:
        combinaciones[i] += combinaciones[i-10] * l
    combinaciones[i] %= ultimosD

print(f"{combinaciones[n]:06d}")