linkEncuestaInicial_2026_1C = {
  "tipo":"LINK",
  "id":"linkEncuestaInicial",
  "nombre":"Encuesta Inicial",
  "url":"-" # TODO
}

def R():
  return {"tex":"\\mathbb{R}"}

def Z():
  return {"tex":"\\mathbb{Z}"}

def spec(nombre, parámetros, tipo, requieres, aseguras):
  resultado = []
  resultado.append("<br><code>problema "+nombre+"</code> (")
  resultado += spec_params(parámetros)
  resultado += [") : ",tipo," {<br>"]
  resultado += spec_nodes("requiere", requieres)
  resultado +=  spec_nodes("asegura", aseguras)
  resultado.append("}<br>")
  return resultado

def spec_params(parámetros):
  if len(parámetros) == 0:
    return []
  resultado = [parámetros[0][0],":",parámetros[0][1]]
  for parámetro in parámetros[1:]:
    resultado.append(", ")
    resultado += [parámetro[0],":",parámetro[1]]
  return resultado

def spec_nodes(pre, nodos):
  resultado = []
  for nodo in nodos:
    resultado.append("&nbsp;&nbsp;<code>"+pre+":</code> {")
    resultado.append(nodo)
    resultado.append("}<br>")
  return resultado

def tBool():
  return "Bool"

def tInt():
  return "Integer"

def tFloat():
  return "Float"

def tFunc(t1,t2):
  return t1 + " -> " + t2

def tPar(t1,t2):
  return "("+t1+","+t2+")"

def tPar3(t1,t2,t3):
  return "("+t1+","+t2+","+t3+")"

def guia3(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia3",
    "nombre":"Guía Práctica 3",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      guia3_ej1a(fechaInicio),
      guia3_ej1b(fechaInicio),
      guia3_ej1c(fechaInicio),
      guia3_ej2a(fechaInicio),
      guia3_ej2b(fechaInicio),
      guia3_ej2c(fechaInicio),
      guia3_ej2di(fechaInicio),
      guia3_ej2dii(fechaInicio),
      guia3_ej2ei(fechaInicio),
      guia3_ej2eii(fechaInicio),
      guia3_ej2f(fechaInicio),
      guia3_ej2g(fechaInicio),
      guia3_ej2h(fechaInicio),
      guia3_ej2i(fechaInicio),
      guia3_ej2j(fechaInicio),
      guia3_ej3(fechaInicio),
      guia3_ej4a(fechaInicio),
      guia3_ej4b(fechaInicio),
      guia3_ej4c(fechaInicio),
      guia3_ej4d(fechaInicio),
      guia3_ej4e(fechaInicio),
      guia3_ej4f(fechaInicio),
      guia3_ej4g(fechaInicio),
      guia3_ej4h(fechaInicio),
      guia3_ej4ii(fechaInicio),
      guia3_ej4iii(fechaInicio),
      guia3_ej4iiii(fechaInicio),
      guia3_ej5(fechaInicio),
      guia3_ej6(fechaInicio),
      guia3_ej7a(fechaInicio),
      guia3_ej7b(fechaInicio),
      guia3_ej8(fechaInicio)
    ]
  }

