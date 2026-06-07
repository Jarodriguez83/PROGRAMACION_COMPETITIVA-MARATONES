import time
import sys
# LISTA DE PAQUETES (PESO, VALOR)
pesos = [5,10,15,22,25,12,18,8,3,17,6,13,7,19,14]
valores = [30,40,45,77,90,60,80,20,15,70,25,55,28,85,65]
# CAPACIDAD MAXIMA
capacidad_max = 50
# MEMOIZACION
memo = {}
# FUNCION RECURSIVA
def mochila(i, capacidad):
    # CASO BASE
    if i == 0 or capacidad == 0:
        return 0
    # SI YA ESTA EN MEMO
    if (i, capacidad) in memo:
        return memo[(i, capacidad)]
    # SI NO CABE
    if pesos[i-1] > capacidad:
        resultado = mochila(i-1, capacidad)
    else:
        # NO TOMAR
        no_tomar = mochila(i-1, capacidad)
        # TOMAR
        tomar = valores[i-1] + mochila(i-1, capacidad - pesos[i-1])
        # MAXIMO
        resultado = max(no_tomar, tomar)
    memo[(i, capacidad)] = resultado
    return resultado
# FUNCION PARA RECONSTRUIR SOLUCION
def obtener_paquetes(i, capacidad):
    seleccionados = []
    while i > 0 and capacidad > 0:
        # SI EL VALOR VIENE DE ARRIBA (NO SE TOMA)
        if mochila(i, capacidad) == mochila(i-1, capacidad):
            i -= 1
        else:
            # SE TOMA EL PAQUETE
            seleccionados.append(i)
            capacidad -= pesos[i-1]
            i -= 1
    return seleccionados
inicio = time.time()
n = len(pesos)
valor_optimo = mochila(n, capacidad_max)
paquetes = obtener_paquetes(n, capacidad_max)
fin = time.time()
# TIEMPO EN MILISEGUNDOS
tiempo_ms = (fin - inicio) * 1000
# MEMORIA APROXIMADA
memoria = sys.getsizeof(memo)
print("VALOR OPTIMO:", valor_optimo)
print("\nPAQUETES SELECCIONADOS:")
peso_total = 0
for p in paquetes:
    print("PAQUETE", p, "| PESO:", pesos[p-1], "| VALOR:", valores[p-1])
    peso_total += pesos[p-1]
print("\nPESO TOTAL:", peso_total)
print("\nTIEMPO DE EJECUCION (MS):", tiempo_ms)
print("MEMORIA USADA (BYTES):", memoria)