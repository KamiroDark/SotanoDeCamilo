n, r = [int(x) for x in input().split()]

s=[int(x) for x in input().split()]

if n == r:
    print("*")
else:
    missing_volunteers = []
    for i in range(1, n+1):
        if i not in s:
            missing_volunteers.append(i)
    print(" ".join(map(str, missing_volunteers)))
