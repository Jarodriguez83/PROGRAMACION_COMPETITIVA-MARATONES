#EJERCICIO: 2178A
t = int(input())
for _ in range(t):
    s = input()
    
    # Verificamos que solo tenga Y y N
    es_valido = all(c == 'Y' or c == 'N' for c in s)  
    cantidad_y = s.count('Y') 
    if es_valido and cantidad_y <= 1:
        print("YES")
    else:
        print("NO")