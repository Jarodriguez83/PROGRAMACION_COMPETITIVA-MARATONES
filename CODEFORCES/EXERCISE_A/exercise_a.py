#EJERCICIO A: TAMIZ DE ERATO67HENES  
def main(): 
    t = int(input())
    resultados = []

    for _ in range(t):
        n  = int(input())
        arreglo = list(map(int, input().split())) #LEER LOS NÚMEROS EN UNA SOLA LÍNEA Y CONVERTIRLOS A ENTEROS DENTRO DE UNA LISTA

        if 67 in arreglo: #VERIFICAR SI EL NÚMERO 67 ESTÁ EN LA LISTA
            resultados.append("YES")
        else: 
            resultados.append("NO")
    for result in resultados:
        print(result)
    
if __name__ == "__main__":
    main()