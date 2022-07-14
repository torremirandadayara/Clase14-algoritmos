def cargar_lista():
    list = []
    for x in range(5):
        valor = int(input("Ingrese valor: "))
        list.append(valor)
    return list


def retornar_mayor_menor(lis):
    mayor = lis[0]
    menor = lis[0]
    for x in range(1, len(lis)):
        if lis[x] > mayor:
            mayor = lis[x]
        else:
            if lis[x] < menor:
                menor = lis[x]
    return [mayor, menor]


# bloque principal

lista = cargar_lista()
rango = retornar_mayor_menor(lista)
print("---------------------------------")
print("El mayor elemento de la lista: ", rango[0])
print("El menor elemento de la lista: ", rango[1])
