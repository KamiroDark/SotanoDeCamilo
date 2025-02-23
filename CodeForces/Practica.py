def totalDePaginas(libros):
    if len(libros)==1:
        return libros[0]
    
    return libros[0] + totalDePaginas(libros[1:])

print(totalDePaginas([50, 100, 150]))