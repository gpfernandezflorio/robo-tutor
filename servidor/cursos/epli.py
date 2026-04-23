títuloBienvenida = "Comenzando"
textoDeBienvenida = "En este experimento te vamos a mostrar distintas actividades diseñadas para evaluar conceptos de programación. Junto a cada consigna te explicamos cuál es el objetivo que guió el diseño de la misma (qué concepto se desea evaluar, para qué público objetivo está pensada, etc.). Te pedimos que califiques cada una de ellas en la escala del 1 al 5, según qué tan bien pensás que se ajusta a los objetivos planteados. Después de cada respuesta brindada vas a tener un campo de texto opcional para justificar tu calificación o agregar comentarios adicionales sobre el ejercicio propuesto.<br><br>Hacé clic en 'Siguiente' para continuar."
títuloEstímulo = "Calificá este ejercicio"
def textoEstímulo(estímulo):
  return [
    estímulo[0] + "<br><br>", # La presentación (Esta es una consigna ...)
    { 'md':estímulo[1], # La consigna en sí
      'css':"border: solid 5pt #ddd;background-color: #f8f8f8;padding: 12px;"
    },
    "<br><br>A continuación calificá el ejercicio propuesto en la escala del 1 al 5:"
  ]
títuloJustificación = "Justificá tu respuesta (opcional)"
textoJustificación = 'En el siguiente campo podés complementar tu respuesta justificando el puntaje que le asignaste al ejercicio o agregando cualquier comentario que te parezca pertinente.<br><br>Si no tenés nada que agregar, escribí "-".'
títuloFinalización = "Eso es todo..."
textoDeFinalización = "¡Muchas gracias por particiar!"

