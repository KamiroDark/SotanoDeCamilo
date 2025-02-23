s = input()
u = 0
l = 0

for element in s:
    if element.isupper():
        u+=1
    elif element.islower():
        l+=1

if u > l:
    s = s.upper()
    
elif l > u:
    s = s.lower()
    
else:
    s = s.lower()
    

print(s)