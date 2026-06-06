# IMPORTAR LIBRERIAS
import time
import sys
import matplotlib.pyplot as plt
# INGRESAR TAMAÑO DEL CATALOGO
cantidad = int(input("INGRESE EL TAMAÑO DEL CATÁLOGO: "))
# GENERAR CATALOGO ORDENADO
catalogo = []
for i in range(1, cantidad + 1):
    catalogo.append(i)
# INGRESAR PRODUCTO A BUSCAR
producto_buscado = int(input("INGRESE EL PRODUCTO A BUSCAR: "))
# INICIAR MEDICION DE TIEMPO
inicio_tiempo = time.perf_counter()
# VARIABLES DE BUSQUEDA
inicio = 0
fin = len(catalogo) - 1
encontrado = False
posicion = -1
comparaciones = 0
# DATOS PARA LA GRAFICA
x = []
y = []
# BUSQUEDA BINARIA
while inicio <= fin:
    comparaciones += 1
    medio = (inicio + fin) // 2
    x.append(comparaciones)
    y.append(medio)
    if catalogo[medio] == producto_buscado:
        encontrado = True
        posicion = medio
        break
    elif producto_buscado < catalogo[medio]:
        fin = medio - 1
    else:
        inicio = medio + 1
# FINALIZAR MEDICION DE TIEMPO
fin_tiempo = time.perf_counter()
# CALCULAR TIEMPO EN MILISEGUNDOS
tiempo_ms = (fin_tiempo - inicio_tiempo) * 1000
# CALCULAR MEMORIA APROXIMADA
memoria = sys.getsizeof(catalogo)
# MOSTRAR RESULTADOS
print("\nRESULTADOS")
if encontrado:
    print("PRODCUTO ENCONTRADO")
    print("POSICIÓN:", posicion)
else:
    print("PRODUCTO NO ENCONTRADO")
print("- N° COMPARACIONES REALIZADAS:", comparaciones)
print("- TIEMPO DE EJECUCIÓN (MILISEGUNDOS):", tiempo_ms)
print("- MEMORIA APROXIMADA (BYTES):", memoria)
# GRAFICA
plt.plot(x, y, marker="o")
plt.title("COMPORTAMIENTO - BÚSQUEDA BINARIA")
plt.xlabel("NÚMERO DE COMPARACIONES")
plt.ylabel("POSICIÓN EVALUADA")
plt.grid(True)
plt.show()