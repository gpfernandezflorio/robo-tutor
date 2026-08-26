from cursos.gbs import *
from msg import *

def fValEq(n):
  return lambda x : x + " == " + str(n)

def ejPythonParaEvaluar(id, nombre, evaluaciones):
  return {
    "tipo":"CODIGO",
    "id":id,
    "nombre":nombre,
    "enunciado":"Asignar 0 a la variable 'x'.",
    "run_data":[{
      "def":"x",
      "assert":"x == 0"
    }],
    "analisisCodigo":evaluaciones
  }

def ejPythonConVals(id, nombre, ev):
  return {
    "tipo":"CODIGO",
    "id":id,
    "nombre":nombre,
    "enunciado":"Asignar 0 a la variable 'x'.",
    "run_data":[{
      "def":"x",
      "eval":ev
    }]
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
    "actividades":[{
      "tipo":"CODIGO",
      "id":"error_relativo",
      "nombre":"error_relativo",
      "enunciado":"Implementar la función <code>error_relativo</code>.",
      "aridad":{"error_relativo":2},
      "pre":"import numpy as np",
      "run_data":[
        {"assert":"np.allclose(error_relativo(1,1.1),0.1)"},
        {"assert":"np.allclose(error_relativo(2,1),0.5)"},
        {"assert":"np.allclose(error_relativo(-1,-1),0)"},
        {"assert":"np.allclose(error_relativo(1,-1),2)"}
      ]
    },
    ejPythonParaEvaluar("cmdXLine", "cmdXLine", [
      {"key":"CMD_X_LINE"}
    ]),
    ejPythonConVals("eval_vals","eval_vals",{"expr":"x","vals":{
      "0":"OK",
      "1":mensajeMenosDeUno,
      "-1":mensajeMásDeMenosUno
    }}),
    ejPythonConVals("eval_checks","eval_checks",{"expr":"x","checks":[{
      "fVal": lambda x : "type(" + x + ") != type(0)",
      "msg": mensajeDebeSerNum
    },{
      "fVal": fValEq(1),
      "msg": mensajeMenosDeUno,
    },{
      "fVal": lambda x : x + "< 0",
      "msg": mensajeNoDebeSerNeg
    },{
      "fVal": lambda x : x + "> 0",
      "msg": mensajeNoDebeSerPos
    },{
      "fVal": fValEq(0),
      "msg": "OK",
    }]})
    ]
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
    "actividades":[
      ejGobstonesParaEvaluar("cmdXLine", "cmdXLine", [
        {"key":"CMD_X_LINE"}
      ]),
      ejGobstonesParaEvaluar("indentNest", "indentNest", [
        {"key":"INDENT_NEST"}
      ])
    ]
  }
}