def fibonacci(n):
    l=[]
    a = 0
    b = 1
    for i in range(n):
        c = a+b
        a = b
        b = c
        l.append(a)
    return l
n = int(input())
print(fibonacci(n))
#for x in range(50):
    #print(fibonacci(x))

def fibo_r(n):
    if n < 2:
        return n
    return fibo_r(n-1)+fibo_r(n-2)

##def fibonacci(n):
    if n <= 2:
        return n - 1
    a, s = 0, 1
    for _ in range(2, n):
        a, s = s, a+s
    return s
##n = int(input())
##print(fibonacci(n)
##algoritmo de euclides python 
