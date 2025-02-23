def generador(s):
    ocurrencias = set(s)
    if len(ocurrencias)%2 == 0 :
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"
   
s=input()
print(generador(s))    