#141A
from collections import Counter
#INGRESAMOS NOMBRE 1  
number_1 = input()
#INGRESAMOS NOMBRE 2
number_2 = input()
#INGRESAMOS LOS NOMBRES COMBINADOS (PILA)
combined = input()
group = Counter(number_1 + number_2)
if Counter(combined) == group:
    print("YES")
else:   
    print("NO")