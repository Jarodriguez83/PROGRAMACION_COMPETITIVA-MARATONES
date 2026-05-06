def maximo(arreglo, inicio, fin):

    # Caso base
    if inicio == fin:
        return arreglo[inicio]

    # Punto medio
    medio = (inicio + fin) // 2

    # Buscar máximo izquierda
    max_izq = maximo(arreglo, inicio, medio)

    # Buscar máximo derecha
    max_der = maximo(arreglo, medio + 1, fin)

    # Combinar resultados
    if max_izq > max_der:
        return max_izq
    else:
        return max_der


numeros = [8, 3, 15, 2, 20, 7, 11]

resultado = maximo(numeros, 0, len(numeros)-1)

print("Máximo:", resultado)