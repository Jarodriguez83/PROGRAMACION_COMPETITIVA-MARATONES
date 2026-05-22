import networkx as nx 
# Crear grafo dirigido 
G = nx.DiGraph() 
# Agregar aristas con capacidades 
edges = [ 
    ("s", "a", 10), 
    ("s", "b", 5), 
    ("a", "b", 15), 
    ("a", "t", 10), 
    ("b", "t", 10), 
] 
for u, v, c in edges: 
    G.add_edge(u, v, capacity=c) 
# Fuente y sumidero 
s, t = "s", "t" 
flow_value, flow_dict = nx.maximum_flow(G, s, t)  # Edmonds–Karp por defecto 

print("Flujo máximo:", flow_value) 
print("Detalle del flujo:") 
for u in flow_dict: 
    for v in flow_dict[u]: 
        if flow_dict[u][v] > 0: 
            print(f"{u} -> {v}: {flow_dict[u][v]}") 

 