players = input()
count_1=0
count_0=0

for i in players:
    if i == '1':
        count_1+=1
        count_0= 0
    elif i == '0':
        count_0+=1
        count_1=0


    if count_1 == 7 or count_0 == 7:
        print("YES")
        break

else:
        print("NO")

