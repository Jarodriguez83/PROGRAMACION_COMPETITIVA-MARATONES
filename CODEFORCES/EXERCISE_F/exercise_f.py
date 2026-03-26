#LEER EL NÚMERO DE CASOS 
t= int(input())
resultados = []
for i in range(t):
    #ENTRADA DE CADA PALABRA
    palabra = input()
    palabra_en_lista = list(palabra)
    if len(palabra_en_lista) > 10: 
        medio = len(palabra_en_lista) - 2
        resultados.append(palabra_en_lista[0] + str(medio) + palabra_en_lista[-1])
    else:
        resultados.append(palabra)
#IMPRIMIR LOS RESULTADOS
for resultado in resultados:
    print(resultado)
