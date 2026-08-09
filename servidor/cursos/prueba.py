from cursos.gbs import *

def ejPythonParaEvaluar(id, nombre, evaluaciones):
  return {
    "tipo":"CODIGO",
    "id":id,
    "nombre":nombre,
    "enunciado":"Asignar 0 a la variable 'x'.",
    "run_data":[{
      "def":"x",
      "post":"x == 0"
    }],
    "analisisCodigo":evaluaciones
  }

def ejGobstonesParaEvaluar(id, nombre, evaluaciones):
  return {
    "tipo":"CODIGO",
    "id":id,
    "nombre":nombre,
    "enunciado":"Implementar la función 'fun0' que devuelve siempre 0.",
    "run_data":[{
      "pre":programParaValidarNumEnCelda("fun0()"),
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    }],
    "analisisCodigo":evaluaciones
  }

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
    "actividades":[ejPythonParaEvaluar("cmdXLine", "cmdXLine", [
      {"key":"CMD_X_LINE"}
    ])]
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
    "actividades":[ejGobstonesParaEvaluar("cmdXLine", "cmdXLine", [
        {"key":"CMD_X_LINE"}
      ]), ejGobstonesParaEvaluar("indentNest", "indentNest", [
        {"key":"INDENT_NEST"}
      ])
    ]
  }
}