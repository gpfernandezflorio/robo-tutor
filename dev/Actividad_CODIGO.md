Campos:
  * tipo: "CODIGO"
  * id: identificador de actividad (debe ser único en el curso).
  * nombre: nombre para mostrar.
  * enunciado: enunciado para mostrar.
  * pre: código para agregar antes en cada ejecución.
  * base: código precargado cuando se abre el ejercicio.
  * post: código para agregar después en cada ejecución.
  * timeout: cantidad de segundos de timeout.
  * run_data: test o lista de tests a ejecutar.
  * pidePrograma (sólo para Gobstones): si es parte del enunciado escribir el programa principal.
  * analisisCodigo: verificador o lista de verificadores de calidad de código.
  * disponible: regla o lista de reglas para que esté disponible.

Test:
  - de tablero (sólo para Gobstones).
    Campos:
      * pre: código para agregar antes de la ejecución.
      * t0: tablero inicial.
      * tf: tablero final esperado.
      * vals: lista que define un test más detallado con varios casos posibles. Cada elemento de la lista debe ser un objeto que incluya el campo "t" con un tablero y el campo "msg" con el mensaje que se debe devolver en el caso de que ese sea el tablero final obtenido.
  - genérico
    Campos:
      * pre: código para agregar antes de la ejecución.
      * def: identificador o lista de identificadores que tienen que haber sido definidos para que pase el test (el output es "DEF " seguido del identificador si no se definió).
      * aridad: objeto cuyos campos son nombres de funciones y sus valores son números. Los nombres de las funciones se corresponden a las funciones que tienen que haber sido definidas y los números a la cantidad de parámetros que deben esperar para que pase los tests (el output es "DEF " seguido del nombre de la función si no se definió o "ARGS " seguido del nombre de la función si la cantidad de parámetros no es la correcta).
      * assert: expresión que debe ser verdadera para que pase el test (devuelve "NO" si es falsa).
      * eval: objeto que define un test más detallado con varios casos posibles. Debe tener el campo "expr" con la expresión a evaluar y un campo más que puede ser:
        1) el campo "vals" con un objeto cuyas claves son los posibles valores resultantes y sus valores los mensajes que se deben devolver (salvo "OK" que está reservado para indicar que es una respuesta correcta) en el caso de que ese sea el resultado obtenido.
        2) el campo "checks" con una lista donde cada elemento es una verificación a ejecutar que debe tener el campo "fVal" (una función que toma el string correspondiente a la expresión a evaluar y devuelve el string correspondiente a la verificación a aplicarle) y el campo msg. Este campo puede ser un string correspondiente al mensaje que se debe devolver (salvo "OK") o una lista de strings que explica cómo construir el mensaje final: reemplazando los elementos que sean None en la lista por el valor de la expresión evaluada y luego concatenando todos los elementos en un único string.

Tablero:
  Campos:
    * head: ubicación de cabezal (puede ser una lista vacía en el tablero final).
    * width: ancho del tablero.
    * height: alto del tablero.
    * board: contenido del tablero.

Regla:
  Campos:
    * desde: fecha en que se habilita.

Verificador:
  Campos:
    * key: clave del verificador.
    * El resto de los campos depende de la clave (ver archivo reglas.py)