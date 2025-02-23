# -*- coding: utf-8 -*-

from procesos import ejecutar

def analizarGobstones(codigo, reglas):
  ast = astGobstones(codigo)
  return analizarAst(ast, reglas)

def analizarPython(codigo, reglas):
  ast = astPython(codigo)
  return analizarAst(ast, reglas)

def astGobstones(codigo):
  return {} # TODO: invocar a parse

def astPython(codigo):
  return {} # TODO

def analizarAst(ast, reglas):
  return None # TODO (Si está todo bien devuelve None. Si no, devuelve el jsonObj para el cliente)