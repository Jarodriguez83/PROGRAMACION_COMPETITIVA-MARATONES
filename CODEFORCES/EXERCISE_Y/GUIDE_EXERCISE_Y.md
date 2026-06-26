# **Y. PROGRAMA DE TELEVISIÓN TÁRTARO**
## **LÍMITE DE TIEMPO:** 2 Segundos
## **LÍMITE DE MEMORIA:** 256 MB

Durante las vacaciones, Egor vino a visitar a su amigo Dabir en la ciudad de Kazán. Por aburrimiento, a Dabir y Egor se les ocurrió una nueva idea de negocio: hacer su propio programa de televisión.  

El formato del programa es muy sencillo: en cada episodio ivitan a un invitado y juegan con él en una cadena binaria.  

En el episodio de hoy, Egor y Dabir invitaron a Arseniy (también conocido como MAKAN), la celebridad principal de Omsk. Para el juego eligieron una cadena binaria *s* de longitud *n* y un número entero *k*.  

Arseniy puede realizar un número ilimitado de movimientos. En un solo movimiento, puede elegir un número entero *i* (1 <= i <= n -k) e invertir los caracteres en posiciones *i* y *i + k*, es decir, cambía de 0 a 1 y de 1 a 0.  

Por ejemplo, si s=10110 y k=2, luego eligiendo i=2, Arseniy invierte los personajes en posiciones 2 y 4: [10110 -> 11100].

Arseniy quiere conseguir el premio principal 1 000 000 tugriks. Para hacer esto, necesita hacer toda la cuerda s igual a cero.  

Ayuda a Arseniy a determinar si puede conseguir su premio o si tendrá que regresar a Omsk sin nada.  

## **ENTRADA:**

La primera línea contiene un solo número entero *t* (1 <= t <= 10^4) el número de casos de prueba.  

La primera línea de cada caso de prueba contiene dos números enteros *n* y *k* (1 <= k <= n <= 2 * 10^5)

La segunda línea de cada caso de prueba contiene una cadena binaria *s* de longitud *n*

Se garantiza que la suma de *n* en todos los casos de prueba no se excede 2 * 10^5

## **SALIDA:**

Para cada caso de prueba, genere "YES" si Arseniy puede hacer que la cadena sea completamente cero y "NO" en caso contrario.  

## **EJEMPLO DEL CASO DE PRUEBA:**
### **ENTRADA:**
- 5
- 4 2
- 1010 
- 3 2 
- 111
- 3 3
- 111
- 3 1
- 110
- 1 1 
- 1

### **SALIDA:**
- YES
- NO
- NO 
- YES
- NO 