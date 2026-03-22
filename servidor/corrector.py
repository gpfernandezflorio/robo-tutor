# -*- coding: utf-8 -*-

import json
from analizador import EvitarCódigoMalicioso
from CorrectorPython import correctorPython
from CorrectorGobstones import correctorGobstones
from CorrectorHaskell import correctorHaskell

EvitarCódigoMalicioso()

def run_code(jsonObj, v):
  if (not ("src" in jsonObj)):
    if (v):
      print("Falta src")
    return {"resultado":"Error", "error":"Falta src"}
  if (not ("lenguaje" in jsonObj)):
    if (v):
      print("Falta lenguaje")
    return {"resultado":"Error", "error":"Falta lenguaje"}
  if (jsonObj["lenguaje"] == "Python"):
    resultado = run_python(jsonObj, v)
  elif (jsonObj["lenguaje"] == "Haskell"):
    resultado = run_haskell(jsonObj, v)
  elif (jsonObj["lenguaje"] == "Gobstones"):
    resultado = run_gobstones(jsonObj, v)
  else:
    if (v):
      print(jsonObj["lenguaje"])
    return {"resultado":"Error", "error":"Lenguaje desconocido: " + jsonObj["lenguaje"]}
  return resultado

def run_python(jsonObj, v):
  return correctorPython.corregir(jsonObj, v)

def run_haskell(jsonObj, v):
  return correctorHaskell.corregir(jsonObj, v)

def run_gobstones(jsonObj, v):
  return correctorGobstones.corregir(jsonObj, v)
