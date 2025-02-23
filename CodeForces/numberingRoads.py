count_test = 0
while True:
    r, n= [int(x) for x in input().split()]

    if n == 0 and r == 0:
        break

    count_test +=1
    count = 0

    if r <= n:
        count = 0
    else:
        count = (r - 1) // n

    if count > 26:
        print(f'Case {count_test}: impossible')
    else:
        print(f'Case {count_test}: {count}')

