# **K. FECHA DE LA OLIMPIADA.**
## **LÍMITE DE TIEMPO:** 1 Segundo  
## **LÍMITE DE MEMORIA:** 256 MG 

La final de la primera Olimpiada del IT Campus "NEIMARK" está prevista para el 1 de marzo de 2025. A un pasante ánimo se le asignó la tarea de formar la fecha de la Olimpiada utilizando los dígitos **01.03.2025**.

Para lograrlo, el pasante tomó una gran bolsa de dígitos y comenzó a dibujarlos uno por uno. En total, dibujó **n** dígitos, el dígito ai fue dibujado en el í-tercer turno. 

Sospechas que el pasante hizo trabajo extra. Determine en qué paso el pasante podría haber ensamblado primero los dígitos para formar la fecha de la Olimpiada (los puntos separadores pueden ignorarse) o informe que es imposible formar esta fecha a partir de los dígitos dibujados. Tenga en cuenta que los ceros iniciales **debe mostrarse**. 

## **ENTRADA:**

Cada prueba contiene múltiples casos de prueba. La primera línea contiene el número de casos de prueba t(1 <= t <= 10000). A continuación, se describe los casos de prueba.  

La primera línea de cada caso de prueba contiene un único número entero n (1 <= n <= 20). 

La segunda línea de cada caso de prueba contiene n números enteros ai (0 <= ai <= 9) los números que el pasante extrajo en orden cronológico.  

## **SALIDA:**

Para cada caso de prueba, muestre la cantidad mínima de dígitos que el pasante podría extraer. Si no se pueden usar todos los dígitos para crear una fecha, muestre el número **0**.

## **EJEMPLO DE PRUEBA:**

### **ENTRADA:**
- 4
- 10 
- 2 0 1 2 3 2 5 0 0 1  
- 8 
- 2 0 1 2 3 2 5 0  
- 8 
- 2 0 1 0 3 2 5 0  
- 16  
- 2 3 1 2 3 0 1 9 2 1 0 3 5 4 0 3  

### **SALIDA:**
- 9 
- 0 
- 8
- 15  
