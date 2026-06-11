preguntasEstímulo = [
 "¿La consigna dada está alineada con los requerimientos del docente?",
 "¿Cómo evaluás la calidad de la consigna en términos de la presencia de errores, ambigüedades y formulaciones confusas?",
 "Si tuvieras que evaluar los mismos requerimientos, ¿cuánto tendrías que ajustar esta consigna para usarla en una evaluación?",
 'Acá podés justificar tus respuestas anteriores o agregar cualquier comentario extra que te parezca pertinente al respecto.<br><br>Si no tenés nada que agregar, escribí "-".'
]
títuloBienvenida = "Comenzando"
textoDeBienvenida = "En este experimento te vamos a mostrar distintas actividades diseñadas para evaluar conceptos de programación. <br>Junto a cada consigna te explicamos cuál es el objetivo que guió el diseño de la misma (esto es, qué concepto se desea evaluar, para qué público objetivo está pensada y más información).<br>Para cada una de ellas, te pedimos que respondas las siguientes preguntas:<br><ol><li>"+preguntasEstímulo[0]+"</li><li>"+preguntasEstímulo[1]+"</li><li>"+preguntasEstímulo[2]+"</li></ol><br>Además, vas a tener un campo de texto opcional para justificar tu calificación o agregar comentarios adicionales sobre el ejercicio propuesto. Tené en cuenta que una vez que respondas ya no vas a poder volver hacia atrás.<br><br>Hacé clic en 'Siguiente' para continuar."
def títuloPágina(j, n):
  return "Consigna " + str(j) + " de " + str(n)
def escala(u,c):
  return " Respondé en la escala del 1 al 5, donde 1 es '<em>"+u+"</em>' y 5 es '<em>"+c+"</em>':"
preguntasEstímulo[0] += escala("Nada alineada", "Totalmente Alineada")
preguntasEstímulo[1] += escala("Muy baja calidad", "Muy alta calidad")
preguntasEstímulo[2] += escala("No sirve, tendría que crear una nueva de cero", "La usaría tal cual está")
def textoEstímulo(estímulo):
  return [
    "<h1>Requerimiento</h1>",
    estímulo[0], # La presentación (Esta es una consigna ...)
    "<h1>Consigna</h1>",
    { 'md':estímulo[1], # La consigna en sí
      'css':{
        border: "solid 5pt #ddd",
        "background-color": "#f8f8f8",
        padding: "12px"
      }
    },
    "<h1>Valoración de la consigna propuesta</h1>"
  ]
def textoPregunta(i):
  return preguntasEstímulo[i-1]
títuloFinalización = "Eso es todo..."
textoDeFinalización = "¡Muchas gracias por participar!"
todosLosEstímulos = [
['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''## Contexto del problema

Una empresa de logística internacional está automatizando su sistema de control de despachos en aduana. Para que un contenedor sea clasificado con **"Prioridad de Embarque"**, debe cumplir estrictamente con ciertas regulaciones de peso y destino basadas en los tratados comerciales vigentes.

Las reglas del sistema dictan que un contenedor obtiene la prioridad si cumple con cualquiera de las siguientes dos condiciones:

1. El destino es Europa (`'UE'`) y su peso (`peso_toneladas`) es estrictamente mayor a 15 toneladas pero menor o igual a 25 toneladas.
2. El destino es Asia (`'AS'`) y su peso (`peso_toneladas`) es exactamente igual a 20 toneladas o exactamente igual a 30 toneladas.

---

## Consigna

Completá el siguiente fragmento de código en Python reemplazando los espacios vacíos (`_______`) con los operadores y operandos necesarios para construir la expresión que determine si el contenedor posee prioridad de embarque (`True`) o no (`False`).

```python
# Datos de prueba (pueden variar durante la evaluación)
destino = "UE"
peso_toneladas = 18.5

# Evaluación de la prioridad
posee_prioridad = (_______) _______ (_______)

# Resultado esperado para los datos de prueba: True
print(posee_prioridad)

```
'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''### Contexto: Sistema de Gestión de Envíos (E-Commerce)

Una empresa de logística internacional necesita automatizar la clasificación de sus paquetes en la categoría **"Envío Prioritario"**. Para que un paquete reciba esta categoría, debe cumplir con ciertas condiciones estrictas de peso, dimensiones y destino.

Las reglas del negocio establecen que un paquete es **Prioritario** si cumple con alguna de las siguientes situaciones:

1. El destino es internacional ("internacional") y el peso del paquete es menor o igual a 5 kg.
2. El destino es nacional ("nacional"), el peso es mayor a 20 kg y además no supera las dimensiones estándar de volumen (es decir, la variable `volumen_excedido` es falsa).

---

### Consigna

En el sistema actual, se disponen de las siguientes variables ya definidas con los datos de cada paquete:

* `destino` (un string que puede ser `"nacional"` o `"internacional"`)
* `peso` (un número flotante que representa los kilogramos)
* `volumen_excedido` (un valor booleano: `True` si el tamaño supera el estándar, `False` si está dentro de lo permitido)

Escriba una única línea de código en Python que determine si un paquete califica como prioritario. Para ello, debe definir una variable llamada `es_prioritario` y asignarle el resultado de evaluar de forma precisa las condiciones anteriores, utilizando las variables existentes.
'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Contexto del problema

Un club de corredores está organizando una maratón exclusiva. Para que una persona pueda inscribirse en la categoría "Elite", el sistema de registro debe validar automáticamente que cumpla con ciertas condiciones estrictas basadas en su historial.

Las reglas del club dictan que un corredor califica para la categoría "Elite" si cumple con **alguno** de los siguientes casos:

1. Ha completado al menos 5 maratones previas **y** su mejor tiempo es menor a 150 minutos.
2. Posee una certificación de atleta profesional vigente, **sin importar** su historial de maratones o tiempos.

---

## Consigna

A continuación, se presentan bloques de código desordenados en Python. Tu tarea es arrastrar y ordenar los bloques de manera secuencial para definir correctamente la función `verificar_categoria_elite`.

Esta función recibe cuatro variables: `maratones_previas` (entero), `mejor_tiempo` (entero), `certificacion_profesional` (booleano) y `certificacion_vigente` (booleano). La función debe evaluar la situación y retornar `True` si el atleta califica para la categoría "Elite", o `False` en caso contrario, utilizando una única expresión condicional eficiente.

**Bloques disponibles (¡Cuidado! Hay bloques distractores que no deben ser utilizados):**

```python
# Bloque A
    atleta_pro = certificacion_profesional and certificacion_vigente

```

```python
# Bloque B
    es_elite = historial_valido or atleta_pro
    return es_elite

```

```python
# Bloque C
def verificar_categoria_elite(maratones_previas, mejor_tiempo, certificacion_profesional, certificacion_vigente):

```

```python
# Bloque D
    historial_valido = maratones_previas >= 5 and mejor_tiempo < 150

```

```python
# Bloque E
    historial_valido = maratones_previas > 5 or mejor_tiempo < 150

```

```python
# Bloque F
    es_elite = historial_valido and atleta_pro
    return es_elite

```
'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''Una empresa de logística necesita determinar si un paquete califica para el "Envío Prioritario Express". Las condiciones para que un paquete sea prioritario son las siguientes:

1. El peso del paquete debe ser menor estricto a 5 kilogramos.
2. El destino debe ser local (representado con un valor booleano `True`).
3. El paquete **no** debe contener materiales frágiles (representado con un valor booleano `True` si es frágil, `False` si no lo es).

Para automatizar esto, un programador escribió el siguiente código en Python:

```python
peso = 4.5
es_local = True
es_fragil = False

resultado = (peso <= 5) and (es_local or not es_fragil)

```

¿Cuál es el valor que se almacena en la variable `resultado` tras ejecutar el código y por qué no evalúa correctamente las condiciones de la empresa?

* A) El valor es `True`. No evalúa correctamente porque la condición del peso permite paquetes de exactamente 5 kg, y la subexpresión de destino y fragilidad (`es_local or not es_fragil`) da `True` si el paquete es local, sin importar si es frágil o no.
* B) El valor es `False`. No evalúa correctamente porque el operador `and` requiere que ambas partes sean verdaderas, y al ser `es_fragil = False`, la negación `not es_fragil` anula el cumplimiento de la condición local.
* C) El valor es `True`. No evalúa correctamente porque utiliza el operador `or` en lugar de `and` para combinar la localidad y la fragilidad, lo que provocaría que un paquete no local pero no frágil sea aprobado si pesa menos de 5 kg.
* D) El valor es `False`. No evalúa correctamente porque la comparación `peso <= 5` es una asignación incorrecta en Python y produce un error de sintaxis que impide conocer el resultado booleano.
'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''## Contexto: Sistema de Gestión de una Biblioteca

Un colega programador ha estado desarrollando el módulo de penalizaciones para el sistema de gestión de una biblioteca universitaria. El objetivo de la función `debe_pagar_multa` es determinar si un usuario que devuelve un libro tarde debe afrontar un cargo económico.

Según el reglamento de la biblioteca, un usuario **debe pagar una multa** si se cumple alguna de las siguientes condiciones:

1. El libro tiene una categoría de "Alta Demanda" y el retraso es de más de 3 días.
2. El libro es de categoría "Regular", el retraso es de más de 7 días y el usuario ya tiene antecedentes de suspensiones previas.

El programador escribió el siguiente código en Python, pero nota que en varios casos del sistema de prueba el resultado es incorrecto (por ejemplo, le cobra a usuarios que no deberían pagar o exime de culpa a quienes sí corresponden).

