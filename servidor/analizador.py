# -*- coding: utf-8 -*-

from analizadorPython import AnalizadorPython
from analizadorGobstones import AnalizadorGobstones
# from analizadorHaskell import AnalizadorHaskell

analizadorPython = AnalizadorPython()
analizadorGobstones = AnalizadorGobstones()
# analizadorHaskell = AnalizadorHaskell()

def analizar(analizador, código, reglas, extras={}):
  desde = extras["desde"] if "desde" in extras else 1
  hasta = extras["hasta"] if "hasta" in extras else código.count("\n")+1
  analizarCódigoMalicioso = extras["evil"] if "evil" in extras else False
  ruta = extras["ruta"] if "ruta" in extras else "."

  AST = analizador.obtenerAst(código, ruta)
  if "error" in AST:
    AST["resultado"] = "Except"
    return AST
  if analizarCódigoMalicioso:
    resultadoCódigoMalicioso = analizador.AnalizarCódigoMalicioso(AST["ast"], código, desde, hasta)
    if len(resultadoCódigoMalicioso) > 0:
      return {"resultado":"EVIL", "error":textoAPartirDeLista(resultadoCódigoMalicioso)}
  resultadoAnálisisCalidad = analizador.AnalizarAst(AST["ast"], código, reglas, desde, hasta)
  if len(resultadoAnálisisCalidad) > 0:
    return {"resultado":"Calidad", "error":textoAPartirDeLista(resultadoAnálisisCalidad)}
  return None

def analizarGobstones(código, reglas, extras={}):
  return analizar(analizadorGobstones, código, reglas, extras)

def analizarPython(código, reglas, extras={}):
  return analizar(analizadorPython, código, reglas, extras)

def analizarHaskell(código, reglas, extras={}):
  return None # analizar(analizadorHaskell, código, reglas, extras)

def textoAPartirDeLista(lista):
  return lista[0]["msg"] # Por ahora sólo devuelvo el primero porque las funciones de buscar_falla asumen que es uno sólo.