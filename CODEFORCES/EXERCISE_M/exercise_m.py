from collections import Counter
resultados = [] #GUARDAR RESULTADOS 
#LEER EL NUMERO DE CASOS  
t = int(input())
for _ in range(t): 
    #LEER EL NUMERO DE SUBCADENAS  
    n = int(input())
    #CONTAR LAS LETRAS DE LAS CADENAS  
    total_leters = Counter()
    for _ in range(n):
        cadenas = input()
        total_leters += Counter(cadenas)
    posible = True  

    for letra in total_leters:  
        if total_leters[letra] % n != 0:
            posible = False
            break
    resultados.append("YES" if posible else "NO")

#IMPRIMIR LOS RESULTADOS
for resultado in resultados:
    print(resultado)
    
    
