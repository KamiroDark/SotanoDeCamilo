n = int(input())
codeforce = "codeforces"

for i in range(0, n):
    palabra = input()
    diferencias = 0

    for j in range(0,len(palabra)):
        if palabra[j] != codeforce[j]:
            diferencias+=1

    print(diferencias)        