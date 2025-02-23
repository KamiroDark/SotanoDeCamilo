n = int(input())
games = str(input())

a=0
d=0
for i in games:
    if i=='A':
        a+=1
    if i=='D':
        d+=1

if a < d:
    print("Danik")
elif a>d:
    print("Anton")
elif a == d:
    print("Friendship")