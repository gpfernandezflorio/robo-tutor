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
  def hijosDeNodo(self, nodo):
    return nodo["_children"] if nodo and ("_children" in nodo) else []
  def esNodoDeTipo(self, nodo, tipo):
    return (nodo and ("_tag" in nodo)) and (nodo["_tag"] == tipo)
  def esUnComandoCompuesto(self, nodo):
    return (nodo and ("_tag" in nodo)) and (nodo["_tag"] in [
      "N_StmtIf",
      "N_StmtRepeat",
      "N_StmtForeach",
      "N_StmtWhile",
      "N_StmtSwitch"
    ])
  def hayRepeticiónSimple(self, AST):
    return self.hayNodoDeTipo(AST, "N_StmtRepeat")
  def hayNombre_(self, AST, nombre):
    return algunoCumple(lambda nodo : nodo["_children"][0]["_value"] == nombre, self.nodosDeTipo(AST, "N_ExprVariable"))
  def hayImport(self, AST):
    return False # No hay imports en Gobstones
  def hayExcepción(self, AST):
    return False # No hay excepciones en Gobstones

def astGobstones(codigo):
  f = open(rutaJail("src.txt"), 'w')
  f.write(codigo)
  f.close()
  errcode, salida, falla = ejecutar("node /rtTest/gbs/dist/gobstones-lang parse -l es -i src.txt")
  if len(falla) > 0:
    return {"error":falla}
  AST = json.loads(json.loads(salida))
  return {"ast":AST}