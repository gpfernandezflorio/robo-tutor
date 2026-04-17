# -*- coding: utf-8 -*-

# Definición de la clase ASTNode de Gobstones: https://github.com/gobstones/gobstones-parser/blob/main/src/parser/ast.ts

import os, json
from analizadorBase import Analizador
from procesos import ejecutar
from utils import algunoCumple

reglasCódigoMalicioso = {
  # No existe código malicioso en Gobstones
}

class AnalizadorGobstones(Analizador):
  def __init__(self, malicioso=reglasCódigoMalicioso.keys()):
    self.clavesReglasCódigoMalicioso = malicioso
    self.reglasCódigoMalicioso = reglasCódigoMalicioso
  def obtenerAst(self, codigo, ruta="."):
    return astGobstones(codigo, ruta)
  def hijosDeNodo_(self, nodo):
    return hijosDeNodo_(nodo)
  def nodoMadreDe_(self, nodo):
    return nodo["_madre"]
  def es_NodoDeTipo_(self, nodo, tipo):
    if not (nodo is None) and ("_tag" in nodo):
      tipos = tipo if type(tipo) == type([]) else [tipo]
      return algunoCumple(lambda t : nodo["_tag"] == t, tipos)
    return False
  def tiposNombre(self):
    return "Nombre"
  def nombreNodo_(self, nodo):
    # PRE: nodo es de tipo Nombre
    return nodo["_value"]
  def tiposComandosCompuestos(self):
    return [
      "N_StmtIf",
      "N_StmtRepeat",
      "N_StmtForeach",
      "N_StmtWhile",
      "N_StmtSwitch"
    ]
  def tiposRepeticiónSimple(self):
    return "N_StmtRepeat"
  def tiposImport(self):
    return [] # No hay imports en Gobstones
  def tiposExcepción(self):
    return [] # No hay excepciones en Gobstones
  def líneaDeNodo_(self, nodo):
    return nodo["_startPos"]["_line"]
  def columnaDeNodo_(self, nodo):
    return nodo["_startPos"]["_column"]
  def actualizarNroLíneas(self, r, d):
    if "línea" in r:
      r["línea"] = r["línea"] -d + 1
    return r
  def astMostrable(self, ast):
    o = {}
    if not (ast is None):
      # if "_tag" in ast and ast["_tag"] == "N_StmtIf":
      #   if "_startPos" in ast and "_index" in ast["_startPos"] and "_string" in ast["_startPos"]:
      #     print(ast["_startPos"]["_string"][ast["_startPos"]["_index"]:])
      #   for k in ast:
      #     if k != "_madre" and k != "_children":
      #       print(k + ": " + str(ast[k]))
      for k in ast:
        if k in ["_tag", "_line", "_value"]:
          o[k] = ast[k]
        if k in ["_startPos"]:
          o[k] = self.astMostrable(ast[k])
      if "_children" in ast:
        o["_children"] = list(map(lambda h : self.astMostrable(h), ast["_children"]))
    return o

def astGobstones(codigo, ruta="."):
  f = open(os.path.join(ruta, "src.txt"), 'w')
  f.write(codigo)
  f.close()
  errcode, salida, falla = ejecutar("node /rtTest/gbs/dist/gobstones-lang parse -l es -i src.txt", ruta)
  if len(falla) > 0:
    return {"error":falla}
  AST = json.loads(json.loads(salida))
  CorregirElseIfs(AST)
  AgregarTagNombre(AST)
  AgregarAtributoMadre(AST)
  AST["_madre"] = None
  return {"ast":AST}

def hijosDeNodo_(nodo):
  hijosPorAhora = []
  if type(nodo) == type({}):
    for hijo in (nodo["_children"] if (not (nodo is None) and ("_children" in nodo)) else []):
      if type(hijo) == type({}):
        hijosPorAhora.append(hijo)
      elif type(hijo) == type([]):
        hijosPorAhora = hijosPorAhora + hijo
  return hijosPorAhora

def CorregirElseIfs(nodo):
  if esUnElseIf(nodo):
    nodo["_tag"] = "N_StmtElseIf"
  for hijo in hijosDeNodo_(nodo):
    CorregirElseIfs(hijo)

def AgregarAtributoMadre(nodo):
  for hijo in hijosDeNodo_(nodo):
    hijo["_madre"] = nodo
    AgregarAtributoMadre(hijo)

def AgregarTagNombre(nodo):
  if not ("_tag" in nodo) and ("_value" in nodo):
    nodo["_tag"] = "Nombre"
  for hijo in hijosDeNodo_(nodo):
    AgregarTagNombre(hijo)

def esUnElseIf(nodo):
  return ("_tag" in nodo) and \
    (nodo["_tag"] == "N_StmtIf") and \
    ("_startPos" in nodo) and \
    ("_index" in nodo["_startPos"]) and \
    ("_string" in nodo["_startPos"]) and \
    (not nodo["_startPos"]["_string"][nodo["_startPos"]["_index"]:].startswith("if"))