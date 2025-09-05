# -*- coding: utf-8 -*-

# Documentación de la clase ast de Python: https://docs.python.org/es/3.9/library/ast.html
# Definición de la clase ASTNode de Gobstones: https://github.com/gobstones/gobstones-parser/blob/main/src/parser/ast.ts

import json
import ast
from procesos import ejecutar
from utils import algunoCumple, aplanar, mapear, singularSiEsta
from reglas import REGLAS

class Analizador(object):
  def analizarAst(self, AST, codigo, reglas):
    cm = self.verificarCodigoMalicioso(AST, codigo)
    if not (cm is None):
      return {"resultado":"EVIL", "error":cm}
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

  def nodosDeTipo(self, AST, tipo):
    return self.foldAST(lambda recs, x : aplanar(recs) + ([x] if self.esNodoDeTipo(x, tipo) else []), AST)
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

class AnalizadorPython(Analizador):
  def obtenerAst(self, codigo):
    return astPython(codigo)
  def verificarCodigoMalicioso(self, AST, codigo):
    for nodo in self.nodosDeTipo(AST, ast.Name):
      if nodo.id in ["exit","print","open"]:
        return "No está permitido usar '" + nodo.id + "'"
    for nodo in self.nodosDeTipo(AST, ast.Import) + self.nodosDeTipo(AST, ast.ImportFrom):
      return "No está permitido importar módulos"
    return None
  def hijosDeNodo(self, nodo):
    if not isinstance(nodo, ast.AST):
      breakpoint()
    return nodo.hijos()
  def esNodoDeTipo(self, nodo, tipo):
    return isinstance(nodo, tipo)
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
  def verificarCodigoMalicioso(self, AST, codigo):
    return None
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
# mod
ast.Module.hijos = lambda self : (self.body + self.type_ignores)
ast.Interactive.hijos = lambda self : self.body
ast.Expression.hijos = lambda self : [self.body]
ast.FunctionType.hijos = lambda self : (self.argtypes + [self.returns])
# stmt
ast.FunctionDef.hijos = lambda self : (
  hijosArgumentos(self.args) +
  self.body +
  self.decorator_list +
  singularSiEsta(self.returns)
)
ast.AsyncFunctionDef.hijos = lambda self : (
  hijosArgumentos(self.args) +
  self.body +
  self.decorator_list +
  singularSiEsta(self.returns)
)
ast.ClassDef.hijos = lambda self : (
  self.bases +
  hijosKeywords(self.keywords) +
  self.body +
  self.decorator_list
)
ast.Return.hijos = lambda self : singularSiEsta(self.value)
ast.Delete.hijos = lambda self : self.targets
ast.Assign.hijos = lambda self : self.targets + [self.value]
ast.AugAssign.hijos = lambda self : [self.target, self.op, self.value]
ast.AnnAssign.hijos = lambda self : ([self.target, self.annotation] +
  singularSiEsta(self.value))