```python
def debe_pagar_multa(categoria_libro, dias_retraso, tiene_antecedentes):
    # Determina si corresponde aplicar una multa económica
    es_alta_demanda = categoria_libro == "Alta Demanda"
    es_regular = categoria_libro == "Regular"
    
    if es_alta_demanda or dias_retraso > 3 and es_regular and dias_retraso > 7 or tiene_antecedentes:
        return True
    else:
        return False

```

## Consigna

Analizá el código proporcionado e identificá detalladamente los errores presentes en la condición del bloque `if` (línea 6).

Para responder, debés:

1. Explicar qué está evaluando erróneamente la línea 6 debido a la precedencia de los operadores lógicos actuales.
2. Señalar un ejemplo de valores de entrada para los parámetros (`categoria_libro`, `dias_retraso`, `tiene_antecedentes`) donde la función devuelva un resultado incorrecto (`True` cuando debería ser `False`, o viceversa), justificando el camino que toma el flujo del programa.
3. Escribir la línea de código corregida con la expresión lógica adecuada para que el sistema funcione según las reglas del negocio.
'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''## Consigna de Evaluación

En una plataforma de comercio electrónico se desea aplicar un descuento automático en el carrito de compras. Para que el beneficio se active, el sistema requiere verificar que se cumplan ciertas condiciones comerciales en base a tres variables del sistema: `monto_total` (un número decimal), `es_cliente_vip` (un valor booleano) y `cupon_valido` (un valor booleano).

Escribí los operadores lógicos y de relación faltantes en los espacios en blanco (`____`) para que la condición del bloque `if` sea **verdadera** únicamente cuando el cliente sea VIP o tenga un cupón válido, y que en cualquiera de esos dos casos el monto total de la compra supere los 5000 pesos.

```python
# El valor de estas variables puede cambiar durante la ejecución
monto_total = 5500.0
es_cliente_vip = False
cupon_valido = True

# Completar los espacios en blanco para activar el descuento de forma correcta
if (es_cliente_vip ____ cupon_valido) ____ monto_total ____ 5000:
    print("Descuento aplicado con éxito.")

```
'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''**Consigna:**

En una plataforma de comercio electrónico se está implementando un sistema de alertas para priorizar la atención a ciertos envíos. Se requiere establecer una condición para identificar si un paquete califica como "Envío Crítico".

Disponemos de las siguientes variables ya definidas en el sistema:

* `distancia_km` (un número entero que indica los kilómetros a recorrer).
* `es_prioritario` (un valor booleano que indica si el usuario pagó una tarifa de entrega rápida).
* `peso_kg` (un número flotante que representa el peso del paquete).
* `intento_fallido` (un valor booleano que indica si ya se intentó entregar el paquete previamente y no se tuvo éxito).

Un paquete se considera "Envío Crítico" si cumple con alguna de las siguientes situaciones:

1. El envío no tiene prioridad contratada, pero la distancia a recorrer es estrictamente mayor a 500 kilómetros y además pesa más de 25 kilogramos.
2. Ya se ha realizado un intento de entrega fallido, sin importar el resto de las condiciones.

Escribir una única expresión lógica en Python que determine si un envío debe ser etiquetado como crítico (evaluando a `True` en caso afirmativo y a `False` en caso contrario).
'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''### Consigna

Un sistema de riego automatizado para un invernadero debe activarse únicamente bajo ciertas condiciones climáticas específicas para cuidar las plantas. Se te solicita ordenar los siguientes fragmentos de código en Python para definir la expresión lógica correcta que determine si el riego debe encenderse.

La condición para activar el riego es que **no esté lloviendo** y que, además, ocurra al menos una de las siguientes situaciones: que la **temperatura sea mayor a 30 grados** o que la **humedad ambiente sea menor al 40%**.

Ordena los siguientes elementos (identificados del 1 al 9) para construir la línea de código que define la variable booleana `activar_riego`. Nota: Algunos elementos son distractores y no deben ser utilizados.

1. `not lluvia and (temperatura > 30 or humedad < 40)`
2. `activar_riego = `
3. `lluvia == False or temperatura > 30 and humedad < 40`
4. `not lluvia or (temperatura > 30 and humedad < 40)`
5. `not lluvia and temperatura > 30 or humedad < 40`
'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''**Consigna:**

Se está diseñando el sistema de control para un invernadero automatizado. Para activar los extractores de aire, el sistema evalúa la siguiente expresión en Python, la cual toma en cuenta la temperatura actual (en grados Celsius) y si el sensor de humedad detecta niveles críticos (representado por una variable booleana):

`(temperatura > 30) or (not humedad_baja and temperatura > 25)`

Si las variables toman los valores `temperatura = 28` y `humedad_baja = False`, ¿cuál es el resultado de evaluar la expresión y qué valores lógicos adoptan sus componentes intermedios?

Opciones:

1. El resultado es `True`, porque el primer término `(temperatura > 30)` es `False` y el segundo término `(not humedad_baja and temperatura > 25)` se evalúa como `True`.
2. El resultado es `False`, porque al ser `temperatura = 28`, la primera condición `(temperatura > 30)` no se cumple y eso invalida toda la expresión controlada por el operador `or`.
3. El resultado es `True`, porque la subexpresión `not humedad_baja` resulta en `False`, lo que obliga al operador `and` a dar un resultado positivo.
4. El resultado es `False`, porque la condición `temperatura > 25` es `True`, pero al aplicarse el operador `and` con una humedad que no es baja, el valor final se cancela.
'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''```markdown
La plataforma de streaming de música "SoundWave" está experimentando fallas en su sistema de reproducción automática para usuarios con cuentas gratuitas. Según las políticas de la empresa, un usuario tiene permitido escuchar la siguiente canción de forma automática solo si no ha superado el límite diario de canciones (que es de 15 canciones) y, además, se cumple alguna de las siguientes dos condiciones: que tenga activa la opción de reproducción aleatoria o bien que la canción pertenezca a una lista de reproducción patrocinada. 

Los desarrolladores detectaron que el sistema está salteando canciones incorrectamente o deteniendo la reproducción de forma imprevista. Tu tarea es revisar el código de la función `puede_reproducir_siguiente`, identificar la línea exacta donde se encuentra el fallo en la evaluación de los permisos y señalar cuál es el error cometido.

```python
def puede_reproducir_siguiente(canciones_escuchadas, aleatorio_activo, es_patrocinada):
    limite_diario = 15
    
    # Evalúa si el usuario cumple con los requisitos para reproducir la siguiente canción
    permitido = canciones_escuchadas < limite_diario and aleatorio_activo or es_patrocinada
    
    if permitido:
        return True
    else:
        return False

```
'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''## Consigna de Evaluación: Compleción de Código

**Dominio:** Sistema de Automatización de Tráfico Aéreo (ATC)

**Nivel:** Universitario (Introducción a la Programación / Algoritmos I)

**Lenguaje:** Python

**Complejidad:** Intermedia

### Contexto del Problema

Estás trabajando en el software de la torre de control de un aeropuerto internacional. Para garantizar la seguridad en las pistas, el sistema debe decidir de forma automática si un avión comercial tiene **permitido aterrizar** inmediatamente o si debe mantenerse en espera (patrón de espera).

Las variables que el sistema evalúa son las siguientes:

* `nivel_combustible` (str): Puede ser `"CRÍTICO"`, `"BAJO"` o `"NORMAL"`.
* `distancia_tormenta` (int): Distancia de una tormenta eléctrica al aeropuerto en kilómetros.
* `pistas_disponibles` (int): Cantidad de pistas libres en el aeropuerto.
* `vuelos_en_emergencia` (bool): `True` si hay otro avión en la zona declarando una emergencia médica o técnica.

### Instrucciones

Completá los espacios vacíos (**`______`**) en el script de Python para definir la **expresión lógica** correcta que determine el estado de la variable booleana `permitir_aterrizaje`.

Para que el aterrizaje sea autorizado (`True`), se deben cumplir **estrictamente** las siguientes reglas de negocio:

1. El combustible del avión está en estado `"CRÍTICO"`. (Si el combustible es crítico, el avión *siempre* debe aterrizar de inmediato, ignorando cualquier otra condición meteorológica o de tráfico).
2. **O BIEN**, si el combustible no es crítico, se debe autorizar el aterrizaje **solo si** se cumplen **todas** las siguientes condiciones en simultáneo:
* El combustible es `"BAJO"` o `"NORMAL"`.
* No hay ningún otro vuelo en emergencia en la zona.
* Hay al menos una pista disponible.
* La tormenta está a una distancia segura (estrictamente mayor a 15 kilómetros) **O** el nivel de combustible es `"BAJO"` (si el combustible ya es bajo, se asume el riesgo de la tormenta cercana para evitar que pase a crítico).



---

### Código a Completar

```python
def evaluar_autorizacion_aterrizaje(nivel_combustible, distancia_tormenta, pistas_disponibles, vuelos_en_emergencia):
    """
    Evalúa si un avión está autorizado a aterrizar según los parámetros de seguridad.
    Retorna True si está autorizado, False de lo contrario.
    """
    
    # ESPACIO A COMPLETAR: Definir la expresión lógica intermedia/avanzada
    permitir_aterrizaje = (
        nivel_combustible == "CRÍTICO" 
        (1)______ 
        (
            (nivel_combustible == "BAJO" or nivel_combustible == "NORMAL") 
            (2)______ 
            (3)______ vuelos_en_emergencia 
            (4)______ pistas_disponibles > 0 
            (5)______ (distancia_tormenta > 15 (6)______ nivel_combustible == "BAJO")
        )
    )
    
    return permitir_aterrizaje

# --- Casos de Prueba para verificación ---
# Caso 1: Combustible crítico (Debe dar True, sin importar la tormenta ni la falta de pistas)
print(evaluar_autorizacion_aterrizaje("CRÍTICO", 5, 0, True))  # Salida esperada: True

# Caso 2: Combustible bajo, tormenta cerca, hay pista, no hay emergencias (Debe dar True por el riesgo de combustible)
print(evaluar_autorizacion_aterrizaje("BAJO", 10, 1, False))   # Salida esperada: True

# Caso 3: Combustible normal, tormenta cerca (Debe dar False, riesgo innecesario)
print(evaluar_autorizacion_aterrizaje("NORMAL", 10, 2, False)) # Salida esperada: False

```
'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Consigna de Evaluación: Sistema de Validación de Tarifas Promocionales (FlightCheck)

