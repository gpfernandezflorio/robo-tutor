# -*- coding: utf-8 -*-

from reglas import REGLAS, buscarNodosCon_YGenerar_
from utils import aplanar, mapear

class Analizador(object):
  def AnalizarCódigoMalicioso(self, AST, código, desde, hasta):
    resultado = []
    for regla in self.clavesReglasCódigoMalicioso:
      resultadoRegla = self.reglasCódigoMalicioso[regla](self, AST, código)
      AgregarDe_A_Si_(resultadoRegla, resultado, lambda x : está_Entre_Y_(x, desde, hasta))
    return resultado
  def AnalizarAst(self, AST, código, reglas, desde, hasta):
    resultado = []
    for regla in reglas:
      resultadoRegla = self.analizarRegla(AST, código, regla)
      AgregarDe_A_Si_(resultadoRegla, resultado, lambda x : está_Entre_Y_(x, desde, hasta))
    return resultado
  def analizarRegla(self, AST, código, regla):
    if (type(regla) == type(lambda x : 0)):
      return regla(AST, código)
    if regla["key"] in REGLAS:
      return REGLAS[regla["key"]](self, AST, código, regla)
    return [] # ¿Error?

  def nodosDeTipo_(self, AST, tipo):
    return self.foldAST(lambda recs, x : aplanar(recs) + ([x] if self.es_NodoDeTipo_(x, tipo) else []), AST)
  def es_UnComandoCompuesto(self, nodo):
    return self.es_NodoDeTipo_(nodo, self.tiposComandosCompuestos())
  def es_RepeticiónSimple(self, nodo):
    return self.es_NodoDeTipo_(nodo, self.tiposRepeticiónSimple())
  def es_UnNombre(self, nodo):
    return self.es_NodoDeTipo_(nodo, self.tiposNombre())
  def es_NodoImport(self, nodo):
    return self.es_NodoDeTipo_(nodo, self.tiposImport())
  def es_NodoExcepción(self, nodo):
    return self.es_NodoDeTipo_(nodo, self.tiposExcepción())

  def foldAST(self, f, nodo):
    return f(mapear(lambda x : self.foldAST(f,x), self.hijosDeNodo_(nodo)), nodo)
  def nivelAnidaciónComandos_(self, nodo):
    anidacionActual = 0
    nodoActual = nodo
    while nodoActual != None:
      nodoActual = self.nodoMadreDe_(nodoActual)
      if self.es_UnComandoCompuesto(nodoActual):
        anidacionActual = anidacionActual + 1
    return anidacionActual

def AgregarDe_A_Si_(listaFuente, listaDestino, fVal):
  for x in listaFuente:
    if fVal(x):
      listaDestino.append(x)

def está_Entre_Y_(hallazgo, inicio, fin):
  return hallazgo["línea"] >= inicio and hallazgo["línea"] <= fin