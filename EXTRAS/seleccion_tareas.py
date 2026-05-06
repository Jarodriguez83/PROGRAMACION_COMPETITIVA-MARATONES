actividades = [
    (1,4),
    (3,5),
    (0,6),
    (5,7),
    (8,9),
    (5,9)
]

# Ordenar por hora de finalización
actividades.sort(key=lambda x: x[1])

seleccionadas = []

# Escoger la primera actividad
seleccionadas.append(actividades[0])

ultima_fin = actividades[0][1]

# Revisar las demás
for actividad in actividades[1:]:

    inicio = actividad[0]
    fin = actividad[1]

    if inicio >= ultima_fin:

        seleccionadas.append(actividad)

        ultima_fin = fin

print("Actividades seleccionadas:")
print(seleccionadas)