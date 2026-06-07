# GRAFO REPRESENTADO COMO LISTA DE ADYACENCIA
grafo = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}
# FUNCION BFS
def bfs(inicio):
    # COLA PARA RECORRIDO
    cola = []
    # LISTA DE VISITADOS
    visitados = []
    # AGREGAR NODO INICIAL
    cola.append(inicio)
    visitados.append(inicio)
    # RECORRIDO
    while len(cola) > 0:
        # SACAR ELEMENTO DE LA COLA
        actual = cola.pop(0)
        # MOSTRAR NODO VISITADO
        print("VISITANDO:", actual)
        # RECORRER VECINOS
        for vecino in grafo[actual]:
            # SI NO HA SIDO VISITADO
            if vecino not in visitados:
                cola.append(vecino)
                visitados.append(vecino)
    # RETORNAR ORDEN
    return visitados
# EJECUCION
resultado = bfs('A')
print("\nORDEN DE VISITA FINAL:")
for nodo in resultado:
    print(nodo)