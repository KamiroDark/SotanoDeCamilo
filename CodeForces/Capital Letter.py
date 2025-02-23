palabra = input()
primeraLetra = palabra[0]

if primeraLetra.isupper():
    print(palabra)
else:
    primeraLetra = primeraLetra.upper()
    palabra = primeraLetra + palabra[1:]
    print(palabra)

