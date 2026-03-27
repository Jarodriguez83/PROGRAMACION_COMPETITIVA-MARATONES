resultados = []
#ENTRADA DE LA PALABRA 
palabra = input()
palabra_en_lista = list(palabra)
#CONTAR LAS MAYÚSCULAS Y LAS MINUSCULAS QUE TIENE palabra_en_lista
mayusculas = 0
minusculas = 0
for letra in palabra_en_lista:
    if letra.isupper(): #SI ES MAYUSCULA 
        mayusculas += 1
    elif letra.islower(): #SI ES MINUSCULA
        minusculas += 1

if mayusculas > minusculas: 
    resultados.append(palabra.upper())
elif minusculas > mayusculas:
    resultados.append(palabra.lower())
elif mayusculas == minusculas:
    resultados.append(palabra.lower())
#IMPRIMIR EL RESULTADO
for resultado in resultados:
    print(resultado)
