from collections import Counter
#LEER LA CADENA S  
s = input()
#LEER EL NÚMERO K 
k = int(input())

if k > len(s): 
    print("impossible")
else:
    letras_distintas = len(Counter(s)) #CONTAR LETRAS DISTINTAS DE LA CADENA S
    if letras_distintas >= k: 
        print("0")
    else:
        print(k - letras_distintas) #CANTIDAD DE LETRAS QUE SE DEBEN AGREGAR PARA LLEGAR A K