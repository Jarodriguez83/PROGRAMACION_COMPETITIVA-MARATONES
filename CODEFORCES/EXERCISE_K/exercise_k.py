from collections import Counter
resultados = [] #LISTA PARA GUARDAR LOS RESULTADOS  
#NÚMERO DE CASOS QUE SE VAN A MANEJAR
t = int(input())
fecha_olim = Counter([0, 1, 0, 3, 2, 0, 2, 5])
for i in range(t): 
    #LEER EL NÚMERO DE ELEMENTOS A QUE VAN A INGRESAR  
    n = int(input())
    #LEER LOS ELEMENTOS Y GUARDARLOS EN UNA LISTA
    elementos = list(map(int, input().split()))
    
    acumulado = Counter()
    respuesta = 0 
    for i in range(n): 
        d = elementos[i]
        if acumulado[d] < fecha_olim[d]:
            acumulado[d] += 1
        if acumulado == fecha_olim: 
            respuesta= i + 1
            break 
    resultados.append(respuesta)


for resultado in resultados: 
    print(resultado)