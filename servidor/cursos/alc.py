# -*- coding: utf-8 -*-

traza = {
  "tipo":"CODIGO",
  "id":"traza",
  "nombre":"5. Traza",
  "enunciado":"Desarrollar una función <code>traza(A)</code> que calcule la traza de una matriz cualquiera <i>A</i>.",
  "aridad":{"traza":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"traza(np.array([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]))==5"}
  ]
}
traspuesta = {
  "tipo":"CODIGO",
  "id":"traspuesta",
  "nombre":"6. Traspuesta",
  "enunciado":"Desarrollar una función <code>traspuesta(A)</code> que devuelva la matriz traspuesta de <i>A</i>.",
  "aridad":{"traspuesta":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(traspuesta(np.array([[1,2],[3,4]])),np.array([[1,3],[2,4]]))"}
  ]
}
producto = {
  "tipo":"CODIGO",
  "id":"producto",
  "nombre":"8. Producto",
  "enunciado":"Desarrollar una función <code>calcularAx(A,x)</code> que recibe una matriz <i>A</i> de tamaño <i>n × m</i> y un vector <i>x</i> de largo <i>m</i> y devuelve un vector <i>b</i> de largo <i>n</i> resultado de la multiplicación vectorial de la matriz y el vector.",
  "aridad":{"calcularAx":2},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"np.array_equal(calcularAx(np.array([[1,2],[3,4]]),np.array([1,1])),np.array([3,7]))"}
  ]
}
esDiagonalDominante = {
  "tipo":"CODIGO",
  "id":"esDiagonalDominante",
  "nombre":"11. Diagonalmente dominante",
  "enunciado":"Desarrollar una función <code>esDiagonalmenteDominante(A)</code> que devuelva <code>True</code> si una matriz cuadrada <i>A</i> es estrictamente diagonalmente dominante. Esto ocurre si para cada fila, el valor absoluto del elemento en la diagonal es mayor que la suma de los valores absolutos de los demás elementos en esa fila.",
  "aridad":{"esDiagonalmenteDominante":1},
  "pre":"import numpy as np",
  "run_data":[
    {"assert":"esDiagonalmenteDominante(np.array([[10,1,1],[-2,8,1],[2,-1,-10]]))"}
  ]
}

CURSOS = {
  "alc_prueba":{
    "nombre":"Álgebra Lineal Computacional - FCEN-UBA (PRUEBA)",
    "anio":"2025",
    "edicion":"Prueba",
    "descripcion":"Curso correspondiente a la materia Álgebra Lineal Computacional de la Facultad de Ciencias Exactas y Naturales (FCEyN), UBA",
    "responsable":{
      "nombre":"Equipo de ALC",
      "contacto":"? (AT) ?"
    },
    "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    # "analisisCodigo":[
    #   {"key":"CMD_X_LINE"},
    #   {"key":"INDENT"},
    #   {"key":"NEST_CMD","max":1}
    # ],
    "actividades":[
      traza,
      traspuesta,
      producto,
      esDiagonalDominante
    ],
    "planilla":{
      "url":"1FAIpQLSfijJIbAFHK5BNEJhi31q1kXa3Z_LuLdiZjz7_O9N4SGu58WA",
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
