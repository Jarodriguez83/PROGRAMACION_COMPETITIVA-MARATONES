resultados = [] #GUARGAR LA RESPUESTA DE CADA CASO 
#LEER EL NUMERO DE CASOS DE PRUEBA
q = int(input())
for i in range(q): 
    #LEER EL NÚMERO DE LONGITUG DE S Y T 
    n = int(input())
    #LEER LAS CADENAS S Y T
    s, t = map(str, input().split())
    #PASAR S A MINUSCULA 
    s = s.lower()
    #PASAR T A MINUSCULA
    t = t.lower()
    #COMPARAR LAS CADENAS S Y T
    if n == len(s) and n == len(t):
        #COMPRAR LOS CARACTERES DE S Y T SIN IMPORTAR EL ORDEN
        if sorted(s) == sorted(t):
            resultados.append("YES")
        else:
            resultados.append("NO")
#IMPRIMIR LOS RESULTADOS DE CADA CASO DE PRUEBA
for resultado in resultados:
    print(resultado)
    