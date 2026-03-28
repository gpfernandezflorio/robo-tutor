# -*- coding: utf-8 -*-

# Documentación de la clase ast de Python: https://docs.python.org/es/3.12/library/ast.html

# Definición de la clase ASTNode de Gobstones: https://github.com/gobstones/gobstones-parser/blob/main/src/parser/ast.ts

# Documentación del parser de Haskell https://hackage.haskell.org/package/haskell-src-exts-1.23.1/docs/Language-Haskell-Exts-Syntax.html

import json
import ast
from procesos import ejecutar, rutaJail
from utils import algunoCumple, aplanar, mapear, singularSiEsta
from reglas import REGLAS

evitandoCódigoMalicioso = False

import sys
versionDePython = sys.version_info
if versionDePython.major != 3 or versionDePython.minor != 12:
  print("ERROR: este script lo tenés que correr con python 3.12")
  exit()

def EvitarCódigoMalicioso():
  global evitandoCódigoMalicioso
  evitandoCódigoMalicioso = True

def PermitirCódigoMalicioso():
  global evitandoCódigoMalicioso
  evitandoCódigoMalicioso = False

class Analizador(object):
  def analizarAst(self, AST, codigo, reglas):
    if evitandoCódigoMalicioso:
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

def buscarNodoDeNombreEnAST(analizador, AST, nombre):
  for nodo in analizador.nodosDeTipo(AST, ast.Name):
    if nodo.id == nombre:
      return "No está permitido usar '" + nodo.id + "'"
  return None

def buscarNodoImportEnAST(analizador, AST):
  return "No está permitido importar módulos" if (
    analizador.hayNodoDeTipo(AST, ast.Import) or
    analizador.hayNodoDeTipo(AST, ast.ImportFrom)
  ) else None

def buscarNodoRaiseEnAST(analizador, AST):
  return "No está permitido generar excepciones" if (
    analizador.hayNodoDeTipo(AST, ast.Raise)
  ) else None

def buscarNodoDeTipo_Con_(analizador, AST, tipo, fVal, fMsg):
  for nodo in analizador.nodosDeTipo(AST, tipo):
    if f(nodo):
      return "No está permitido usar '" + fMsg(nodo) + "'"
  return None

reglasCódigoMalicioso = {
  "PYTHON":{
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
  },
  "HASKELL":{
    # TODO
  }
}

class AnalizadorPython(Analizador):
  def __init__(self, malicioso=reglasCódigoMalicioso["PYTHON"].keys()):
    self.reglasCódigoMalicioso = malicioso
  def obtenerAst(self, codigo):
    return astPython(codigo)
  def verificarCodigoMalicioso(self, AST, codigo):
    for regla in self.reglasCódigoMalicioso:
      resultado = reglasCódigoMalicioso["PYTHON"][regla](self, AST)
      if not (resultado is None):
        return resultado
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
  def hayRepeticiónSimple(self, AST):
    return False # No hay repetición simple en Python

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
  def hayRepeticiónSimple(self, AST):
    return self.hayNodoDeTipo(AST, "N_StmtRepeat")

class AnalizadorHaskell(Analizador):
  def __init__(self, malicioso=reglasCódigoMalicioso["HASKELL"].keys()):
    self.reglasCódigoMalicioso = malicioso
  def obtenerAst(self, codigo):
    return astHaskell(codigo)
  def verificarCodigoMalicioso(self, AST, codigo):
    for regla in self.reglasCódigoMalicioso:
      resultado = reglasCódigoMalicioso["HASKELL"][regla](self, AST)
      if not (resultado is None):
        return resultado
    return None
  def hijosDeNodo(self, nodo):
    hijosPorAhora = []
    for k in nodo:
      if not (k in ["tipo", "en", "valor", "original"]):
        másHijos = nodo[k]
        for hijo in (másHijos if (type(másHijos) == type([])) else [másHijos]):
          hijosPorAhora.append(hijo)
    return hijosPorAhora
  def esNodoDeTipo(self, nodo, tipo):
    return nodo["tipo"] == tipo
  def esUnComandoCompuesto(self, nodo):
    return False # No hay comandos compuestos en Haskell
  def hayRepeticiónSimple(self, AST):
    return False # No hay repetición simple en Haskell

analizadorPython = AnalizadorPython()

analizadorGobstones = AnalizadorGobstones()

analizadorHaskell = AnalizadorHaskell()

