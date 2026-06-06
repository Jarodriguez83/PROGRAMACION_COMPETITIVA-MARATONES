# IMPORTAR LIBRERIAS
import time
import sys
import matplotlib.pyplot as plt
# INGRESAR TAMAÑO DEL CATALOGO
cantidad = int(input("INGRESE EL TAMAÑO DEL CATALOGO: "))
# GENERAR CATALOGO AUTOMATICAMENTE
catalogo = []
for i in range(1, cantidad + 1):
    catalogo.append(i)
# INGRESAR PRODUCTO A BUSCAR
producto_buscado = int(input("INGRESE EL PRODUCTO A BUSCAR: "))
# INICIAR MEDICION DE TIEMPO
inicio_tiempo = time.perf_counter()
# VARIABLES DE BUSQUEDA
encontrado = False
posicion = -1
comparaciones = 0
# BUSQUEDA SECUENCIAL
for i in range(len(catalogo)):
    comparaciones += 1
    if catalogo[i] == producto_buscado:
        encontrado = True
        posicion = i
        break
# FINALIZAR MEDICION DE TIEMPO
fin_tiempo = time.perf_counter()
# CALCULAR TIEMPO EN MILISEGUNDOS
tiempo_ms = (fin_tiempo - inicio_tiempo) * 1000
# CALCULAR MEMORIA APROXIMADA
memoria = sys.getsizeof(catalogo)
# MOSTRAR RESULTADOS
print("\nRESULTADOS")
if encontrado:
    print("PRODUCTO ENCONTRADO")
    print("POSICIÓN:", posicion)
else:
    print("PRODUCTO NO ENCONTRADO")
print("- N° COMPARACIONES REALIZADAS:", comparaciones)
print("- TIEMPO DE EJECUCIÓN (MILISEGUNDOS):", tiempo_ms)
print("- MEMORIA APROXIMADA (BYTES):", memoria)
# GRAFICA
x = list(range(1, comparaciones + 1))
y = x
plt.plot(x, y)
plt.title("COMPORTAMIENTO - BÚSQUEDA SECUENCIAL")
plt.xlabel("COMPARACIONES")
plt.ylabel("ELEMENTOS REVISADOS")
plt.grid(True)
plt.show()