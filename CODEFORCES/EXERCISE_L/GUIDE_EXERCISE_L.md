# **L. NOMBRE DEL ARCHIVO**
## **LÍMITE DE TIEMPO:** 1 Segundo 
## **LÍMITE DE MEMORIA:** 256 MB 

No puedes simplemente tomar el archivo y enviarlo. Cuando Polycarp intentó enviar un archivo en la red social "CodeHorses", se encontró con un problema inesperado. Si el nombre del archivo contiene tres o más "x" (letras latinas minúsculas "x") en la fila, el sistema considera que el contenido del archivo no corresponde al tema de la red social. En este caso, el archivo no se envía y se muestra un mensaje de error. 

Determine la cantidad mínima de caracteres a eliminar del nombre del archivo para que después el nombre no contenga "xxx" como subcadena. Imprimir 0 si el nombre del archivo no contiene inicialmente una subcadena prohibida "xxx". 

Puedes eliminar caracteres en posiciones arbitrarias (no necesariamente consecutivas). Si elimina un carácter, la longitud de una cadena se reduce en 1. Por ejemplo, si eliminas el carácter en la posición 2 de la cadena "exxxii", entonces la cadena resultante es "exxii". 

## **ENTRADA:**

La primera línea contiene un número entero n (3 <= n <= 100) la longitud del nombre del archivo. 

La segunda línea contiene una cadena de longitud n consta únicamente de letras latinas minúsculas (el nombre del archivo).  

## **SALIDA:**

Imprima la cantidad mínima de caracteres a eliminar del nombre del archivo para que después el nombre no contenga "xxx" como subcadena. Si inicialmente el nombre del archivo no contiene una subcadena prohibida "xxx", imprimir 0.  

## **EJEMPLO DE PRUEBA:**

### **ENTRADA:**
- 6
- xxxiii
### **SALIDA:**
- 1
### **ENTRADA:**
- 5
- xxxxx
### **SALIDA:**
- 3
### **ENTRADA:**
- 10
- xxxxxxxxxx
### **SALIDA:**
- 8
