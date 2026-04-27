from collections import Counter
# EJERCICIO: 2167A
resultados = []
#LEER EL NÚMERO DE CASOS DE PRUEBA
t = int(input())
for _ in range(t):
    #LEER LOS NÚMEROS 4 NÚMEROS DE ENTRADA
    a, b, c, d = map(int, input().split())
    lista = [a, b, c, d]
    counter = 0
    
    if Counter(lista)[lista[0]] >= 4:
            resultados.append("YES")
    else:
            resultados.append("NO")
for resultado in resultados:
    print(resultado)