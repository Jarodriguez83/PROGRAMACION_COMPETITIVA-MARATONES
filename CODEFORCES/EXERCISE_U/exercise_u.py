#EJERCICIO 520A
#LEEMOS EL NÚMERO DE CARACTERES DE LA CADENA N 
n = int(input())
s = input().lower()  #CONVERTIR A MINÚSCULAS  

letras = set(s)  #CONJUNTO DE LETRAS ÚNICAS EN LA CADENA

if len(letras) >= 26:
    print("YES")
else:
    print("NO")