def analizar(analizador, codigo, reglas):
  AST = analizador.obtenerAst(codigo)
  if "error" in AST:
    AST["resultado"] = "Except"
    return AST
  elif "evil" in AST: # Algunos analizadores (como el de Haskell) ya pueden arrojar esto al obtener el AST
    AST["resultado"] = "EVIL"
    return AST
  return analizador.analizarAst(AST["ast"], codigo, reglas)

def analizarGobstones(codigo, reglas):
  return analizar(analizadorGobstones, codigo, reglas)

def analizarPython(codigo, reglas):
  return analizar(analizadorPython, codigo, reglas)

def analizarHaskell(codigo, reglas):
  return analizar(analizadorHaskell, codigo, reglas)

def astGobstones(codigo):
  f = open(rutaJail("src.txt"), 'w')
  f.write(codigo)
  f.close()
  errcode, salida, falla = ejecutar("node /rtTest/gbs/dist/gobstones-lang parse -l es -i src.txt")
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

def astHaskell(codigo):
  f = open(rutaJail('src.hs'), 'w')
  f.write("{-# LANGUAGE TemplateHaskell #-}\n{-# LANGUAGE DataKinds #-}\n\n" + codigo)
  f.close()
  errcode, salida, falla = ejecutar("echo 'main' | ghci -v0 /rtTest/parser.hs")
  if len(falla) > 0:
    # No debería pasar. Si el parser falla devuelve ParseFailed por stdout.
    pass

  # print(errcode)

  haskellParser.parse(salida)
  if haskellParser.hayElementoProhibido():
    return {"evil":"No se puede procesar porque se están usando elementos del lenguaje que no están permitidos"}
  if haskellParser.falló():
    return {"error":haskellParser.errorMsg() + "\n\n" + haskellParser.ubicaciónATexto(haskellParser.errorLoc())}
  return {"ast":haskellParser.ast()}

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

