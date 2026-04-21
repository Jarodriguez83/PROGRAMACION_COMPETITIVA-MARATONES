#LISTA PARA RESULTADOS 
resultados = []
#LEER EL NÚMERO DE CASOS 
t = int(input())
#LEER LA CADENA S 
key = list('codeforces')
for _ in range(t): 
    s = input()
    counter = 0
    for i in range(10): 
        if s[i] != key[i]: 
            counter += 1 
    resultados.append(counter)
        
for resultado in resultados: 
    print (resultado)