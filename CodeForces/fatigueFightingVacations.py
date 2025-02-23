d, c, r = [int(x) for x in input().split()]

agotadoras = []
for _ in range(c):
    agotadoras.append(int(input()))

vigorizantes=[]
for _ in range(r):
    vigorizantes.append(int(input()))

ind_agotadoras=0
ind_vigorizantes = 0
actividades = 0

while ind_agotadoras < c or ind_vigorizantes < r:
    if ind_agotadoras < c and d >= agotadoras[ind_agotadoras]:
        d-=agotadoras[ind_agotadoras]
        ind_agotadoras +=1
        actividades+=1
    elif ind_vigorizantes < r:
        d+=vigorizantes[ind_vigorizantes]
        ind_vigorizantes+=1
        actividades+=1
    else:
        break

print(actividades)