class HaskellParser(object):
  def parse(self, salida):
    self.resultado = "OK"
    self.mensajeError = ""
    self.ubicaciónDelError = ""
    self.raíz = None
    self.salidaCompleta = salida
    self.salida = salida
    self.parenStack = []
    if self.salida.startswith("ParseFailed"):
      self.resultado = "FAIL"
      self.AvanzarSalida(len("ParseFailed"))
      self.ubicaciónDelError = self.parsearUbicación()
      self.mensajeError = self.parsearString()
      return
    if self.salida.startswith("ParseOk"):
      self.AvanzarSalida(len("ParseOk"))
      self.raíz = self.parsearNodoRaíz()
      return
    self.errorDesconocido("La salida no empieza con (ParseOk) ni con (ParseFailed)")
  def elementoProhibido(self):
    self.resultado = "EVIL"
  def ubicaciónATexto(self, ubicación):
    return "Línea " + str(ubicación["línea"] - 3) + ", columna " + str(ubicación["columna"])
  def errorDesconocido(self, mensaje):
    # print(mensaje)
    # import traceback
    # traceback.print_stack()
    # f = open('hsParseErr.txt', 'w')
    # f.write(mensaje + "\n\n" + self.salida + "\n\n" + self.salidaCompleta)
    # f.close()
    # exit()
    pass # TODO: probablemente sea un bug en el servidor
  def ast(self):
    return self.raíz
  def falló(self):
    return self.resultado == "FAIL"
  def hayElementoProhibido(self):
    return self.resultado == "EVIL"
  def errorMsg(self):
    return self.mensajeError
  def errorLoc(self):
    return self.ubicaciónDelError
  def AvanzarSalida(self, i):
    self.salida = self.salida[i +
      (1 if i < len(self.salida) and self.salida[i] == " " else 0)
    :]
  def abreParen(self):
    if self.salida.startswith('('):
      self.AvanzarSalida(1)
      self.parenStack.append(True)
    else:
      self.parenStack.append(False)
  def cierraParen(self):
    paren = self.parenStack.pop()
    if paren:
      if self.salida.startswith(')'):
        self.AvanzarSalida(1)
      else:
        self.errorDesconocido("La falta cerrar un paréntesis: ')'")

  ## Tipos auxiliares
  def parsearUbicación(self):
    # SrcLoc "..." l c | SrcSpanInfo { srcInfoSpan = (SrcSpan ...), srcInfoPoints = [(SrcSpan ...)] }
    self.abreParen()
    if self.salida.startswith('SrcLoc'):
      self.AvanzarSalida(len('SrcLoc'))
      self.parsearString()
      línea = self.parsearNúmero()
      columna = self.parsearNúmero()
      self.cierraParen()
      return {"línea":línea, "columna":columna}
    if self.salida.startswith('SrcSpanInfo'):
      self.AvanzarSalida(len('SrcSpanInfo'))
      registro = self.parsearRegistro([
        ["srcInfoSpan", getattr(self, "parsearSrcSpan")],
        ["srcInfoPoints", self.fParsearLista("parsearSrcSpan")]
      ])["srcInfoSpan"]
      self.cierraParen()
      return registro
    self.errorDesconocido("La ubicación no empieza con 'SrcLoc' ni con 'SrcSpanInfo'")
  def parsearSrcSpan(self):
    # SrcSpan "..." l c
    self.abreParen()
    if self.salida.startswith('SrcSpan'):
      self.AvanzarSalida(len('SrcSpan'))
      self.parsearString()
      línea = self.parsearNúmero()
      columna = self.parsearNúmero()
      self.parsearNúmero()
      self.parsearNúmero()
      self.cierraParen()
      return {"línea":línea, "columna":columna}
    self.errorDesconocido("La ubicación no empieza con 'SrcSpan'")
  def parsearString(self):
    # "..." | '...'
    if self.salida.startswith('"'):
      i = posCaracterNoEscapeado(self.salida, '"', '\\"', 1)
    elif self.salida.startswith("'"):
      i = posCaracterNoEscapeado(self.salida, "'", "\\'", 1)
    else:
      self.errorDesconocido("El string no empieza con \" ni con '")
    contenido = self.salida[1:i]
    self.AvanzarSalida(i+1)
    return contenido
  def parsearNúmero(self):
    # n
    i = 0
    while i < len(self.salida) and esCharNumérico(self.salida[i]):
      i += 1
    if i == 0:
      self.errorDesconocido("El número no empieza con caracteres numéricos")
    n = int(self.salida[:i])
    self.AvanzarSalida(i)
    return n
  def parsearRegistro(self, clavesYFunciones):
    # { clavei = valori }
    resultado = {}
    if self.salida.startswith("{"):
      self.AvanzarSalida(1)
      for claveYFunción in clavesYFunciones:
        if self.salida.startswith(claveYFunción[0]):
          self.AvanzarSalida(len(claveYFunción[0]))
          if self.salida.startswith("="):
            self.AvanzarSalida(1)
            resultado[claveYFunción[0]] = claveYFunción[1]()
            if self.salida.startswith(",") or self.salida.startswith("}"):
              self.AvanzarSalida(1)
            else:
              self.errorDesconocido("Registro mal formado (no cierra con '}' y no sigue con ',')")
          else:
            self.errorDesconocido("Registro mal formado (falta el '=')")
        else:
          self.errorDesconocido("Registro mal formado (no aparece la clave '" + claveYFunción[0] + "')")
    else:
      self.errorDesconocido("Registro mal formado (no abre con '{')")
    return resultado
  def parsearLista(self, fElemento):
    # [ elementoi ]
    resultado = []
    if self.salida.startswith("["):
      self.AvanzarSalida(1)
      finLista = self.salida.startswith("]")
      f = getattr(self, fElemento)
      while not finLista:
        resultado.append(f())
        if self.salida.startswith(","):
          self.AvanzarSalida(1)
        elif self.salida.startswith("]"):
          finLista = True
        else:
          self.errorDesconocido("Lista mal formada")
      self.AvanzarSalida(1)
    return resultado
  def fParsearLista(self, fElemento):
    return lambda: getattr(self, "parsearLista")(fElemento)
  def parsearMaybe(self, fElemento):
    # Nothing | Just v
    self.abreParen()
    if self.salida.startswith('Nothing'):
      self.AvanzarSalida(len('Nothing'))
      self.cierraParen()
      return {
        "tipo":"Nada"
      }
    if self.salida.startswith('Just'):
      self.AvanzarSalida(len('Just'))
      dato = getattr(self, fElemento)()
      self.cierraParen()
      return dato
    self.errorDesconocido("El Maybe no empieza con 'Nothing' ni con 'Just'")
  
  ## Nodos
  def parsearNodoRaíz(self):
    # Module
    self.abreParen()
    if self.salida.startswith('Module'):
      self.AvanzarSalida(len('Module'))
      ubicación = self.parsearUbicación()
      encabezado = self.parsearMaybe("parsearModuleHead")
      pragmas = self.parsearLista("parsearModulePragma")
      imports = self.parsearLista("parsearImportDecl")
      declaraciones = self.parsearLista("parsearDecl")
      self.cierraParen()
      return {
        "tipo":"Módulo",
        "en":ubicación,
        "declaraciones":declaraciones
      }
    if self.salida.startswith('XmlPage'):
      self.cierraParen()
      self.elementoProhibido() # TODO: https://hackage.haskell.org/package/haskell-src-exts-1.23.1/docs/Language-Haskell-Exts-Syntax.html#g:1
      return
    if self.salida.startswith('XmlHybrid'):
      self.cierraParen()
      self.elementoProhibido() # TODO
      return
    self.errorDesconocido("Nodo desconocido")
  def parsearModuleHead(self):
    # Encabezado de módulo
    self.abreParen()
    if self.salida.startswith('ModuleHead'):
      self.AvanzarSalida(len('ModuleHead'))
      self.parsearUbicación()
      nombre = self.parsearNombreMódulo()
      advertencia = self.parsearMaybe("parsearWarningText")
      exports = self.parsearMaybe("parsearExportSpecList")
      self.cierraParen()
      return {
        "tipo":"EncabezadoMódulo",
        "en":ubicación,
        "nombre":nombre
      }
    self.errorDesconocido("El encabezado del módulo no empieza con 'ModuleHead'")
  def parsearNombreMódulo(self):
    # Nombre de módulo
    self.abreParen()
    if self.salida.startswith('ModuleName'):
      self.AvanzarSalida(len('ModuleName'))
      self.parsearUbicación()
      nombre = self.parsearString()
      self.cierraParen()
      return {
        "tipo":"Nombre",
        "en":ubicación,
        "valor":nombre
      }
    self.errorDesconocido("El nombre del módulo no empieza con 'ModuleName'")
  def parsearWarningText(self):
    # Texto de advertencia (?)
    self.abreParen()
    if self.salida.startswith('DeprText'):
      self.AvanzarSalida(len('DeprText'))
      self.parsearUbicación()
      texto = self.parsearString()
      self.cierraParen()
      return texto
    self.abreParen()
    if self.salida.startswith('WarnText'):
      self.AvanzarSalida(len('WarnText'))
      self.parsearUbicación()
      texto = self.parsearString()
      self.cierraParen()
      return texto
    self.errorDesconocido("El texto de advertencia no empieza con 'DeprText' ni con 'WarnText'")
  def parsearExportSpecList(self):
    # Lista de exports
    self.abreParen()
    if self.salida.startswith('ExportSpecList'):
      self.AvanzarSalida(len('ExportSpecList'))
      self.parsearUbicación()
      exports = self.parsearLista("parsearExportSpec")
      self.cierraParen()
      return exports
    self.errorDesconocido("La lista de exports no empieza con 'ExportSpecList'")
  def parsearExportSpec(self):
    # Un export
    self.abreParen()
    if self.salida.startswith('EVar'):
      self.AvanzarSalida(len('EVar'))
      self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return nombre
    if self.salida.startswith('EAbs'):
      self.AvanzarSalida(len('EAbs'))
      self.parsearUbicación()
      nameSpace = self.parsearNameSpace()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return nombre
    if self.salida.startswith('EThingWith'):
      self.AvanzarSalida(len('EThingWith'))
      self.parsearUbicación()
      self.parsearWildCard()
      nombre = self.parsearNombreQ()
      nombresSub = self.parsearLista("parsearNombreC")
      self.cierraParen()
      return nombre
    if self.salida.startswith('EModuleContents'):
      self.AvanzarSalida(len('EModuleContents'))
      self.parsearUbicación()
      nombre = self.parsearNombreMódulo()
      self.cierraParen()
      return nombre
    self.errorDesconocido("El export no empieza con 'EVar', 'EAbs', 'EThingWith' ni con 'EModuleContents'")
  def parsearNameSpace(self):
    # Un nameSpace
    self.abreParen()
    if self.salida.startswith('NoNamespace'):
      self.AvanzarSalida(len('NoNamespace'))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "tipo":"NameSpace"
      }
    if self.salida.startswith('TypeNamespace'):
      self.AvanzarSalida(len('TypeNamespace'))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "tipo":"NameSpace"
      }
    if self.salida.startswith('PatternNamespace'):
      self.AvanzarSalida(len('PatternNamespace'))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "tipo":"NameSpace"
      }
    self.errorDesconocido("El NameSpace no empieza con 'NoNamespace', con 'TypeNamespace' ni con 'PatternNamespace'")
  def parsearWildCard(self):
    # Un wildcard
    self.abreParen()
    if self.salida.startswith('NoWildcard'):
      self.AvanzarSalida(len('NoWildcard'))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "tipo":"WildCard"
      }
    if self.salida.startswith('EWildcard'):
      self.AvanzarSalida(len('EWildcard'))
      self.parsearUbicación()
      self.parsearNúmero()
      self.cierraParen()
      return {
        "tipo":"WildCard"
      }
    self.errorDesconocido("El WildCard no empieza con 'NoWildcard', ni con 'EWildcard'")
  def parsearModulePragma(self):
    # Un pragma
    self.abreParen()
    if self.salida.startswith('LanguagePragma'):
      self.AvanzarSalida(len('LanguagePragma'))
      self.parsearUbicación()
      self.parsearLista("parsearNombre")
      self.cierraParen()
      return {
        "tipo":"Pragma"
      }
    if self.salida.startswith('OptionsPragma'):
      self.AvanzarSalida(len('OptionsPragma'))
      self.parsearUbicación()
      self.parsearMaybe("parsearTool")
      self.parsearString()
      self.cierraParen()
      return {
        "tipo":"Pragma"
      }
    if self.salida.startswith('AnnModulePragma'):
      self.AvanzarSalida(len('AnnModulePragma'))
      self.parsearUbicación()
      self.parsearAnotación()
      self.cierraParen()
      return {
        "tipo":"Pragma"
      }
    self.errorDesconocido("El Pragma no empieza con 'LanguagePragma', con 'OptionsPragma' ni con 'AnnModulePragma'")
  def parsearTool(self):
    # Una herramienta (?)
    self.abreParen()
    for i in ["GHC","HUGS","NHC98","YHC","HADDOCK"]:
      if self.salida.startswith(i):
        self.AvanzarSalida(len(i))
        self.cierraParen()
        return {
          "tipo":"Tool",
          "valor":i
        }
    if self.salida.startswith("UnknownTool"):
      self.AvanzarSalida(len("UnknownTool"))
      self.parsearString()
      self.cierraParen()
      return {
        "tipo":"Tool",
        "valor":"UnknownTool"
      }
    self.errorDesconocido("La herramienta no empieza con 'UnknownTool', ni con alguna de las herramientas conocidas")
  def parsearAnotación(self):
    # Una anotación (?)
    if self.salida.startswith("Ann"):
      self.AvanzarSalida(len("Ann"))
      self.parsearUbicación()
      self.parsearNombre()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "tipo":"Anotación"
      }
    if self.salida.startswith("TypeAnn"):
      self.AvanzarSalida(len("TypeAnn"))
      self.parsearUbicación()
      self.parsearNombre()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "tipo":"Anotación"
      }
    if self.salida.startswith("ModuleAnn"):
      self.AvanzarSalida(len("ModuleAnn"))
      self.parsearUbicación()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "tipo":"Anotación"
      }
    self.errorDesconocido("La herramienta no empieza con 'Ann', con 'TypeAnn' ni con 'ModuleAnn'")
  def parsearImportDecl(self):
    self.elementoProhibido() # TODO https://hackage.haskell.org/package/haskell-src-exts-1.23.1/docs/Language-Haskell-Exts-Syntax.html#t:ImportDecl
    return
  
  ## Declaraciones
  def parsearDecl(self):
    self.abreParen()
    if self.salida.startswith('FunBind'):
      self.AvanzarSalida(len('FunBind'))
      ubicación = self.parsearUbicación()
      matchs = self.parsearLista("parsearMatch")
      self.cierraParen()
      return {
        "tipo":"Función",
        "en":ubicación,
        "ecuaciones":matchs
      }
  def parsearMatch(self):
    self.abreParen()
    if self.salida.startswith('Match'):
      self.AvanzarSalida(len('Match'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      patrones = self.parsearLista("parsearPattern")
      definición = self.parsearRhs()
      binds = self.parsearMaybe("parsearBind")
      self.cierraParen()
      return {
        "tipo":"Ecuación",
        "en":ubicación,
        "nombre":nombre,
        "patrones":patrones,
        "definición":definición
      }
  def parsearNombre(self):
    self.abreParen()
    if self.salida.startswith('Ident'):
      self.AvanzarSalida(len('Ident'))
    elif self.salida.startswith('Symbol'):
      self.AvanzarSalida(len('Symbol'))
    else:
      pass # error
    ubicación = self.parsearUbicación()
    nombre = self.parsearString()
    self.cierraParen()
    return {
      "tipo":"Nombre",
      "en":ubicación,
      "valor":nombre
    }
  def parsearNombreQ(self):
    self.abreParen()
    if self.salida.startswith('UnQual'):
      self.AvanzarSalida(len('UnQual'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return nombre
  def parsearNombreC(self):
    self.abreParen()
    if self.salida.startswith('VarName'):
      self.AvanzarSalida(len('VarName'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return nombre
    if self.salida.startswith('ConName'):
      self.AvanzarSalida(len('ConName'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return nombre
  def parsearOperadorQ(self):
    self.abreParen()
    if self.salida.startswith('QVarOp'):
      self.AvanzarSalida(len('QVarOp'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
      "tipo":"Operador",
      "en":ubicación,
      "operador":nombre
    }
  def parsearPattern(self):
    self.abreParen()
    if self.salida.startswith('PVar'):
      self.AvanzarSalida(len('PVar'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "tipo":"Variable",
        "en":ubicación,
        "valor":nombre["valor"]
      }
    if self.salida.startswith('PLit'):
      self.AvanzarSalida(len('PLit'))
      ubicación = self.parsearUbicación()
      signo = self.parsearSigno()
      literal = self.parsearLiteral()
      self.cierraParen()
      return {
        "tipo":"Literal",
        "en":ubicación,
        "signo":signo,
        "literal":literal
      }
    if self.salida.startswith('PInfixApp'):
      self.AvanzarSalida(len('PInfixApp'))
      ubicación = self.parsearUbicación()
      izq = self.parsearPattern()
      q = self.parsearNombreQ()
      der = self.parsearPattern()
      self.cierraParen()
      return {
        "tipo":"AppInfija",
        "en":ubicación,
        "izq":izq,
        "q":q,
        "der":der
      }
  def parsearRhs(self):
    self.abreParen()
    if self.salida.startswith('UnGuardedRhs'):
      self.AvanzarSalida(len('UnGuardedRhs'))
      ubicación = self.parsearUbicación()
      expresión = self.parsearExpresión()
      self.cierraParen()
      return expresión
  def parsearBind(self):
    pass # TODO
  def parsearExpresión(self):
    self.abreParen()
    if self.salida.startswith('Var'):
      self.AvanzarSalida(len('Var'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
        "tipo":"Variable",
        "en":ubicación,
        "valor":nombre["valor"]
      }
    if self.salida.startswith('Lit'):
      self.AvanzarSalida(len('Lit'))
      ubicación = self.parsearUbicación()
      literal = self.parsearLiteral()
      self.cierraParen()
      return literal
    if self.salida.startswith('InfixApp'):
      self.AvanzarSalida(len('InfixApp'))
      ubicación = self.parsearUbicación()
      izq = self.parsearExpresión()
      op = self.parsearOperadorQ()
      der = self.parsearExpresión()
      self.cierraParen()
      return {
        "tipo":"AppInfija",
        "en":ubicación,
        "izq":izq,
        "op":op,
        "der":der
      }
    self.errorDesconocido("La expresión no empieza con 'Var', con 'Lit' ni con 'InfixApp'")
  def parsearSigno(self):
    self.abreParen()
    if self.salida.startswith('Signless'):
      self.AvanzarSalida(len('Signless'))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "tipo":"Signo",
        "en":ubicación,
        "valor":"Positivo"
      }
    if self.salida.startswith('Negative'):
      self.AvanzarSalida(len('Negative'))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "tipo":"Signo",
        "en":ubicación,
        "valor":"Negativo"
      }
    self.errorDesconocido("El signo no empieza con 'Signless' ni con 'Negative'")
  def parsearLiteral(self):
    self.abreParen()
    if self.salida.startswith('Int'):
      self.AvanzarSalida(len('Int'))
      ubicación = self.parsearUbicación()
      valor = self.parsearNúmero()
      original = self.parsearString()
      self.cierraParen()
      return {
        "tipo":"LiteralNúmero",
        "en":ubicación,
        "valor":valor,
        "original":original
      }

haskellParser = HaskellParser()

def posCaracterNoEscapeado(texto, caracter, secuenciaEscape, desde=0):
  i = desde
  iCaracter = texto.find(caracter, i)
  iEscape = texto.find(secuenciaEscape, i)
  while iEscape >= 0 and iEscape <= iCaracter and iEscape + len(secuenciaEscape) < len(texto):
    i = iEscape + len(secuenciaEscape)
    iCaracter = texto.find(caracter, i)
    iEscape = texto.find(secuenciaEscape, i)
  return iCaracter

def esCharNumérico(c):
  return c in "1234567890-."