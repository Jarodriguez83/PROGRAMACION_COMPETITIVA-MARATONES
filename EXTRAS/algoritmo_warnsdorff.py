# PARTE 1 - MOVIMIENTOS DEL CABALLO Y VARIABLES GLOBALES
# MOVIMIENTOS POSIBLES DEL CABALLO EN AJEDREZ
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

# PARTE 2 - CREAR TABLERO
def crear_tablero(n):
    # CREA UNA MATRIZ nxn CON CEROS
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        tablero.append(fila)
    return tablero

# PARTE 3 - VALIDAR MOVIMIENTOS
def movimiento_valido(x, y, tablero, n):
    # VERIFICA QUE ESTE DENTRO DEL TABLERO
    if x >= 0 and x < n and y >= 0 and y < n:
        # VERIFICA QUE NO ESTE VISITADA
        if tablero[x][y] == 0:
            return True
    return False

# PARTE 4 - CONTAR MOVIMIENTOS FUTUROS
def contar_movimientos(x, y, tablero, n):
    contador = 0
    # REVISA LOS 8 MOVIMIENTOS POSIBLES
    for i in range(8):
        nuevo_x = x + mov_x[i]
        nuevo_y = y + mov_y[i]
        # CUENTA MOVIMIENTOS VALIDOS
        if movimiento_valido(nuevo_x, nuevo_y, tablero, n):
            contador += 1
    return contador

# PARTE 5 - ALGORITMO VORAZ DEL CABALLO
def recorrido_caballo(n, inicio_x, inicio_y):
    tablero = crear_tablero(n)
    # MARCA LA POSICION INICIAL
    tablero[inicio_x][inicio_y] = 1
    # POSICION ACTUAL DEL CABALLO
    x = inicio_x
    y = inicio_y
    # CONTADOR DE CASILLAS RECORRIDAS
    visitadas = 1
    print("\nRECORRIDO DEL CABALLO:\n")
    print("PASO 1 -> POSICION:", (x, y))
    paso = 2
    # EL MAXIMO DE MOVIMIENTOS ES n*n
    while visitadas < n * n:
        mejor_x = -1
        mejor_y = -1
        menor_grado = 999
        # REVISA LOS 8 MOVIMIENTOS
        for i in range(8):
            nuevo_x = x + mov_x[i]
            nuevo_y = y + mov_y[i]
            if movimiento_valido(nuevo_x, nuevo_y, tablero, n):
                # CUENTA MOVIMIENTOS FUTUROS
                grado = contar_movimientos(
                    nuevo_x,
                    nuevo_y,
                    tablero,
                    n
                )
                # ESCOGE EL MENOR
                if grado < menor_grado:
                    menor_grado = grado
                    mejor_x = nuevo_x
                    mejor_y = nuevo_y
        # SI NO HAY MAS MOVIMIENTOS
        if mejor_x == -1:
            print("\nEL CABALLO NO PUEDE CONTINUAR.")
            break
        # MOVER EL CABALLO
        x = mejor_x
        y = mejor_y
        visitadas += 1
        tablero[x][y] = visitadas
        print("PASO", paso, "-> POSICION:", (x, y))
        paso += 1
    return tablero, visitadas

# PARTE 6 - ENTRADA DE DATOS Y RESULTADOS

# PEDIR TAMAÑO DEL TABLERO
n = int(input("INGRESE EL TAMAÑO DEL TABLERO nxn: "))
# PEDIR POSICION INICIAL
inicio_x = int(input("INGRESE LA FILA INICIAL DEL CABALLO: "))
inicio_y = int(input("INGRESE LA COLUMNA INICIAL DEL CABALLO: "))

# EJECUTAR ALGORITMO
tablero, visitadas = recorrido_caballo(
    n,
    inicio_x,
    inicio_y
)

# MOSTRAR TABLERO FINAL
print("\nTABLERO FINAL:\n")
for fila in tablero:
    print(fila)
# MOSTRAR RESUMEN
total = n * n

print("\nRESUMEN FINAL")
print("TOTAL DE CASILLAS:", total)
print("CASILLAS RECORRIDAS:", visitadas)

if visitadas == total:
    print("EL CABALLO RECORRIO TODO EL TABLERO.")
else:
    print("EL CABALLO NO LOGRO RECORRER TODO EL TABLERO.")