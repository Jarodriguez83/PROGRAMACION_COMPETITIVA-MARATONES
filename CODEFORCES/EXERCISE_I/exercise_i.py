#I. MI PRIMER PROBLEMA DE CLASIFICACIÓN  
resultados = [] #LISTA PARA GUARDAR LOS RESULTADOS
#ENTRADA DEL NÚMERO DE CASOS
t = int(input())
for i in range(t):  
    #LEER X Y Y 
    x, y = map(int, input().split())
    resultados.append((min(x, y), max(x, y)))

for resultado in resultados: 
    print(resultado[0], resultado[1])