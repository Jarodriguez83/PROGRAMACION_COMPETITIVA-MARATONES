resultados = []
#EJERCICIO 1760A  
#LEEMOS EL NUMERO DE CASOS DE PRUEBA
t = int(input())
for _ in range(t):
    #LEEMOS LOS NUMEROS DE LA PRUEBA
    a, b, c = map(int, input().split())
    lista = [a, b, c]
    #ORDEN
    lista.sort()
    resultados.append(lista[1])
for resultado in resultados:
    print(resultado)