todosLosEstímulos = [
['''Esta es una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. ''','''## Evaluación de Programación: Dominio "El Robot Recolector"

En un tablero que representa un depósito, un robot debe decidir si puede realizar una tarea de recolección de materiales. El robot solo puede activar su brazo mecánico si se cumplen **todas** las siguientes condiciones simultáneamente:
1. El robot tiene al menos una batería (representada por bolitas de color **Verde**).
2. Hay material para recoger en la celda actual (representado por bolitas de color **Rojo**).
3. No hay obstáculos de seguridad en la celda (representados por bolitas de color **Negro**).

### Consigna
Completa el siguiente bloque de código en **Gobstones** definiendo la expresión lógica necesaria para que la función `puedeRecogerMaterial()` devuelva `Verdadero` únicamente cuando se cumplen las tres condiciones mencionadas.

```gobstones
function puedeRecogerMaterial() {
    /*
        Propósito: Indica si el robot está en condiciones de recolectar.
        Tipo: Booleano.
        Precondición: Ninguna.
    */
    return ( __________ )
}
```'''],['''Esta es una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Evaluación de Programación: Expresiones Lógicas

### Contexto: El Escenario del Robot Recolector
En un tablero de Gobstones, un robot se encuentra en una parcela (celda) que puede contener diferentes elementos: **Bolitas Verdes** (que representan plantas sanas), **Bolitas Rojas** (que representan frutos maduros) y **Bolitas Negras** (que representan plagas).

Para optimizar la cosecha, el robot debe decidir si una parcela es considerada **"Apta para Cosecha Premium"**. 

### Consigna
Escribí una función en lenguaje **Gobstones** que determine si la celda actual cumple con las condiciones para la cosecha premium. Una parcela se considera apta únicamente si se cumplen simultáneamente los siguientes requisitos:
1. La cantidad de frutos maduros es estrictamente mayor a la cantidad de plantas sanas.
2. Hay al menos una planta sana en la parcela.
3. La parcela no tiene plagas.

La función debe devolver un valor booleano que indique si la parcela es apta o no, sin modificar el contenido del tablero.
'''],['''Esta es una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Consigna de Evaluación: El Robot Clasificador de Celdas

**Dominio:** Estás programando el sensor de un robot encargado de inspeccionar un tablero de materiales. El robot debe decidir si una celda cumple con los estándares de seguridad para ser procesada.

**Problema:**
Se necesita definir una función que determine si una celda es **"Apta para Procesamiento"**. Una celda se considera apta únicamente si cumple con **todas** las siguientes condiciones de manera simultánea:
1.  Contiene al menos una bolita de color **Verde**.
2.  No es una celda de borde (es decir, el robot puede moverse en las cuatro direcciones: Norte, Sur, Este y Oeste).
3.  La cantidad total de bolitas de color **Rojo** es exactamente igual a 3, **o bien**, la celda está vacía de bolitas de color **Azul**.

**Instrucciones:**
Reordena los siguientes bloques de código para definir la función `esAptaParaProcesar()` de manera correcta en el lenguaje Gobstones. **Nota:** No todos los bloques deben ser utilizados necesariamente, pero debes seleccionar aquellos que construyan la lógica pedida.

### Bloques disponibles (Desordenados)

* `function esAptaParaProcesar() {`
* `hayBolitas(Verde) && puedeMover(Norte) && puedeMover(Sur) && puedeMover(Este) && puedeMover(Oeste)`
* `return (`
* `nroBolitas(Rojo) == 3 || not hayBolitas(Azul)`
* `&&`
* `)`
* `}`
* `if (hayBolitas(Verde)) {`
'''],['''Esta es una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. ''','''### Contexto del Problema: El Escáner de Minerales
En una excavación minera controlada por un cabezal robótico (el cabezal de Gobstones), se ha definido un protocolo de seguridad para la extracción de cristales. El robot se encuentra en una celda que puede contener bolitas de tres colores: **Verdes** (que representan esmeraldas), **Rojas** (que representan sensores térmicos) y **Azules** (que representan suministros de agua). 

Para que la extracción sea segura en la celda actual, se deben cumplir **simultáneamente** las siguientes condiciones:
1. Debe haber al menos una esmeralda (bolita Verde).
2. No debe haber más de dos sensores térmicos (bolitas Rojas).
3. No debe ser cierto que falten suministros de agua (bolitas Azules).

### Consigna
Dada la configuración actual del tablero, ¿cuál de las siguientes expresiones lógicas de Gobstones evalúa correctamente si la celda es **segura para la extracción** siguiendo el protocolo mencionado?

**Opciones:**

A) `hayBolitas(Verde) && nroBolitas(Rojo) <= 2 && hayBolitas(Azul)`

B) `hayBolitas(Verde) || nroBolitas(Rojo) < 2 || hayBolitas(Azul)`

C) `nroBolitas(Verde) >= 1 && (nroBolitas(Rojo) > 2 || not hayBolitas(Azul))`

D) `hayBolitas(Verde) && nroBolitas(Rojo) < 3 && not hayBolitas(Azul)`
'''],['''Esta es una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''## Evaluación de Programación: El Controlador de Almacén

**Dominio:** Un robot encargado de organizar suministros en un depósito. El robot debe colocar una "Caja de Seguridad" (una bolita de color Verde) solo si se cumplen estrictamente las condiciones de seguridad del estante.

---

### Consigna

Un programador junior ha desarrollado la función `puedeColocarCajaSeguridad()`, la cual debería informar si el robot está habilitado para colocar una bolita Verde en la celda actual. Según el manual de operaciones, las condiciones para colocar la caja son las siguientes:

> "Se debe colocar una caja de seguridad si, y solo si, en la posición actual **hay al menos una pieza de repuesto (bolita Roja)** y, al mismo tiempo, **no hay herramientas pesadas (bolitas Negras) ni productos frágiles (bolitas Azules)**."

Sin embargo, el robot está teniendo comportamientos erráticos: coloca cajas donde no debe o se salta estantes válidos. A continuación, se presenta el código que contiene el error:

```gobstones
function puedeColocarCajaSeguridad() {
    /* PROPÓSITO: Indica si se cumplen las condiciones para colocar 
       una caja de seguridad en la celda actual.
       RETORNA: Booleano.
    */
    return (hayBolitas(Rojo) || not hayBolitas(Negro) && not hayBolitas(Azul));
}
```

**Tu tarea:**
Identificá la línea o sección del código donde se encuentra el error de lógica, explicá por qué esa expresión no cumple con el manual de operaciones y escribí la expresión lógica corregida.
'''],['''Esta es una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. ''','''## Consigna de Evaluación

En el contexto de un tablero de **Gobstones**, donde el cabezal se encuentra en una celda que contiene bolitas de diversos colores, se requiere definir una condición específica para un mecanismo de control.

Completá la siguiente expresión para que la misma sea verdadera **únicamente** cuando se cumplan simultáneamente las siguientes condiciones:
1. La celda actual **no** tiene bolitas de color Negro.
2. La cantidad de bolitas de color Azul es **exactamente igual** a la cantidad de bolitas de color Rojo.

```gobstones
_________ (nroBolitas(Negro) == 0) _________ (nroBolitas(Azul) == nroBolitas(Rojo))
```'''],['''Esta es una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Consigna de Evaluación

**Contexto del Dominio: Sistema de Control de Almacén**

En una cuadrícula que representa un depósito de suministros, cada celda puede contener bolitas de diferentes colores que representan recursos:
* **Rojas**: Sensores de temperatura.
* **Verdes**: Módulos de energía.
* **Azules**: Unidades de procesamiento.

Se requiere establecer una condición para un sistema automatizado de inventario. El sistema debe validar si la celda actual se encuentra en un **estado crítico de desbalance**. 

Un estante se considera en "desbalance crítico" cuando ocurre alguna de las siguientes situaciones:
1. La cantidad de sensores de temperatura es estrictamente mayor a la suma de los otros dos componentes (energía y procesamiento).
2. No hay módulos de energía, pero sí hay al menos una unidad de procesamiento presente.

**Tarea:**
Definir la expresión lógica en lenguaje **Gobstones** que permita determinar si la ubicación actual cumple con la condición de **estado crítico de desbalance**. Para obtener las cantidades necesarias, disponés de las siguientes funciones totales (puras) ya integradas al lenguaje:
* `nroBolitas(color)`: Retorna la cantidad de bolitas del color indicado en la celda actual.
* `hayBolitas(color)`: Retorna un valor booleano indicando si existe al menos una bolita del color indicado.
'''],['''Esta es una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''### Consigna de Evaluación

**Dominio:** Sistema de Control de Calidad de Cultivos en un Tablero Espacial.

En el lenguaje **Gobstones**, el cabezal se encuentra sobre una celda que representa una parcela de cultivo. Para que una parcela sea considerada "Apta para Cosecha Especial", debe cumplir con las siguientes condiciones simultáneamente:
1.  Debe haber presencia de bolitas de color **Azul** (que representan minerales).
2.  La cantidad de bolitas de color **Rojo** (sensores de calor) sumada a las de color **Verde** (sensores de humedad) debe ser exactamente igual a **15**.

**Tarea:**
A continuación, se presenta una lista de fragmentos de código desordenados. Tu objetivo es seleccionar y ordenar los bloques necesarios para construir la **expresión lógica** que determine si la parcela actual es "Apta para Cosecha Especial". 

*Nota: Algunos bloques son distractores y no deben ser utilizados.*

1. `nroBolitas(Azul) > 0`
2. `nroBolitas(Rojo) + nroBolitas(Verde)`
3. `== 15`
4. `&&`
5. `nroBolitas(Azul) == 0`
6. `||`
7. `nroBolitas(Rojo) * nroBolitas(Verde)`
8. `> 15`
'''],['''Esta es una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. ''','''### Consigna de Evaluación

**Dominio:** Gestión de inventario de recursos en un tablero de minería espacial.

Dada la siguiente expresión lógica escrita en Gobstones, la cual se utiliza para determinar si un robot recolector debe entrar en modo de ahorro de energía:

`not (nroBolitas(Verde) >= 3) && (nroBolitas(Rojo) == nroBolitas(Azul))`

¿Cuál de las siguientes configuraciones de bolitas en la celda actual hace que la expresión sea **verdadera**?

**Opciones:**

1. 2 bolitas verdes, 4 bolitas rojas y 5 bolitas azules.
2. 3 bolitas verdes, 2 bolitas rojas y 2 bolitas azules.
3. 2 bolitas verdes, 3 bolitas rojas y 3 bolitas azules.
4. 4 bolitas verdes, 1 bolita roja y 1 bolita azul.

***
'''],['''Esta es una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''## Consigna

El equipo de mantenimiento de una aplicación de logística para depósitos está teniendo problemas con el sistema de control de stock automatizado. El objetivo del sistema es alertar cuando una ubicación del depósito necesita reposición inmediata. Según el manual de procedimientos, una ubicación debe marcarse para **"Reposición"** únicamente cuando **no tiene mercadería** (está vacía) **y** además **no tiene un pedido de reabastecimiento en curso**.

Sin embargo, los operarios informan que el sistema está emitiendo alertas de reposición incluso cuando la ubicación todavía tiene cajas, o peor aún, no emite la alerta cuando la ubicación está vacía pero ya se pidió la mercadería.

Se ha identificado que el error reside específicamente en la función que analiza el estado de la celda actual en el tablero de control. Tu tarea es identificar el error lógico en la siguiente pieza de código y explicar por qué impide el funcionamiento correcto del sistema.

```gobstones
function necesitaReposición() {
    /* PROPÓSITO: Indica si la ubicación actual requiere un pedido de reposición.
       PRECONDICIÓN: Ninguna.
       RETORNA: Booleano.
    */
    return (not hayCajas() || tienePedidoEnCurso())
}

function hayCajas() {
    // Retorna verdadero si hay bolitas de color Verde (representan cajas)
    return (hayBolitas(Verde))
}

function tienePedidoEnCurso() {
    // Retorna verdadero si hay bolitas de color Rojo (representan pedido realizado)
    return (hayBolitas(Rojo))
}
```
'''],['''Esta es una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. ''','''### Consigna: El Robot Sanitario

**Contexto:**
Un robot debe limpiar una celda solo si se cumplen ciertas condiciones de seguridad y necesidad. El robot detecta **Bolinhas Verdes** como señal de "Celda Sucia" y **Bolinhas Rojas** como "Obstáculo Crítico".

**Objetivo:**
Completar las expresiones lógicas en el código de Gobstones para que la función `puedeLimpiar()` retorne `Verdadeiro` únicamente cuando:
1. Hay al menos una bolinha verde (está sucio).
2. **Y** no hay bolinhas rojas (no hay obstáculos).
3. **Y** el robot tiene espacio para moverse al Norte después de limpiar (no está en el borde Norte).

---

```gobstones
function puedeLimpiar() {
    /* CONSIGNA: Completar los espacios vacíos con la expresión lógica 
       que combine las tres condiciones mencionadas.
    */
    return ( __________ && __________ && __________ )
}

/* Ayuda: 
   - Para ver si hay bolinhas: hayBolitas(Color)
   - Para ver si puede moverse: puedeMover(Direccion)
   - Operadores: && (y), || (o), ! (no)
*/
```
'''],['''Esta es una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Evaluación: Expresiones Lógicas en Gobstones

### Contexto: El Sistema de Riego Automatizado
En una plantación automatizada, el cabezal representa un sensor que debe decidir si activar o no los aspersores basándose en las condiciones del suelo. El suelo se representa con bolitas de colores:
* **Bolitas Verdes:** Representan el nivel de humedad.
* **Bolitas Rojas:** Representan la temperatura del suelo.
* **Bolitas Negras:** Representan la presencia de plagas.

---

### La Consigna

Diseñá e implementá una **función** en Gobstones llamada `debeActivarseRiego()`. Esta función debe retornar un valor de tipo booleano que determine si el riego debe comenzar. 

Para que la función retorne `Verdadero`, deben cumplirse **simultáneamente** las siguientes condiciones lógicas basadas en la celda actual:

1.  **Humedad Crítica:** El nivel de humedad (bolitas verdes) debe ser menor a 3.
2.  **Temperatura de Riesgo:** La temperatura (bolitas rojas) debe ser estrictamente mayor al doble del nivel de humedad presente.
3.  **Seguridad Sanitaria:** **No** debe haber presencia de plagas (bolitas negras). Se considera que hay plaga si hay al menos una bolita negra.

**Requerimiento Técnico:** No podés utilizar estructuras de control condicional (`if` / `si`) para retornar los valores. Debes definir la lógica de la función puramente a través de una **expresión lógica compuesta**, utilizando operadores booleanos y de comparación.

'''],['''Esta es una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>DEFINICIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e implementación de expresiones lógicas.''','''## Consigna de Examen: Problema de Parsons

**Dominio:** Un robot recolector en un jardín cuadriculado.
**Contexto:** El robot debe identificar si una celda es **"Apta para Cultivo"**. Una celda se considera apta si se cumplen las siguientes condiciones simultáneamente:
1.  Hay al menos una semilla (bolita de color **Verde**).
2.  **No** hay maleza (bolita de color **Negro**).
3.  El robot tiene espacio para trabajar, es decir, existe una celda lindante hacia el **Norte**.

### Tarea
Ordená los siguientes bloques de código para definir la función `esCeldaAptaParaCultivo()`. Tené en cuenta que la expresión debe ser eficiente y seguir las reglas de Gobstones.

---

### Bloques Desordenados (Parsons Puzzle)

> **Nota:** Algunos bloques pueden sobrar o estar diseñados para evaluar errores comunes de lógica.

* `&& puedeMover(Norte)`
* `return (`
* `nroBolitas(Verde) >= 1`
* `function esCeldaAptaParaCultivo() {`
* `&& not hayBolitas(Negro)`
* `}`
* `nroBolitas(Verde) == 0`
'''],['''Esta es una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>EVALUACIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. ''','''## Evaluación de Expresiones Lógicas en Gobstones

### Contexto del Dominio: El Almacén de Suministros
En un tablero que representa un almacén, las bolitas de colores simbolizan diferentes tipos de suministros:
* **Azules:** Cantidad de packs de agua.
* **Negras:** Cantidad de raciones de comida.
* **Rojas:** Alertas de seguridad (si hay más de una, el sector es peligroso).

### Consigna
Se desea determinar si un sector (la celda actual) cumple con las condiciones para ser considerado un **"Sector de Distribución Prioritaria"**. Un sector recibe esta categoría solo si:
1.  Tiene **más de 3** packs de agua **o** **más de 2** raciones de comida.
2.  **No** debe ser un sector peligroso (es decir, no puede tener más de una bolita roja).
3.  Debe haber al menos una ración de comida presente.

Dada la siguiente expresión lógica en Gobstones, ¿cuál es la opción que evalúa correctamente si la celda actual es un **Sector de Distribución Prioritaria**?

---

### Opciones

**A)**
```gobstones
(nroBolitas(Azul) > 3 || nroBolitas(Negro) > 2) && 
not (nroBolitas(Rojo) > 1) && 
hayBolitas(Negro)
```

**B)**
```gobstones
(nroBolitas(Azul) > 3 && nroBolitas(Negro) > 2) || 
nroBolitas(Rojo) <= 1 || 
nroBolitas(Negro) >= 1
```

**C)**
```gobstones
nroBolitas(Azul) > 3 || nroBolitas(Negro) > 2 && 
nroBolitas(Rojo) < 1 && 
hayBolitas(Negro)
```

**D)**
```gobstones
not (nroBolitas(Azul) <= 3 && nroBolitas(Negro) <= 2) && 
nroBolitas(Rojo) > 1 && 
hayBolitas(Negro)
```
'''],['''Esta es una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b> de <b>EXPRESIÓN LÓGICA</b>' con un nivel de complejidad <b>INTERMEDIO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Seguimiento de funciones y directivas de selección.''','''### Contexto de Dominio: El Sistema de Riego Automatizado
En una plantación de hortalizas, un cabezal robótico (el cabezal de Gobstones) debe decidir si activar los aspersores. La regla de negocio indica que un sector debe regarse **solo si** se cumplen estas condiciones simultáneamente:
1.  Hay **Humedad Baja** (representado por la ausencia de bolitas Azules).
2.  **No hay Alerta de Helada** (representado por menos de 3 bolitas Rojas).
3.  Es **Horario de Riego** (representado por la presencia de al menos una bolita Verde).

---

### Consigna de Evaluación

**Título:** Depuración del Sensor de Riego Crítico.

**Situación:**
Un programador novato escribió la siguiente función para determinar si el robot debe iniciar el riego. Sin embargo, se ha detectado que el robot está regando en momentos inapropiados, lo que desperdicia agua y pone en riesgo los cultivos durante las heladas.

```gobstones
function debeRegar() {
  /* PROPÓSITO: Indica si el sector actual cumple las condiciones de riego.
     PRECONDICIÓN: Ninguna.
  */
  return (not hayBolitas(Azul) || nroBolitas(Rojo) <= 3 && hayBolitas(Verde))
}
```

**Tu Tarea (Señalamiento de Ocurrencia):**
Analizá la expresión lógica dentro del `return`. Se afirma que la expresión contiene errores de lógica y de precedencia que provocan "falsos positivos" (el robot riega cuando no debería).

1.  **Identificá la ocurrencia del error de precedencia:** Explicá qué parte de la expresión se evalúa primero debido a la falta de paréntesis y cómo esto altera el resultado final frente a los requerimientos del dominio.
2.  **Identificá el error de borde:** Señalá específicamente qué sucede cuando hay exactamente 3 bolitas Rojas y por qué esto contradice la regla de "Alerta de Helada".
3.  **Proponé la corrección:** Escribí la expresión lógica corregida que garantice que las tres condiciones se evalúen como un conjunto estricto.
'''],['''Esta es una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación: El recolector de semillas

En el tablero de **Gobstones**, un robot debe recorrer una fila de celdas para recolectar semillas (representadas por bolitas de color **Verde**). Se ha definido una función `haySemilla()` que indica si hay bolitas verdes en la celda actual, y un procedimiento `RecogerSemilla()` que se encarga de recolectarlas.

Sin embargo, el siguiente programa, diseñado para limpiar una fila de 5 celdas de ancho (comenzando desde el borde Oeste), contiene errores que impiden que el robot cumpla su objetivo de manera eficiente o correcta.

**Tu tarea:**
Identifica y señala las líneas de código donde se producen errores. Explica por qué ese fragmento impide el funcionamiento esperado y describe qué sucede al intentar ejecutarlo.

```gobstones
program {
  IrAlBorde(Oeste)
  LimpiarFilaDeSemillas()
}

procedure LimpiarFilaDeSemillas() {
  repeat (4) {
    if (haySemilla()) {
        RecogerSemilla()
    }
    Mover(Este)
  }
}
```
'''],['''Esta es una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación: El Robot Cosechador

En un tablero que representa un huerto, se ha definido una función llamada `hayFruta()` que indica si existe un elemento en la celda actual, y un procedimiento `RecogerFruta()` que se encarga de recolectar un elemento del suelo.

Tu tarea es completar el siguiente procedimiento para que un robot cosechador recoja exactamente **5 ejemplares** de fruta de la celda donde se encuentra posicionado. No debe quedar fruta sin recoger si hay exactamente 5, ni el robot debe intentar realizar acciones de más.

Completa los espacios en blanco para que el código cumpla su función:

```gobstones
procedure CosecharCincoFrutas() {
    /* Propósito: Recoger 5 frutas de la posición actual.
       Precondición: Debe haber al menos 5 frutas en la celda actual.
    */
    repeat ( __________ ) {
        __________
    }
}
```
'''],['''Esta es una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación

**Dominio:** Sistema de Carga de Contenedores Marítimos.
**Contexto:** En un puerto, se utiliza un brazo mecánico para organizar filas de contenedores en el muelle. Cada contenedor está representado por una bolita de color **Azul**. El brazo mecánico se encuentra actualmente en una celda que representa el inicio de una plataforma de carga.

**Tarea:**
Escribí un procedimiento llamado `CargarFilaDeContenedores()` que se encargue de colocar exactamente 5 contenedores en la celda actual. Para realizar esta tarea, ya contás con un procedimiento predefinido llamado `PonerContenedor()`, el cual se encarga de realizar la acción física de colocar una bolita de color Azul. 
'''],['''Esta es una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación

**Contexto: El Robot Pintor**
En un tablero de Gobstones, un robot debe pintar una línea horizontal de celdas de color **Verde**. El robot comienza en una celda cualquiera y debe pintar la celda actual y las **3 celdas siguientes** hacia el **Este**.

**Tu tarea:**
Ordena los siguientes bloques de código para construir el procedimiento `PintarLineaVerde()`. Ten en cuenta que debes utilizar una estructura que permita repetir la acción de manera eficiente, aprovechando que ya conoces la cantidad exacta de veces que el robot debe avanzar y pintar.

**Bloques a ordenar (Problema de Parsons):**

* `Poner(Verde)`
* `Mover(Este)`
* `}`
* `repeat (3) {`
* `procedure PintarLineaVerde() {`
* `}`

'''],['''Esta es una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''### Consigna de Evaluación

**Contexto: El Robot Cosechador**
Un robot se encuentra en una parcela de un campo representada por un tablero. En la celda actual del robot, hay una cantidad de semillas representadas por bolitas de color **Rojo**. Se ha definido el siguiente procedimiento para que el robot recoja las semillas una por una y las procese:

```gobstones
procedure RecolectarYProcesar() {
    repeat (numeroDeBolitas(Rojo)) {
        Sacar(Rojo)
        ProcesarSemilla()
    }
}

procedure ProcesarSemilla() {
    Poner(Verde) -- Representa una semilla procesada
}
```

Si al iniciar la ejecución del procedimiento `RecolectarYProcesar`, la celda actual contiene **3 bolitas Rojas** y **0 bolitas Verdes**, ¿cuál será el estado final de dicha celda tras finalizar la ejecución?

* A) La celda tendrá 3 bolitas Rojas y 3 bolitas Verdes.
* B) La celda tendrá 0 bolitas Rojas y 1 bolita Verde.
* C) La celda tendrá 0 bolitas Rojas y 3 bolitas Verdes.
* D) La celda tendrá 3 bolitas Rojas y 0 bolitas Verdes.

'''],['''Esta es una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Evaluación

**Dominio:** Sistema de balizamiento de pista de aterrizaje.
**Contexto:** Se requiere señalizar una sección de la pista colocando una baliza (representada por una bolita de color **Verde**) en cada celda, cubriendo un trayecto lineal de exactamente **4 celdas** hacia el Norte, incluyendo la celda donde se inicia el procedimiento.

Se presenta el siguiente código desarrollado para cumplir con dicha tarea, pero el equipo de control de calidad ha detectado que el programa no se comporta según lo esperado.

```gobstones
procedure BalizarTramoNorte() {
    /* PROPÓSITO: Colocar una baliza verde en cada celda de un tramo 
       de 4 celdas hacia el Norte, iniciando en la celda actual.
       PRECONDICIÓN: Hay al menos 3 celdas al Norte de la celda actual.
    */
    repeat (3) {
        Poner(Verde)
        Mover(Norte)
    }
}
```

**Tarea:** Identifique cuál de las siguientes observaciones describe correctamente la falla en la **Directiva de Repetición** o su bloque asociado para que el programa cumpla con su propósito:

A) El cuerpo del `repeat` tiene las instrucciones invertidas; primero debe moverse y luego poner la bolita.
B) La cantidad de iteraciones en el `repeat` es insuficiente para cubrir las 4 celdas del tramo.
C) El programa termina su ejecución sin colocar la bolita verde en la última celda del tramo.
D) La precondición es incorrecta y debería exigir 4 celdas al Norte en lugar de 3.

'''],['''Esta es una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Consigna

En el tablero de Gobstones, un robot encargado de mantenimiento debe delimitar una zona de seguridad. Para ello, se requiere que el robot coloque una línea de **12 bolitas azules** en la celda actual. 

Sin embargo, debido a una restricción en los sensores de movimiento, el robot solo puede ejecutar comandos de colocación en grupos de a 3 unidades por cada movimiento del brazo mecánico.

Completá el siguiente procedimiento para que cumpla con su objetivo de dejar exactamente 12 bolitas azules en la ubicación actual:

```gobstones
procedure DelimitarZonaSeguridad() {
    repeat ________ {
        ________(Azul)
        Poner(Azul)
        Poner(Azul)
    }
}
```
'''],['''Esta es una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna

En el lenguaje **Gobstones**, el tablero representa un territorio donde un robot recolector debe realizar tareas de mantenimiento. En esta ocasión, se requiere automatizar una tarea de limpieza en una columna del tablero.

Escribí un procedimiento llamado `LimpiarLíneaDeCincoAlEste()` que permita al cabezal recoger exactamente una bolita de color **Verde** de la celda actual y de cada una de las siguientes 4 celdas hacia el **Este**. 
'''],['''Esta es una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna

**Dominio:** El Tablero Mágico de Piedras.

En el mundo de Gobstones, un aprendiz necesita automatizar la creación de una "Línea de Seguridad". Para ello, debe definir un procedimiento que coloque una hilera de exactamente 5 bolitas de color Azul, comenzando desde la celda actual y moviéndose hacia el Este tras colocar cada bolita.

A continuación, se presentan una serie de bloques de código desordenados. Tu tarea es seleccionar y ordenar los bloques necesarios para construir la solución correcta. **Atención:** Algunos bloques son distractores y no deben utilizarse.

1. `  Mover(Este)`
2. `procedure ConstruirLineaDeSeguridad() {`
3. `repeat (5) {`
4. `  Poner(Azul)`
5. `  Poner(Rojo)`
6. `}`
7. `repeat (4) {`
8. `  Mover(Sur)`

'''],['''Esta es una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''## Consigna

Se dispone de un tablero con un cabezal inicialmente posicionado en una celda cualquiera (lejos de los bordes). El dominio del problema consiste en el desplazamiento de un robot recolector que debe marcar un camino específico.

¿Cuál es la posición final del cabezal, respecto de la posición inicial, tras ejecutar el siguiente procedimiento en **Gobstones**?

```gobstones
procedure MarcarRecorrido() {
    Mover(Norte)
    repeat (3) {
        Mover(Este)
        Mover(Sur)
    }
    Mover(Norte)
    Mover(Oeste)
}
```

**Opciones:**

1.  Dos celdas al Este de la posición inicial.
2.  Tres celdas al Este de la posición inicial.
3.  Dos celdas al Este y una al Norte de la posición inicial.
4.  En la misma posición inicial.
'''],['''Esta es una consigna del tipo '<b>SEÑALAMIENTO DE OCURRENCIA</b>' para evaluar '<b>DEPURACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Contexto del Problema
En el simulador de **Jardinería Digital**, un robot debe plantar una fila de flores (representadas por bolitas rojas) en un cantero rectangular. Para optimizar el código, se ha implementado una función llamada `cantidadDeEspaciosARecorrer()` que calcula cuántos casilleros debe avanzar el robot según el tamaño del cantero actual.

Sin embargo, el equipo de programación ha reportado que el siguiente procedimiento **no funciona correctamente**: el robot se detiene antes de terminar la fila o intenta moverse fuera del tablero, causando un error de ejecución.

### Código a Evaluar

```gobstones
procedure PlantarFilaDeFlores() {
    /* PROPÓSITO: Plantar una flor en cada celda de la fila actual hacia el Este.
       PRECONDICIÓN: Hay al menos tantas celdas hacia el Este como indica 
                     la función cantidadDeEspaciosARecorrer().
    */
    repeat (cantidadDeEspaciosARecorrer()) {
        Poner(Rojo)
        Mover(Este)
    }
}
```

### Consigna

Se sabe que el procedimiento anterior tiene un **error de ocurrencia** respecto a su propósito: la última celda de la fila queda vacía o el robot intenta moverse un lugar de más.

1.  **Identifique el error:** Explique por qué la estructura `repeat` actual no cumple con el objetivo de dejar una flor en cada celda del camino definido.
2.  **Señalamiento:** Si `cantidadDeEspaciosARecorrer()` devuelve el valor **5**, ¿cuántas flores se ponen y cuántos movimientos se realizan?
3.  **Corrección:** Proponga una modificación lógica (utilizando el concepto de "procesar y mover" o ajustando el límite) para que el procedimiento sea correcto.

'''],['''Esta es una consigna del tipo '<b>COMPLECIÓN DE ESPACIOS VACÍOS</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''### Consigna
Dada la siguiente solución incompleta, completa los espacios vacíos para que el procedimiento `DibujarLadoDelLote()` coloque una bolita negra en la celda actual y en las 3 celdas siguientes hacia el **Este**, dejando el cabezal en la última celda donde colocó una bolita. 

Debes utilizar una **directiva de repetición** fija y aprovechar la función `pasosRestantes()` (ya definida) que devuelve la cantidad de veces que el robot debe moverse.

---

### Código a completar

```gobstones
/* Propósito: Dibuja una línea de 4 bolitas negras hacia el Este.
   Precondición: Hay al menos 3 celdas al Este de la actual.
*/
procedure DibujarLadoDelLote() {
    repeat ( __________ ) { 
        Poner(Negro)
        __________ (Este)
    }
    Poner(Negro)
}

/* Función de apoyo disponible */
function pasosRestantes() {
    return (3)
}
```
'''],['''Esta es una consigna del tipo '<b>RESPUESTA ABIERTA</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Programación: El Huerto de Naranjas

**Contexto:**
En el tablero de Gobstones, representamos un huerto. Cada celda puede contener una cantidad variable de **bolitas naranjas**, que simbolizan las naranjas caídas de los árboles. El cabezal se encuentra actualmente sobre un árbol que ha tenido una cosecha excepcional.

**El Desafío:**
Debés implementar un procedimiento llamado `CosecharNaranjas(cantidadACosechar)` que se encargue de recolectar una cantidad específica de naranjas en la celda actual. 

Para lograrlo, se deben cumplir las siguientes condiciones:
1.  **Uso de Repetición:** Utilizar la estructura de control `repeat` para realizar la recolección.
2.  **Modularización:** Es obligatorio definir y utilizar una **función** auxiliar llamada `hayNaranjasSuficientes(cantidad)`, que devuelva un valor booleano indicando si en la celda actual hay al menos la cantidad de bolitas naranjas que se desean cosechar.
3.  **Acción:** Si hay suficientes, el cabezal debe sacar la cantidad indicada de bolitas naranjas. 

---

### Tareas a realizar:

1.  **Definir la función** `hayNaranjasSuficientes(cantidad)`:
    * Debe retornar `True` si el número de bolitas de color **Naranja** en la celda actual es mayor o igual al parámetro `cantidad`.
2.  **Implementar el procedimiento** `CosecharNaranjas(cantidadACosechar)`:
    * Debe invocar a la función anterior dentro de una estructura condicional.
    * Si el resultado es afirmativo, debe ejecutar un ciclo `repeat` para sacar las bolitas una por una.

> **Nota para el estudiante:** Recordá que en Gobstones no podés sacar bolitas que no existen. La validación previa con la función es fundamental para evitar errores de ejecución.

---

### Ejemplo de uso esperado:

Si en la celda actual hay **5 bolitas naranjas** y se invoca a `CosecharNaranjas(3)`:
* La función `hayNaranjasSuficientes(3)` retornará `True`.
* El bloque `repeat(3)` se ejecutará, sacando 3 bolitas.
* Resultado final: Quedan **2 bolitas naranjas** en la celda.
'''],['''Esta es una consigna del tipo '<b>PARSONS</b>' para evaluar '<b>IMPLEMENTACIÓN</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones.''','''## Consigna de Programación: El Camino de Cuentas

### Contexto del Dominio
En el tablero de Gobstones, un robot recolector debe automatizar la creación de una "línea de seguridad" en una zona de excavación. El objetivo es colocar una hilera de **Cuentas Verdes** de un largo específico, pero para asegurar la visibilidad, cada celda debe tener exactamente **3 cuentas**.

### El Desafío
Tu tarea es implementar el procedimiento `PonerLineaDeSeguridad(cantidadDeCeldas)`, que debe colocar 3 cuentas verdes en la celda actual y luego moverse hacia el **Este**, repitiendo esta acción tantas veces como indique el parámetro. 

**Restricción importante:** Para colocar las 3 cuentas, **debés invocar** la función (ya definida) `Poner3Verdes()`.

---

### Bloques de Código (Desordenados)
Para resolver el problema, debés seleccionar y ordenar los siguientes bloques. **¡Cuidado!** Hay bloques que sobran o tienen errores de lógica (distractores).

```gobstones
// Bloque A
procedure PonerLineaDeSeguridad(cantidadDeCeldas) {

// Bloque B
  repeat (cantidadDeCeldas) {

// Bloque C
    Poner3Verdes()
    Mover(Este)

// Bloque D
  }

// Bloque E
}

// Bloque F (Distractor: Error de lógica)
  repeat (3) {
    PonerVerde()
  }

// Bloque G (Distractor: Parámetro incorrecto)
  repeat (cantidadDeCeldas + 1) {
```
'''],['''Esta es una consigna del tipo '<b>OPCIÓN MÚLTIPLE CON RESPUESTA ÚNICA</b>' para evaluar '<b>SEGUIMIENTO</b> de <b>REPETICIÓN</b>' con un nivel de complejidad <b>BÁSICO</b>. La consigna generada está diseñada para estudiantes de <b>NIVEL UNIVERSITARIO</b> y para ser resuelta en el lenguaje de programación <b>GOBSTONES</b>. Además, los estudiantes cuentan con los siguientes conocimientos previos: Definición e Implementación de funciones. ''','''### Consigna
En un tablero que representa un estante de un depósito, el cabezal se encuentra sobre una celda que contiene una cantidad arbitraria de bolitas **Negras** (que representan cajas vacías). Se desea implementar un procedimiento que transforme todas esas cajas vacías en "cajas con productos", representadas por bolitas **Verdes**.

Para ello, contamos con la siguiente función ya definida:

```gobstones
function cantidadDeCajasEnCelda() {
    /* PROPÓSITO: Indica la cantidad de bolitas Negras en la celda actual.
       TIPO: Número
    */
    return (nroBolitas(Negro))
}
```

¿Cuál de los siguientes fragmentos de código completa correctamente el propósito de **reemplazar cada caja negra por una verde** en la celda actual, utilizando la estructura de repetición adecuada?

---

### Opciones

**A)**
```gobstones
procedure CargarProductosEnCelda() {
    repeat (cantidadDeCajasEnCelda()) {
        Sacar(Negro)
        Poner(Verde)
    }
}
```

**B)**
```gobstones
procedure CargarProductosEnCelda() {
    repeat (nroBolitas(Verde)) {
        Sacar(Negro)
        Poner(Verde)
    }
}
```

**C)**
```gobstones
procedure CargarProductosEnCelda() {
    if (hayBolitas(Negro)) {
        Sacar(Negro)
        Poner(Verde)
    }
}
```

**D)**
```gobstones
procedure CargarProductosEnCelda() {
    repeat (cantidadDeCajasEnCelda) {
        Poner(Verde)
    }
}
```
''']
]

