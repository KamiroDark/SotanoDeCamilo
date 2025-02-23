def calculate_T(n):
    mod = 10007
    T = 0

    # Calcular la expresión para todos los valores posibles de i, j, k, l, m
    for i in range(1, n + 1):
        j=1
        k=1
        l=1
        m=1
        term = abs(i - j) * abs(j - k) * abs(k - l) * abs(l - m) * abs(m - i)
        j+=1
        k+=1
        l+=1
        m+=1
        T = (T + term) % mod

    return T

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(calculate_T(n))

if __name__ == "__main__":
    main()
