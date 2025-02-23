def organizadorSuma(s):  

    return '+'.join(sorted(s.split('+')))

s = input()

print(organizadorSuma(s))