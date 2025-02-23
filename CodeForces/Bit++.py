n = int(input())
contador = 0
for i in range(n):
    valor = input()
    if valor == "++X" or valor == "X++":
        contador += 1
    elif valor == "--X" or valor == "X--":
        contador -= 1

print(contador)