def comparate_strings():    
    cadena1=input().strip()
    cadena2=input().strip()

    lowerC1 = cadena1.lower()
    lowerC2 = cadena2.lower()

    if lowerC1 < lowerC2:
        return -1
    elif lowerC1 > lowerC2:
        return 1
    elif lowerC1 == lowerC2:
        return 0

print(comparate_strings())    