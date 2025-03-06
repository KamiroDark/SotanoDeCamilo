n = int(input())
tram = int(0)
maxPassengers = int(0)

for _ in range(n):
    a, b = [int(x) for x in input().split()]

    tram-=a
    tram+=b

    if tram >= maxPassengers:
        maxPassengers = tram

print(maxPassengers)

#Un dato es que se puede poner más limpio el codigo si en vez de la comparación solo colocamos: maxPassengers = max(maxPassengers, tram)