ast.For.hijos = lambda self : ([self.target, self.iter] + self.body + self.orelse)
ast.AsyncFor.hijos = lambda self : ([self.target, self.iter] + self.body + self.orelse)
ast.While.hijos = lambda self : ([self.test] + self.body + self.orelse)
ast.If.hijos = lambda self : ([self.test] + self.body + self.orelse)
ast.With.hijos = lambda self : (hijosWithitem(self.items) + self.body)
ast.AsyncWith.hijos = lambda self : (hijosWithitem(self.items) + self.body)
ast.Raise.hijos = lambda self : (singularSiEsta(self.exc) + singularSiEsta(self.cause))
ast.Try.hijos = lambda self : (self.body + self.handlers + self.orelse + self.finalbody)
ast.Assert.hijos = lambda self : (self.test + singularSiEsta(self.msg))
ast.Import.hijos = lambda self : []
ast.ImportFrom.hijos = lambda self : []
ast.Global.hijos = lambda self : []
ast.Nonlocal.hijos = lambda self : []
ast.Expr.hijos = lambda self : [self.value]
ast.Pass.hijos = lambda self : []
ast.Break.hijos = lambda self : []
ast.Continue.hijos = lambda self : []
# expr
ast.BoolOp.hijos = lambda self : ([self.op] + self.values)
ast.NamedExpr.hijos = lambda self : [self.target, self.value]
ast.BinOp.hijos = lambda self : [self.left, self.op, self.right]
ast.UnaryOp.hijos = lambda self : [self.op, self.operand]
ast.Lambda.hijos = lambda self : (hijosArgumentos(self.args) + [self.body])
ast.IfExp.hijos = lambda self : [self.test, self.body, self.orelse]
ast.Dict.hijos = lambda self : (self.keys + self.values)
ast.Set.hijos = lambda self : self.elts
ast.ListComp.hijos = lambda self : ([self.elt] + hijosComprehension(self.generators))
ast.SetComp.hijos = lambda self : ([self.elt] + hijosComprehension(self.generators))
ast.DictComp.hijos = lambda self : ([self.key, self.value] + hijosComprehension(self.generators))
ast.GeneratorExp.hijos = lambda self : ([self.elt] + hijosComprehension(self.generators))
ast.Await.hijos = lambda self : [self.value]
ast.Yield.hijos = lambda self : singularSiEsta(self.value)
ast.YieldFrom.hijos = lambda self : [self.value]
ast.Compare.hijos = lambda self : ([self.left] + self.ops + self.comparators)
ast.Call.hijos = lambda self : ([self.func] + self.args + hijosKeywords(self.keywords))
ast.FormattedValue.hijos = lambda self : ([self.value] + singularSiEsta(self.format_spec))
ast.JoinedStr.hijos = lambda self : self.values
ast.Constant.hijos = lambda self : []
ast.Attribute.hijos = lambda self : [self.value, self.ctx]
ast.Subscript.hijos = lambda self : [self.value, self.slice, self.ctx]
ast.Starred.hijos = lambda self : [self.value, self.ctx]
ast.Name.hijos = lambda self : [self.ctx]
ast.List.hijos = lambda self : self.elts + [self.ctx]
ast.Tuple.hijos = lambda self : self.elts + [self.ctx]
ast.Slice.hijos = lambda self : (
  singularSiEsta(self.lower) +
  singularSiEsta(self.upper) +
  singularSiEsta(self.step)
)
# expr_context
ast.Load.hijos = lambda self : []
ast.Store.hijos = lambda self : []
ast.Del.hijos = lambda self : []
# boolop
ast.And.hijos = lambda self : []
ast.Or.hijos = lambda self : []
# operator
ast.Add.hijos = lambda self : []
ast.Sub.hijos = lambda self : []
ast.Mult.hijos = lambda self : []
ast.MatMult.hijos = lambda self : []
ast.Div.hijos = lambda self : []
ast.Mod.hijos = lambda self : []
ast.Pow.hijos = lambda self : []
ast.LShift.hijos = lambda self : []
ast.RShift.hijos = lambda self : []
ast.BitOr.hijos = lambda self : []
ast.BitXor.hijos = lambda self : []
ast.BitAnd.hijos = lambda self : []
ast.FloorDiv.hijos = lambda self : []
# unaryop
ast.Invert.hijos = lambda self : []
ast.Not.hijos = lambda self : []
ast.UAdd.hijos = lambda self : []
ast.USub.hijos = lambda self : []
# cmpop
ast.Eq.hijos = lambda self : []
ast.NotEq.hijos = lambda self : []
ast.Lt.hijos = lambda self : []
ast.LtE.hijos = lambda self : []
ast.Gt.hijos = lambda self : []
ast.GtE.hijos = lambda self : []
ast.Is.hijos = lambda self : []
ast.IsNot.hijos = lambda self : []
ast.In.hijos = lambda self : []
ast.NotIn.hijos = lambda self : []
ast.ExceptHandler.hijos = lambda self : (singularSiEsta(self.type) + self.body)
ast.TypeIgnore.hijos = lambda self : []

def hijosArgumentos(args): # es uno
  return (
    hijosArgumento(args.posonlyargs) +
    hijosArgumento(args.args) +
    ([] if (args.vararg is None) else hijosArgumento([args.vararg])) + 
    hijosArgumento(args.kwonlyargs) +
    hijosArgumento(args.kw_defaults) +
    ([] if (args.kwarg is None) else hijosArgumento([args.kwarg])) + 
    args.defaults
  )

def hijosArgumento(args): # es una lista
  return aplanar(mapear(lambda x : singularSiEsta(x.annotation), args))

def hijosKeywords(keywords): # es una lista
  return mapear(lambda x : x.value, keywords)

def hijosWithitem(withitem): # es una lista
  return aplanar(mapear(lambda x : ([x.context_expr] + singularSiEsta(x.optional_vars)), withitem))

def hijosComprehension(comprehension): # es una lista
  return aplanar(mapear(lambda x : ([x.target,x.iter] + x.ifs), withitem))
