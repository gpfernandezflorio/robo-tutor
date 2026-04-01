# -*- coding: utf-8 -*-

from analizadorPython import AnalizadorPython
from analizadorGobstones import AnalizadorGobstones
# from analizadorHaskell import AnalizadorHaskell

analizadorPython = AnalizadorPython()
analizadorGobstones = AnalizadorGobstones()
# analizadorHaskell = AnalizadorHaskell()

def analizar(analizador, codigo, reglas, analizarCódigoMalicioso=False):
  AST = analizador.obtenerAst(codigo)
  if "error" in AST:
    AST["resultado"] = "Except"
    return AST
  if analizarCódigoMalicioso:
    resultadoCódigoMalicioso = analizador.analizarCódigoMalicioso(AST["ast"], codigo)
    if not (resultadoCódigoMalicioso is None):
      return resultadoCódigoMalicioso
  return analizador.analizarAst(AST["ast"], codigo, reglas)

def analizarGobstones(codigo, reglas, analizarCódigoMalicioso=False):
  return analizar(analizadorGobstones, codigo, reglas, analizarCódigoMalicioso)

def analizarPython(codigo, reglas, analizarCódigoMalicioso=False):
  return analizar(analizadorPython, codigo, reglas, analizarCódigoMalicioso)

def analizarHaskell(codigo, reglas, analizarCódigoMalicioso=False):
  return None # analizar(analizadorHaskell, codigo, reglas, analizarCódigoMalicioso)