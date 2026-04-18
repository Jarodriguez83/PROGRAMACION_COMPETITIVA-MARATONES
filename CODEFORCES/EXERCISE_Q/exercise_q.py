#INGRESA LA CADENA S  
s = input()
#INGRESA LA CADENA T
t = input()
#IMPRIME LA CADENA S 
reves = reversed(s)
comparar = (''.join(reves)) # EL .JOIN ES PARA UNIR LOS ELEMENTOS DE LA CADENA REVERSED EN UNA SOLA CADENA.
if comparar == t: 
    print("YES")
else:
    print("NO")