### Contexto del Dominio

Estás trabajando en el módulo de facturación de una aerolínea. La empresa ha lanzado una campaña de tarifas promocionales llamada **"Viaje Flex"**. Sin embargo, para evitar abusos del sistema, la tarifa con descuento solo debe aplicarse si el pasajero cumple con una combinación estricta de condiciones de viaje y fidelidad.

### El Desafío

Debes diseñar una función en Python llamada `elegible_para_promocion` que reciba los datos de un cliente y un vuelo, y devuelva `True` si el pasajero califica para el descuento, o `False` en caso contrario.

Para que un pasajero sea **elegible**, se debe cumplir **al menos una** de las siguientes dos condiciones generales:

1. **Condición de Viajero Frecuente Fiel:**
* El pasajero es miembro del club VIP (*Gold* o *Platinum*).
* **Y** el destino del vuelo no es una ruta internacional restringida.


2. **Condición de Compra Anticipada y Temporada Baja:**
* El vuelo se está comprando con un mínimo de 30 días de anticipación.
* **Y** la temporada de viaje es considerada "Baja".
* **Y** el pasajero, si bien no es VIP, al menos tiene una cuenta registrada en el sistema (es decir, no es un usuario "Invitado").



**Exclusión Crítica (Restricción Absoluta):**
Sin importar si se cumple la Condición 1 o la Condición 2, el descuento **nunca** se aplicará si el peso del equipaje de bodega supera los 23 kg, o si el billete se compra utilizando puntos de otra aerolínea aliada en un código compartido (*codeshare*).

---

### Lo que debes hacer (Instrucciones para el estudiante)

Escribe el código en Python que resuelva este problema utilizando **una única expresión lógica principal** para el retorno de la función (puedes usar variables auxiliares previas para mejorar la legibilidad si lo consideras necesario, pero la lógica debe estar centralizada).

La función debe recibir los siguientes parámetros:

* `categoria_usuario` (str): `"Platinum"`, `"Gold"`, `"Registrado"` o `"Invitado"`.
* `es_ruta_restringida` (bool): `True` si el destino tiene restricciones, `False` si no.
* `dias_anticipacion` (int): Días que faltan para el vuelo desde el momento de la compra.
* `es_temporada_baja` (bool): `True` si es temporada baja, `False` si es alta.
* `peso_equipaje` (float): Peso en kilogramos del equipaje facturado.
* `es_codeshare` (bool): `True` si es un vuelo compartido con otra aerolínea, `False` si es operado 100% por la empresa.

#### Esqueleto de código para completar:

```python
def elegible_para_promocion(categoria_usuario, es_ruta_restringida, dias_anticipacion, es_temporada_baja, peso_equipaje, es_codeshare):
    # Desarrolla tus expresiones lógicas aquí
    
    # El resultado final debe ser un valor booleano
    return resultado

```
'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''### Consigna para el Estudiante (Problema de Parsons)

**Dominio:** Seguridad Informática / Automatización.
**Nivel:** Universitario (Intermedio).
**Lenguaje:** Python.

**Contexto:**
Estás programando el módulo de autenticación y seguridad para el ingreso a un laboratorio de investigación biológica. Para que una persona pueda entrar de forma autónoma, el sistema debe evaluar una expresión lógica compleja basada en cuatro variables booleanas que representan el estado del usuario y del entorno:

1. `tiene_credencial` (bool): El usuario posee una tarjeta de acceso válida.
2. `huella_verificada` (bool): El escáner biométrico confirmó la identidad.
3. `es_horario_laboral` (bool): El intento de acceso ocurre entre las 08:00 y las 20:00.
4. `modo_emergencia` (bool): El edificio se encuentra en estado de alerta o evacuación.

**Reglas de negocio para permitir el acceso (`permitir_acceso = True`):**

* El sistema **nunca** debe permitir el acceso si el `modo_emergencia` está activo (verdadero), sin importar ninguna otra condición.
* Si no hay emergencia, el usuario puede acceder de dos formas:
1. Si está dentro del `es_horario_laboral`, necesita obligatoriamente que `tiene_credencial` **o** `huella_verificada` sea verdadero (basta con uno de los dos mecanismos).
2. Si está **fuera** del horario laboral (es decir, es horario nocturno/fin de semana), el protocolo es estricto: requiere obligatoriamente que **ambos** factores de autenticación (`tiene_credencial` **y** `huella_verificada`) sean verdaderos.



**Tu tarea:**
Ordená y sangrá (indentá) correctamente los siguientes bloques de código mezclados para definir la función `evaluar_acceso` que implemente correctamente esta expresión lógica y devuelva el resultado esperado. **Nota:** Algunos bloques pueden requerir identación interna bajo las estructuras de control.

---

### Bloques de código desordenados (Desafío de Parsons)

A continuación se presentan las líneas que debés ordenar. *(Nota para el docente: se entregan desordenadas para que el alumno las arrastre o numere en el orden e indentación correctos)*.

```python
        return permitir_acceso
def evaluar_acceso(tiene_credencial, huella_verificada, es_horario_laboral, modo_emergencia):
    if modo_emergencia:
        permitir_acceso = (tiene_credencial or huella_verificada)
        permitir_acceso = False
    else:
        permitir_acceso = (tiene_credencial and huella_verificada)
    if es_horario_laboral:
    else:

```
'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''### Consigna

Un sistema universitario utiliza un script en Python para determinar si un estudiante de intercambio califica para una beca de manutención excepcional. El algoritmo evalúa tres condiciones principales:

1. `rendimiento_alto`: Si el promedio del estudiante es mayor o igual a 8.5.
2. `ingresos_bajos`: Si los ingresos familiares mensuales están por debajo del umbral mínimo.
3. `actividades_extra`: Si el estudiante participa en al menos dos actividades extracurriculares certificadas.

La regla del negocio establece que un estudiante califica si tiene un rendimiento alto y, además, cumple con la condición de tener ingresos bajos o participar en actividades extracurriculares. Sin embargo, debido a una reciente actualización de presupuesto, si el estudiante tiene ingresos bajos **y** participa en las actividades, se le otorga la beca de forma directa, sin importar si su rendimiento es alto o no.

Se ha escrito la siguiente expresión lógica en Python para evaluar la elegibilidad (`califica`):

```python
califica = (rendimiento_alto and ingresos_bajos) or actividades_extra and (ingresos_bajos or rendimiento_alto)

```

Analizá el comportamiento de la expresión anterior considerando la precedencia de operadores en Python e identificá cuál de los siguientes enunciados describe correctamente el resultado de su evaluación.

---

### Opciones de respuesta

**A)** La expresión evalúa correctamente la regla del negocio en todos los casos, garantizando la beca si se cumplen ambas condiciones de apoyo (ingresos y actividades) o si se tiene rendimiento alto junto con cualquiera de las otras dos.

**B)** La expresión es incorrecta porque el operador `or` tiene mayor precedencia que `and`, lo que provoca que primero se evalúe `actividades_extra and ingresos_bajos` antes que las demás relaciones.

**C)** La expresión es incorrecta. Debido a la precedencia de operadores, se evalúa como `(rendimiento_alto and ingresos_bajos) or (actividades_extra and ingresos_bajos) or (actividades_extra and rendimiento_alto)`. Esto causa que un estudiante con rendimiento bajo e ingresos altos califique si únicamente cumple con las actividades extracurriculares.

**D)** La expresión falla en un escenario crítico: si un estudiante **no** tiene un rendimiento alto, **no** tiene ingresos bajos, pero **sí** participa en actividades extracurriculares, la expresión evaluará como `True`, otorgándole la beca de forma errónea.
'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''## Consigna de Evaluación: Depuración de Expresiones Lógicas

**Asignatura:** Programación I / Introducción a la Algoritmia

**Nivel:** Universitario

**Lenguaje:** Python

**Tipo de ítem:** Señalamiento de ocurrencia y depuración

**Complejidad:** Intermedia

### Contexto del Dominio

El banco "FinTechFuturo" utiliza un script en Python para evaluar si un cliente es apto para un crédito hipotecario. Las reglas del banco para otorgar el crédito son estrictas y **deben cumplirse en su totalidad**:

1. El cliente debe ser mayor de edad (18 años o más) **y** menor de 65 años.
2. Los ingresos mensuales deben ser mayores a $1,500 **o** el cliente debe contar con un aval solidario garantizado (`tiene_aval = True`).
3. El cliente **no** debe estar registrado en el sistema de deudores morosos (`en_mora = False`).

### El Problema

Un programador junior escribió la función `evaluar_credito`. Sin embargo, el departamento de control de calidad detectó que el sistema está aprobando créditos a personas que no cumplen con los requisitos, y rechazando a otras que sí los cumplen. El problema radica exclusivamente en la **expresión lógica** del condicional.

