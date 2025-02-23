n, k = map(int, input().split())  
a = list(map(int, input().split()))  


a.sort()


i, d = a[n // 2], a[n // 2] + k  


while i < d:
    mid = (i + d + 1) // 2

    
    operaciones = 0
    for j in range(n // 2, n):  
        if a[j] < mid:
            operaciones += mid - a[j]

    
    if operaciones <= k:
        i = mid 
    else:
        d = mid - 1  


print(i)