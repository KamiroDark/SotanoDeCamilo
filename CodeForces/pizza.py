def solve(n):
    if n<10:
        return str(n)
    for div in range(2, 10):
        if n % div == 0:
            coc = n // div
            return str(div) + solve(coc)

t=int(input())
for _ in range(t):
    n = int(input())
    q = solve(n)
    print(q)