A continuación se presenta el código defectuoso:

```python
def evaluar_credito(edad, ingresos, tiene_aval, en_mora):
    # EXPRESIÓN LÓGICA CON ERRORES
    if edad >= 18 or edad < 65 and ingresos > 1500 or tiene_aval and not en_mora == False:
        return "CRÉDITO APROBADO"
    else:
        return "CRÉDITO RECHAZADO"

# Ejemplo de prueba que falla debido al error:
# Un cliente de 70 años (fuera de rango), con ingresos de 2000, sin aval y sin mora,
# debería ser RECHAZADO, pero el sistema actual lo APRUEBA.
print(evaluar_credito(70, 2000, False, False)) 

```

### Tareas que debes realizar:

1. **Señalamiento de Ocurrencia (Identificación del error):**
* Realizá un seguimiento de la expresión lógica actual utilizando los valores del ejemplo de prueba: `edad = 70`, `ingresos = 2000`, `tiene_aval = False`, `en_mora = False`.
* Explicá detalladamente **por qué** la expresión actual evalúa como `True` en lugar de `False`. *Pista: Tené en cuenta la precedencia de los operadores lógicos (`not`, `and`, `or`).*


2. **Depuración (Corrección):**
* Reescribí la función `evaluar_credito` corrigiendo la expresión lógica dentro del `if` para que refleje fielmente las 3 reglas del banco.
* Utilizá **paréntesis** de forma explícita para agrupar las condiciones y garantizar que la precedencia de operadores sea la correcta.


'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Situación Problemática: Sistema de Control de Acceso

En el sistema de seguridad de una empresa, se implementó una función llamada `validar_intentos_ingreso()`. El objetivo de esta función es permitir que un usuario intente ingresar su clave secreta hasta un máximo de 3 veces. Si el usuario ingresa la clave correcta (`"Acesso2026"`), el bucle debe detenerse inmediatamente y el acceso debe ser concedido.

Sin embargo, el equipo de soporte técnico detectó que el código actual tiene un fallo crítico: **el sistema se queda congelado en un bucle infinito** y nunca le permite al usuario ingresar el segundo o tercer intento, bloqueando la terminal.

A continuación, se presenta el código que contiene el error:

```python
def validar_intentos_ingreso():
    clave_correcta = "Acceso2026"
    intentos_maximos = 3
    intentos_realizados = 0
    acceso_concedido = False
    
    while intentos_realizados < intentos_maximos:
        clave_ingresada = input("Ingrese su clave secreta: ")
        
        if clave_ingresada == clave_correcta:
            acceso_concedido = True
            print("Acceso concedido al sistema.")
            break
        else:
            print("Clave incorrecta. Intente nuevamente.")
            # El error se produce en esta sección
            
    if not acceso_concedido:
        print("Se ha superado el límite de intentos. Cuenta bloqueada.")

# Llamada a la función para probar el comportamiento
validar_intentos_ingreso()

```

### Tu Tarea (Señalamiento de Ocurrencia)

1. **Identifica y señala** la línea exacta o sección del código donde se produce la falla que genera el bucle infinito. Explica brevemente por qué ocurre este comportamiento anómalo.
2. **Escribe el fragmento de código corregido** que resuelve el problema, asegurando que el ciclo termine correctamente después de los 3 intentos fallidos.
'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Contexto del Problema

En un refugio de animales se registra diariamente la cantidad de alimento en kilogramos que consume cada perro. Para optimizar la compra de provisiones, el sistema necesita calcular cuántos kilos de alimento consumió en total un grupo de 5 perros seleccionados al azar durante el día de hoy.

El sistema ya cuenta con una función llamada `solicitar_cantidad_alimento()` que, cada vez que es invocada, le pide al usuario que ingrese la cantidad de alimento (un número entero) consumida por un perro y devuelve dicho valor.

---

### Consigna

Completá el siguiente bloque de código en Python llenando los espacios vacíos (`_____`) para que el programa calcule correctamente el consumo total de los 5 perros utilizando la función existente. **Nota:** No debés modificar ninguna otra parte del código provisto.

```python
def calcular_consumo_total():
    total_alimento = 0
    
    # Repetir el proceso exactamente para los 5 perros
    for i in _____(_____):
        cantidad_perro = solicitar_cantidad_alimento()
        total_alimento = _____ + _____
        
    return total_alimento

```
'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Contexto y Enunciado de la Actividad

Un refugio de animales local registra diariamente la cantidad de alimento (en kilogramos) que consumen los perros alojados. Para optimizar la compra de provisiones, el coordinador del refugio necesita un programa que le permita ingresar los consumos diarios de una semana y calcular automáticamente el total de alimento utilizado.

Escribí una función en Python llamada `calcular_total_alimento` que no reciba parámetros. La función debe solicitar al usuario, uno por uno, la cantidad de alimento consumido durante 7 días consecutivos. Al finalizar la carga, la función debe retornar el total acumulado de kilogramos de alimento.
'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''# Consigna de Evaluación

Un refugio de animales necesita un programa para registrar de forma automática la cantidad de alimento diario que consume un grupo de cachorros rescatados. El sistema recibe una lista con los pesos en gramos de las porciones consumidas por cada cachorro de forma individual y debe calcular el total acumulado de alimento consumido por todo el grupo.

Tu tarea es ordenar los siguientes bloques de código en Python para completar la función `calcular_total_alimento(porciones)`. Esta función recibe la lista de porciones y debe retornar la suma total consumida. Hay bloques que corresponden a la estructura correcta de la función, otros que representan la inicialización, el procesamiento de los datos y el retorno del resultado.

Ordena los bloques de manera que el programa sea sintácticamente correcto y cumpla con el objetivo planteado.

**Bloques disponibles (desordenados):**

```python
    return total

```

```python
    for porcion in porciones:

```

```python
def calcular_total_alimento(porciones):

```

```python
    total = 0

```

```python
        total = total + porcion

```

---

# Solución y Explicación Paso a Paso

Para resolver el problema planteado, se debe reconstruir la lógica de la función en Python respetando la sangría (*indentación*) y el flujo de control adecuado para recorrer una estructura de datos secuencial de forma básica.

### Paso 1: Definición de la función

El punto de partida de la solución es la cabecera de la función. Utilizando los conocimientos previos sobre funciones, se identifica el bloque que utiliza la palabra clave `def`, el nombre de la función y el parámetro requerido.

```python
def calcular_total_alimento(porciones):

```

### Paso 2: Inicialización del acumulador

Antes de comenzar a procesar los elementos de la lista, es indispensable contar con una variable que almacene la suma total. Como se arranca sin procesar ningún dato, se inicializa el contador/acumulador en cero. Este bloque debe llevar un nivel de sangría (4 espacios) por estar dentro de la función.

```python
    total = 0

```

### Paso 3: Configuración del ciclo de repetición

Para procesar cada uno de los elementos de la lista `porciones` de manera secuencial y simplificada, se requiere una estructura que itere por cada elemento. Se utiliza la directiva de repetición `for`, la cual recorrerá la lista asignando cada valor a la variable temporal `porcion`. Mantiene el mismo nivel de sangría que la inicialización de la variable.

```python
    for porcion in porciones:

```

### Paso 4: Actualización del acumulador (Cuerpo del ciclo)

Dentro del ciclo, por cada iteración realizada, se debe añadir el valor de la porción actual al total acumulado previamente. Este bloque requiere un nivel extra de sangría (8 espacios en total) para denotar que pertenece al cuerpo de la directiva de repetición.

```python
        total = total + porcion

```

### Paso 5: Retorno del resultado

Una vez que el ciclo finaliza y se han procesado todos los elementos de la lista, la función debe devolver el valor final calculado. El bloque de retorno (`return`) debe alinearse con el flujo principal de la función (4 espacios de sangría), quedando fuera del ciclo `for`.

```python
    return total

```

### Código Final Integrado

Al unir y tabular correctamente todos los bloques seleccionados, se obtiene la solución esperada:

```python
def calcular_total_alimento(porciones):
    total = 0
    for porcion in porciones:
        total = total + porcion
    return total

```'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''## Contexto: Control de Calidad en una Planta de Envasado

En una planta de envasado de jugos, una máquina automatizada mide el volumen (en mililitros) de cada botella que pasa por la cinta transportadora. Si una botella contiene menos de 240 ml, se considera "defectuosa" por estar incompleta.

Para analizar el comportamiento del sistema, se ha programado la siguiente función en Python:

```python
def analizar_lote(botellas):
    conteo = 0
    for volumen in botellas:
        if volumen < 240:
            conteo = conteo + 1
    return conteo

```

Si ejecutamos la función pasando como argumento la lista de volúmenes `[250, 235, 245, 238, 260]`, ¿cuál es el valor exacto que retorna la función al finalizar su ejecución?

* A) 5
* B) 2
* C) 3
* D) 0
'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna

El siguiente programa en Python contiene un error que impide que cumpla con su objetivo. La función `generar_alertas_inventario` tiene como propósito imprimir una alerta para cada uno de los primeros 5 productos registrados en una lista de stock, indicando que se debe realizar un pedido de reposición.

Identificá la línea exacta donde se produce el comportamiento incorrecto, explicá en qué consiste la falla y cómo debería corregirse el código para que funcione según lo esperado.

```python
def generar_alertas_inventario(lista_productos):
    """
    Imprime una alerta de reposición para los primeros 5 productos de la lista.
    Precondición: lista_productos contiene al menos 5 elementos.
    """
    for i in range(1, 5):
        producto = lista_productos[i]
        print(f"Alerta: Stock bajo para el producto: {producto}. Solicitar reposición.")

```
'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Consigna

