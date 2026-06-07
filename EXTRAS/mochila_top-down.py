# LISTA DE PAQUETES (PESO, VALOR)
pesos = [5,10,15,22,25,12,18,8,3,17,6,13,7,19,14]
valores = [30,40,45,77,90,60,80,20,15,70,25,55,28,85,65]
# CAPACIDAD MAXIMA
capacidad_max = 50
# DICCIONARIO PARA MEMOIZACION
memo = {}
# FUNCION RECURSIVA TOP-DOWN
def mochila(i, capacidad):
    # CASO BASE
    if i == 0 or capacidad == 0:
        return 0
    # VERIFICAR SI YA ESTA CALCULADO
    if (i, capacidad) in memo:
        return memo[(i, capacidad)]
    # SI EL PESO DEL PAQUETE ACTUAL ES MAYOR
    if pesos[i-1] > capacidad:
        resultado = mochila(i-1, capacidad)
    else:
        # NO TOMAR EL PAQUETE
        no_tomar = mochila(i-1, capacidad)
        # TOMAR EL PAQUETE
        tomar = valores[i-1] + mochila(i-1, capacidad - pesos[i-1])
        # ELEGIR EL MAXIMO
        resultado = max(no_tomar, tomar)
    # GUARDAR EN MEMO
    memo[(i, capacidad)] = resultado
    return resultado
# LLAMADA PRINCIPAL
n = len(pesos)
resultado = mochila(n, capacidad_max)
print("VALOR MAXIMO:", resultado)