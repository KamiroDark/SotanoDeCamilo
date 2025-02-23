
    
n, p, h =[int(x) for x in input().split()]
p -= 1
h -= 1  
    
w = []
ans = []
    
for k in range(n - 1, -1, -1):
        w.append(h >= (1 << k))
        if w[-1]:
            h = (1 << (k + 1)) - 1 - h
    
for k in range(n - 1, -1, -1):
        if w[k]:
            if p < (1 << k):
                ans.append('L')
                p = (1 << k) - 1 - p
            else:
                ans.append('R')
                p = (1 << (k + 1)) - 1 - p
        else:
            if p < (1 << k):
                ans.append('R')
            else:
                ans.append('L')
                p -= (1 << k)

print("".join(ans))

