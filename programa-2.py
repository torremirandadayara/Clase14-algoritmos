def caracteres(lista):
    palabra = 0
    for x in range(1, len(lista)):
        if len(lista[x]) > len(lista[palabra]):
            palabra = x
    return lista(palabra)


# bloque principal

palabras = ["Hugo", "Alejandro", "Leo", "Lucas", "Martin", "Mateo"]
print(palabras)
print("Palabra con mas caracteres:", caracteres(palabras))
