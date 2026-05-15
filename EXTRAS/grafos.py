#GRAFOS: 
 # - RECORRIDO BFS (BREADTH FIRST SEARCH)
 # - RECORRIDO DFS (DEPTH FIRST SEARCH)

# EJERCICIO: Pasar por cada uno de los nodos, en donde se trabaja con grafos no dirigidos y definir un vector con los vecinos. 

# DEFINICIÓN DE LA MATRIZ
G = [[0, 0, 2, 1],
     [1, 0, 0, 1],
     [2, 0, 0, 0],
     [0, 1, 0, 0]]
# TRAER LAS POSICIONES DIFERENTES DE CERO 
for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j] != 0:
            print (f"VECINO EN POSICIÓN: {i} - {j}")

#RUTA QUE PASE POR TODOS LOS NODOS:
def dfs(grafo, nodo, visitados):
    visitados.add(nodo)
    print(f"Visitando nodo: {nodo}")
    
    for vecino in range(len(grafo[nodo])):
        if grafo[nodo][vecino] != 0 and vecino not in visitados:
            dfs(grafo, vecino, visitados)

#IMRPIMIR LA RUTA
visitados = set()
dfs(G, 0, visitados)

#CANTIDAD DE ENTRADAS ES IGUAL A LA CANTIDAD DE SALIDAS, EN ESTE CASO ES CICLICO 
