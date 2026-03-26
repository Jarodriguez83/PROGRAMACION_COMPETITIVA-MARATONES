# **F. PALABRAS DEMASIADO LARGAS**
## **LÍMITE DE TIEMPO:** 1 Segundo
## **LÍMITE DE MEMORIA:** 256 MB

A veces algunas palabras como "localización" o "internacionalización" son tan largas que escribirlas muchas veces en un solo texto resulta bastante aburrido. 

Consideremos una palabra demasiado larga, si su longitud es estrictamente más que 10 personajes. Todas las palabras demasiado largas deberían sustituirse por una abreviatura especial. 

Esta abreviatura se hace así: escribimos la primera y la última letra de una palabra y entre ellas escribimos el número de letras entre la primera y la última letra. Ese número está en sistema decimal y no contiene ningún cero inicial. 

Así "localización" se escribirá como "l10n" y "internacionalización" se escribirá como "i18n". 

Se sugiere automatizar el proceso de cambio de palabras con abreviaturas. En este caso, las palabras demasiado largas deberían sustituirse por la abreviatura y las palabras que no sean demasiado largas no deberían sufrir ningún cambio.

## **ENTRADA:**
La primera línea contiene un número entero n (1 <= n <= 100). Cada uno de los siguientes n. Las líneas contienen una palabra. Todas las palabras constan de letras latinas minúsculas y poseen longitudes desde 1 a 100 personajes.  

## **SALIDA:**
Imprimir n líneas. El i la línea debe contener el resultado de reemplazar la i-ésima palabra de los datos de entrada.  

## **EJEMPLO DE PRUEBA:**
### **ENTRADA:**
- 4
- palabra
- localización
- internacionalización
- neumonoultramicroscópicailicovolcanoconiosis
### **SALIDA:**
- palabra
- l10n
- i18n
- p43s
