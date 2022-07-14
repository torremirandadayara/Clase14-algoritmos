def elementos_enteros():
    lista = []
    for x in range(10):
        valor = int(input("Ingresa un valor: "))
        lista.append(valor)
    return lista


def generar_lista(lista):
    listanegativa = []
    listapositiva = []
    for x in range(len(lista)):
        if lista[x] < 0:
            listanegativa.append(lista[x])
        else:
            if lista[x] > 0:
                listapositiva.append(lista[x])
    return [listanegativa, listapositiva]


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])


# bloque principal

lista = elementos_enteros()
listanegativa, listapositiva = generar_lista(lista)
print("---------------------------------")
print("Lista con los valores negativos: ")
imprimir(listanegativa)
print("---------------------------------")
print("Lista con valores positivos: ")
imprimir(listapositiva)
