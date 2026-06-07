# GRAFO REPRESENTADO COMO LISTA DE ADYACENCIA
grafo = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}
# FUNCION DFS RECURSIVA
def dfs(nodo, visitados):
    # MARCAR COMO VISITADO
    visitados.append(nodo)
    print("VISITANDO:", nodo)
    # RECORRER VECINOS
    for vecino in grafo[nodo]:
        # SI NO HA SIDO VISITADO
        if vecino not in visitados:
            dfs(vecino, visitados)
# EJECUCION
visitados = []
dfs('A', visitados)
print("\nORDEN DE VISITA FINAL:")
for nodo in visitados:
    print(nodo)