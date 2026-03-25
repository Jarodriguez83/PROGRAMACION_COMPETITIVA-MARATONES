#IMPORTAMOS LA LIBRERÍA MATH 
import math
#LEEMOS LOS VALORES DE M Y N EN UNA MISMA LINEA
m, n = map(int, input().split())
AreaTablero = m * n
AreaFicha = 2 
#NÚMERO DE FICHAS QUE SE PUEDEN PONER
num_fichas= math.floor(AreaTablero / AreaFicha)
print(num_fichas)