#DEFINIMOS LA FUNCION PRINCIPAL
def main(): 
    #LEER EL NÚMERO DE CASOS DE PRUEBA
    t = int(input())
    resultados = [] #LISTA PARA GUARDAR LOS RESULTADOS
    for _ in range(t):
        #LEER EL TOTAL DE NÚMEROS EN LA PIZARRA
        n = int(input())
        if n % 4 == 0: 
            resultados.append("Bob")
        else: 
            resultados.append("Alice")
    for result in resultados:
        print(result)
if __name__ == "__main__":
    main()