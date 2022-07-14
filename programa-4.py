def cargar_sueldos():
    sueldos = []
    for x in range(10):
        sueldo = int(input("Ingrese el sueldo: "))
        sueldos.append(sueldo)
    return sueldos


def imprimir_sueldos(sueldos):
    print("Listado de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])


def sueldos_mayor_a_4000(sueldos):
    cant = 0
    for x in range(len(sueldos)):
        if sueldos[x] > 4000:
            cant = cant + 1
    print("--------------------------------------------------------")
    print("Cantidad de empleados con un sueldo mayor a 4000: ", cant)


def promedio(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    promedio = suma // 10
    return promedio


def sueldos_bajos(sueldos):
    pro = promedio(sueldos)
    print("Promedio de sueldos de los empleados: ", pro)
    print("Sueldos debajo del promedio: 2344")
    for x in range(len(sueldos)):
        if sueldos[x] < pro:
            print(sueldos[x])


# bloque principal

sueldos = cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor_a_4000(sueldos)
sueldos_bajos(sueldos)