sujetos = [
  "alanrodas@gmail.com",                # 1
  "maurosalina85@gmail.com",            # 2
  "Federico.Cherchyk@gmail.com",        # 3
  "alan.nicolas.rodriguez@gmail.com",   # 4
  "cuococarlos@gmail.com",              # 5
  "martin.sauczuk@gmail.com",           # 6
  "pablo.g.marrero@gmail.com",          # 7
  "vdecristofolo@gmail.com",            # 8
  "sabaliauskaspablo@gmail.com",        # 9
  "pablotobia@gmail.com",               # 10
  "duglas.espanol@gmail.com",           # 11
  "eugeniocalcena@gmail.com",           # 12
  "juliatroilo@gmail.com"               # 13
]

estímulosPorSujeto = [ # Índices de los estímulos asignados a cada sujeto
  # 1
  [0,1,2,3,4,5,6,7,8,9],
  # 2
  [10,11,12,13,14,15,16,17,18,19],
  # 3
  [20,21,22,23,24,25,26,27,28,29],
  # 4
  [0,1,2,3,4,5,6,7,8,9],
  # 5
  [10,11,12,13,14,15,16,17,18,19],
  # 6
  [20,21,22,23,24,25,26,27,28,29],
  # 7
  [0,1,2,3,4,5,6,7,8,9],
  # 8
  [10,11,12,13,14,15,16,17,18,19],
  # 9
  [20,21,22,23,24,25,26,27,28,29],
  # 10
  [0,1,2,3,4,5,6,7,8,9],
  # 11
  [10,11,12,13,14,15,16,17,18,19],
  # 12
  [20,21,22,23,24,25,26,27,28,29],
  # 13
  [0,1,2,3,4,5,6,7,8,9]
]

def estímulosPara_(i):
  # i es un número entre 1 y la cantidad de sujetos
  return list(map(lambda x : todosLosEstímulos[x], estímulosPorSujeto[i-1]))

def cuestionarioPara_ConEstímulos_(sujeto, estímulos, i):
  preguntas = [{
    "tipo":"SOLO_TEXTO",
    "titulo":títuloBienvenida,
    "pregunta":textoDeBienvenida
  }]
  for estímulo in estímulos:
    preguntas.append({
      "tipo":"SLIDER",
      "titulo":títuloEstímulo,
      "pregunta":textoEstímulo(estímulo),
      "rango":{"desde":1,"hasta":5,"paso":1}
    })
    preguntas.append({
      "tipo":"TEXTO_LIBRE",
      "titulo":títuloJustificación,
      "pregunta":textoJustificación
    })
  preguntas.append({
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
    "preguntas":preguntas,
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
  "progreval2026":{
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
      "url":"1FAIpQLScgDso9R1aU0b_IwOtpr6RwhRlma8j52YEZX6bc5SO1pqVkpQ",
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
