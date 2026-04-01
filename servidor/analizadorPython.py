# -*- coding: utf-8 -*-

# Documentación de la clase ast de Python: https://docs.python.org/es/3.12/library/ast.html

import sys
versionDePython = sys.version_info
if versionDePython.major != 3 or versionDePython.minor != 12:
  print("ERROR: este script lo tenés que correr con python 3.12")
  exit()

import ast
from analizadorBase import buscarNodoDeNombreEnAST, buscarNodoImportEnAST, buscarNodoRaiseEnAST, buscarNodoDeTipo_Con_, Analizador
from utils import algunoCumple, aplanar, mapear, singularSiEsta

reglasCódigoMalicioso = {
  "EXIT":lambda analizador, AST : buscarNodoDeNombreEnAST(analizador, AST, "exit"),
  "PRINT":lambda analizador, AST : buscarNodoDeNombreEnAST(analizador, AST, "print"),
  "OPEN":lambda analizador, AST : buscarNodoDeNombreEnAST(analizador, AST, "open"),
  "EXEC":lambda analizador, AST : buscarNodoDeNombreEnAST(analizador, AST, "exec"),
  "EVAL":lambda analizador, AST : buscarNodoDeNombreEnAST(analizador, AST, "eval"),
  "GETATTR":lambda analizador, AST : buscarNodoDeNombreEnAST(analizador, AST, "getattr"),
  "IMPORT":lambda analizador, AST : buscarNodoImportEnAST(analizador, AST),
  "RAISE":lambda analizador, AST : buscarNodoRaiseEnAST(analizador, AST),
  "NombrePrivado":lambda analizador, AST : buscarNodoDeTipo_Con_(analizador, AST, ast.Name,
    lambda n : n.id.startswith("__"), lambda n : n.id
  ),
  "AtributoPrivado":lambda analizador, AST : buscarNodoDeTipo_Con_(analizador, AST, ast.Attribute,
    lambda n : n.attr.startswith("__"), lambda n : n.attr
  )
}

class AnalizadorPython(Analizador):
  def __init__(self, malicioso=reglasCódigoMalicioso.keys()):
    self.clavesReglasCódigoMalicioso = malicioso
    self.reglasCódigoMalicioso = reglasCódigoMalicioso
  def obtenerAst(self, codigo):
    return astPython(codigo)
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
  def hayRepeticiónSimple(self, AST):
    return False # No hay repetición simple en Python
  def hayNombre_(self, AST, nombre):
    return algunoCumple(lambda nodo : nodo.id == nombre, self.nodosDeTipo(AST, ast.Name))
  def hayImport(self, AST):
    return self.hayNodoDeTipo(AST, ast.Import) or \
      self.hayNodoDeTipo(AST, ast.ImportFrom)
  def hayExcepción(self, AST):
    return self.hayNodoDeTipo(AST, ast.Raise)

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
    singularSiEsta(self.returns) +
    self.type_params
  )
  ,
  "AsyncFunctionDef": lambda self : (
    hijosArgumentos(self.args) +
    self.body +
    self.decorator_list +
    singularSiEsta(self.returns) +
    self.type_params
  )
  ,
  "ClassDef": lambda self : (
    self.bases +
    hijosKeywords(self.keywords) +
    self.body +
    self.decorator_list +
    self.type_params
  )
  ,
  "Return": lambda self : singularSiEsta(self.value)
  ,
  "Delete": lambda self : self.targets
  ,
  "Assign": lambda self : self.targets + [self.value]
  ,
  "TypeAlias": lambda self : [self.name,self.value] + self.type_params
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
  "Match": lambda self : ([self.subject] + hijosMatchCase(self.cases))
  ,
  "Raise": lambda self : (singularSiEsta(self.exc) + singularSiEsta(self.cause))
  ,
  "Try": lambda self : (self.body + self.handlers + self.orelse + self.finalbody)
  ,
  "TryStar": lambda self : (self.body + self.handlers + self.orelse + self.finalbody)
  ,
  "Assert": lambda self : ([self.test] + singularSiEsta(self.msg))
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
  "MatchValue": lambda self : [self.value]
  ,
  "MatchSingleton": lambda self : []
  ,
  "MatchSequence": lambda self : self.patterns
  ,
  "MatchMapping": lambda self : self.keys + self.patterns
  ,
  "MatchClass": lambda self : [self.cls] + self.patterns + self.kwd_patterns
  ,
  "MatchStar": lambda self : []
  ,
  "MatchAs": lambda self : singularSiEsta(self.pattern)
  ,
  "MatchOr": lambda self : self.patterns
  ,
  "TypeIgnore": lambda self : []
  ,
  "TypeVar": lambda self : singularSiEsta(self.bound)
  ,
  "ParamSpec": lambda self : []
  ,
  "TypeVarTuple": lambda self : []
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

def hijosMatchCase(cases): # es una lista
  return aplanar(mapear(lambda x : ([x.pattern] + x.body + singularSiEsta(x.guard)), cases))