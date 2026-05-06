lista = [1, 2, 3, 4, 5]
inicio = 0
fin = len(lista) - 1
medio = (inicio + fin) // 2
target = 3
while inicio <= fin:
    if lista[medio] == target:
        print("ENCONTRADO EN LA POSICION", medio)
        break
    elif lista[medio] < target:
        inicio = medio + 1
    else:
        fin = medio - 1
    medio = (inicio + fin) // 2