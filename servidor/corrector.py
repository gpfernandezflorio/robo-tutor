# -*- coding: utf-8 -*-

import os, shutil
from correctorPython import CorrectorPython
from correctorGobstones import CorrectorGobstones
from correctorHaskell import CorrectorHaskell
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
    resultado = corregir(CorrectorPython(), jsonObj, v)
  elif (jsonObj["lenguaje"] == "Haskell"):
    resultado = corregir(CorrectorHaskell(), jsonObj, v)
  elif (jsonObj["lenguaje"] == "Gobstones"):
    resultado = corregir(CorrectorGobstones(), jsonObj, v)
  else:
    if (v):
      print(jsonObj["lenguaje"])
    return {"resultado":"Error", "error":"Lenguaje desconocido: " + jsonObj["lenguaje"]}
  return resultado

def corregir(corrector, jsonObj, v):
  usuario = limpiar(jsonObj['usuario'])
  ruta = os.path.join('/','rtTest', usuario)
  if os.path.isdir(ruta):
    return {'resultado':"Error", 'mensaje':"Demasiados intentos seguidos"}
  os.mkdir(ruta)
  os.chmod(ruta, 0o777)
  resultado = corrector.corregir(jsonObj, ruta, v)
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