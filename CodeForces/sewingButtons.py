def count_ways(m, k, button_counts):
    n

# Procesamiento de entrada y salida
while True:
    m, k = map(int, input().split())
    if m == 0 and k == 0:
        break
    
    button_counts = [int(input()) for _ in range(k)]
    result = count_ways(m, k, button_counts)
    print(result)