Un local de comida rápida necesita automatizar el sistema de su dispensador de bebidas. Cuando un cliente selecciona un combo grande, la máquina debe activar la válvula de servido exactamente **4 veces** para llenar el vaso por completo sin que se desborde.

Completá los espacios en blanco del siguiente código en Python para que la función `servir_combo_grande` cumpla con su objetivo. Cada espacio en blanco está representado por una línea continua (`_______`).

```python
def activar_valvula():
    # Esta función ya está implementada y simula la descarga de una porción de bebida
    print("Válvula activada: sirviendo una porción.")

def servir_combo_grande():
    # Completar para que la válvula se active exactamente 4 veces
    _______ i in _______(_______):
        activar_valvula()

```
'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Consigna

Un gimnasio de alto rendimiento necesita registrar de forma automatizada las cargas máximas levantadas por un atleta durante su circuito de entrenamiento de fuerza. El circuito consta exactamente de 6 estaciones de ejercicios diferentes. En cada estación, un sensor registra el peso máximo (en kilogramos) que el atleta logra levantar.

Escribir una función en Python llamada `registrar_circuito()` que simule este proceso. La función no recibe parámetros y debe solicitar al usuario, uno por uno, el peso levantado en cada una de las 6 estaciones utilizando la función `input()`. Al finalizar el ingreso de todos los datos, la función debe mostrar por pantalla el peso total acumulado que levantó el atleta a lo largo de todo el circuito, empleando la función `print()`.
'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación

**Contexto del problema:** En una fábrica textil automatizada, una máquina de coser industrial necesita realizar un patrón de costura estándar sobre el borde de una prenda. Para asegurar la resistencia de la costura, el diseño requiere que la aguja realice exactamente **5 puntadas consecutivas en línea recta**, avanzando una posición fija después de cada puntada.

**Tu tarea:**
A continuación, se presentan un conjunto de líneas de código desordenadas. Debes seleccionar y ordenar las instrucciones correctas para construir la función `realizar_costura_borde()` que cumpla con el requerimiento de la máquina textil.

*Nota: Ten en cuenta que algunas líneas son distractores innecesarios y no deben incluirse en la solución final.*

**Líneas de código disponibles (desordenadas):**

1. `    for i in range(5):`
2. `def realizar_costura_borde():`
3. `        dar_puntada()`
4. `    for i in range(1, 5):`
5. `def realizar_costura_borde(puntadas):`
6. `        avanzar_posicion()`
7. `    dar_puntada()`
8. `    avanzar_posicion()`
'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''### Consigna

Un robot de limpieza se desplaza por un pasillo recto dividido en casilleros. Su posición inicial se representa por las coordenadas $(X=0, Y=0)$. Se ejecuta la siguiente función en Python para realizar una rutina de mantenimiento:

```python
def ejecutar_mantenimiento():
    x = 0
    y = 0
    
    y = y + 2
    for i in range(3):
        x = x + 1
        y = y + 1
        
    x = x - 1
    return (x, y)

```

¿Cuál es la posición final del robot (valor de las variables `x` e `y`) al finalizar la ejecución de la función?

**Opciones:**

1. `(x=2, y=5)`
2. `(x=3, y=5)`
3. `(x=2, y=4)`
4. `(x=3, y=2)`
'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Consigna de Evaluación

**Dominio Concreto:** Sistema de Gestión de Inventario para una Tienda de Mascotas.
**Nivel:** Universitario (Básico)
**Lenguaje:** Python
**Conocimientos previos requeridos:** Definición e implementación de funciones, estructuras de control iterativas (`while`).

#### Contexto del problema

Una tienda de mascotas local utiliza un pequeño script en Python para controlar el stock de sus productos. Un desarrollador junior implementó la función `actualizar_inventario_por_ventas`, cuyo objetivo es procesar una lista de cantidades vendidas y restarlas del stock inicial de un producto hasta que se procesen todas las ventas del día o hasta que el stock llegue a cero (lo que ocurra primero).

Sin embargo, el dueño de la tienda nota que cuando se ejecuta la función, el programa se queda "colgado" (bloqueado) y nunca termina de mostrar el stock final.

#### Código con error (Bug)

```python
def actualizar_inventario_por_ventas(stock_inicial, lista_ventas):
    stock_actual = stock_inicial
    indice = 0
    
    # Se procesan las ventas mientras quede stock y haya elementos en la lista
    while stock_actual > 0 and indice < len(lista_ventas):
        venta_actual = lista_ventas[indice]
        
        if venta_actual <= stock_actual:
            stock_actual = stock_actual - venta_actual
            print(f"Venta procesada: {venta_actual} unidades.")
        else:
            print(f"No hay stock suficiente para una venta de {venta_actual} unidades.")
            stock_actual = 0  # Se agota el stock restante
            
        # El desarrollador olvidó modificar una variable crítica aquí

    return stock_actual

# Simulación de prueba
stock_disponible = 50
ventas_del_dia = [10, 15, 5, 20]
stock_final = actualizar_inventario_por_ventas(stock_disponible, ventas_del_dia)
print(f"Stock final del producto: {stock_final}")

```

#### Tarea para el estudiante (Señalamiento de ocurrencia)

Analizá el código provisto e identificá el error que causa el comportamiento indefinido de la directiva de repetición (`while`). Luego, respondé:

1. **Señalamiento:** ¿Cuál es la línea exacta o el bloque de código dentro del ciclo `while` donde ocurre la falla de lógica que impide que el bucle finalice correctamente?
2. **Explicación:** Explicá brevemente por qué la omisión o el estado de esa variable produce un bucle infinito en este escenario.
3. **Corrección:** Escribí la línea de código faltante en el lugar correspondiente para corregir la directiva de repetición.
'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Consigna de Evaluación

**Dominio:** Gestión de inventario en una tienda de mascotas.
**Contexto:** Se solicita completar una función en Python encargada de calcular la cantidad total de alimento balanceado acumulado en el depósito a partir de una lista de bolsas disponibles.

**Instrucciones para el estudiante:** Complete el espacio vacío `_______` con la estructura de repetición adecuada para que el código recorra cada uno de los pesos de las bolsas de alimento y calcule correctamente el total acumulado.

```python
def calcular_total_alimento(lista_bolsas):
    """
    Recibe una lista con los pesos (en kg) de las bolsas de alimento
    y retorna la suma total del inventario.
    """
    total_kilos = 0
    
    # Completar aquí con la directiva de repetición adecuada
    _______ bolsa in lista_bolsas:
        total_kilos += bolsa
        
    return total_kilos

# Ejemplo de uso esperado:
# inventario = [15, 20, 7, 10]
# print(calcular_total_alimento(inventario)) -> Debe mostrar 52

```
'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación: Control de Stock en una Tienda de Mascotas

**Contexto:**
Una reconocida tienda de mascotas local necesita automatizar el control de su inventario de bolsas de alimento balanceado. Actualmente, reciben camiones con mercadería de diferentes pesos y necesitan un programa que les permita registrar las bolsas que ingresan hasta que se decida finalizar la carga.

**Tu Tarea:**
Debes desarrollar un programa en Python que asista al personal del depósito. Para ello, se solicita la implementación de una función principal y el uso de estructuras de repetición.

Escribí un script en Python que cumpla con los siguientes requisitos:

1. **Definición de Función:** Crea una función llamada `registrar_inventario()` que no reciba parámetros.
2. **Estructura de Repetición (Bucle):** Dentro de la función, se debe solicitar iterativamente (repetidamente) al usuario que ingrese el peso de una bolsa de alimento (en kilogramos).
3. **Condición de Parada:** El ingreso de datos debe finalizar cuando el usuario ingrese un peso igual a `0` (cero), lo que indica que no hay más bolsas por registrar.
4. **Cálculo y Salida:** Al finalizar el bucle (cuando se ingresa el 0), la función debe calcular y mostrar por pantalla:
* La cantidad total de bolsas registradas.
* El peso total acumulado de todas las bolsas.

'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación: El Contador de Órbitas (Satélites)

### Contexto del Dominio

En el centro de control de una agencia aeroespacial, recibimos un flujo de datos con las altitudes (en kilómetros) registradas por un satélite meteorológico durante varias horas. Para verificar que el satélite se mantiene en una **órbita baja estable**, necesitamos analizar una lista de mediciones y contar cuántas de ellas se encuentran estrictamente dentro del rango seguro: entre **400 km y 800 km** (inclusive). El análisis debe detenerse inmediatamente si se detecta una anomalía crítica, es decir, una altitud de **0 km o menos**, ya que indicaría una falla en los sensores.

### Tarea

Tu objetivo es ordenar los siguientes bloques de código para implementar la función `contar_orbitas_estables(mediciones)`. La función recibe una lista de números (altitudes) y debe devolver la cantidad de mediciones que cumplen con el criterio de estabilidad, procesándolas una a una hasta el final de la lista o hasta encontrar la anomalía.

---

### Bloques de Código (Desordenados)

A continuación se presentan los bloques que debes arrastrar y ordenar de manera lógica y con la sangría (indentación) correcta en Python:

```python
# BLOQUE A
    return correctas

```

```python
# BLOQUE B
def contar_orbitas_estables(mediciones):

```

```python
# BLOQUE C
        if altitud <= 0:
            break

```

```python
# BLOQUE D
        if 400 <= altitud <= 800:
            correctas += 1

```

```python
# BLOQUE E
    correctas = 0

```

```python
# BLOQUE F
    for altitud in mediciones:

```
'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''## Consigna de Evaluación