def guia3_ej1a(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej1a",
    "nombre":"Guía 3 - Ejercicio 1 (a)",
    "lenguaje":"Haskell",
    "enunciado":["Implementar la función parcial <code>f :: Integer -> Integer</code> definida por extensión de la siguiente manera:<br><em>f(1) = 8</em><br><em>f(4) = 131</em><br><em>f(16) = 16</em><br>y cuya especificación es:"]+spec(
      "f",[("n",Z())],Z(),
      [{"tex":"n = 1 \\lor n = 4 \\lor n = 16"}],
      [{"tex":"(n = 1 \\rightarrow res = 8) \\land (n = 4 \\rightarrow res = 131) \\land (n = 16 \\rightarrow res = 16)"}]
    ),
    "aridad":{"f":tFunc(tInt(),tInt())},
    "run_data":[{
      "assert":"f(1)==8"
    },{
      "assert":"f(4)==131"
    },{
      "assert":"f(16)==16"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej1b(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej1b",
    "nombre":"Guía 3 - Ejercicio 1 (b)",
    "lenguaje":"Haskell",
    "enunciado":"Análogamente, especificar e implementar la función parcial  <code>g :: Integer -> Integer</code><br><em>g(8) = 16</em><br><em>g(16) = 4</em><br><em>g(131) = 1</em>",
    "aridad":{"g":tFunc(tInt(),tInt())},
    "run_data":[{
      "assert":"g(8)==16"
    },{
      "assert":"g(16)==4"
    },{
      "assert":"g(131)==1"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej1c(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej1c",
    "nombre":"Guía 3 - Ejercicio 1 (c)",
    "lenguaje":"Haskell",
    "enunciado":"A partir de las funciones definidas en los ítems a) y b), implementar las funciones parciales <em>h = f o g</em> y <em>k = g o f</em>",
    "aridad":{"h":tFunc(tInt(),tInt()), "k":tFunc(tInt(),tInt())},
    "run_data":[{
      "assert":"h(8)==16"
    },{
      "assert":"h(16)==131"
    },{
      "assert":"h(131)==8"
    },{
      "assert":"k(1)==16"
    },{
      "assert":"k(4)==1"
    },{
      "assert":"k(16)==4"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2a(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2a",
    "nombre":"Guía 3 - Ejercicio 2 (a)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>absoluto</code>: calcula el valor absoluto de un número entero.",
    "aridad":{"absoluto":tFunc(tInt(),tInt())},
    "run_data":[{
      "assert":"absoluto(0)==0"
    },{
      "assert":"absoluto(3)==3"
    },{
      "assert":"absoluto(-5)==5"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2b(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2b",
    "nombre":"Guía 3 - Ejercicio 2 (b)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>maximoAbsoluto</code>: devuelve el máximo entre el valor absoluto de dos números enteros.",
    "aridad":{"maximoAbsoluto":tFunc(tInt(),tFunc(tInt(),tInt()))},
    "run_data":[{
      "assert":"(maximoAbsoluto 0 0)==0"
    },{
      "assert":"(maximoAbsoluto 2 3)==3"
    },{
      "assert":"(maximoAbsoluto -2 3)==3"
    },{
      "assert":"(maximoAbsoluto -3 -2)==3"
    },{
      "assert":"(maximoAbsoluto -3 2)==3"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2c(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2c",
    "nombre":"Guía 3 - Ejercicio 2 (c)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>maximo3</code>: devuelve el máximo entre tres números enteros.",
    "aridad":{"maximo3":tFunc(tInt(),tFunc(tInt(),tFunc(tInt(),tInt())))},
    "run_data":[{
      "assert":"(maximo3 0 0 0)==0"
    },{
      "assert":"(maximo3 3 2 5)==5"
    },{
      "assert":"(maximo3 -3 2 -5)==2"
    },{
      "assert":"(maximo3 3 2 -5)==3"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2di(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2di",
    "nombre":"Guía 3 - Ejercicio 2 (d) (I)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>algunoEsCero</code>: dados dos números racionales, decide si alguno es igual a 0 (resolverlo con <em>pattern matching</em>).",
    "aridad":{"algunoEsCero":tFunc(tFloat(),tFunc(tFloat(),tBool()))},
    "run_data":[{
      "assert":"(algunoEsCero 0 0)"
    },{
      "assert":"(algunoEsCero 0 5)"
    },{
      "assert":"(algunoEsCero 5 0)"
    },{
      "assert":"not (algunoEsCero 5 5)"
    },{
      "assert":"not (algunoEsCero -5 -5)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2dii(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2dii",
    "nombre":"Guía 3 - Ejercicio 2 (d) (II)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>algunoEsCero</code>: dados dos números racionales, decide si alguno es igual a 0 (resolverlo sin <em>pattern matching</em>).",
    "aridad":{"algunoEsCero":tFunc(tFloat(),tFunc(tFloat(),tBool()))},
    "run_data":[{
      "assert":"(algunoEsCero 0 0)"
    },{
      "assert":"(algunoEsCero 0 5)"
    },{
      "assert":"(algunoEsCero 5 0)"
    },{
      "assert":"not (algunoEsCero 5 5)"
    },{
      "assert":"not (algunoEsCero -5 -5)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2ei(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2ei",
    "nombre":"Guía 3 - Ejercicio 2 (e) (I)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>ambosSonCero</code>: dados dos números racionales, decide si ambos son iguales a 0 (resolverlo con <em>pattern matching</em>).",
    "aridad":{"ambosSonCero":tFunc(tFloat(),tFunc(tFloat(),tBool()))},
    "run_data":[{
      "assert":"(ambosSonCero 0 0)"
    },{
      "assert":"not (ambosSonCero 0 5)"
    },{
      "assert":"not (ambosSonCero 5 0)"
    },{
      "assert":"not (ambosSonCero 5 5)"
    },{
      "assert":"not (ambosSonCero -5 -5)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2eii(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2eii",
    "nombre":"Guía 3 - Ejercicio 2 (e) (II)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>ambosSonCero</code>: dados dos números racionales, decide si ambos son iguales a 0 (resolverlo sin <em>pattern matching</em>).",
    "aridad":{"ambosSonCero":tFunc(tFloat(),tFunc(tFloat(),tBool()))},
    "run_data":[{
      "assert":"(ambosSonCero 0 0)"
    },{
      "assert":"not (ambosSonCero 0 5)"
    },{
      "assert":"not (ambosSonCero 5 0)"
    },{
      "assert":"not (ambosSonCero 5 5)"
    },{
      "assert":"not (ambosSonCero -5 -5)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2f(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2f",
    "nombre":"Guía 3 - Ejercicio 2 (f)",
    "lenguaje":"Haskell",
    "enunciado":["Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>enMismoIntervalo</code>: dados dos números reales, indica si están relacionados por la relación de equivalencia en ",R()," cuyas clases de equivalencia son: (",{"tex":"-\\infty"},", 3], (3, 7] y (7, ",{"tex":"\\infty"},"), o dicho de otra manera, si pertenecen al mismo intervalo."],
    "aridad":{"enMismoIntervalo":tFunc(tFloat(),tFunc(tFloat(),tBool()))},
    "run_data":[{
      "assert":"(enMismoIntervalo 0 0)"
    },{
      "assert":"(enMismoIntervalo -6 -4)"
    },{
      "assert":"(enMismoIntervalo -6 2)"
    },{
      "assert":"(enMismoIntervalo 0 2)"
    },{
      "assert":"(enMismoIntervalo -1 3)"
    },{
      "assert":"(enMismoIntervalo 4 6)"
    },{
      "assert":"(enMismoIntervalo 4 6)"
    },{
      "assert":"(enMismoIntervalo 8 10)"
    },{
      "assert":"not (enMismoIntervalo 3 7)"
    },{
      "assert":"not (enMismoIntervalo 3 4)"
    },{
      "assert":"not (enMismoIntervalo 7 10)"
    },{
      "assert":"not (enMismoIntervalo -4 4)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2g(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2g",
    "nombre":"Guía 3 - Ejercicio 2 (g)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>sumaDistintos</code>: que dados tres números enteros calcule la suma sin sumar repetidos (si los hubiera).",
    "aridad":{"sumaDistintos":tFunc(tInt(),tFunc(tInt(),tFunc(tInt(),tInt())))},
    "run_data":[{
      "assert":"(sumaDistintos 0 0 0)==0"
    },{
      "assert":"(sumaDistintos 1 1 1)==1"
    },{
      "assert":"(sumaDistintos -4 0 4)==0"
    },{
      "assert":"(sumaDistintos -1 -1 -1)==-1"
    },{
      "assert":"(sumaDistintos 2 3 2)==5"
    },{
      "assert":"(sumaDistintos 2 3 6)==12"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2h(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2h",
    "nombre":"Guía 3 - Ejercicio 2 (h)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>esMultiploDe</code>: dados dos números naturales, decide si el primero es múltiplo del segundo.",
    "aridad":{"esMultiploDe":tFunc(tInt(),tFunc(tInt(),tBool()))},
    "run_data":[{
      "assert":"(esMultiploDe 0 0)"
    },{
      "assert":"(esMultiploDe 1 1)"
    },{
      "assert":"(esMultiploDe 5 5)"
    },{
      "assert":"(esMultiploDe 0 5)"
    },{
      "assert":"not (esMultiploDe 5 0)"
    },{
      "assert":"(esMultiploDe -12 2)"
    },{
      "assert":"(esMultiploDe 9 -3)"
    },{
      "assert":"not (esMultiploDe 2 6)"
    },{
      "assert":"not (esMultiploDe 4 -16)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2i(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2i",
    "nombre":"Guía 3 - Ejercicio 2 (i)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>digitoUnidades</code>: dado un número entero, extrae su dígito de las unidades.",
    "aridad":{"digitoUnidades":tFunc(tInt(),tInt())},
    "run_data":[{
      "assert":"(digitoUnidades 0)==0"
    },{
      "assert":"(digitoUnidades 1)==1"
    },{
      "assert":"(digitoUnidades 23)==3"
    },{
      "assert":"(digitoUnidades 1548)==8"
    },{
      "assert":"(digitoUnidades -62)==2"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej2j(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2j",
    "nombre":"Guía 3 - Ejercicio 2 (j)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función, incluyendo su tipo.<br><code>digitoDecenas</code>: dado un número entero mayor a 9, extrae su dígito de las decenas.",
    "aridad":{"digitoDecenas":tFunc(tInt(),tInt())},
    "run_data":[{
      "assert":"(digitoDecenas 10)==1"
    },{
      "assert":"(digitoDecenas 30)==3"
    },{
      "assert":"(digitoDecenas 103)==0"
    },{
      "assert":"(digitoUnidades 1548)==4"
    },{
      "assert":"(digitoUnidades -62)==6"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej3(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej3",
    "nombre":"Guía 3 - Ejercicio 3",
    "lenguaje":"Haskell",
    "enunciado":["Implementar una función <code>estanRelacionados :: Integer -> Integer -> Bool</code>"]+spec(
      "estanRelacionados", [("a",Z()),("b",Z())], "Bool",
      [{"tex":"a \\neq 0 \\land b \\neq 0"}],
      [[{"tex":"(res = true) \\leftrightarrow (a \\ast a + a \\ast b \\ast k = 0"}," para algún ",{"tex":"k \\in \\mathbb{Z}"}," con ",{"tex":"k \\neq 0)"}]]
    ) + ["<em>Por ejemplo:</em><br><code>estanRelacionados 8 2</code> ",{"tex":"\\leadsto"}," <code>True</code> porque existe ",{"tex":"k = -4"}," tal que ",{"tex":"8^2 + 8 \\times 2 \\times (-4) = 0"},"<br><code>estanRelacionados 7 3</code> ",{"tex":"\\leadsto"}," <code>False</code> porque no existe un ",{"tex":"k"}," entero tal que ",{"tex":"7^2 + 7 \\times 3 \\times k = 0"}],
    "aridad":{"estanRelacionados":tFunc(tInt(),tFunc(tInt(),tBool()))},
    "run_data":[{
      "assert":"(estanRelacionados 8 2)"
    },{
      "assert":"not (estanRelacionados 7 3)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4a(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4a",
    "nombre":"Guía 3 - Ejercicio 4 (a)",
    "lenguaje":"Haskell",
    "enunciado":["Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>productoInterno</code>: calcula el producto interno entre dos tuplas de ",{"tex":"\\mathbb{R} \\times \\mathbb{R}"},"."],
    "aridad":{"productoInterno":tFunc(tPar(tFloat(),tFloat()),tFunc(tPar(tFloat(),tFloat()),tFloat()))},
    "pre":"eqFloats :: Float -> Float -> Bool\neqFloats x y = abs (x-y) < 0.01",
    "run_data":[{
      "assert":"eqFloats (productoInterno (0,0) (0,0)) 0"
    },{
      "assert":"eqFloats (productoInterno (2,6) (3,4)) 30"
    },{
      "assert":"eqFloats (productoInterno (2,-6) (-3,-4)) 18"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4b(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4b",
    "nombre":"Guía 3 - Ejercicio 4 (b)",
    "lenguaje":"Haskell",
    "enunciado":["Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>esParMenor</code>: dadas dos tuplas de ",{"tex":"\\mathbb{R} \\times \\mathbb{R}"},", decide si cada coordenada de la primera tupla es menor a la coordenada correspondiente de la segunda tupla."],
    "aridad":{"esParMenor":tFunc(tPar(tFloat(),tFloat()),tFunc(tPar(tFloat(),tFloat()),tBool()))},
    "run_data":[{
      "assert":"not (esParMenor (0,0) (0,0))"
    },{
      "assert":"not (esParMenor (3,4) (4,4))"
    },{
      "assert":"not (esParMenor (4,3) (4,4))"
    },{
      "assert":"esParMenor (2,3) (3,4)"
    },{
      "assert":"esParMenor (-5,-1) (-3,1)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4c(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4c",
    "nombre":"Guía 3 - Ejercicio 4 (c)",
    "lenguaje":"Haskell",
    "enunciado":["Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>distancia</code>: calcula la distancia euclídea entre dos puntos de ",{"tex":"\\mathbb{R}^2"},"."],
    "aridad":{"distancia":tFunc(tPar(tFloat(),tFloat()),tFunc(tPar(tFloat(),tFloat()),tFloat()))},
    "pre":"eqFloats :: Float -> Float -> Bool\neqFloats x y = abs (x-y) < 0.01",
    "run_data":[{
      "assert":"eqFloats (distancia (0,0) (0,0)) 0"
    },{
      "assert":"eqFloats (distancia (6,4) (6,4)) 0"
    },{
      "assert":"eqFloats (distancia (-1,4) (3,1)) 5"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4d(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4d",
    "nombre":"Guía 3 - Ejercicio 4 (d)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>sumaTerna</code>: dada una terna de enteros, calcula la suma de sus tres elementos.",
    "aridad":{"sumaTerna":tFunc(tPar3(tInt(),tInt(),tInt()),tInt())},
    "run_data":[{
      "assert":"sumaTerna (0,0,0) == 0"
    },{
      "assert":"sumaTerna (1,2,3) == 6"
    },{
      "assert":"sumaTerna (-5,4,2) == 1"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4e(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4e",
    "nombre":"Guía 3 - Ejercicio 4 (e)",
    "lenguaje":"Haskell",
    "enunciado":["Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>sumarSoloMultiplos</code>: dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que son múltiplos del número natural.<br><em>Por ejemplo:</em><br><code>sumarSoloMultiplos (10,-8,-5) 2</code> ",{"tex":"\\leadsto"}," <code>2</code><br><code>sumarSoloMultiplos (66,21,4) 5</code> ",{"tex":"\\leadsto"}," <code>0</code><br><code>sumarSoloMultiplos (-30,2,12) 3</code> ",{"tex":"\\leadsto"}," <code>-18</code>"],
    "aridad":{"sumarSoloMultiplos":tFunc(tPar3(tInt(),tInt(),tInt()),tFunc(tInt(),tInt()))},
    "run_data":[{
      "assert":"sumarSoloMultiplos (10,-8,-5) 2 == 2"
    },{
      "assert":"sumarSoloMultiplos (66,21,4) 5 == 0"
    },{
      "assert":"sumarSoloMultiplos (-30,2,12) 3 == -18"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4f(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4f",
    "nombre":"Guía 3 - Ejercicio 4 (f)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>posPrimerPar</code>: dada una terna de enteros, devuelve la posición del primer número par si es que hay alguno, o devuelve 4 si son todos impares.",
    "aridad":{"posPrimerPar":tFunc(tPar3(tInt(),tInt(),tInt()),tInt())},
    "run_data":[{
      "assert":"posPrimerPar (10,20,30) == 1"
    },{
      "assert":"posPrimerPar (5,10,15) == 2"
    },{
      "assert":"posPrimerPar (3,5,3) == 4"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4g(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4g",
    "nombre":"Guía 3 - Ejercicio 4 (g)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>crearPar :: a -> b -> (a, b)</code>: a partir de dos componentes, crea un par con esos valores. Debe funcionar para elementos de cualquier tipo.",
    "aridad":{"crearPar":tFunc("a",tFunc("b",tPar("a","b")))},
    "run_data":[{
      "assert":"(crearPar 3 4) == (3,4)"
    },{
      "assert":"(crearPar True False) == (True, False)"
    },{
      "assert":"(crearPar True 4) == (True, 4)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4h(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4h",
    "nombre":"Guía 3 - Ejercicio 4 (h)",
    "lenguaje":"Haskell",
    "enunciado":"Especificar e implementar la siguiente función utilizando tuplas para representar pares y ternas de números.<br><code>invertir :: (a, b) -> (b, a)</code>: invierte los elementos del par pasado como parámetro. Debe funcionar para elementos de cualquier tipo.",
    "aridad":{"invertir":tFunc(tPar("a","b"),tPar("b","a"))},
    "run_data":[{
      "assert":"(invertir (3,4)) == (4,3)"
    },{
      "assert":"(invertir (3,True)) == (True,3)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4ii(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4ii",
    "nombre":"Guía 3 - Ejercicio 4 (i) (I)",
    "lenguaje":"Haskell",
    "enunciado":"Reescribir el ejercicio <code>productoInterno</code> usando el siguiente renombre de tipos:<br><code>type Punto2D = (Float, Float)</code>",
    # "aridad":{"productoInterno":tFunc("Punto2D",tFunc("Punto2D",tFloat()))},
    "aridad":{"productoInterno":tFunc(tPar(tFloat(),tFloat()),tFunc(tPar(tFloat(),tFloat()),tFloat()))},
    "pre":"eqFloats :: Float -> Float -> Bool\neqFloats x y = abs (x-y) < 0.01",
    "base":"type Punto2D = (Float, Float)\n\nproductoInterno :: ...\nproductoInterno ...",
    "run_data":[{
      "assert":"eqFloats (productoInterno (0,0) (0,0)) 0"
    },{
      "assert":"eqFloats (productoInterno (2,6) (3,4)) 30"
    },{
      "assert":"eqFloats (productoInterno (2,-6) (-3,-4)) 18"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4iii(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4iii",
    "nombre":"Guía 3 - Ejercicio 4 (i) (II)",
    "lenguaje":"Haskell",
    "enunciado":"Reescribir el ejercicio <code>esParMenor</code> usando el siguiente renombre de tipos:<br><code>type Punto2D = (Float, Float)</code>",
    # "aridad":{"esParMenor":tFunc("Punto2D",tFunc("Punto2D",tBool()))},
    "aridad":{"esParMenor":tFunc(tPar(tFloat(),tFloat()),tFunc(tPar(tFloat(),tFloat()),tBool()))},
    "base":"type Punto2D = (Float, Float)\n\nesParMenor :: ...\nesParMenor ...",
    "run_data":[{
      "assert":"not (esParMenor (0,0) (0,0))"
    },{
      "assert":"not (esParMenor (3,4) (4,4))"
    },{
      "assert":"not (esParMenor (4,3) (4,4))"
    },{
      "assert":"esParMenor (2,3) (3,4)"
    },{
      "assert":"esParMenor (-5,-1) (-3,1)"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej4iiii(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4iiii",
    "nombre":"Guía 3 - Ejercicio 4 (i) (III)",
    "lenguaje":"Haskell",
    "enunciado":"Reescribir el ejercicio <code>distancia</code> usando el siguiente renombre de tipos:<br><code>type Punto2D = (Float, Float)</code>",
    # "aridad":{"distancia":tFunc("Punto2D",tFunc("Punto2D",tFloat()))},
    "aridad":{"distancia":tFunc(tPar(tFloat(),tFloat()),tFunc(tPar(tFloat(),tFloat()),tFloat()))},
    "base":"type Punto2D = (Float, Float)\n\ndistancia :: ...\ndistancia ...",
    "pre":"eqFloats :: Float -> Float -> Bool\neqFloats x y = abs (x-y) < 0.01",
    "run_data":[{
      "assert":"eqFloats (distancia (0,0) (0,0)) 0"
    },{
      "assert":"eqFloats (distancia (6,4) (6,4)) 0"
    },{
      "assert":"eqFloats (distancia (-1,4) (3,1)) 5"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej5(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej5",
    "nombre":"Guía 3 - Ejercicio 5",
    "lenguaje":"Haskell",
    "enunciado":["Implementar la función <code>todosMenores :: (Integer, Integer, Integer) -> Bool</code>"]+spec(
      "todosMenores", [("t",{"tex":"\\mathbb{Z}\\times\\mathbb{Z}\\times\\mathbb{Z}"})], "Bool",
      ["True"],
      [{"tex":"(res = true) \\leftrightarrow ((f(t_0) > g(t_0)) \\land (f(t_1) > g(t_1)) \\land (f(t_2) > g(t_2)))"}]
    )+spec(
      "f", [("n",Z())], Z(),
      ["True"],
      [{"tex":"(n \\leq 7 \\rightarrow res = n^2) \\land (n > 7 \\rightarrow res = 2n-1)"}]
    )+spec(
      "g", [("n",Z())], Z(),
      ["True"],
      [["Si ",{"tex":"n"}," es un número par entonces ",{"tex":"res = n/2"},", en caso contrario, ",{"tex":"res = 3n+1"}]]
    ),
    "aridad":{"todosMenores":tFunc(tPar3(tInt(),tInt(),tInt()),tBool())},
    "run_data":[{
      "assert":"not (todosMenores (2,3,1))" # 4,9,1 ; 1,10,4
    },{
      "assert":"todosMenores (4,6,2)" # 16,36,4 ; 2,3,1
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej6(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej6",
    "nombre":"Guía 3 - Ejercicio 6",
    "lenguaje":"Haskell",
    "enunciado":["Usando los siguientes tipos:<br>&nbsp;<code>type Anio = Integer</code><br>&nbsp;<code>type EsBisiesto = Bool</code><br><br>Programar la función <code>bisiesto :: Anio -> EsBisiesto</code> según la siguiente especificación:"]+spec(
      "bisiesto", [("año",Z())], "Bool",
      ["True"],
      [[{"tex":"(res = false) \\leftrightarrow "},"(año no es múltiplo de 4, o bien, año es múltiplo de 100 pero no de 400)"]]
    )+["<br><em>Por ejemplo:</em><br><code>bisiesto 1901</code> ",{"tex":"\\leadsto"}," <code>False</code><br><code>bisiesto 1904</code> ",{"tex":"\\leadsto"}," <code>True</code><code>bisiesto 1900</code> ",{"tex":"\\leadsto"}," <code>False</code><code>bisiesto 2000</code> ",{"tex":"\\leadsto"}," <code>True</code>"],
    # "aridad":{"bisiesto":tFunc("Anio","EsBisiesto")},
    "aridad":{"bisiesto":tFunc(tInt(),tBool())},
    "base":"type Anio = Integer\ntype EsBisiesto = Bool\n\n",
    "run_data":[{
      "assert":"not (bisiesto 1901)"
    },{
      "assert":"bisiesto 1904"
    },{
      "assert":"not (bisiesto 1900)"
    },{
      "assert":"bisiesto 2000"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej7a(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej7a",
    "nombre":"Guía 3 - Ejercicio 7 (a)",
    "lenguaje":"Haskell",
    "enunciado":["Implementar la función:<br><code>distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float</code>"]+spec(
      "distanciaManhattan", [
        ("p",{"tex":"\\mathbb{R}\\times\\mathbb{R}\\times\\mathbb{R}"}),
        ("q",{"tex":"\\mathbb{R}\\times\\mathbb{R}\\times\\mathbb{R}"})
      ], R(),
      ["True"],
      [{"tex":"res = \\sum_{i=0}^{2} |p_i - q_i|"}]
    )+["<br><em>Por ejemplo:</em><br><code>distanciaManhattan (2, 3, 4) (7, 3, 8)</code> ",{"tex":"\\leadsto"}," <code>9</code><br><code>distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4))</code> ",{"tex":"\\leadsto"}," <code>12.8</code>"],
    "aridad":{"distanciaManhattan":tFunc(
      tPar3(tFloat(),tFloat(),tFloat()),
      tFunc(tPar3(tFloat(),tFloat(),tFloat()),tFloat())
    )},
    "pre":"eqFloats :: Float -> Float -> Bool\neqFloats x y = abs (x-y) < 0.01",
    "run_data":[{
      "assert":"eqFloats (distanciaManhattan (2, 3, 4) (7, 3, 8)) 9"
    },{
      "assert":"eqFloats (distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4))) 12.8"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej7b(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej7b",
    "nombre":"Guía 3 - Ejercicio 7 (b)",
    "lenguaje":"Haskell",
    "enunciado":"Reimplementar la función teniendo en cuenta el siguiente tipo: <code>type Punto3D = (Float, Float, Float)</code>",
    # "aridad":{"distanciaManhattan":tFunc(
    #   "Punto3D",
    #   tFunc("Punto3D",tFloat)
    # )},
    "aridad":{"distanciaManhattan":tFunc(
      tPar3(tFloat(),tFloat(),tFloat()),
      tFunc(tPar3(tFloat(),tFloat(),tFloat()),tFloat())
    )},
    "pre":"eqFloats :: Float -> Float -> Bool\neqFloats x y = abs (x-y) < 0.01",
    "base":"type Punto3D = (Float, Float, Float)\n\n",
    "run_data":[{
      "assert":"eqFloats (distanciaManhattan (2, 3, 4) (7, 3, 8)) 9"
    },{
      "assert":"eqFloats (distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4))) 12.8"
    }],
    "visible":{"desde":fechaInicio}
  }

def guia3_ej8(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej8",
    "nombre":"Guía 3 - Ejercicio 8",
    "lenguaje":"Haskell",
    "enunciado":["Implementar la función <code>comparar :: Integer -> Integer -> Integer</code>"]+spec(
      "comparar", [("a",Z()),("b",Z())], Z(),
      ["True"], [
        {"tex":"(res = 1) \\leftrightarrow (sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))"},
        {"tex":"(res = -1) \\leftrightarrow (sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))"},
        {"tex":"(res = 0) \\leftrightarrow (sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))"}
      ]
    )+spec(
      "sumaUltimosDosDigitos", [("x",Z())], Z(),
      ["True"], [
        [{"tex":"res = (|x| "},"mód",{"tex":" 10) + (\\lfloor \\frac{|x|}{10} \\rfloor "},"mód",{"tex":" 10)"}]
      ]
    )+["<br><em>Por ejemplo:</em><br><code>comparar 45 312</code> ",{"tex":"\\leadsto"}," <code>-1</code> porque 45 ",{"tex":"\\prec"}," 312 y 4 + 5 > 1 + 2.<br><code>comparar 2312 7</code> ",{"tex":"\\leadsto"}," <code>1</code> porque 2312 ",{"tex":"\\prec"}," 7 y 1 + 2 > 0 + 7.<br><code>comparar 45 172</code> ",{"tex":"\\leadsto"}," <code>0</code> porque no vale 45 ",{"tex":"\\prec"}," 172 ni tampoco 172 ",{"tex":"\\prec"}," 45."],
    "aridad":{"comparar":tFunc(tInt(),tFunc(tInt(),tInt()))},
    "run_data":[{
      "assert":"(comparar 45 312) == -1"
    },{
      "assert":"(comparar 2312 7) == 1"
    },{
      "assert":"(comparar 45 172) == 0"
    }],
    "visible":{"desde":fechaInicio}
  }

CURSOS = {
  "dc_ip_2026_1c":{
    "nombre":"Introducción a la Programación - DC (2026 - 1c)",
    "anio":"2026",
    "edicion":"Primer Cuatrimestre",
    "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Ciencias de la Computación y Licenciatura en Ciencias de Datos de la Universidad de Buenos Aires",
    "responsable":{
      "nombre":"Equipo de IP",
      "contacto":"a través del campus de la materia"
    },
    "institucion":"Universidad de Buenos Aires (UBA)",
    "lenguaje_display":"none",
    # "analisisCodigo":[
    #   {"key":"CMD_X_LINE"},
    #   {"key":"INDENT"},
    #   {"key":"NEST_CMD","max":1}
    # ],
    "actividades":[
      # linkEncuestaInicial_2026_1C,
      guia3("30/3/2026-8:00")
    ],
    "planilla":{
      "url":"1FAIpQLSdgcbGNTcG5ZoZRntXhfszHTvZ8wfEDlcdzZ6PWjnunthLpfQ",
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
