# **PROBLEMA H. VERIFICACIÓN DE IP.** 

## **TIEMPO LIMITADO EN EJECUCIÓN:** 1 Segundo 

## **LÍMITE DE MEMORIA:** 256 MB

Una dirección IP es una dirección de 32 bits, con el formato:  
a.b.c.d 
donde a,b,c,d son enteros en el rango de 0 a 255. 

Ahora se te dan dos direcciones IP: 

    - La primera en forma decimal. 
    - La segunda en forma binaria. 

La tarea es determinar si representan la misma dirección o no.  

### **ENTRADA:**
La entrada comienza con un entero T(<= 100), que indica el número de casos de prueba. 
Cada caso de prueba contiene dos líneas: 

    1. La primera línea contiene una dirección IP en forma decimal.  
    2. La segunda línea contiene una dirección IP en forma binaria, donde cada una de las cuatro partes tiene exactamete 8 dígitos.  
Se puede asumir que todas las direcciones proporcionadas son válidas. 

### **SALIDA:**
Para cada caso, imprime: 

    * El número del caso. 
    * Y 'YES' si ambas direcciones IP son iguales.  
    * Si son diferentes imprime 'NO'

### **EJEMPLO DE UN CASO DE PRUEBA:**

**INPUT:**

- 2
- 192.168.0.100
- 11000000.10101000.00000000.11001000
- 65.254.63.122
- 01000001.11111110.00111111.01111010

**OUTPUT:**

- CASE 1: NO
- CASE 2: YES