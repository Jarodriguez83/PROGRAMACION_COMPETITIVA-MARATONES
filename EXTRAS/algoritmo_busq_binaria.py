# PARTE 1 - INGRESO DEL TAMAÑO DE LA LISTA
# PEDIR LA CANTIDAD DE ELEMENTOS
n = int(input("INGRESE LA CANTIDAD DE ELEMENTOS DE LA LISTA: "))

# CREAR LISTA VACIA
lista = []

# PARTE 2 - INGRESO DE LOS VALORES

# PEDIR CADA VALOR DE LA LISTA
for i in range(n):
    valor = int(input("INGRESE EL VALOR PARA LA POSICION " + str(i) + ": "))
    lista.append(valor)

# PARTE 3 - ORDENAR LA LISTA
# ORDENAMIENTO BURBUJA
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux
            
# MOSTRAR LISTA ORDENADA
print("\nLISTA ORDENADA:")
print(lista)

# PARTE 4 - INGRESO DEL TARGET
# PEDIR EL NUMERO A BUSCAR
target = int(input("\nINGRESE EL NUMERO QUE DESEA BUSCAR: "))

# PARTE 5 - FUNCION DE BUSQUEDA BINARIA

def doSearch(array, target):
    # DEFINIR LIMITES
    minimo = 0
    maximo = len(array) - 1
    # REPETIR MIENTRAS EL RANGO SEA VALIDO
    while minimo <= maximo:
        # CALCULAR POSICION CENTRAL
        guess = (minimo + maximo) // 2
        print("\nMIN:", minimo)
        print("MAX:", maximo)
        print("GUESS:", guess)
        print("VALOR CENTRAL:", array[guess])

        # SI ENCUENTRA EL ELEMENTO
        if array[guess] == target:

            return guess

        # SI EL VALOR CENTRAL ES MENOR
        elif array[guess] < target:

            minimo = guess + 1

        # SI EL VALOR CENTRAL ES MAYOR
        else:

            maximo = guess - 1

    # SI EL ELEMENTO NO EXISTE
    return -1

# PARTE 6 - RESULTADOS FINALES

# EJECUTAR BUSQUEDA
resultado = doSearch(lista, target)

# MOSTRAR RESULTADO FINAL
print("\nRESULTADO FINAL")

# SI SE ENCUENTRA
if resultado != -1:
    print(
        "EL NUMERO",
        target,
        "SI SE ENCUENTRA EN LA POSICION",
        resultado
    )

# SI NO SE ENCUENTRA
else:
    print(-1)
    print(
        "EL NUMERO",
        target,
        "NO SE ENCUENTRA EN LA LISTA"
    )