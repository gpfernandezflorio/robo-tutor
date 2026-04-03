# -*- coding: utf-8 -*-

import os, shutil
from correctorPython import correctorPython
from correctorGobstones import correctorGobstones
from correctorHaskell import correctorHaskell
from utils import ejecutandoLocal

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
    resultado = corregir(correctorPython, jsonObj, v)
  elif (jsonObj["lenguaje"] == "Haskell"):
    resultado = corregir(correctorHaskell, jsonObj, v)
  elif (jsonObj["lenguaje"] == "Gobstones"):
    resultado = corregir(correctorGobstones, jsonObj, v)
  else:
    if (v):
      print(jsonObj["lenguaje"])
    return {"resultado":"Error", "error":"Lenguaje desconocido: " + jsonObj["lenguaje"]}
  return resultado

def corregir(corrector, jsonObj, v):
  usuario = limpiar(jsonObj['usuario'])
  ruta = os.path.join('/','rtTest', usuario)
  if os.path.isdir(ruta):
    shutil.rmtree(ruta)
  os.mkdir(ruta)
  os.chmod(ruta, 0o777)
  resultado = corrector.corregir(jsonObj, ruta, v)
  if not ejecutandoLocal():
    shutil.rmtree(ruta)
  return resultado

def limpiar(textoOriginal):
  resultado = ""
  for x in textoOriginal:
    if x in "1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM":
      resultado += x
    else:
      resultado += "_"
  return resultado