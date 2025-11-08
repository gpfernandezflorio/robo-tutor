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
    return HIJOS[type(nodo).__name__](nodo)
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
  if "error" in AST:
    AST["resultado"] = "Except"
    return AST
  return analizador.analizarAst(AST["ast"], codigo, reglas)

def analizarGobstones(codigo, reglas):
  return analizar(analizadorGobstones, codigo, reglas)

def analizarPython(codigo, reglas):
  return analizar(analizadorPython, codigo, reglas)

def astGobstones(codigo):
  errcode, salida, falla = ejecutar("node gobstones-lang/dist/gobstones-lang parse -l es -i src.txt")
  if len(falla) > 0:
    return {"error":falla}
  AST = json.loads(json.loads(salida))
  return {"ast":AST}

def astPython(codigo):
  try:
    AST = ast.parse(codigo)
    return {"ast":AST} # TODO
  except Exception as e:
    return {"error":str(e).replace("<unknown>, ","").replace("line","línea")}

HIJOS = {
  "AST": lambda self : []
  # mod
  ,
  "Module": lambda self : (self.body + self.type_ignores)
  ,
  "Interactive": lambda self : self.body
  ,
  "Expression": lambda self : [self.body]
  ,
  "FunctionType": lambda self : (self.argtypes + [self.returns])
  # stmt
  ,
  "FunctionDef": lambda self : (
    hijosArgumentos(self.args) +
    self.body +
    self.decorator_list +
    singularSiEsta(self.returns)
  )
  ,
  "AsyncFunctionDef": lambda self : (
    hijosArgumentos(self.args) +
    self.body +
    self.decorator_list +
    singularSiEsta(self.returns)
  )
  ,
  "ClassDef": lambda self : (
    self.bases +
    hijosKeywords(self.keywords) +
    self.body +
    self.decorator_list
  )
  ,
  "Return": lambda self : singularSiEsta(self.value)
  ,
  "Delete": lambda self : self.targets
  ,
  "Assign": lambda self : self.targets + [self.value]
  ,
  "AugAssign": lambda self : [self.target, self.op, self.value]
  ,
  "AnnAssign": lambda self : ([self.target, self.annotation] +
    singularSiEsta(self.value))
  ,
  "For": lambda self : ([self.target, self.iter] + self.body + self.orelse)
  ,
  "AsyncFor": lambda self : ([self.target, self.iter] + self.body + self.orelse)
  ,
  "While": lambda self : ([self.test] + self.body + self.orelse)
  ,
  "If": lambda self : ([self.test] + self.body + self.orelse)
  ,
  "With": lambda self : (hijosWithitem(self.items) + self.body)
  ,
  "AsyncWith": lambda self : (hijosWithitem(self.items) + self.body)
  ,
  "Raise": lambda self : (singularSiEsta(self.exc) + singularSiEsta(self.cause))
  ,
  "Try": lambda self : (self.body + self.handlers + self.orelse + self.finalbody)
  ,
  "Assert": lambda self : (self.test + singularSiEsta(self.msg))
  ,
  "Import": lambda self : []
  ,
  "ImportFrom": lambda self : []
  ,
  "Global": lambda self : []
  ,
  "Nonlocal": lambda self : []
  ,
  "Expr": lambda self : [self.value]
  ,
  "Pass": lambda self : []
  ,
  "Break": lambda self : []
  ,
  "Continue": lambda self : []
  # expr
  ,
  "BoolOp": lambda self : ([self.op] + self.values)
  ,
  "NamedExpr": lambda self : [self.target, self.value]
  ,
  "BinOp": lambda self : [self.left, self.op, self.right]
  ,
  "UnaryOp": lambda self : [self.op, self.operand]
  ,
  "Lambda": lambda self : (hijosArgumentos(self.args) + [self.body])
  ,
  "IfExp": lambda self : [self.test, self.body, self.orelse]
  ,
  "Dict": lambda self : (self.keys + self.values)
  ,
  "Set": lambda self : self.elts
  ,
  "ListComp": lambda self : ([self.elt] + hijosComprehension(self.generators))
  ,
  "SetComp": lambda self : ([self.elt] + hijosComprehension(self.generators))
  ,
  "DictComp": lambda self : ([self.key, self.value] + hijosComprehension(self.generators))
  ,
  "GeneratorExp": lambda self : ([self.elt] + hijosComprehension(self.generators))
  ,
  "Await": lambda self : [self.value]
  ,
  "Yield": lambda self : singularSiEsta(self.value)
  ,
  "YieldFrom": lambda self : [self.value]
  ,
  "Compare": lambda self : ([self.left] + self.ops + self.comparators)
  ,
  "Call": lambda self : ([self.func] + self.args + hijosKeywords(self.keywords))
  ,
  "FormattedValue": lambda self : ([self.value] + singularSiEsta(self.format_spec))
  ,
  "JoinedStr": lambda self : self.values
  ,
  "Constant": lambda self : []
  ,
  "Attribute": lambda self : [self.value, self.ctx]
  ,
  "Subscript": lambda self : [self.value, self.slice, self.ctx]
  ,
  "Starred": lambda self : [self.value, self.ctx]
  ,
  "Name": lambda self : [self.ctx]
  ,
  "List": lambda self : self.elts + [self.ctx]
  ,
  "Tuple": lambda self : self.elts + [self.ctx]
  ,
  "Slice": lambda self : (
    singularSiEsta(self.lower) +
    singularSiEsta(self.upper) +
    singularSiEsta(self.step)
  )
  # expr_context
  ,
  "Load": lambda self : []
  ,
  "Store": lambda self : []
  ,
  "Del": lambda self : []
  # boolop
  ,
  "And": lambda self : []
  ,
  "Or": lambda self : []
  # operator
  ,
  "Add": lambda self : []
  ,
  "Sub": lambda self : []
  ,
  "Mult": lambda self : []
  ,
  "MatMult": lambda self : []
  ,
  "Div": lambda self : []
  ,
  "Mod": lambda self : []
  ,
  "Pow": lambda self : []
  ,
  "LShift": lambda self : []
  ,
  "RShift": lambda self : []
  ,
  "BitOr": lambda self : []
  ,
  "BitXor": lambda self : []
  ,
  "BitAnd": lambda self : []
  ,
  "FloorDiv": lambda self : []
  # unaryop
  ,
  "Invert": lambda self : []
  ,
  "Not": lambda self : []
  ,
  "UAdd": lambda self : []
  ,
  "USub": lambda self : []
  # cmpop
  ,
  "Eq": lambda self : []
  ,
  "NotEq": lambda self : []
  ,
  "Lt": lambda self : []
  ,
  "LtE": lambda self : []
  ,
  "Gt": lambda self : []
  ,
  "GtE": lambda self : []
  ,
  "Is": lambda self : []
  ,
  "IsNot": lambda self : []
  ,
  "In": lambda self : []
  ,
  "NotIn": lambda self : []
  ,
  "ExceptHandler": lambda self : (singularSiEsta(self.type) + self.body)
  ,
  "TypeIgnore": lambda self : []
}

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
  return aplanar(mapear(lambda x : ([x.target,x.iter] + x.ifs), comprehension))