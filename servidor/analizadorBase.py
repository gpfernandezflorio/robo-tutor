# -*- coding: utf-8 -*-

from reglas import REGLAS
from utils import aplanar, mapear

def buscarNodoDeNombreEnAST(analizador, AST, nombre):
  if analizador.hayNombre_(AST, nombre):
    return "No está permitido usar '" + nombre + "'"
  return None

def buscarNodoImportEnAST(analizador, AST):
  return "No está permitido importar módulos" if (
    analizador.hayImport(AST)
  ) else None

def buscarNodoRaiseEnAST(analizador, AST):
  return "No está permitido generar excepciones" if (
    analizador.hayExcepción(AST)
  ) else None

def buscarNodoDeTipo_Con_(analizador, AST, tipo, fVal, fMsg):
  for nodo in analizador.nodosDeTipo(AST, tipo):
    if fVal(nodo):
      return "No está permitido usar '" + fMsg(nodo) + "'"
  return None

class Analizador(object):
  def analizarCódigoMalicioso(self, AST, código):
    cm = self.verificarCodigoMalicioso(AST, código)
    if not (cm is None):
      return {"resultado":"EVIL", "error":cm}
    return None
  def verificarCodigoMalicioso(self, AST, código):
    for regla in self.clavesReglasCódigoMalicioso:
      resultado = self.reglasCódigoMalicioso[regla](self, AST)
      if not (resultado is None):
        return resultado
    return None
  def analizarAst(self, AST, código, reglas):
    for regla in reglas:
      resultado = self.analizarRegla(AST, código, regla)
      if not(resultado is None):
        return resultado
    return None
  def analizarRegla(self, AST, código, regla):
    error = ""
    if (type(regla) == type(lambda x : 0)):
      error = regla(AST, código)
    elif regla["key"] in REGLAS:
      error = REGLAS[regla["key"]](self, AST, código, regla)
    if (error is None) or len(error) == 0:
      return None
    return {"resultado":"Calidad", "error":error}

  def nodosDeTipo(self, AST, tipo):
    return self.foldAST(lambda recs, x : aplanar(recs) + ([x] if self.esNodoDeTipo(x, tipo) else []), AST)
  def hayNodoDeTipo(self, AST, tipo):
    return self.foldAST(lambda recs, x : any(recs) or self.esNodoDeTipo(x, tipo), AST)
  def foldAST(self, f, nodo):
    return f(mapear(lambda x : self.foldAST(f,x), self.hijosDeNodo(nodo)), nodo)
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