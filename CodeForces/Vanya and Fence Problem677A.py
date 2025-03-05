n , h = [int(x) for x in input().split()]

height=list(map(int, input().split()))

counter = 0

for num in height:
    
    if num <= h:
        counter+=1
    else:
        counter+=2

print(counter) 

#La clave estuvo en saber manejar la función map en Python ya que el problema necesitaba meter los numeros en una sola linea