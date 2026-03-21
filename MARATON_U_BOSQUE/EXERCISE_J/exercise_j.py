def main():
    #ENTRADA DEL NÚMERO DE CASOS  
    t = int(input())
    #LISTA PARA GUARDAR LOS RESULTADOS
    resultados = []
    i=0
    for _ in range(t):
        #ENTRADA DEL NÚMERO 
        n = int(input())
        #PASAMOS EL NÚMERO A BINARIO Y CONTAMOS LOS 1 QUE TIENE
        binario = bin(n)[2:] #PASAR A BINARIO Y QUITAR EL PREFIJO '0b'
        cantidad_unos = binario.count('1')
        #EVALUAR SI LA CANTIDAD DE 1 ES PAR O IMPAR
        i=i+1
        if cantidad_unos % 2 == 0: 
            resultados.append(f"CASE {i}: EVEN")
        else:
            resultados.append(f"CASE {i}: ODD")
    for result in resultados:
        print(result)

if __name__ == "__main__":
    main()