**Dominio:** Gestión de Inventario
**Nivel:** Universitario (Básico)
**Lenguaje:** Python 3.x

### Enunciado

En una tienda de electrónica se necesita automatizar el control de stock. Para ello, se diseñó la función `actualizar_inventario`, la cual recibe una lista con las cantidades actuales de varios productos y un "umbral de alerta". La función debe procesar los productos uno por uno para determinar cuántos de ellos se encuentran por debajo de ese umbral (es decir, que requieren reposición urgente).

Analizá con atención el siguiente código en Python:

```python
def actualizar_inventario(productos, umbral):
    alertas_generadas = 0
    indice = 0
    
    while indice < len(productos):
        if productos[indice] < umbral:
            alertas_generadas += 1
        indice += 1
        
    return alertas_generadas

# Ejecución del programa
stock_actual = [15, 4, 8, 23, 3]
limite_minimo = 10
resultado = actualizar_inventario(stock_actual, limite_minimo)

```

Luego de realizar el seguimiento del código (traceo), ¿cuál es el valor final que almacena la variable `resultado` al terminar la ejecución?

### Opciones

* **A)** `5`
* **B)** `2`
* **C)** `3`
* **D)** `10`
'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''## Consigna

Dominio: acceso a una plataforma de cursos.

Completá los espacios vacíos del siguiente programa en Python para definir una condición que indique si una persona puede acceder a un curso.

```python
edad = 17
tiene_autorizacion = True
curso_activo = True

puede_acceder = _______________________________

print(puede_acceder)
```

La persona puede acceder si:

* el curso está activo;
* y, además, cumple una de estas dos condiciones:

  * tiene 18 años o más;
  * o tiene autorización.
'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Consigna

En el dominio de **gestión de reservas para salas de estudio universitarias**, definí en Python una condición que permita decidir si una solicitud de reserva debe ser aceptada.

Una reserva puede aceptarse únicamente cuando se cumplen todas estas reglas:

* La sala está disponible.
* La persona solicitante es estudiante regular o docente.
* La duración solicitada está entre 30 y 120 minutos inclusive.
* La reserva no se realiza para un horario bloqueado por mantenimiento.
* Si la reserva es para después de las 20:00, la persona debe tener autorización especial.

Escribí la condición completa usando variables previamente definidas, por ejemplo:

```python
sala_disponible
es_estudiante_regular
es_docente
duracion_minutos
horario_bloqueado
hora_inicio
tiene_autorizacion_especial
```

Además, explicá con tus palabras qué representa cada parte de la condición.
'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Consigna

Dominio: gestión de turnos médicos.

Ordená los fragmentos para completar la función `puede_reservar_turno`, que debe indicar si una persona puede reservar un turno según estas reglas:

Una persona puede reservar turno si:

* es mayor de edad o tiene autorización;
* tiene cobertura médica o puede pagar particular;
* no tiene una deuda activa.

```python
def puede_reservar_turno(edad, tiene_autorizacion, tiene_cobertura, puede_pagar, tiene_deuda):
```

Fragmentos disponibles:

```python
A) return puede_reservar

B) sin_deuda = not tiene_deuda

C) puede_reservar = condicion_edad and condicion_pago and sin_deuda

D) condicion_pago = tiene_cobertura or puede_pagar

E) condicion_edad = edad >= 18 or tiene_autorizacion
```

---

'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''**Dominio:** gestión de turnos médicos

En Python se ejecuta:

```python
edad = 67
tiene_orden = True
es_urgente = False

resultado = edad >= 65 and tiene_orden or es_urgente
```

¿Cuál es el valor de `resultado`?

A. `True`
B. `False`
C. `67`
D. Error'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''## Consigna

En una plataforma de turnos médicos, el siguiente programa debería indicar si una solicitud debe ser revisada manualmente.

```python
def requiere_revision(edad, tiene_obra_social, es_urgente, adeuda_turnos):
    if edad < 18 and es_urgente or not tiene_obra_social and adeuda_turnos:
        return True
    return False
```

El criterio correcto es:

Una solicitud requiere revisión manual cuando el paciente es menor de edad **y**, además, ocurre al menos una de estas situaciones:

* el turno es urgente;
* no tiene obra social y adeuda turnos anteriores.

Analizá el programa dado y señalá en qué casos produce un resultado incorrecto. Luego corregí la condición del `if`.

'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''**Consigna**

En una reserva natural se registra la información de cada visitante mediante las variables:

```python
edad
tiene_autorizacion
es_socio
```

donde:

* `edad` es un número entero.
* `tiene_autorizacion` es un valor booleano (`True` o `False`).
* `es_socio` es un valor booleano (`True` o `False`).

Completar los espacios en blanco de la siguiente expresión para que resulte verdadera cuando el visitante sea mayor o igual a 18 años y, además, tenga autorización o sea socio de la reserva.

```python
(edad __ 18) __ (tiene_autorizacion __ es_socio)
```

---

'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''**Consigna**

En un sistema de inscripción a un torneo de videojuegos se registran los siguientes datos de cada participante:

* `edad` (entero)
* `tiene_autorizacion` (booleano)
* `cuota_al_dia` (booleano)

Definí una única expresión en Python que permita determinar si una persona puede completar la inscripción según las siguientes reglas:

* Puede inscribirse si tiene 18 años o más y tiene la cuota al día.
* También puede inscribirse si es menor de 18 años, pero tiene autorización y la cuota al día.

Escribí la expresión lógica utilizando únicamente las variables indicadas.

---

'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''En un sistema de acceso a una biblioteca, se necesita definir una condición que resulte verdadera cuando una persona puede ingresar a una sala de estudio especial. Una persona puede ingresar si:

* Tiene una membresía activa **o** es estudiante.
* Y además, no posee multas pendientes.

Ordená los siguientes fragmentos para construir una única expresión en Python que represente esa condición.

1. `membresia_activa`
2. `or`
3. `estudiante`
4. `and`
5. `not`
6. `multas_pendientes`
7. `(`
8. `)`

'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''````markdown
Consigna:

En un sistema de inscripción a un taller, se usa la siguiente expresión en Python:

```python
edad >= 18 and tiene_cupo
````

¿Qué valores hacen que la expresión se evalúe como `True`?

Opciones:

1. `edad = 17`, `tiene_cupo = True`
2. `edad = 18`, `tiene_cupo = False`
3. `edad = 20`, `tiene_cupo = True`
4. `edad = 16`, `tiene_cupo = False`

```'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''**Consigna:**

```python
def debe_aplicar_descuento(edad, es_socio, monto_compra):
    if edad >= 65 and es_socio or monto_compra > 20000:
        return True
    else:
        return False
```

Un supermercado aplica un descuento especial únicamente a clientes que sean socios y que, además, cumplan al menos una de estas condiciones: tener 65 años o más, o haber realizado una compra mayor a $20000.

Sin embargo, algunos clientes no socios están recibiendo el descuento.

Señalá la o las ocurrencias del código que causan el comportamiento incorrecto y explicá cómo deberían corregirse.

'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''### Consigna: Compleción de espacios vacíos — Definición de Expresión Lógica (Nivel Intermedio)

**Dominio:** Sistema de control de acceso a un laboratorio universitario de investigación.

En un laboratorio de investigación, el acceso está permitido únicamente si se cumple la siguiente condición:

* La persona posee una credencial válida **y**
* (es investigador autorizado **o** tiene un permiso temporal activo) **y**
* no se encuentra suspendida.

Completa los espacios vacíos para construir correctamente la **expresión lógica** que determine si una persona puede ingresar al laboratorio.

#### Código a completar

```python
credencial_valida = True
investigador_autorizado = False
permiso_temporal = True
suspendido = False

puede_ingresar = ______ and (______ or ______) and ______

print("¿Puede ingresar al laboratorio?", puede_ingresar)
```

#### Instrucciones

1. Completa los cuatro espacios vacíos utilizando las variables definidas.
2. Utiliza los operadores lógicos de Python (`and`, `or`, `not`) según corresponda.
3. La expresión final debe representar exactamente la política de acceso descrita.

'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''**Consigna (Respuesta Abierta – Nivel Intermedio)**

**Dominio:** Sistema de control de acceso a una biblioteca universitaria.

En una biblioteca universitaria se desea automatizar la validación de ingreso de estudiantes a una sala de estudio restringida. Un estudiante puede ingresar únicamente si cumple con la siguiente condición:

* Posee una credencial universitaria válida (`credencial_valida`), **y además**
* Tiene una reserva activa de la sala (`reserva_activa`) **o** es miembro del programa de investigación de la universidad (`es_investigador`).

### Actividad

1. Explicá con tus palabras qué es una **expresión lógica** y cuál es su utilidad en la programación.
2. Identificá las variables lógicas involucradas en el problema y describí qué representa cada una.
3. Construí la **expresión lógica** que modela la condición de ingreso a la sala de estudio.
4. Implementá dicha expresión en Python utilizando variables booleanas.
5. Mostrá un ejemplo de ejecución asignando valores a las variables y explicá por qué el resultado obtenido permite o no el ingreso.

### Criterios de evaluación

* Comprensión del concepto de expresión lógica.
* Correcta identificación de variables booleanas.
* Adecuada construcción de la expresión lógica utilizando operadores `and` y `or`.
* Correcta implementación en Python.
* Claridad y coherencia en la justificación del resultado obtenido.'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''### Consigna tipo Parsons (Nivel Intermedio)

**Tema:** Definición de Expresiones Lógicas en Python
**Nivel:** Universitario
**Dominio:** Sistema de acceso a una biblioteca universitaria

#### Contexto

La biblioteca de una universidad posee un sistema automático que determina si un estudiante puede ingresar a una sala de estudio especial.

