# **W. SÍ O SÍ**
## **LÍMITE DE TIEMPO:** 1 Segundo
## **LÍMITE DE MEMORIA:** 256 MB  

La Navidad pasada, tu amigo Fernando te regaló una cuerda **s** compuesta únicamente por los personajes **Y** y **N**, que representan "YES" y "NO", respectivamente. 

Puede aplicar repetidamente la siguiente operación en **s**: 

- Elija dos caracteres adyacentes cuales quiera y reemplácelos con sus lógicos O. 

Formalmente, en cada operación, puedes elegir un índice í (1 <= í <= |s| - 1), eliminar los caracteres s-i y s-i+1 luego inserte:  

- Un solo **Y** si al menos uno de s-i o s-i+1 es **Y**.  
- Un solo **N** si ambos s-i y s-i+1 son **N**.  

Tenga en cuenta que después de cada operación, la duración de s disminuye en 1. 

Desafortunadamente, Fernando no quiere que combines "SÍ O SÍ", ya que ha experimentado un trauma relacionado con una determinada canción. 

Determinar si es posible reducir **s** a un solo carácter aplicando repetidamente la operación anterior, sin siempre combinando dos Y's. 

## **ENTRADA:**

Cada prueba contiene múltiples casos de prueba. La primera línea contiene el número de casos de prueba t (1 <= t <= 500). A continuación, se describe los casos de prueba.  

La única línea de cada caso de prueba contiene la cadena s (2 <= |s| <= 100). Está garantizado que s-i = Y o N. 

## **SALIDA:**

Para cada caso de prueba, imprima "YES" si la cadena se puede reducir a un solo carácter aplicando repetidamente la operación descrita, y "NO" de lo contrario. 

## **EJEMPLO DE CASO DE PRUEBA:**

### **ENTRADA:**
- 7
- YY
- NN
- NNY
- YYYNY
- NNNNN
- AAAA
- YNNNNN

### **SALIDA:**
- NO
- YES
- YES
- NO 
- YES
- NO
- YES