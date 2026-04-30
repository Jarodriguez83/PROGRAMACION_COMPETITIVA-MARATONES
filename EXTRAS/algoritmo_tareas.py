# PARTE 1 - DATOS DE LAS TAREAS
# LISTA DE GANANCIAS
ganancias = [10, 20, 8, 15, 30, 10, 5, 10, 2, 9]
# LISTA DE PLAZOS
plazos = [1, 4, 4, 1, 4, 2, 3, 4, 5, 4]

# NUMERO DE TAREAS
n = len(ganancias)

# PARTE 2 - CREAR LISTA DE TAREAS

# CADA TAREA TENDRA:
# [NUMERO_TAREA, GANANCIA, PLAZO]

tareas = []
for i in range(n):

    tarea = [i + 1, ganancias[i], plazos[i]]
    tareas.append(tarea)
# PARTE 3 - ORDENAR POR MAYOR GANANCIA
# ORDENAMIENTO BURBUJA
# ORDENA DE MAYOR A MENOR GANANCIA

for i in range(n):
    for j in range(0, n - i - 1):

        if tareas[j][1] < tareas[j + 1][1]:
            aux = tareas[j]
            tareas[j] = tareas[j + 1]
            tareas[j + 1] = aux

# PARTE 4 - CREAR ESPACIOS DE TIEMPO
# BUSCAR EL MAYOR PLAZO
max_plazo = 0

for plazo in plazos:
    if plazo > max_plazo:
        max_plazo = plazo

# CREAR ESPACIOS VACIOS
# -1 SIGNIFICA VACIO
espacios = []

for i in range(max_plazo):
    espacios.append(-1)

# PARTE 5 - ALGORITMO VORAZ
ganancia_total = 0

print("\nPLANIFICACION DE TAREAS:\n")

# RECORRER TAREAS ORDENADAS
for tarea in tareas:
    numero = tarea[0]
    ganancia = tarea[1]
    plazo = tarea[2]
    # BUSCAR ESPACIO LIBRE
    # DESDE EL FINAL HACIA ATRAS
    for tiempo in range(plazo - 1, -1, -1):
        # SI EL ESPACIO ESTA LIBRE
        if espacios[tiempo] == -1:
            espacios[tiempo] = numero
            ganancia_total += ganancia
            print(
                "TAREA T" + str(numero),
                "-> GANANCIA:",
                ganancia,
                "| PLAZO:",
                plazo,
                "| ASIGNADA AL TIEMPO:",
                tiempo + 1
            )
            break

# PARTE 6 - RESULTADOS FINALES
print("\nPLANIFICACION FINAL:\n")

for i in range(max_plazo):

    if espacios[i] != -1:
        print(
            "TIEMPO",
            i + 1,
            "-> TAREA T" + str(espacios[i])
        )
    else:
        print(
            "TIEMPO",
            i + 1,
            "-> VACIO"
        )

print("\nGANANCIA TOTAL MAXIMA:", ganancia_total)
print("\nTOTAL DE TAREAS:", n)
# CONTAR TAREAS EJECUTADAS
contador = 0

for espacio in espacios:
    if espacio != -1:
        contador += 1

print("TAREAS EJECUTADAS:", contador)
print("TAREAS NO EJECUTADAS:", n - contador)