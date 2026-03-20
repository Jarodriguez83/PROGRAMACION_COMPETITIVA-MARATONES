#EJERCICIO H 
#PROBLEMA DE PARSING + CONVERSIÓN
def main():
    import sys #LIBRERÍA PARA LEER ENTRADA MÁS RÁPIDO
    input = sys.stdin.readline #LEE LA ENRADA MÁS RÁPIDO
    T = int(input())
    results = []  # ARREGLO PARA GUARDAR LOS RESULTADOS DE CADA CASO
    for t in range(1, T + 1):
        ip_decimal = input().strip() #UTILIZAMOS STRIP PARA ELIMINAR ESPACIOS EN BLANCO
        ip_binary = input().strip() #UTILIZAMOS STRIP PARA ELIMINAR ESPACIOS EN BLANCO
        dec = list(map(int, ip_decimal.split('.'))) #UTILIZAMOS SPLIT PARA SEPARAR LOS OCTETOS Y MAP PARA CONVERTIRLOS A ENTEROS
        bin_parts = ip_binary.split('.') #UTILIZAMOS SPLIT PARA SEPARAR LOS OCTETOS EN BINARIO
        same = True
        for i in range(4):
            if int(bin_parts[i], 2) != dec[i]: #COMPARA SI EL OCTETO EN BINARIO CONVERTIDO A DECIMAL ES IGUAL AL OCTETO DECIMAL ORIGINAL    
                same = False
                break
        # GUARDAR EL RESULTADO
        results.append(f"Case {t}: {'YES' if same else 'NO'}")
    #IMPRIMIR
    for res in results:
        print(res)

if __name__ == "__main__":
    main()