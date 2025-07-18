# -*- coding: utf-8 -*-

import json
from functools import reduce
from procesos import ejecutar

def analizarGobstones(codigo, reglas):
  ast = astGobstones(codigo)
  if "falla" in ast:
    return ast
  return analizarAst(ast["ast"], codigo, reglas)

def analizarPython(codigo, reglas):
  ast = astPython(codigo)
  return analizarAst(ast, codigo, reglas)

def astGobstones(codigo):
  errcode, salida, falla = ejecutar("node gobstones-lang/dist/gobstones-lang parse -l es -i src.txt")
  if len(falla) > 0:
    return {"falla":falla}
  ast = json.loads(json.loads(salida))
  return {"ast":ast}

def astPython(codigo):
  return {} # TODO

def analizarAst(ast, codigo, reglas):
  for regla in reglas:
    resultado = analizarRegla(ast, codigo, regla)
    if not(resultado is None):
      return resultado
  return None

def analizarRegla(ast, codigo, regla):
  error = ""
  if (type(regla) == type(lambda x : 0)):
    error = regla(ast, codigo)
  elif regla["key"] in REGLAS:
    error = REGLAS[regla["key"]](ast, codigo, regla)
  if (error is None) or len(error) == 0:
    return None
  return {"resultado":"Calidad", "error":error}

def reglaComandosAnidados(ast, codigo, regla):
  maximaAnidacion = regla["max"] if "max" in regla else 1
  return "No está bueno anidar comandos compuestos" if nivelesAnidacionComandos(ast) > maximaAnidacion else None

def reglaUnComandoPorLinea(ast, codigo, regla):
  return None

def reglaIndentacion(ast, codigo, regla):
  return None

REGLAS = {
  "NEST_CMD":reglaComandosAnidados,
  "CMD_X_LINE":reglaUnComandoPorLinea,
  "INDENT":reglaIndentacion
}

def nivelesAnidacionComandos(ast):
  anidacionActual = 0
  hijos = ast["_children"] if ast and ("_children" in ast) else []
  if len(hijos) > 0:
    maxAnidacion = nivelesAnidacionComandos(hijos[0])
    for i in range(1, len(hijos)):
      maxAnidacion = max(maxAnidacion, nivelesAnidacionComandos(hijos[i]))
    anidacionActual = maxAnidacion
  if esUnComandoCompuesto(ast):
    anidacionActual = anidacionActual + 1
  return anidacionActual

def esUnComandoCompuesto(ast):
  return (ast and ("_tag" in ast)) and (ast["_tag"] in [
    "N_StmtIf",
    "N_StmtRepeat",
    "N_StmtForeach",
    "N_StmtWhile",
    "N_StmtSwitch"
  ])