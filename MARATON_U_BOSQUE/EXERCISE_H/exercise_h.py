#EJERCICIO H 
#PROBLEMA DE PARSING + CONVERSIÓN
import sys #LIBRERÍA PARA LEER ENTRADA MÁS RÁPIDO
input = sys.stdin.readline #LEE LA ENRADA MÁS RÁPIDO

T = int(input())

results = []  # aquí guardamos las respuestas

for t in range(1, T + 1):

    ip_decimal = input().strip()
    ip_binary = input().strip()

    dec = list(map(int, ip_decimal.split('.')))
    bin_parts = ip_binary.split('.')

    same = True

    for i in range(4):
        if int(bin_parts[i], 2) != dec[i]:
            same = False
            break

    # guardamos el resultado
    results.append(f"Case {t}: {'YES' if same else 'NO'}")


# imprimimos TODO al final
for res in results:
    print(res)