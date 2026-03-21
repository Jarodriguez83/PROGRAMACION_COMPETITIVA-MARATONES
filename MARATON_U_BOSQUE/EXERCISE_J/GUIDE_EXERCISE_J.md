# **PROBLEMA J. PARIDAD**
## **TIEMPO LÍMITE DE EJECUCIÓN:** 1 Segundo
## **LÍMITE DE MEMORIA:** 256 MB

Dado un entero n, primero lo representamos en binario. 

Luego contamos la cantidad de (1) en esa representación.  
- Decimos que n tiene paridad impar si la cantidad de unos es impar.  
- De lo contrario, decimos que n tiene paridad par. 

Por ejemplo:  
- 21 = (10101)|2| tiene paridad impar porque contiene 3 unos.  
- 6 = (110)|2| tiene paridad par. 

Ahora, dado n, debemos decir si n tiene partidad par o impar.  

### **ENTRADA:**

La entrada comienza con un entero T(<=1000), que indica el número de casos de prueba. 

Cada caso contiene un entero:  
- n, con 1 <= n < 2^31

### **SALIDA:**

Para cada caso imprime:  
- El número del caso. 
- Y 'ODD' si n tiene paridad IMPAR.  
- Y 'EVEN' si n tiene paridad PAR. 

### **EJEMPLO DE UN CASO DE PRUEBA:**

**INPUT:**
- 2
- 21
- 6

**OUTPUT:**
- Case 1: ODD
- Case 22: EVEN