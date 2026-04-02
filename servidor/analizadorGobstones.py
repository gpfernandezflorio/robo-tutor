# -*- coding: utf-8 -*-

# Definición de la clase ASTNode de Gobstones: https://github.com/gobstones/gobstones-parser/blob/main/src/parser/ast.ts

import json
from analizadorBase import Analizador
from procesos import ejecutar, rutaJail
from utils import algunoCumple

reglasCódigoMalicioso = {
  # No existe código malicioso en Gobstones
}

class AnalizadorGobstones(Analizador):
  def __init__(self, malicioso=reglasCódigoMalicioso.keys()):
    self.clavesReglasCódigoMalicioso = malicioso
    self.reglasCódigoMalicioso = reglasCódigoMalicioso
  def obtenerAst(self, codigo):
    return astGobstones(codigo)
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
    return "N_ExprVariable"
  def nombreNodo_(self, nodo):
    # PRE: nodo es de tipo Nombre
    return nodo["_children"][0]["_value"]
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

def astGobstones(codigo):
  f = open(rutaJail("src.txt"), 'w')
  f.write(codigo)
  f.close()
  errcode, salida, falla = ejecutar("node /rtTest/gbs/dist/gobstones-lang parse -l es -i src.txt")
  if len(falla) > 0:
    return {"error":falla}
  AST = json.loads(json.loads(salida))
  AgregarAtributoMadre(AST)
  AST["_madre"] = None
  return {"ast":AST}

def hijosDeNodo_(nodo):
  return nodo["_children"] if (not (nodo is None) and ("_children" in nodo)) else []

def AgregarAtributoMadre(nodo):
  for hijo in hijosDeNodo_(nodo):
    hijo["_madre"] = nodo
    AgregarAtributoMadre(hijo)