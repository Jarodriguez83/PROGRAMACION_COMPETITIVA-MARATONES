# **C. JUEGO DE LA PIZARRA**
## **LÍMITE DE TIEMPO:** 1 Segundo 
## **LÍMITE DE MEMORIA:** 256 MB 

Inicialmente, los números enteros de 0 a N-1, están escritos en una pizarra. 

En una ronda,  
- Alice elige un número entero a en la pizarra y lo borra. 
- Entonces Bob elige un número b en la pizarra de tal manera que: a + b = 3 (mod 4) y lo borra. 

Las rondas se llevan a cabo en sucesión hasta que un jugador no pueda realizar un movimiento. El primer jugador que no puede realizar un movimiento pierde. Determina quién gana con un juego óptimo.  

- Definimos eso x = y (mod m) cuando sea x - y un múltiplo entero de m.  

## **ENTRADA:**

La primera línea contiene un número entero t (1 <= t <= 100). El número de casos de prueba.  

La única línea de cada caso de prueba contiene un número entero N (1 <= n <= 100). El número de números enteros escritos en la pizarra.  

## **SALIDA:**

Para cada caso de prueba, salida en una sola línea "Alice" si Alice gana con un juego óptimo y "Bob" si Bob gana con un juego óptimo.  

## **EJEMPLO DE PRUEBA:**
### **ENTRADA:**
- 5
- 2
- 4
- 5
- 7
- 100

### **SALIDA:**
- Alice
- Bob
- Alice
- Alice
- Bob