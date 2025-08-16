# -*- coding: utf-8 -*-

# Documentación de la clase ast de Python: https://docs.python.org/es/3.9/library/ast.html
# Definición de la clase ASTNode de Gobstones: https://github.com/gobstones/gobstones-parser/blob/main/src/parser/ast.ts

import json
import ast
from functools import reduce
from procesos import ejecutar
from utils import algunoCumple
from reglas import REGLAS

class Analizador(object):
  def analizarAst(self, AST, codigo, reglas):
    for regla in reglas:
      resultado = self.analizarRegla(AST, codigo, regla)
      if not(resultado is None):
        return resultado
    return None

  def analizarRegla(self, AST, codigo, regla):
    error = ""
    if (type(regla) == type(lambda x : 0)):
      error = regla(AST, codigo)
    elif regla["key"] in REGLAS:
      error = REGLAS[regla["key"]](self, AST, codigo, regla)
    if (error is None) or len(error) == 0:
      return None
    return {"resultado":"Calidad", "error":error}

  def nivelesAnidacionComandos(self, nodo):
    anidacionActual = 0
    hijos = self.hijosDeNodo(nodo)
    if len(hijos) > 0:
      maxAnidacion = self.nivelesAnidacionComandos(hijos[0])
      for i in range(1, len(hijos)):
        maxAnidacion = max(maxAnidacion, self.nivelesAnidacionComandos(hijos[i]))
      anidacionActual = maxAnidacion
    if self.esUnComandoCompuesto(nodo):
      anidacionActual = anidacionActual + 1
    return anidacionActual

class AnalizadorPython(Analizador):
  def obtenerAst(self, codigo):
    return astPython(codigo)
  def hijosDeNodo(self, nodo):
    return nodo.hijos()
  def esUnComandoCompuesto(self, nodo):
    return algunoCumple(lambda x : isinstance(nodo, x), [
      ast.For,
      ast.AsyncFor,
      ast.While,
      ast.If,
      ast.With,
      ast.AsyncWith,
      ast.Try
    ])

class AnalizadorGobstones(Analizador):
  def obtenerAst(self, codigo):
    return astGobstones(codigo)
  def hijosDeNodo(self, nodo):
    return nodo["_children"] if nodo and ("_children" in nodo) else []
  def esUnComandoCompuesto(self, nodo):
    return (nodo and ("_tag" in nodo)) and (nodo["_tag"] in [
      "N_StmtIf",
      "N_StmtRepeat",
      "N_StmtForeach",
      "N_StmtWhile",
      "N_StmtSwitch"
    ])

analizadorPython = AnalizadorPython()

analizadorGobstones = AnalizadorGobstones()

def analizar(analizador, codigo, reglas):
  AST = analizador.obtenerAst(codigo)
  if "falla" in AST:
    return AST
  return analizador.analizarAst(AST["ast"], codigo, reglas)

def analizarGobstones(codigo, reglas):
  return analizar(analizadorGobstones, codigo, reglas)

def analizarPython(codigo, reglas):
  return analizar(analizadorPython, codigo, reglas)

def astGobstones(codigo):
  errcode, salida, falla = ejecutar("node gobstones-lang/dist/gobstones-lang parse -l es -i src.txt")
  if len(falla) > 0:
    return {"falla":falla}
  AST = json.loads(json.loads(salida))
  return {"ast":AST}

def astPython(codigo):
  try:
    AST = ast.parse(codigo)
    return {"ast":AST} # TODO
  except e:
    return {"falla":e}

ast.AST.hijos = lambda self : []
ast.Module.hijos = lambda self : self.body
ast.Interactive.hijos = lambda self : self.body
ast.Expression.hijos = lambda self : [self.body]
ast.FunctionDef.hijos = lambda self : self.body
ast.AsyncFunctionDef.hijos = lambda self : self.body
ast.ClassDef.hijos = lambda self : self.body
ast.Return.hijos = lambda self : [] if (self.value is None) else [self.value]
ast.Assign.hijos = lambda self : [self.value]
ast.AugAssign.hijos = lambda self : [self.value]
ast.AnnAssign.hijos = lambda self : [] if (self.value is None) else [self.value]
ast.For.hijos = lambda self : self.body + self.orelse
ast.AsyncFor.hijos = lambda self : self.body + self.orelse
ast.While.hijos = lambda self : self.body + self.orelse
ast.If.hijos = lambda self : self.body + self.orelse
ast.With.hijos = lambda self : self.body
ast.AsyncWith.hijos = lambda self : self.body
ast.Raise.hijos = lambda self : [] if (self.exc is None) else [self.exc]
ast.Try.hijos = lambda self : self.body + self.orelse + self.finalbody