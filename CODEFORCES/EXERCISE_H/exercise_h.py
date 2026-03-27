resultados = []
codeforces = ['c', 'o', 'd', 'e', 'f', 'o', 'r', 'c', 'e', 's']
#ENTRADA DEL NÚMERO DE CASOS
n = int(input())
for i in range(n):
    #ENTRADA DEL CARACTER
    caracter = input()
    if caracter in codeforces:
        resultados.append("YES")
    elif caracter not in codeforces:
        resultados.append("NO")
#IMPRIMIR LOS RESULTADOS
for resultado in resultados:
    print(resultado)