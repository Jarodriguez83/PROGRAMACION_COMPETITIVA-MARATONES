import time
import sys
# LISTA DE PAQUETES (PESO, VALOR)
pesos = [5,10,15,22,25,12,18,8,3,17,6,13,7,19,14]
valores = [30,40,45,77,90,60,80,20,15,70,25,55,28,85,65]
# CAPACIDAD MAXIMA
capacidad_max = 50
inicio = time.time()
n = len(pesos)
# CREAR TABLA DP
dp = []
for i in range(n+1):
    fila = []
    for c in range(capacidad_max+1):
        fila.append(0)
    dp.append(fila)
# LLENAR TABLA
for i in range(1, n+1):
    for c in range(1, capacidad_max+1):
        # SI NO CABE
        if pesos[i-1] > c:
            dp[i][c] = dp[i-1][c]
        else:
            # NO TOMAR
            no_tomar = dp[i-1][c]
            # TOMAR
            tomar = valores[i-1] + dp[i-1][c - pesos[i-1]]
            # MAXIMO
            if tomar > no_tomar:
                dp[i][c] = tomar
            else:
                dp[i][c] = no_tomar
# VALOR OPTIMO
valor_optimo = dp[n][capacidad_max]
paquetes = []
c = capacidad_max
for i in range(n, 0, -1):
    if dp[i][c] != dp[i-1][c]:
        paquetes.append(i)
        c -= pesos[i-1]
fin = time.time()
# TIEMPO EN MS
tiempo_ms = (fin - inicio) * 1000
# MEMORIA APROXIMADA
memoria = sys.getsizeof(dp)
print("VALOR OPTIMO:", valor_optimo)
print("\nPAQUETES SELECCIONADOS:")
peso_total = 0
for p in paquetes:
    print("PAQUETE", p, "| PESO:", pesos[p-1], "| VALOR:", valores[p-1])
    peso_total += pesos[p-1]
print("\nPESO TOTAL:", peso_total)
print("\nTIEMPO DE EJECUCION (MS):", tiempo_ms)
print("MEMORIA USADA (BYTES):", memoria)