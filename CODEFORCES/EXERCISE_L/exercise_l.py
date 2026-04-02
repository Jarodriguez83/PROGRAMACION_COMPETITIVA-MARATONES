#LEER LA LONGITUD N  
n = int(input())
#LEER EL NOMBRE DEL ARCHIVO
archivo = input()

eliminaciones = 0 
cant_x = 0

for c in archivo: 
    if c == 'x': 
        cant_x += 1
        if cant_x >= 3: 
            eliminaciones += 1
    else:
        cant_x = 0
print(eliminaciones)