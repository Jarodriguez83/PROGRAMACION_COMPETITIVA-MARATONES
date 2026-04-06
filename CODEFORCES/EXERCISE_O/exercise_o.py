#LEER LA CADENA S  
s = input()
buscar = "heidi"  
contador = 0

for letra in s: 
    if len(buscar) == contador:
        break
    if letra == buscar[contador]:
        contador += 1
if contador == len(buscar):
    print("YES")
else:
    print("NO")