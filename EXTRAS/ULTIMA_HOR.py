grafo = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

visitados = []

def dfs(nodo):

    visitados.append(nodo)

    print(nodo)

    for vecino in grafo[nodo]:

        if vecino not in visitados:

            dfs(vecino)

print("RECORRIDO DFS:\n")

dfs("A")