Un estudiante podrá ingresar únicamente si:

* Tiene una credencial válida (`credencial_valida` es `True`).
* No posee sanciones vigentes (`tiene_sanciones` es `False`).
* Además, debe cumplir **al menos una** de las siguientes condiciones:

  * Tener una reserva activa (`reserva_activa` es `True`).
  * Ser estudiante de posgrado (`es_posgrado` es `True`).

#### Objetivo

A continuación se presentan líneas de código desordenadas. Ordenalas correctamente para construir una expresión lógica que determine si el estudiante puede ingresar a la sala.

**Importante:** No todas las líneas son necesariamente incorrectas por sí mismas, pero solo una combinación y orden producen la solución adecuada.

#### Bloques desordenados

```python
puede_ingresar =
(reserva_activa or es_posgrado)
credencial_valida and
not tiene_sanciones and
```

#### Tarea

1. Reordená los bloques para formar una única instrucción válida en Python.
2. La variable resultante debe llamarse `puede_ingresar`.
3. La expresión debe reflejar exactamente las reglas de acceso descritas en el enunciado.

#### Variables disponibles

```python
credencial_valida      # bool
tiene_sanciones        # bool
reserva_activa         # bool
es_posgrado            # bool
```

#### Ejemplo de comportamiento esperado

Si:

```python
credencial_valida = True
tiene_sanciones = False
reserva_activa = False
es_posgrado = True
```

entonces:

```python
puede_ingresar
```

debería valer:

```python
True
```

#### Competencia evaluada

* Construcción y comprensión de expresiones lógicas compuestas.
* Uso correcto de operadores booleanos (`and`, `or`, `not`).
* Interpretación de requisitos expresados en lenguaje natural y traducción a una condición lógica en Python.
'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. ''','''**Dominio concreto:** gestión de turnos en una clínica universitaria.

¿Cuál de las siguientes expresiones en Python evalúa correctamente si un turno debe marcarse como **“prioritario”** cuando se cumple que: el paciente tiene más de 65 años **o** presenta síntomas graves, y además tiene cobertura médica activa?

A. `edad > 65 or sintomas_graves and cobertura_activa`
B. `(edad > 65 or sintomas_graves) and cobertura_activa`
C. `edad > 65 and sintomas_graves or cobertura_activa`
D. `edad > 65 or (sintomas_graves and not cobertura_activa)`

'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad '<b>INTERMEDIO</b>' (Expresiones lógicas cuyos términos son expresiones básicas y/o variables booleanas relacionados mediante operadores lógicos). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''**Consigna: Señalamiento de ocurrencia — Depuración de Expresión Lógica**

Dominio: **sistema de reservas de salas universitarias**

Una universidad usa la siguiente función en Python para decidir si una solicitud de reserva de sala debe aprobarse automáticamente:

```python
def aprobar_reserva(es_docente, es_estudiante, tiene_autorizacion, sala_disponible, horario_habilitado):
    if es_docente or es_estudiante and tiene_autorizacion and sala_disponible or horario_habilitado:
        return "Reserva aprobada"
    else:
        return "Reserva rechazada"
```

La regla institucional correcta es:

> Una reserva debe aprobarse solo si la sala está disponible y el horario está habilitado. Además, quien solicita debe ser docente, o bien estudiante con autorización.

Sin ejecutar el programa, señalá una combinación concreta de valores booleanos para los parámetros de la función en la que el resultado producido por el código sea incorrecto respecto de la regla institucional.

Luego, explicá brevemente:

1. Qué resultado devuelve la función con esos valores.
2. Qué resultado debería devolver según la regla.
3. Qué parte de la expresión lógica causa el error.
4. Cómo reescribirías la condición del `if` para corregirla.'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna

Dominio: control de stock en una librería.

El siguiente programa debería mostrar cuántos productos tienen stock igual a `0`, pero el resultado no es correcto.

```python
def contar_agotados(stocks):
    agotados = 0
    posicion = 0

    while posicion < len(stocks):
        if stocks[posicion] == 0:
            agotados = agotados + 1
        posicion = posicion + 2

    return agotados
```

Para la lista:

```python
stocks = [3, 0, 5, 0, 0, 8]
```

el programa debería devolver `3`.

Señalá en qué línea ocurre el error y explicá por qué produce un resultado incorrecto. Luego escribí una versión corregida de la función.

'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna

Dominio: control de stock en una biblioteca.

Completá los espacios vacíos del siguiente programa para que la función `contar_disponibles` reciba una lista de cantidades de ejemplares disponibles por libro y devuelva cuántos libros tienen al menos un ejemplar disponible.

```python
def contar_disponibles(stock):
    cantidad = 0

    for disponibles in ______:
        if disponibles > 0:
            cantidad = ______

    return ______
```

Ejemplo esperado:

```python
print(contar_disponibles([0, 3, 1, 0, 5]))
```

Salida:

```python
3
```

'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Dominio:** Control de asistencia en un club deportivo.

Un club deportivo registra la asistencia de sus socios a una clase especial. Se dispone de una función ya implementada llamada `leer_asistencia()` que no recibe parámetros y devuelve un número entero: `1` si un socio asistió y `0` si no asistió.

Escribí una función en Python llamada `contar_asistentes(cantidad_socios)` que reciba la cantidad de socios registrados para esa clase y devuelva cuántos asistieron.

**Ejemplo:**

Si `cantidad_socios` vale `5` y las llamadas a `leer_asistencia()` devuelven sucesivamente:

`1, 0, 1, 1, 0`

la función debe devolver:

`3`

---

'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna

**Dominio:** control de stock en una librería.

Ordená los siguientes bloques para implementar la función `contar_bajos_stock`, que recibe una lista de cantidades de productos y devuelve cuántos productos tienen menos de 5 unidades disponibles.

```python
def contar_bajos_stock(cantidades):
```

```python
    contador = 0
```

```python
    for cantidad in cantidades:
```

```python
        if cantidad < 5:
```

```python
            contador = contador + 1
```

```python
    return contador
```

---

'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''```python
def contar_alertas(mediciones):
    alertas = 0
    for temperatura in mediciones:
        if temperatura > 38:
            alertas = alertas + 1
    return alertas

datos = [36, 39, 38, 41, 37]
resultado = contar_alertas(datos)
print(resultado)
```

En el contexto de monitoreo de temperatura corporal en una guardia médica, ¿qué valor se muestra por pantalla al ejecutar el programa?

A. `1`
B. `2`
C. `3`
D. `5`

'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Consigna:**

En una biblioteca se necesita registrar la cantidad de libros prestados durante 5 días hábiles. El siguiente programa debería devolver el total de préstamos realizados en esos 5 días, pero tiene una falla.

Identificá en qué línea ocurre el error, explicá por qué produce un resultado incorrecto y proponé una corrección.

```python
1. def total_prestamos():
2.     total = 0
3.     for dia in range(5):
4.         prestamos = int(input("Cantidad de préstamos del día: "))
5.         total = prestamos
6.     return total
```

'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Consigna:**

Dominio: control de inventario de una librería.

Completá la función para que devuelva la cantidad total de cuadernos recibidos durante 5 días, sabiendo que cada día se recibieron 12 cuadernos.

```python
def total_cuadernos_recibidos():
    total = 0

    for dia in range(_____):
        total = total + _____

    return total
```

'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Consigna:**

```markdown
En una biblioteca escolar se quiere registrar la cantidad de páginas leídas durante una semana.

Escribir una función en Python llamada `total_paginas_semana(paginas_por_dia)` que reciba una lista con exactamente 7 números enteros, donde cada número representa la cantidad de páginas leídas en un día de la semana.

La función debe devolver el total de páginas leídas en toda la semana.
```

'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Consigna:**

Ordenar las siguientes instrucciones para que la función calcule el total recaudado por la venta de 8 entradas de cine, todas con el mismo precio.

1. `total = 0`
2. `return total`
3. `for i in range(8):`
4. `def calcular_recaudacion(precio_entrada):`
5. `total = precio_entrada`
6. `total = total + precio_entrada`
7. `return precio_entrada`
8. `for i in range(precio_entrada):`

'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''**Consigna:**

En una biblioteca, la función `contar_estantes()` registra cuántos libros se revisan en total.

¿Qué valor tiene la variable `total` justo antes de ejecutar `return total`?

```python
def contar_estantes():
    total = 0

    for estante in range(4):
        total = total + 3

    total = total - 2
    return total
```

**Opciones:**

1. `3`
2. `10`
3. `12`
4. `14`
'''],['''Se quiere crear una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Consigna — Señalamiento de ocurrencia**

**Dominio:** Gestión de inventario de una biblioteca universitaria.

Se tiene la siguiente función en Python, cuyo objetivo es contar cuántos libros de una lista tienen una cantidad de ejemplares disponibles menor o igual a `2`.

```python
def contar_libros_escasos(ejemplares):
    contador = 0

    for cantidad in ejemplares:
        if cantidad <= 2:
            contador = 1

    return contador
```

Por ejemplo, para la lista:

```python
[5, 2, 0, 3, 1]
```

la función debería devolver `3`, porque hay tres libros con pocos ejemplares disponibles: `2`, `0` y `1`.

**Tarea**

Señalá en qué línea ocurre el error dentro de la directiva de repetición y explicá brevemente por qué la función no devuelve el resultado esperado.

Luego, corregí la función para que cuente correctamente la cantidad de libros escasos.'''],['''Se quiere crear una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Dominio concreto:** control de stock en una librería universitaria.

Complete los espacios vacíos para que la función reciba una lista de cantidades de libros vendidos por día y devuelva el total vendido. Use una directiva de repetición.

```python
def calcular_total_vendido(ventas_diarias):
    total = 0
    for cantidad in __________:
        total = total + __________
    return total
```

'''],['''Se quiere crear una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Consigna de respuesta abierta**

Dominio concreto: **gestión de turnos en una clínica universitaria**

En una clínica universitaria se necesita calcular cuántos pacientes fueron atendidos durante una mañana. Escribí un programa en **Python** que incluya una función llamada `contar_pacientes()`.

La función debe pedir al usuario, de forma repetida, el nombre de cada paciente atendido. La carga debe finalizar cuando el usuario ingrese la palabra `"fin"`. Al terminar, la función debe devolver la cantidad total de pacientes registrados.

Luego, desde el programa principal, llamá a la función y mostrale al usuario un mensaje con el total de pacientes atendidos.

En tu respuesta, incluí el código completo y una breve explicación de cómo utilizaste la directiva de repetición.'''],['''Se quiere crear una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''**Consigna Parsons — Nivel básico**

**Dominio:** gestión de una biblioteca universitaria.

Un sistema de biblioteca necesita una función que cuente cuántos libros de una lista tienen más de cierta cantidad de páginas. Reordená los bloques de código para implementar correctamente la función `contar_libros_extensos(libros, minimo_paginas)`.

```python
def contar_libros_extensos(libros, minimo_paginas):
```

```python
    contador = 0
```

```python
    for paginas in libros:
```

```python
        if paginas > minimo_paginas:
```

```python
            contador = contador + 1
```

```python
    return contador
```

La función debe recibir una lista de números enteros, donde cada número representa la cantidad de páginas de un libro, y devolver cuántos libros superan el mínimo indicado.'''],['''Se quiere crear una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b>' de '<b>REPETICIÓN</b>' con un nivel de complejidad '<b>BÁSICO</b>' (Repetición simple, cantidad fija de iteraciones). La consigna debe estar diseñada para estudiantes de '<b>NIVEL UNIVERSITARIO</b>' y para ser resuelta en el lenguaje de programación '<b>PYTHON</b>'. Además, se puede suponer que los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''**Consigna**

Una función procesa las temperaturas registradas durante una semana y cuenta cuántos días tuvieron una temperatura mayor a 25°C.

```python
def contar_dias_calidos(temperaturas):
    contador = 0

    for temperatura in temperaturas:
        if temperatura > 25:
            contador = contador + 1

    return contador
```

¿Qué valor devuelve la siguiente llamada?

```python
contar_dias_calidos([22, 28, 31, 19, 25, 27, 24])
```

**Opciones**

A. `2`
B. `3` 
C. `4`
D. `5`

''']
]

