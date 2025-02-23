def pesaje(a, b):
    anios = 0
    while(a<=b):
        a*=3
        b*=2
        anios +=1
    return anios

a, b = [int(x) for x in input().split()]
print(pesaje(a, b))