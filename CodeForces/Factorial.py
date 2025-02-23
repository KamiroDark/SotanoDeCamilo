def iterativo(n):
    if n < 0:
        return "No existe"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado
    
def recursivo(n):
    if n == 1:
        return 1
    return n * recursivo(n-1)

n = int(input())
print(iterativo(n))
