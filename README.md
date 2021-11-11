# python-exponential-backoff-retry
## Resumen
Guion para realizar una pequeña formación en reintentos

## Guion
- [python-exponential-backoff-retry](#python-exponential-backoff-retry)
  - [Resumen](#resumen)
  - [Guion](#guion)
  - [Fallos transitorios](#fallos-transitorios)
  - [Retry pattern](#retry-pattern)
    - [Reintentos simples](#reintentos-simples)
    - [Exponential backoff](#exponential-backoff)


## Fallos transitorios
Los fallos transitorios ocurren mientas nos comunicamos con componentes o servicios externos cuando estos no estan disponibles o se ha superado la capacidad de estos.

Estos fallos hacen referencia a problemas de conectividad o de sobrecarga que no tienen que ver con los servicios. 
Ejemplo fallos  en la conexion a internet.

Lo normal es que si volvemos a llamar al servicio de nuevo funcionen de manera correcta.

## Retry pattern
El patron de reintentos tiene como objectivo lograr la estabilidad del sistema y trata de lograr el éxito de una llamada a otra, tratando que el sistema haga lo mejor que pueda para responder adecuadamente.

### Reintentos simples
Una de las formas mas sencillas de plantear esto es con reintentos simples:

1. Definimos un maximo de reintentos
2. Identificamos el fallo
3. Reintentamos la llamada y aumentamos el contador
4. Si la llamada es correcta, seguimos con la ejecucion
5. Si la llamada no es correcta, seguimos reintentando hasta alcanzar el limite de reintentos
6. Si alcanzamos el limite de reintentos lanzamos el fallo a nuestro sistema

Este algoritmo tiene problemas con aquellos servicios que implementan `throttling` un ejemplo de esto pueden ser algunas bases de datos.
Ej. DynamoDB cuando se alcanza el limite de escritura/lectura.

### Exponential backoff
La idea principal de exponential backoff es hacer una espera exponencial antes del reintento.
De esta forma antes del primer reintento esperariamos 1 segundo, antes del segundo reintento esperariamos 2 segundos, antes del tercero 4 segundos...

Incrementar las esperas de forma exponencial permite que los sistemas externos puedan restaurarse de manera mas rapida sin que los estemos sobrecargando mas.

1. Definimos un maximo de reintentos
2. Identificamos el fallo
3. Esperamos un tiempo definido, reintentamos la llamada y aumentamos el contador
4. Si la llamada es correcta, seguimos con la ejecucion
5. Si la llamada no es correcta, aumentamos el tiempo de espera y seguimos reintentando hasta alcanzar el limite de reintentos (por cada reintento aumentará la espera)
6. Si alcanzamos el limite de reintentos lanzamos el fallo a nuestro sistema