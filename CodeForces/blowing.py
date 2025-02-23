
while True:
    n, m, c = [int(x) for x in input().split()]
    volt = []
    
    if n == 0 and m == 0 and c == 0:
        break

    for i in range(n+m):
        valor=input()
        volt.append(valor)

    print(volt)

