#FUNCIÓN PARA EL EJERCICIO 
def main(): 
    #LEER EL NÚMERO DE CASOS DE PRUEBA
    t = int(input())
    resultados = [] #LISTA PARA GUARDAR LOS RESULTADOS
    for _ in range(t):
        #LEER EL NÚMERO DE PERSONAS 
        n = int(input())
        if n == 2:
            resultados.append("2")
        elif n == 3:
            resultados.append("3")
        elif n % 2 == 0:
            resultados.append("0")
        else:
            resultados.append("1")
    for result in resultados: 
        print(result)

if __name__ == "__main__":
    main()


#UTILIZAMOS ELIF PARA QUE SOLO SE CUMPLA UNA DE LAS CONDICIONES