# print(len(todosLosEstímulos))

sujetos = [
  "progreval01",
  "progreval02",
  "progreval03",
  "progreval04",
  "progreval05",
  "progreval06",
  "progreval07",
  "progreval08",
  "progreval09",
  "progreval10",
  "progreval11",
  "progreval12",
  "progreval13",
  "progreval14",
  "progreval15",
  "progreval16",
  "progreval17",
  "progreval18",
  "progreval19",
  "progreval20"
]

estímulosPorSujeto = [ # Índices de los estímulos asignados a cada sujeto
  # 1
  [28, 7, 56, 55, 57, 44, 1, 24, 31, 51, 47, 13, 0, 41, 50, 12, 52, 33, 23, 49],
  # 2
  [47, 13, 0, 41, 50, 12, 52, 33, 23, 49, 26, 45, 6, 16, 36, 30, 46, 21, 29, 32],
  # 3
  [26, 45, 6, 16, 36, 30, 46, 21, 29, 32, 59, 40, 4, 22, 35, 2, 11, 53, 18, 17],
  # 4
  [59, 40, 4, 22, 35, 2, 11, 53, 18, 17, 58, 54, 37, 34, 27, 20, 19, 14, 38, 42],
  # 5
  [58, 54, 37, 34, 27, 20, 19, 14, 38, 42, 10, 3, 25, 43, 8, 48, 9, 39, 5, 15],
  # 6
  [10, 3, 25, 43, 8, 48, 9, 39, 5, 15, 28, 7, 56, 55, 57, 44, 1, 24, 31, 51],
  # 7
  [51, 17, 40, 43, 19, 29, 8, 35, 2, 34, 36, 20, 56, 21, 32, 26, 23, 53, 55, 59],
  # 8
  [36, 20, 56, 21, 32, 26, 23, 53, 55, 59, 27, 15, 25, 0, 28, 52, 14, 22, 10, 13],
  # 9
  [27, 15, 25, 0, 28, 52, 14, 22, 10, 13, 16, 58, 9, 41, 49, 30, 4, 1, 12, 47],
  # 10
  [16, 58, 9, 41, 49, 30, 4, 1, 12, 47, 48, 6, 18, 54, 33, 38, 24, 45, 31, 50],
  # 11
  [48, 6, 18, 54, 33, 38, 24, 45, 31, 50, 7, 39, 44, 37, 5, 42, 46, 3, 11, 57],
  # 12
  [7, 39, 44, 37, 5, 42, 46, 3, 11, 57, 51, 17, 40, 43, 19, 29, 8, 35, 2, 34],
  # 13
  [20, 56, 23, 31, 0, 7, 15, 52, 17, 57, 59, 26, 30, 47, 24, 5, 32, 14, 37, 16],
  # 14
  [41, 9, 12, 35, 22, 58, 25, 53, 18, 11, 40, 4, 1, 33, 51, 34, 46, 43, 2, 42],
  # 15
  [29, 54, 45, 8, 3, 36, 39, 19, 55, 6, 49, 44, 48, 38, 21, 10, 28, 13, 27, 50],
  # 16
  [25, 7, 8, 54, 39, 6, 3, 50, 11, 42, 20, 58, 15, 22, 44, 16, 23, 28, 12, 4],
  # 17
  [30, 2, 38, 36, 41, 19, 10, 29, 52, 45, 59, 26, 14, 53, 33, 40, 57, 18, 49, 56],
  # 18
  [47, 31, 48, 5, 51, 9, 43, 1, 46, 24, 55, 32, 34, 21, 13, 35, 37, 17, 0, 27],
  # 19
  [46, 25, 3, 59, 23, 44, 11, 9, 21, 14, 33, 48, 34, 26, 28, 17, 41, 0, 43, 58],
  # 20
  [15, 12, 45, 52, 56, 53, 42, 7, 37, 4, 40, 35, 1, 5, 29, 24, 16, 55, 32, 27],
  # 21
  [6, 50, 51, 38, 10, 39, 20, 54, 2, 13, 47, 18, 49, 57, 36, 8, 19, 22, 31, 30]
]

def estímulosPara_(i):
  # i es un número entre 1 y la cantidad de sujetos
  return list(map(lambda x : todosLosEstímulos[x], estímulosPorSujeto[i-1]))

def pregunta_ParaEstímulo_(i, estímulo, j, n):
  pregunta = {
    # "titulo":títuloPregunta(i),
    "pregunta":textoPregunta(i)
  }
  if (i == 4):
    pregunta["tipo"] = "TEXTO_LIBRE"
  else:
    pregunta["tipo"] = "SLIDER"
    pregunta["rango"] = {"desde":1,"hasta":5,"paso":1}
  return pregunta

def cuestionarioPara_ConEstímulos_(sujeto, estímulos, i):
  páginas = [{
    "tipo":"SOLO_TEXTO",
    "titulo":títuloBienvenida,
    "pregunta":textoDeBienvenida
  }]
  n = len(estímulos)
  j = 1
  for estímulo in estímulos:
    preguntas = [
      pregunta_ParaEstímulo_(1, estímulo, j, n),
      pregunta_ParaEstímulo_(2, estímulo, j, n),
      pregunta_ParaEstímulo_(3, estímulo, j, n),
      pregunta_ParaEstímulo_(4, estímulo, j, n)
    ]
    páginas.append({
      "tipo":"MULTI",
      "titulo":títuloPágina(j, n),
      "contenido":textoEstímulo(estímulo),
      "preguntas": preguntas
    })
    j += 1
  páginas.append({
    "tipo":"SOLO_TEXTO",
    "titulo":títuloFinalización,
    "pregunta":textoDeFinalización
  })
  return {
    "tipo":"CUESTIONARIO",
    "id":"progreval_q" + str(i),
    "nombre":"Calificación de ejercicios de programación",
    "puedenReintentar":False,
    "puedenSaltearPreguntas":False,
    "puedenRetroceder":False,
    "preguntas":páginas,
    "visible":{"usuariosSi":sujeto}
  }

actividades = [
  cuestionarioPara_ConEstímulos_("estudiante_ficticio", todosLosEstímulos, 0)
]

i = 1
for sujeto in sujetos:
  actividades.append(cuestionarioPara_ConEstímulos_(sujeto, estímulosPara_(i), i))
  i += 1

CURSOS = {
  "progrevalpy":{
    "nombre":"-",
    "anio":"-",
    "edicion":"-",
    "descripcion":"-",
    "responsable":{
      "nombre":"-",
      "contacto":"-"
    },
    "institucion":"-",
    "actividades":actividades,
    "planilla":{
      "url":"1FAIpQLSeTVmH_U1RRpP2DCord_RZpNHzhfuCSKPSy6cxx_Zh9TC4j-g",
      "campos":{
        "usuario":"9867257",
        "actividad":"1165966175",
        "respuesta":"1778184894",
        "resultado":"1496208069",
        "duracion":"1460244707"
      }
    }
  }
}