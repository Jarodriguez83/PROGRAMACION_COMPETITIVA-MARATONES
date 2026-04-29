# **X. PETYA Y CUERDAS**
## **LÍMITE DE TIEMPO:** 2 Segundos  
## **LÍMITE DE MEMORIA:** 256 MB 

A la pequeña Petya le encantan los regalos. Su madre le compró dos cuerdas del mismo tamaño para su cumpleaños. Las cadenas constan de letras latinas mayúsculas y minúsculas. Ahora Petya quiere comparar esas dos cuerdas lexicográficamente. No importa el caso de las letras, es decir, una letra mayúscula se considera equivalente a la letra minúscula correspondiente. Ayude a Petya a realizar la comparación. 

## **ENTRADA:**

Cada una de las dos primeras líneas contiene una cadena comprada. Las longitudes de las cuerdas varían desde 1 a 1000 inclusivo. Se garantiza que las cadenas tengan la misma longitud y además estén formadas por letras latinas mayúsculas y minúsculas.  

## **SALIDA:**

Si la primera cadena es menor que la segunda, imprima "-1". Si la segunda cadena es menor que la primera, imprima "1". Si las cadenas son iguales, imprima "0". Tenga en cuenta que el caso de las letras no se tiene en cuenta cuando se comparan las cadenas. 

## **EJEMPLO DEL CASO DE PRUEBA:**
### **ENTRADA:**
- aaaa
- aaaA

### **SALIDA:**
- 0

### **ENTRADA:**
- abs
- Abz

### **SALIDA:**
- -1

### **ENTRADA:**
- abcdefg
- AbCdEfF

### **SALIDA:**
- 1