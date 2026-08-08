from cursos.gbs import *

CURSOS = {
  "curso_ficticio_python":{
    "nombre":"Curso Ficticio Python",
    "anio":"0",
    "edicion":"Prueba",
    "descripcion":"Curso para hacer pruebas",
    "responsable":{
      "nombre":"Nadie",
      "contacto":"? (AT) ?"
    },
    "institucion":"Ninguna",
    "lenguaje":"Python",
    "actividades":[{
      "tipo":"CODIGO",
      "id":"cmdXLine",
      "nombre":"cmdXLine",
      "enunciado":"Asignar 0 a la variable 'x'.",
      "run_data":[{
        "def":"x",
        "post":"x == 0"
      }],
      "analisisCodigo":[
        {"key":"CMD_X_LINE"}
      ]
    }]
  },
  "curso_ficticio_gobstones":{
    "nombre":"Curso Ficticio Gobstones",
    "anio":"0",
    "edicion":"Prueba",
    "descripcion":"Curso para hacer pruebas",
    "responsable":{
      "nombre":"Nadie",
      "contacto":"? (AT) ?"
    },
    "institucion":"Ninguna",
    "lenguaje":"Gobstones",
    "actividades":[{
      "tipo":"CODIGO",
      "id":"cmdXLine",
      "nombre":"cmdXLine",
      "enunciado":"Implementar la función 'fun0' que devuelve siempre 0.",
      "run_data":[{
        "pre":programParaValidarNumEnCelda("fun0()"),
        "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
        "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
      }],
      "analisisCodigo":[
        {"key":"CMD_X_LINE"}
      ]
    }]
  }
}