# -*- coding: utf-8 -*-

# Documentación del parser de Haskell https://hackage.haskell.org/package/haskell-src-exts-1.23.1/docs/Language-Haskell-Exts-Syntax.html

from analizadorBase import Analizador
from procesos import ejecutar, rutaJail
from utils import algunoCumple

reglasCódigoMalicioso = {
  # TODO
}

class AnalizadorHaskell(Analizador):
  def __init__(self, malicioso=reglasCódigoMalicioso.keys()):
    self.clavesReglasCódigoMalicioso = malicioso
    self.reglasCódigoMalicioso = reglasCódigoMalicioso
  def obtenerAst(self, codigo):
    return astHaskell(codigo)
  def hijosDeNodo_(self, nodo):
    return hijosDeNodo_(nodo)
  def nodoMadreDe_(self, nodo):
    return nodo.["_madre"]
  def es_NodoDeTipo_(self, nodo, tipo):
    if not (nodo is None):
      tipos = tipo if type(tipo) == type([]) else [tipo]
      return algunoCumple(lambda t : nodo["t"] == t, tipos)
    return False
  def tiposNombre(self):
    return "Nombre"
  def nombreNodo_(self, nodo):
    # PRE: nodo es de tipo Nombre
    return nodo["valor"]
  def tiposComandosCompuestos(self):
    return [] # No hay comandos compuestos en Haskell
  def tiposRepeticiónSimple(self):
    return [] # No hay repetición simple en Haskell
  def tiposImport(self):
    return ["Import","DeclaraciónImport"]
  def tiposExcepción(self):
    return [] # TODO! ¿exitWith?
  def líneaDeNodo_(self, nodo):
    return líneaDeUbicación(nodo["en"]) if ("en" in nodo) else "?"
  def columnaDeNodo_(self, nodo):
    return columnaDeUbicación(nodo["en"]) if ("en" in nodo) else "?"

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
  if haskellParser.falló():
    return {"error":haskellParser.errorMsg() + "\n\n" + haskellParser.ubicaciónATexto(haskellParser.errorLoc())}
  AST = haskellParser.ast()
  AgregarAtributoMadre(AST)
  AST["_madre"] = None
  return {"ast":AST}

def hijosDeNodo_(nodo):
  hijosPorAhora = []
  for k in nodo:
    if not (k in ["t", "en", "valor", "original", "_madre"]):
      másHijos = nodo[k]
      for hijo in (másHijos if (type(másHijos) == type([])) else [másHijos]):
        hijosPorAhora.append(hijo)
  return hijosPorAhora

def AgregarAtributoMadre(nodo):
  for hijo in hijosDeNodo_(nodo):
    hijo["_madre"] = nodo
    AgregarAtributoMadre(hijo)

def líneaDeUbicación(ubicación):
  return (ubicación["línea"] - 3) if ("línea" in ubicación) else "?"
def columnaDeUbicación(ubicación):
  return ubicación["columna"] if ("columna" in ubicación) else "?"

class HaskellParser(object):
  def parse(self, salida):
    self.resultado = "OK"
    self.mensajeError = ""
    self.ubicaciónDelError = ""
    self.raíz = None
    self.salidaCompleta = salida
    self.salida = salida
    self.parenStack = []
    if self.salida.startswith("ParseFailed "):
      self.AvanzarSalida(len("ParseFailed "))
      self.resultado = "FAIL"
      self.ubicaciónDelError = self.parsearUbicación()
      self.mensajeError = self.parsearString()
      return
    if self.salida.startswith("ParseOk "):
      self.AvanzarSalida(len("ParseOk "))
      self.raíz = self.parsearNodoRaíz()
      return
    self.errorDesconocido("La salida no empieza con (ParseOk) ni con (ParseFailed)")
  def ubicaciónATexto(self, ubicación):
    return "Línea " + str(líneaDeUbicación(ubicación)) + ", columna " + str(columnaDeUbicación(ubicación))
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
  def funciónAPartirDe(self, cosa):
    if (type(cosa) == type("")):
      return getattr(self, "parsearSrcSpan")
    # Si no es string, asumo que ya es una función
    return cosa
  def parsearUbicación(self):
    # SrcLoc "..." l c | SrcSpanInfo { srcInfoSpan = (SrcSpan ...), srcInfoPoints = [(SrcSpan ...)] }
    self.abreParen()
    if self.salida.startswith('SrcLoc '):
      self.AvanzarSalida(len('SrcLoc '))
      self.parsearString()
      línea = self.parsearNúmero()
      columna = self.parsearNúmero()
      self.cierraParen()
      return {"línea":línea, "columna":columna}
    if self.salida.startswith('SrcSpanInfo '):
      self.AvanzarSalida(len('SrcSpanInfo '))
      registro = self.parsearRegistro([
        ["srcInfoSpan", "parsearSrcSpan"],
        ["srcInfoPoints", self.fParsearLista("parsearSrcSpan")]
      ])["srcInfoSpan"]
      self.cierraParen()
      return registro
    self.errorDesconocido("La ubicación no empieza con 'SrcLoc' ni con 'SrcSpanInfo'")
  def parsearSrcSpan(self):
    # SrcSpan "..." l c
    self.abreParen()
    if self.salida.startswith('SrcSpan '):
      self.AvanzarSalida(len('SrcSpan '))
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
  def parsearBooleano(self):
    # True | False
    if self.salida.startswith("True"):
      self.AvanzarSalida(len("True"))
      return True
    if self.salida.startswith("False"):
      self.AvanzarSalida(len("False"))
      return False
    self.errorDesconocido("El booleano no es 'True' ni 'False'")
  def parsearRegistro(self, clavesYFunciones):
    # { clavei = valori }
    resultado = {}
    if self.salida.startswith("{"):
      self.AvanzarSalida(1)
      for claveYFunción in clavesYFunciones:
        if self.salida.startswith(claveYFunción[0] + " "):
          self.AvanzarSalida(len(claveYFunción[0] + " "))
          if self.salida.startswith("="):
            self.AvanzarSalida(1)
            resultado[claveYFunción[0]] = self.funciónAPartirDe(claveYFunción[1])()
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
      f = self.funciónAPartirDe(fElemento)
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
        "t":"Nada"
      }
    if self.salida.startswith('Just '):
      self.AvanzarSalida(len('Just '))
      dato = self.funciónAPartirDe(fElemento)()
      self.cierraParen()
      return dato
    self.errorDesconocido("El Maybe no empieza con 'Nothing' ni con 'Just'")
  def parsearMaybeList(self, fElemento):
    # Nothing | Just [...]
    return self.parsearMaybe(self.fParsearLista(fElemento))
  def parsearTupla(self, fElementoS):
    # ( elementoi )
    resultado = []
    if self.salida.startswith("("):
      self.AvanzarSalida(1)
      i = 0
      n = len(fElementoS)
      finLista = self.salida.startswith(")")
      while not finLista:
        if i >= n:
          self.errorDesconocido("Sobran elementos en la tupla (hay al menos "+str(i)" pero debería haber "+str(n)+")")
        resultado.append(self.funciónAPartirDe(fElementoS[i])())
        i += 1
        if self.salida.startswith(","):
          self.AvanzarSalida(1)
        elif self.salida.startswith(")"):
          finLista = True
        else:
          self.errorDesconocido("Tupla mal formada")
      if i < n:
        self.errorDesconocido("Faltan elementos en la tupla (hay "+str(i)" pero debería haber "+str(n)+")")
      self.AvanzarSalida(1)
    return resultado
  def fParsearTupla(self, fElementoS):
    return lambda: getattr(self, "parsearTupla")(fElementoS)

  ## Nodos
  def parsearNodoRaíz(self):
    # Module
    self.abreParen()
    if self.salida.startswith('Module '):
      self.AvanzarSalida(len('Module '))
      ubicación = self.parsearUbicación()
      encabezado = self.parsearMaybe("parsearModuleHead")
      pragmas = self.parsearLista("parsearModulePragma")
      imports = self.parsearLista("parsearImportDecl")
      declaraciones = self.parsearLista("parsearDecl")
      self.cierraParen()
      return {
        "t":"Módulo",
        "en":ubicación,
        "declaraciones":declaraciones
      }
    if self.salida.startswith('XmlPage '):
      self.AvanzarSalida(len('XmlPage '))
      ubicación = self.parsearUbicación()
      nombreMódulo = self.parsearNombreMódulo()
      pragmas = self.parsearLista("parsearModulePragma")
      nombreXml = self.parsearNombreXml()
      attrs = self.parsearLista("parsearAtributoXML")
      expresiónPrincipal = self.parsearMaybe("parsearExpresión")
      otrasExpresiones = self.parsearLista("parsearExpresión")
      self.cierraParen()
      return {
        "t":"Módulo",
        "en":ubicación,
        "declaraciones":[]
      }
    if self.salida.startswith('XmlHybrid '):
      self.AvanzarSalida(len('XmlHybrid '))
      ubicación = self.parsearUbicación()
      encabezado = self.parsearMaybe("parsearModuleHead")
      pragmas = self.parsearLista("parsearModulePragma")
      imports = self.parsearLista("parsearImportDecl")
      declaraciones = self.parsearLista("parsearDecl")
      nombreXml = self.parsearNombreXml()
      attrs = self.parsearLista("parsearAtributoXML")
      expresiónPrincipal = self.parsearMaybe("parsearExpresión")
      otrasExpresiones = self.parsearLista("parsearExpresión")
      self.cierraParen()
      return {
        "t":"Módulo",
        "en":ubicación,
        "declaraciones":declaraciones
      }
    self.errorDesconocido("El módulo no empieza con 'Module', con 'XmlPage' ni con 'XmlHybrid'")
  def parsearModuleHead(self):
    # Encabezado de módulo
    self.abreParen()
    if self.salida.startswith('ModuleHead '):
      self.AvanzarSalida(len('ModuleHead '))
      self.parsearUbicación()
      nombre = self.parsearNombreMódulo()
      advertencia = self.parsearMaybe("parsearWarningText")
      exports = self.parsearMaybe("parsearExportSpecList")
      self.cierraParen()
      return {
        "t":"EncabezadoMódulo",
        "en":ubicación,
        "nombre":nombre
      }
    self.errorDesconocido("El encabezado del módulo no empieza con 'ModuleHead'")
  def parsearNombreMódulo(self):
    # Nombre de módulo
    self.abreParen()
    if self.salida.startswith('ModuleName '):
      self.AvanzarSalida(len('ModuleName '))
      self.parsearUbicación()
      nombre = self.parsearString()
      self.cierraParen()
      return {
        "t":"Nombre",
        "en":ubicación,
        "valor":nombre
      }
    self.errorDesconocido("El nombre del módulo no empieza con 'ModuleName'")
  def parsearNombreXml(self):
    # Nombre de elemento XML
    self.abreParen()
    if self.salida.startswith('XName '):
      self.AvanzarSalida(len('XName '))
      self.parsearUbicación()
      nombre = self.parsearString()
      self.cierraParen()
      return {
        "t":"NombreXML",
        "en":ubicación,
        "valor":nombre
      }
    if self.salida.startswith('XDomName '):
      self.AvanzarSalida(len('XDomName '))
      self.parsearUbicación()
      nombre1 = self.parsearString()
      nombre2 = self.parsearString()
      self.cierraParen()
      return {
        "t":"NombreXML",
        "en":ubicación,
        "valor":nombre1
      }
    self.errorDesconocido("El nombre XML no empieza con 'XName' ni con 'XDomName'")
  def parsearAtributoXML(self):
    # Atributo XML
    self.abreParen()
    if self.salida.startswith('XAttr '):
      self.AvanzarSalida(len('XAttr '))
      self.parsearUbicación()
      nombre = self.parsearNombreXml()
      expresión = self.parsearExpresión()
      self.cierraParen()
      return {
        "t":"AtributoXML",
        "en":ubicación,
        "nombre":nombre,
        "expresión":expresión
      }
    self.errorDesconocido("El atributo XML no empieza con 'XAttr'")
  def parsearWarningText(self):
    # Texto de advertencia (?)
    self.abreParen()
    if self.salida.startswith('DeprText '):
      self.AvanzarSalida(len('DeprText '))
      self.parsearUbicación()
      texto = self.parsearString()
      self.cierraParen()
      return texto
    self.abreParen()
    if self.salida.startswith('WarnText '):
      self.AvanzarSalida(len('WarnText '))
      self.parsearUbicación()
      texto = self.parsearString()
      self.cierraParen()
      return texto
    self.errorDesconocido("El texto de advertencia no empieza con 'DeprText' ni con 'WarnText'")
  def parsearImportSpecList(self):
    # Lista de imports
    self.abreParen()
    if self.salida.startswith('ImportSpecList '):
      self.AvanzarSalida(len('ImportSpecList '))
      self.parsearUbicación()
      hide = self.parsearBooleano()
      imports = self.parsearLista("parsearImportSpec")
      self.cierraParen()
      return imports
    self.errorDesconocido("La lista de imports no empieza con 'ImportSpecList'")  
  def parsearImportSpec(self):
    # Un import
    self.abreParen()
    if self.salida.startswith('IVar '):
      self.AvanzarSalida(len('IVar '))
      self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return nombre
    if self.salida.startswith('IAbs '):
      self.AvanzarSalida(len('IAbs '))
      self.parsearUbicación()
      nameSpace = self.parsearNameSpace()
      nombre = self.parsearNombre()
      self.cierraParen()
      return nombre
    if self.salida.startswith('IThingAll '):
      self.AvanzarSalida(len('IThingAll '))
      self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return nombre
    if self.salida.startswith('IThingWith '):
      self.AvanzarSalida(len('IThingWith '))
      self.parsearUbicación()
      nombre = self.parsearNombre()
      nombresSub = self.parsearLista("parsearNombreC")
      self.cierraParen()
      return nombre
    self.errorDesconocido("El import no empieza con 'IVar', 'IAbs', 'IThingAll' ni con 'IThingWith'")
  def parsearExportSpecList(self):
    # Lista de exports
    self.abreParen()
    if self.salida.startswith('ExportSpecList '):
      self.AvanzarSalida(len('ExportSpecList '))
      self.parsearUbicación()
      exports = self.parsearLista("parsearExportSpec")
      self.cierraParen()
      return exports
    self.errorDesconocido("La lista de exports no empieza con 'ExportSpecList'")
  def parsearExportSpec(self):
    # Un export
    self.abreParen()
    if self.salida.startswith('EVar '):
      self.AvanzarSalida(len('EVar '))
      self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return nombre
    if self.salida.startswith('EAbs '):
      self.AvanzarSalida(len('EAbs '))
      self.parsearUbicación()
      nameSpace = self.parsearNameSpace()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return nombre
    if self.salida.startswith('EThingWith '):
      self.AvanzarSalida(len('EThingWith '))
      self.parsearUbicación()
      self.parsearWildCard()
      nombre = self.parsearNombreQ()
      nombresSub = self.parsearLista("parsearNombreC")
      self.cierraParen()
      return nombre
    if self.salida.startswith('EModuleContents '):
      self.AvanzarSalida(len('EModuleContents '))
      self.parsearUbicación()
      nombre = self.parsearNombreMódulo()
      self.cierraParen()
      return nombre
    self.errorDesconocido("El export no empieza con 'EVar', 'EAbs', 'EThingWith' ni con 'EModuleContents'")
  def parsearNameSpace(self):
    # Un nameSpace
    self.abreParen()
    if self.salida.startswith('NoNamespace '):
      self.AvanzarSalida(len('NoNamespace '))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"NameSpace"
      }
    if self.salida.startswith('TypeNamespace '):
      self.AvanzarSalida(len('TypeNamespace '))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"NameSpace"
      }
    if self.salida.startswith('PatternNamespace '):
      self.AvanzarSalida(len('PatternNamespace '))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"NameSpace"
      }
    self.errorDesconocido("El NameSpace no empieza con 'NoNamespace', con 'TypeNamespace' ni con 'PatternNamespace'")
  def parsearWildCard(self):
    # Un wildcard
    self.abreParen()
    if self.salida.startswith('NoWildcard '):
      self.AvanzarSalida(len('NoWildcard '))
      self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"WildCard"
      }
    if self.salida.startswith('EWildcard '):
      self.AvanzarSalida(len('EWildcard '))
      self.parsearUbicación()
      self.parsearNúmero()
      self.cierraParen()
      return {
        "t":"WildCard"
      }
    self.errorDesconocido("El WildCard no empieza con 'NoWildcard', ni con 'EWildcard'")
  def parsearModulePragma(self):
    # Un pragma
    self.abreParen()
    if self.salida.startswith('LanguagePragma '):
      self.AvanzarSalida(len('LanguagePragma '))
      self.parsearUbicación()
      self.parsearLista("parsearNombre")
      self.cierraParen()
      return {
        "t":"Pragma"
      }
    if self.salida.startswith('OptionsPragma '):
      self.AvanzarSalida(len('OptionsPragma '))
      self.parsearUbicación()
      self.parsearMaybe("parsearTool")
      self.parsearString()
      self.cierraParen()
      return {
        "t":"Pragma"
      }
    if self.salida.startswith('AnnModulePragma '):
      self.AvanzarSalida(len('AnnModulePragma '))
      self.parsearUbicación()
      self.parsearAnotación()
      self.cierraParen()
      return {
        "t":"Pragma"
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
          "t":"Tool",
          "valor":i
        }
    if self.salida.startswith("UnknownTool "):
      self.AvanzarSalida(len("UnknownTool "))
      self.parsearString()
      self.cierraParen()
      return {
        "t":"Tool",
        "valor":"UnknownTool"
      }
    self.errorDesconocido("La herramienta no empieza con 'UnknownTool', ni con alguna de las herramientas conocidas")
  def parsearAnotación(self):
    # Una anotación (?)
    self.abreParen()
    if self.salida.startswith("Ann "):
      self.AvanzarSalida(len("Ann "))
      self.parsearUbicación()
      self.parsearNombre()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "t":"Anotación"
      }
    if self.salida.startswith("TypeAnn "):
      self.AvanzarSalida(len("TypeAnn "))
      self.parsearUbicación()
      self.parsearNombre()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "t":"Anotación"
      }
    if self.salida.startswith("ModuleAnn "):
      self.AvanzarSalida(len("ModuleAnn "))
      self.parsearUbicación()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "t":"Anotación"
      }
    self.errorDesconocido("La herramienta no empieza con 'Ann', con 'TypeAnn' ni con 'ModuleAnn'")
  def parsearImportDecl(self):
    # Una declaración de importación
    self.abreParen()
    if self.salida.startswith('ImportDecl '):
      self.AvanzarSalida(len('ImportDecl '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombreMódulo()
      q = self.parsearBooleano()
      conSrc = self.parsearBooleano()
      esSeguro = self.parsearBooleano()
      nombreExplícito = self.parsearMaybe("parsearString")
      alias = self.parsearMaybe("parsearNombreMódulo")
      specs = self.parsearMaybe("parsearImportSpecList")
      self.cierraParen()
      return {
        "t":"Import",
        "módulo":nombre
      }
    self.errorDesconocido("La declaración de importación no empieza con 'ImportDecl'")
  def parsearAsociación(self):
    # Asociación de un operador
    self.abreParen()
    if self.salida.startswith('AssocNone '):
      self.AvanzarSalida(len('AssocNone '))
    elif self.salida.startswith('AssocLeft '):
      self.AvanzarSalida(len('AssocLeft '))
    elif self.salida.startswith('AssocRight '):
      self.AvanzarSalida(len('AssocRight '))
    else:
      self.errorDesconocido("La asociación no empieza con 'AssocNone', con 'AssocLeft' ni con 'AssocRight'")
    self.parsearUbicación()
    self.cierraParen()
    return {
      "t":"Asociación"
    }

  ## Declaraciones
  def parsearDecl(self):
    self.abreParen()
    if self.salida.startswith('TypeDecl '):
      self.AvanzarSalida(len('TypeDecl '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearDeclHead()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "nombre":nombre,
        "tipo":tipo
      }
    if self.salida.startswith('TypeFamDecl '):
      self.AvanzarSalida(len('TypeFamDecl '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearDeclHead()
      self.parsearMaybe("parsearResultSig")
      self.parsearMaybe("parsearInjectInfo")
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('ClosedTypeFamDecl '):
      self.AvanzarSalida(len('ClosedTypeFamDecl '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearDeclHead()
      self.parsearMaybe("parsearResultSig")
      self.parsearMaybe("parsearInjectInfo")
      self.parsearLista("parsearTypeEqn")
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('DataDecl '):
      self.AvanzarSalida(len('DataDecl '))
      ubicación = self.parsearUbicación()
      don = self.parsearDataOrNew()
      self.parsearMaybe("parsearContexto")
      nombre = self.parsearDeclHead()
      self.parsearLista("parsearQualConDecl")
      self.parsearLista("parsearDeriving")
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('GDataDecl '):
      self.AvanzarSalida(len('GDataDecl '))
      ubicación = self.parsearUbicación()
      don = self.parsearDataOrNew()
      self.parsearMaybe("parsearContexto")
      nombre = self.parsearDeclHead()
      self.parsearMaybe("parsearKind")
      self.parsearLista("parsearGatlDecl")
      self.parsearLista("parsearDeriving")
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('DataFamDecl '):
      self.AvanzarSalida(len('DataFamDecl '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearContexto")
      nombre = self.parsearDeclHead()
      self.parsearMaybe("parsearResultSig")
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('TypeInsDecl '):
      self.AvanzarSalida(len('TypeInsDecl '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "tipo":tipo1
      }
    if self.salida.startswith('DataInsDecl '):
      self.AvanzarSalida(len('DataInsDecl '))
      ubicación = self.parsearUbicación()
      don = self.parsearDataOrNew()
      tipo = self.parsearTipo()
      self.parsearLista("parsearQualConDecl")
      self.parsearLista("parsearDeriving")
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "tipo":tipo
      }
    if self.salida.startswith('GDataInsDecl '):
      self.AvanzarSalida(len('GDataInsDecl '))
      ubicación = self.parsearUbicación()
      don = self.parsearDataOrNew()
      tipo = self.parsearTipo()
      self.parsearMaybe("parsearKind")
      self.parsearLista("parsearGatlDecl")
      self.parsearLista("parsearDeriving")
      self.cierraParen()
      return {
        "t":"DeclaraciónTipo",
        "en":ubicación,
        "tipo":tipo
      }
    if self.salida.startswith('ClassDecl '):
      self.AvanzarSalida(len('ClassDecl '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearContexto")
      nombre = self.parsearDeclHead()
      self.parsearLista("parsearFunDep")
      self.parsearMaybeList("parsearClassDecl")
      self.cierraParen()
      return {
        "t":"DeclaraciónClase",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('InstDecl '):
      self.AvanzarSalida(len('InstDecl '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearOverlap")
      self.parsearInstRule()
      self.parsearMaybeList("parsearInstDecl")
      self.cierraParen()
      return {
        "t":"DeclaraciónInstancia",
        "en":ubicación
      }
    if self.salida.startswith('DerivDecl '):
      self.AvanzarSalida(len('DerivDecl '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearDerivStrategy")
      self.parsearMaybe("parsearOverlap")
      self.parsearInstRule()
      self.cierraParen()
      return {
        "t":"DeclaraciónInstancia",
        "en":ubicación
      }
    if self.salida.startswith('InfixDecl '):
      self.AvanzarSalida(len('InfixDecl '))
      ubicación = self.parsearUbicación()
      self.parsearAsociación()
      self.parsearMaybe("parsearNúmero")
      self.parsearLista("parsearOperador")
      self.cierraParen()
      return {
        "t":"DeclaraciónInfix",
        "en":ubicación
      }
    if self.salida.startswith('DefaultDecl '):
      self.AvanzarSalida(len('DefaultDecl '))
      ubicación = self.parsearUbicación()
      tipos = self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"DeclaraciónDefault",
        "en":ubicación
        "tipos":tipos
      }
    if self.salida.startswith('SpliceDecl '):
      self.AvanzarSalida(len('SpliceDecl '))
      ubicación = self.parsearUbicación()
      expresión = self.parsearExpresión()
      self.cierraParen()
      return expresión
    if self.salida.startswith('TSpliceDecl '):
      self.AvanzarSalida(len('TSpliceDecl '))
      ubicación = self.parsearUbicación()
      expresión = self.parsearExpresión()
      self.cierraParen()
      return expresión
    if self.salida.startswith('TypeSig '):
      self.AvanzarSalida(len('TypeSig '))
      ubicación = self.parsearUbicación()
      nombres = self.parsearLista("parsearNombre")
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónTipado",
        "nombres":nombres,
        "tipo":tipo
      }
    if self.salida.startswith('PatSynSig '):
      self.AvanzarSalida(len('PatSynSig '))
      ubicación = self.parsearUbicación()
      nombres = self.parsearLista("parsearNombre")
      self.parsearMaybeList("parsearTyVarBind")
      self.parsearMaybe("parsearContexto")
      self.parsearMaybeList("parsearTyVarBind")
      self.parsearMaybe("parsearContexto")
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónTipado",
        "nombres":nombres,
        "tipo":tipo
      }
    if self.salida.startswith('FunBind '):
      self.AvanzarSalida(len('FunBind '))
      ubicación = self.parsearUbicación()
      matchs = self.parsearLista("parsearMatch")
      self.cierraParen()
      return {
        "t":"DeclaraciónFunción",
        "en":ubicación,
        "ecuaciones":matchs
      }
    if self.salida.startswith('PatBind '):
      self.AvanzarSalida(len('PatBind '))
      ubicación = self.parsearUbicación()
      patrón = self.parsearPattern()
      definición = self.parsearRhs()
      binds = self.parsearMaybe("parsearBind")
      self.cierraParen()
      return {
        "t":"DeclaraciónPatrón",
        "en":ubicación,
        "patrón":patrón,
        "definición":definición
      }
    if self.salida.startswith('PatSyn '):
      self.AvanzarSalida(len('PatSyn '))
      ubicación = self.parsearUbicación()
      patrón1 = self.parsearPattern()
      patrón2 = self.parsearPattern()
      dirección = self.parsearPatternSynDirection()
      self.cierraParen()
      return {
        "t":"DeclaraciónPatrón",
        "en":ubicación,
        "patrón":patrón1
      }
    if self.salida.startswith('ForImp '):
      self.AvanzarSalida(len('ForImp '))
      ubicación = self.parsearUbicación()
      callConv = self.parsearCallConv()
      self.parsearMaybe("parsearSafety")
      self.parsearMaybe("parsearString")
      nombre = self.parsearNombre()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónImport",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('ForExp '):
      self.AvanzarSalida(len('ForExp '))
      ubicación = self.parsearUbicación()
      callConv = self.parsearCallConv()
      self.parsearMaybe("parsearString")
      nombre = self.parsearNombre()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónImport",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('RulePragmaDecl '):
      self.AvanzarSalida(len('RulePragmaDecl '))
      ubicación = self.parsearUbicación()
      self.parsearLista("parsearRule")
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('DeprPragmaDecl '):
      self.AvanzarSalida(len('DeprPragmaDecl '))
      ubicación = self.parsearUbicación()
      self.parsearLista(self.fParsearTupla([self.fParsearLista("parsearNombre"), "parsearString"]))
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('WarnPragmaDecl '):
      self.AvanzarSalida(len('WarnPragmaDecl '))
      ubicación = self.parsearUbicación()
      self.parsearLista(self.fParsearTupla([self.fParsearLista("parsearNombre"), "parsearString"]))
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('InlineSig '):
      self.AvanzarSalida(len('InlineSig '))
      ubicación = self.parsearUbicación()
      self.parsearBooleano()
      self.parsearMaybe("parsearActivación")
      self.parsearNombreQ()
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('InlineConlikeSig '):
      self.AvanzarSalida(len('InlineConlikeSig '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearActivación")
      self.parsearNombreQ()
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('SpecSig '):
      self.AvanzarSalida(len('SpecSig '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearActivación")
      self.parsearNombreQ()
      self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('SpecInlineSig '):
      self.AvanzarSalida(len('SpecInlineSig '))
      ubicación = self.parsearUbicación()
      self.parsearBooleano()
      self.parsearMaybe("parsearActivación")
      self.parsearNombreQ()
      self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('InstSig '):
      self.AvanzarSalida(len('InstSig '))
      ubicación = self.parsearUbicación()
      self.parsearInstRule()
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('AnnPragma '):
      self.AvanzarSalida(len('AnnPragma '))
      ubicación = self.parsearUbicación()
      self.parsearAnotación()
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('MinimalPragma '):
      self.AvanzarSalida(len('MinimalPragma '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearFórmulaBooleana")
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('RoleAnnotDecl '):
      self.AvanzarSalida(len('RoleAnnotDecl '))
      ubicación = self.parsearUbicación()
      self.parsearNombreQ()
      self.parsearLista("parsearRol")
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    if self.salida.startswith('CompletePragma '):
      self.AvanzarSalida(len('CompletePragma '))
      ubicación = self.parsearUbicación()
      self.parsearLista("parsearNombre")
      self.parsearMaybe("parsearNombreQ")
      self.cierraParen()
      return {
        "t":"DeclaraciónPragma",
        "en":ubicación
      }
    self.errorDesconocido("La declaración no empieza con un identificador conocido")
  def parsearDeclHead(self):
    self.abreParen()
    if self.salida.startswith('DHead '):
      self.AvanzarSalida(len('DHead '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "t":"EncabezadoDeclaración",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('DHInfix '):
      self.AvanzarSalida(len('DHInfix '))
      ubicación = self.parsearUbicación()
      self.parsearTyVarBind()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "t":"EncabezadoDeclaración",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('DHParen '):
      self.AvanzarSalida(len('DHParen '))
      ubicación = self.parsearUbicación()
      rec = self.parsearDeclHead()
      self.cierraParen()
      return rec
    if self.salida.startswith('DHApp '):
      self.AvanzarSalida(len('DHApp '))
      ubicación = self.parsearUbicación()
      rec = self.parsearDeclHead()
      self.parsearTyVarBind()
      self.cierraParen()
      return rec
    self.errorDesconocido("El encabezado de la declaración no empieza con 'DHead', 'DHInfix', 'DHParen' ni con 'DHApp'")
  def parsearTipo(self):
    self.abreParen()
    if self.salida.startswith('TyForall '):
      self.AvanzarSalida(len('TyForall '))
      ubicación = self.parsearUbicación()
      self.parsearMaybeList("parsearTyVarBind")
      self.parsearMaybe("parsearContexto")
      tipo = self.parsearTipo()
      self.cierraParen()
      return tipo
    if self.salida.startswith('TyStar '):
      self.AvanzarSalida(len('TyStar '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Estrella"
      }
    if self.salida.startswith('TyFun '):
      self.AvanzarSalida(len('TyFun '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Función",
        "tipo1":tipo1,
        "tipo2":tipo2
      }
    if self.salida.startswith('TyTuple '):
      self.AvanzarSalida(len('TyTuple '))
      ubicación = self.parsearUbicación()
      self.parsearBoxed()
      tipos = self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Tupla",
        "tipos":tipos
      }
    if self.salida.startswith('TyUnboxedSum '):
      self.AvanzarSalida(len('TyUnboxedSum '))
      ubicación = self.parsearUbicación()
      tipos = self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Tupla",
        "tipos":tipos
      }
    if self.salida.startswith('TyList '):
      self.AvanzarSalida(len('TyList '))
      ubicación = self.parsearUbicación()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Lista",
        "tipo":tipo
      }
    if self.salida.startswith('TyParArray '):
      self.AvanzarSalida(len('TyParArray '))
      ubicación = self.parsearUbicación()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Lista",
        "tipo":tipo
      }
    if self.salida.startswith('TyApp '):
      self.AvanzarSalida(len('TyApp '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"AplicaciónConstructor",
        "tipo1":tipo1,
        "tipo2":tipo2
      }
    if self.salida.startswith('TyVar '):
      self.AvanzarSalida(len('TyVar '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Variable",
        "nombre":nombre
      }
    if self.salida.startswith('TyCon '):
      self.AvanzarSalida(len('TyCon '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Constructor",
        "nombre":nombre
      }
    if self.salida.startswith('TyParen '):
      self.AvanzarSalida(len('TyParen '))
      ubicación = self.parsearUbicación()
      tipo = self.parsearTipo()
      self.cierraParen()
      return tipo
    if self.salida.startswith('TyInfix '):
      self.AvanzarSalida(len('TyInfix '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      nombre = self.parsearMaybePromotedName()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"ConstructorInfijo",
        "nombre":nombre,
        "tipo1":tipo1,
        "tipo2":tipo2
      }
    if self.salida.startswith('TyKind '):
      self.AvanzarSalida(len('TyKind '))
      ubicación = self.parsearUbicación()
      tipo = self.parsearTipo()
      self.parsearKind()
      self.cierraParen()
      return tipo
    if self.salida.startswith('TyPromoted '):
      self.AvanzarSalida(len('TyPromoted '))
      ubicación = self.parsearUbicación()
      promo = self.parsearPromo()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Promo",
        "promo":promo
      }
    if self.salida.startswith('TyEquals '):
      self.AvanzarSalida(len('TyEquals '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Igualdad",
        "tipo1":tipo1,
        "tipo2":tipo2
      }
    if self.salida.startswith('TySplice '):
      self.AvanzarSalida(len('TySplice '))
      ubicación = self.parsearUbicación()
      splice = self.parsearSplice()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"Splice",
        "splice":splice
      }
    if self.salida.startswith('TyBang '):
      self.AvanzarSalida(len('TyBang '))
      ubicación = self.parsearUbicación()
      self.parsearBangType()
      self.parsearUnpackedness()
      tipo = self.parsearTipo()
      self.cierraParen()
      return tipo
    if self.salida.startswith('TyWildCard '):
      self.AvanzarSalida(len('TyWildCard '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearMaybe("parsearNombre")
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"WildCard",
        "nombre":nombre
      }
    if self.salida.startswith('TyQuasiQuote '):
      self.AvanzarSalida(len('TyQuasiQuote '))
      ubicación = self.parsearUbicación()
      self.parsearString()
      self.parsearString()
      self.cierraParen()
      return {
        "t":"Tipo",
        "en":ubicación,
        "valor":"QuasiQuote"
      }
    self.errorDesconocido("El tipo no empieza con un identificador conocido")
  def parsearResultSig(self):
    self.abreParen()
    if self.salida.startswith('KindSig '):
      self.AvanzarSalida(len('KindSig '))
      ubicación = self.parsearUbicación()
      self.parsearKind()
      self.cierraParen()
      return {
        "t":"ResultSig",
        "en":ubicación
      }
    if self.salida.startswith('TyVarSig '):
      self.AvanzarSalida(len('TyVarSig '))
      ubicación = self.parsearUbicación()
      self.parsearTyVarBind()
      self.cierraParen()
      return {
        "t":"ResultSig",
        "en":ubicación
      }
    self.errorDesconocido("El ResultSig no empieza con 'KindSig' ni con 'TyVarSig'")
  def parsearInjectInfo(self):
    self.abreParen()
    if self.salida.startswith('InjectivityInfo '):
      self.AvanzarSalida(len('InjectivityInfo '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      nombres = self.parsearLista("parsearNombre")
      self.cierraParen()
      return {
        "t":"InjectivityInfo",
        "en":ubicación
      }
    self.errorDesconocido("La información de inyectividad no empieza con 'InjectivityInfo'")
  def parsearTypeEqn(self):
    self.abreParen()
    if self.salida.startswith('TypeEqn '):
      self.AvanzarSalida(len('TypeEqn '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"EcuaciónDeTipo",
        "en":ubicación,
        "tipo1":tipo1,
        "tipo2":tipo2
      }
    self.errorDesconocido("La ecuación de tipo no empieza con 'TypeEqn'")
  def parsearDataOrNew(self):
    self.abreParen()
    if self.salida.startswith('XXX'):
      self.AvanzarSalida(len('XXX'))
    elif self.salida.startswith('XXX'):
      self.AvanzarSalida(len('XXX'))
    else:
      self.errorDesconocido("El DataONew no empieza con 'DataType' ni con 'NewType'")
    ubicación = self.parsearUbicación()
    self.cierraParen()
    return {
      "t":"DataONew",
      "en":ubicación
    }
  def parsearContexto(self):
    self.abreParen()
    if self.salida.startswith('CxSingle '):
      self.AvanzarSalida(len('CxSingle '))
      ubicación = self.parsearUbicación()
      self.parsearAsst()
      self.cierraParen()
      return {
        "t":"Contexto",
        "en":ubicación
      }
    if self.salida.startswith('CxTuple '):
      self.AvanzarSalida(len('CxTuple '))
      ubicación = self.parsearUbicación()
      self.parsearLista("parsearAsst")
      self.cierraParen()
      return {
        "t":"Contexto",
        "en":ubicación
      }
    if self.salida.startswith('CxEmpty '):
      self.AvanzarSalida(len('CxEmpty '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"Contexto",
        "en":ubicación
      }
    self.errorDesconocido("El contexto no empieza con 'CxSingle', 'CxTuple' ni con 'CxEmpty'")
  def parsearConDecl(self):
    self.abreParen()
    if self.salida.startswith('ConDecl '):
      self.AvanzarSalida(len('ConDecl '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      tipos = self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"ConDecl",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('InfixConDecl '):
      self.AvanzarSalida(len('InfixConDecl '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      nombre = self.parsearNombre()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"ConDecl",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('RecDecl '):
      self.AvanzarSalida(len('RecDecl '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      tipos = self.parsearLista("parsearCampo")
      self.cierraParen()
      return {
        "t":"ConDecl",
        "en":ubicación,
        "nombre":nombre
      }
    self.errorDesconocido("La declaración de constructor no empieza con 'ConDecl', 'InfixConDecl' ni con 'RecDecl'")
  def parsearQualConDecl(self):
    self.abreParen()
    if self.salida.startswith('QualConDecl '):
      self.AvanzarSalida(len('QualConDecl '))
      ubicación = self.parsearUbicación()
      self.parsearMaybeList("parsearTyVarBind")
      self.parsearMaybe("parsearContexto")
      conDecl = self.parsearConDecl()
      self.cierraParen()
      return conDecl
    self.errorDesconocido("El QualConDecl no empieza con 'QualConDecl'")
  def parsearDeriving(self):
    self.abreParen()
    if self.salida.startswith('Deriving '):
      self.AvanzarSalida(len('Deriving '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearDerivStrategy")
      self.parsearLista("parsearInstRule")
      self.cierraParen()
      return {
        "t":"Deriving",
        "en":ubicación
      }
    self.errorDesconocido("La cláusula de derivación no empieza con 'Deriving'")
  def parsearKind(self):
    return self.parsearTipo()
  def parsearGatlDecl(self):
    self.abreParen()
    if self.salida.startswith('GadtDecl '):
      self.AvanzarSalida(len('GadtDecl '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.parsearMaybeList("parsearTyVarBind")
      self.parsearMaybe("parsearContexto")
      self.parsearMaybeList("parsearCampo")
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"GADT",
        "en":ubicación,
        "nombre":nombre,
        "tipo":tipo
      }
    self.errorDesconocido("La declaración de GADT no empieza con 'GadtDecl'")
  def parsearFunDep(self):
    self.abreParen()
    if self.salida.startswith('FunDep '):
      self.AvanzarSalida(len('FunDep '))
      ubicación = self.parsearUbicación()
      nombres1 = self.parsearLista("parsearNombre")
      nombres2 = self.parsearLista("parsearNombre")
      self.cierraParen()
      return {
        "t":"DependenciaFuncional",
        "en":ubicación
      }
    self.errorDesconocido("La dependecia funcional no empieza con 'FunDep'")
  def parsearClassDecl(self):
    self.abreParen()
    if self.salida.startswith('ClsDecl '):
      self.AvanzarSalida(len('ClsDecl '))
      ubicación = self.parsearUbicación()
      self.parsearDecl()
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeClase",
        "en":ubicación
      }
    if self.salida.startswith('ClsDataFam '):
      self.AvanzarSalida(len('ClsDataFam '))
      ubicación = self.parsearUbicación()
      self.parsearMaybe("parsearContexto")
      self.parsearDeclHead()
      self.parsearMaybe("parsearResultSig")
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeClase",
        "en":ubicación
      }
    if self.salida.startswith('ClsTyFam '):
      self.AvanzarSalida(len('ClsTyFam '))
      ubicación = self.parsearUbicación()
      self.parsearDeclHead()
      self.parsearMaybe("parsearResultSig")
      self.parsearMaybe("parsearInjectInfo")
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeClase",
        "en":ubicación
      }
    if self.salida.startswith('ClsTyDef '):
      self.AvanzarSalida(len('ClsTyDef '))
      ubicación = self.parsearUbicación()
      self.parsearTypeEqn()
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeClase",
        "en":ubicación
      }
    if self.salida.startswith('ClsDefSig '):
      self.AvanzarSalida(len('ClsDefSig '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeClase",
        "en":ubicación
      }
    self.errorDesconocido("La declaración dentro de la clase no empieza con 'ClsDecl', 'ClsDataFam', 'ClsTyFam', 'ClsTyDef' ni con 'ClsDefSig'")
  def parsearInstDecl(self):
    self.abreParen()
    if self.salida.startswith('InsDecl '):
      self.AvanzarSalida(len('InsDecl '))
      ubicación = self.parsearUbicación()
      self.parsearDecl()
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeInstancia",
        "en":ubicación
      }
    if self.salida.startswith('InsType '):
      self.AvanzarSalida(len('InsType '))
      ubicación = self.parsearUbicación()
      tipo1 = self.parsearTipo()
      tipo2 = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeInstancia",
        "en":ubicación
      }
    if self.salida.startswith('InsData '):
      self.AvanzarSalida(len('InsData '))
      ubicación = self.parsearUbicación()
      don = self.parsearDataOrNew()
      tipo = self.parsearTipo()
      self.parsearLista("parsearQualConDecl")
      self.parsearLista("parsearDeriving")
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeInstancia",
        "en":ubicación
      }
    if self.salida.startswith('InsGData '):
      self.AvanzarSalida(len('InsGData '))
      ubicación = self.parsearUbicación()
      don = self.parsearDataOrNew()
      tipo = self.parsearTipo()
      self.parsearMaybe("parsearKind")
      self.parsearLista("parsearGatlDecl")
      self.parsearLista("parsearDeriving")
      self.cierraParen()
      return {
        "t":"DeclaraciónDentroDeInstancia",
        "en":ubicación
      }
    self.errorDesconocido("La declaración dentro de la instancia no empieza con 'InsDecl', 'InsType', 'InsData' ni con 'InsGData'")
  def parsearOverlap(self):
    self.abreParen()
    if self.salida.startswith('NoOverlap '):
      self.AvanzarSalida(len('NoOverlap '))
    elif self.salida.startswith('Overlap '):
      self.AvanzarSalida(len('Overlap '))
    elif self.salida.startswith('Overlapping '):
      self.AvanzarSalida(len('Overlapping '))
    elif self.salida.startswith('Overlaps '):
      self.AvanzarSalida(len('Overlaps '))
    elif self.salida.startswith('Overlappable '):
      self.AvanzarSalida(len('Overlappable '))
    elif self.salida.startswith('Incoherent '):
      self.AvanzarSalida(len('Incoherent '))
    else:
      self.errorDesconocido("El overlap no empieza con 'NoOverlap', 'Overlap', 'Overlapping', 'Overlaps', 'Overlappable' ni con 'Incoherent'")
    ubicación = self.parsearUbicación()
    self.cierraParen()
    return {
      "t":"Overlap",
      "en":ubicación
    }
  def parsearRule(self):
    self.abreParen()
    if self.salida.startswith('Rule '):
      self.AvanzarSalida(len('Rule '))
      ubicación = self.parsearUbicación()
      self.parsearString()
      self.parsearMaybe("parsearActivación")
      self.parsearMaybeList("parsearRuleVar")
      self.parsearExpresión()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "t":"Regla",
        "en":ubicación
      }
    self.errorDesconocido("La regla no empieza con 'Rule'")
  def parsearInstRule(self):
    self.abreParen()
    if self.salida.startswith('IRule '):
      self.AvanzarSalida(len('IRule '))
      ubicación = self.parsearUbicación()
      self.parsearMaybeList("parsearTyVarBind")
      self.parsearMaybe("parsearContexto")
      self.parsearInstHead()
      self.cierraParen()
      return {
        "t":"ReglaDeInstancia",
        "en":ubicación
      }
    if self.salida.startswith('IParen '):
      self.AvanzarSalida(len('IParen '))
      ubicación = self.parsearUbicación()
      rec = self.parsearInstRule()
      self.cierraParen()
      return rec
    self.errorDesconocido("La regla de instancia no empieza con 'IRule' ni con 'IParen'")
  def parsearDerivStrategy(self):
    self.abreParen()
    if self.salida.startswith('DerivStock '):
      self.AvanzarSalida(len('DerivStock '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"DerivStrategy",
        "en":ubicación
      }
    if self.salida.startswith('DerivAnyclass '):
      self.AvanzarSalida(len('DerivAnyclass '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"DerivStrategy",
        "en":ubicación
      }
    if self.salida.startswith('DerivNewtype '):
      self.AvanzarSalida(len('DerivNewtype '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"DerivStrategy",
        "en":ubicación
      }
    if self.salida.startswith('DerivVia '):
      self.AvanzarSalida(len('DerivVia '))
      ubicación = self.parsearUbicación()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"DerivStrategy",
        "en":ubicación
      }
    self.errorDesconocido("La estrategia de derivación no empieza con 'DerivStock', 'DerivAnyclass', 'DerivNewtype' ni con 'DerivVia'")
  def parsearTyVarBind(self):
    self.abreParen()
    if self.salida.startswith('KindedVar '):
      self.AvanzarSalida(len('KindedVar '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.parsearKind()
      self.cierraParen()
      return {
        "t":"VariableDeTipo",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('UnkindedVar '):
      self.AvanzarSalida(len('UnkindedVar '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "t":"VariableDeTipo",
        "en":ubicación,
        "nombre":nombre
      }
    self.errorDesconocido("La variable de tipo no empieza con 'KindedVar' ni con 'UnkindedVar'")
  def parsearPatternSynDirection(self):
    self.abreParen()
    if self.salida.startswith('Unidirectional '):
      self.AvanzarSalida(len('Unidirectional '))
      self.cierraParen()
      return {
        "t":"DirecciónDePatrón"
      }
    if self.salida.startswith('ImplicitBidirectional '):
      self.AvanzarSalida(len('ImplicitBidirectional '))
      self.cierraParen()
      return {
        "t":"DirecciónDePatrón"
      }
    if self.salida.startswith('ExplicitBidirectional '):
      self.AvanzarSalida(len('ExplicitBidirectional '))
      ubicación = self.parsearUbicación()
      self.parsearLista("parsearDecl")
      self.cierraParen()
      return {
        "t":"DirecciónDePatrón"
      }
    self.errorDesconocido("La dirección de patrón no empieza con 'Unidirectional', 'ImplicitBidirectional' ni con 'ExplicitBidirectional'")
  def parsearCallConv(self):
    self.abreParen()
    if self.salida.startswith('StdCall '):
      self.AvanzarSalida(len('StdCall '))
    elif self.salida.startswith('CCall '):
      self.AvanzarSalida(len('CCall '))
    elif self.salida.startswith('CPlusPlus '):
      self.AvanzarSalida(len('CPlusPlus '))
    elif self.salida.startswith('DotNet '):
      self.AvanzarSalida(len('DotNet '))
    elif self.salida.startswith('Jvm '):
      self.AvanzarSalida(len('Jvm '))
    elif self.salida.startswith('Js '):
      self.AvanzarSalida(len('Js '))
    elif self.salida.startswith('JavaScript '):
      self.AvanzarSalida(len('JavaScript '))
    elif self.salida.startswith('CApi '):
      self.AvanzarSalida(len('CApi '))
    else:
      self.errorDesconocido("La convención de invocación no empieza con ninguno de los identificadores conocidos")
    ubicación = self.parsearUbicación()
    self.cierraParen()
    return {
      "t":"ConvenciónInvocación",
      "en":ubicación
    }
  def parsearSafety(self):
    self.abreParen()
    if self.salida.startswith('PlayRisky '):
      self.AvanzarSalida(len('PlayRisky '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"Seguridad",
        "en":ubicación
      }
    if self.salida.startswith('PlaySafe '):
      self.AvanzarSalida(len('PlaySafe '))
      ubicación = self.parsearUbicación()
      self.parsearBooleano()
      self.cierraParen()
      return {
        "t":"Seguridad",
        "en":ubicación
      }
    if self.salida.startswith('PlayInterruptible '):
      self.AvanzarSalida(len('PlayInterruptible '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"Seguridad",
        "en":ubicación
      }
    self.errorDesconocido("La seguridad no empieza con 'PlayRisky', 'PlaySafe' ni con 'PlayInterruptible'")
  def parsearActivación(self):
    self.abreParen()
    if self.salida.startswith('ActiveFrom '):
      self.AvanzarSalida(len('ActiveFrom '))
    elif self.salida.startswith('ActiveUntil '):
      self.AvanzarSalida(len('ActiveUntil '))
    else:
      self.errorDesconocido("La activación no empieza con 'ActiveFrom' ni con 'ActiveUntil'")
    ubicación = self.parsearUbicación()
    self.parsearNúmero()
    self.cierraParen()
    return {
      "t":"Activación",
      "en":ubicación
    }
  def parsearFórmulaBooleana(self):
    self.abreParen()
    if self.salida.startswith('VarFormula '):
      self.AvanzarSalida(len('VarFormula '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "t":"FórmulaBooleana",
        "en":ubicación
      }
    if self.salida.startswith('AndFormula '):
      self.AvanzarSalida(len('AndFormula '))
      ubicación = self.parsearUbicación()
      self.parsearLista("parsearFórmulaBooleana")
      self.cierraParen()
      return {
        "t":"FórmulaBooleana",
        "en":ubicación
      }
    if self.salida.startswith('OrFormula '):
      self.AvanzarSalida(len('OrFormula '))
      ubicación = self.parsearUbicación()
      self.parsearLista("parsearFórmulaBooleana")
      self.cierraParen()
      return {
        "t":"FórmulaBooleana",
        "en":ubicación
      }
    if self.salida.startswith('ParenFormula '):
      self.AvanzarSalida(len('ParenFormula '))
      ubicación = self.parsearUbicación()
      self.parsearFórmulaBooleana()
      self.cierraParen()
      return {
        "t":"FórmulaBooleana",
        "en":ubicación
      }
    self.errorDesconocido("La fórmula booleana no empieza con 'VarFormula', 'AndFormula', 'OrFormula' ni con 'ParenFormula'")
  def parsearRol(self):
    self.abreParen()
    if self.salida.startswith('Nominal '):
      self.AvanzarSalida(len('Nominal '))
    elif self.salida.startswith('Representational '):
      self.AvanzarSalida(len('Representational '))
    elif self.salida.startswith('Phantom '):
      self.AvanzarSalida(len('Phantom '))
    elif self.salida.startswith('RoleWildcard '):
      self.AvanzarSalida(len('RoleWildcard '))
    else:
      self.errorDesconocido("El rol no empieza con 'Nominal', 'Representational', 'Phantom' ni con 'RoleWildcard'")
    ubicación = self.parsearUbicación()
    self.cierraParen()
    return {
      "t":"Rol",
      "en":ubicación
    }
  def parsearBoxed(self):
    # Boxed | Unboxed
    if self.salida.startswith("Boxed"):
      self.AvanzarSalida(len("Boxed"))
      return {
        "t":"Boxed",
        "valor":True
      }
    if self.salida.startswith("Unboxed"):
      self.AvanzarSalida(len("Unboxed"))
      return {
        "t":"Boxed",
        "valor":False
      }
    self.errorDesconocido("El boxed no es 'Boxed' ni 'Unboxed'")
  def parsearPromo(self):
    self.abreParen()
    if self.salida.startswith('PromotedInteger '):
      self.AvanzarSalida(len('PromotedInteger '))
      ubicación = self.parsearUbicación()
      self.parsearNúmero()
      self.parsearString()
      self.cierraParen()
      return {
        "t":"Promoción",
        "en":ubicación
      }
    if self.salida.startswith('PromotedString '):
      self.AvanzarSalida(len('PromotedString '))
      ubicación = self.parsearUbicación()
      self.parsearString()
      self.parsearString()
      self.cierraParen()
      return {
        "t":"Promoción",
        "en":ubicación
      }
    if self.salida.startswith('PromotedCon '):
      self.AvanzarSalida(len('PromotedCon '))
      ubicación = self.parsearUbicación()
      self.parsearBooleano()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
        "t":"Promoción",
        "en":ubicación
      }
    if self.salida.startswith('PromotedList '):
      self.AvanzarSalida(len('PromotedList '))
      ubicación = self.parsearUbicación()
      self.parsearBooleano()
      tipos = self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"Promoción",
        "en":ubicación
      }
    if self.salida.startswith('PromotedTuple '):
      self.AvanzarSalida(len('PromotedTuple '))
      ubicación = self.parsearUbicación()
      tipos = self.parsearLista("parsearTipo")
      self.cierraParen()
      return {
        "t":"Promoción",
        "en":ubicación
      }
    if self.salida.startswith('PromotedUnit '):
      self.AvanzarSalida(len('PromotedUnit '))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"Promoción",
        "en":ubicación
      }
    self.errorDesconocido("La promoción no empieza con 'PromotedInteger', 'PromotedString', 'PromotedCon', 'PromotedList', 'PromotedTuple' ni con 'PromotedUnit'")
  def parsearSplice(self):
    self.abreParen()
    if self.salida.startswith('IdSplice '):
      self.AvanzarSalida(len('IdSplice '))
      ubicación = self.parsearUbicación()
      self.parsearString()
      self.cierraParen()
      return {
        "t":"Splice",
        "en":ubicación
      }
    if self.salida.startswith('TIdSplice '):
      self.AvanzarSalida(len('TIdSplice '))
      ubicación = self.parsearUbicación()
      self.parsearString()
      self.cierraParen()
      return {
        "t":"Splice",
        "en":ubicación
      }
    if self.salida.startswith('ParenSplice '):
      self.AvanzarSalida(len('ParenSplice '))
      ubicación = self.parsearUbicación()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "t":"Splice",
        "en":ubicación
      }
    if self.salida.startswith('TParenSplice '):
      self.AvanzarSalida(len('TParenSplice '))
      ubicación = self.parsearUbicación()
      self.parsearExpresión()
      self.cierraParen()
      return {
        "t":"Splice",
        "en":ubicación
      }
    self.errorDesconocido("El splice no empieza con 'IdSplice', 'TIdSplice', 'ParenSplice' ni con 'TParenSplice'")
  def parsearBangType(self):
    self.abreParen()
    if self.salida.startswith('BangedTy '):
      self.AvanzarSalida(len('BangedTy '))
    elif self.salida.startswith('LazyTy '):
      self.AvanzarSalida(len('LazyTy '))
    elif self.salida.startswith('NoStrictAnnot '):
      self.AvanzarSalida(len('NoStrictAnnot '))
    else:
      self.errorDesconocido("El bang (?) no empieza con 'BangedTy', 'LazyTy' ni con 'NoStrictAnnot'")
    ubicación = self.parsearUbicación()
    self.cierraParen()
    return {
      "t":"Bang",
      "en":ubicación
    }
  def parsearUnpackedness(self):
    self.abreParen()
    if self.salida.startswith('Unpack '):
      self.AvanzarSalida(len('Unpack '))
    elif self.salida.startswith('NoUnpack '):
      self.AvanzarSalida(len('NoUnpack '))
    elif self.salida.startswith('NoUnpackPragma '):
      self.AvanzarSalida(len('NoUnpackPragma '))
    else:
      self.errorDesconocido("El unpack (?) no empieza con 'Unpack', 'NoUnpack' ni con 'NoUnpackPragma'")
    ubicación = self.parsearUbicación()
    self.cierraParen()
    return {
      "t":"Unpack",
      "en":ubicación
    }
  def parsearCampo(self):
    self.abreParen()
    if self.salida.startswith('FieldDecl '):
      self.AvanzarSalida(len('FieldDecl '))
      ubicación = self.parsearUbicación()
      nombres = self.parsearLista("parsearNombre")
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"Campo",
        "en":ubicación,
        "nombres":nombres
        "tipo":tipo
      }
    self.errorDesconocido("El campo no empieza con 'FieldDecl'")
  def parsearRuleVar(self):
    self.abreParen()
    if self.salida.startswith('RuleVar '):
      self.AvanzarSalida(len('RuleVar '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "t":"VariableEnRegla",
        "en":ubicación
      }
    if self.salida.startswith('TypedRuleVar '):
      self.AvanzarSalida(len('TypedRuleVar '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      tipo = self.parsearTipo()
      self.cierraParen()
      return {
        "t":"VariableEnRegla",
        "en":ubicación
      }
    self.errorDesconocido("La variable en regla no empieza con 'RuleVar' ni con 'TypedRuleVar'")
  def parsearInstHead(self):
    self.abreParen()
    if self.salida.startswith('IHCon '):
      self.AvanzarSalida(len('IHCon '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
        "t":"EncabezadoInstancia",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('IHInfix '):
      self.AvanzarSalida(len('IHInfix '))
      ubicación = self.parsearUbicación()
      tipo = self.parsearTipo()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
        "t":"EncabezadoInstancia",
        "en":ubicación,
        "nombre":nombre
      }
    if self.salida.startswith('IHParen '):
      self.AvanzarSalida(len('IHParen '))
      ubicación = self.parsearUbicación()
      rec = self.parsearInstHead()
      self.cierraParen()
      return rec
    if self.salida.startswith('IHApp '):
      self.AvanzarSalida(len('IHApp '))
      ubicación = self.parsearUbicación()
      rec = self.parsearInstHead()
      tipo = self.parsearTipo()
      self.cierraParen()
      return rec
    self.errorDesconocido("El encabezado de la instancia no empieza con 'IHCon', 'IHInfix', 'IHParen' ni con 'IHApp'")

  ### XXXXXX

  # (self):
  #   self.abreParen()
  #   if self.salida.startswith('XXX'):
  #     self.AvanzarSalida(len('XXX'))
  #     ubicación = self.parsearUbicación()
  #     ...
  #     self.cierraParen()
  #     return {
  #       "t":"XXX",
  #       "en":ubicación
  #     }
  #   self.errorDesconocido("XXX no empieza con '', '', '' ni con ''")

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
        "t":"Ecuación",
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
      "t":"Nombre",
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
  def parsearOperador(self):
    # Un operador
    self.abreParen()
    if self.salida.startswith('VarOp '):
      self.AvanzarSalida(len('VarOp '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
      "t":"Operador",
      "en":ubicación,
      "operador":nombre
    }
    if self.salida.startswith('ConOp '):
      self.AvanzarSalida(len('ConOp '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
      "t":"Operador",
      "en":ubicación,
      "operador":nombre
    }
    self.errorDesconocido("El operador no empieza con 'VarOp' ni con 'ConOp'")
  def parsearOperadorQ(self):
    # Un operador Q
    self.abreParen()
    if self.salida.startswith('QVarOp '):
      self.AvanzarSalida(len('QVarOp '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
      "t":"Operador",
      "en":ubicación,
      "operador":nombre
    }
    if self.salida.startswith('QConOp '):
      self.AvanzarSalida(len('QConOp '))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombreQ()
      self.cierraParen()
      return {
      "t":"Operador",
      "en":ubicación,
      "operador":nombre
    }
    self.errorDesconocido("El operador no empieza con 'QVarOp' ni con 'QConOp'")
  def parsearPattern(self):
    self.abreParen()
    if self.salida.startswith('PVar'):
      self.AvanzarSalida(len('PVar'))
      ubicación = self.parsearUbicación()
      nombre = self.parsearNombre()
      self.cierraParen()
      return {
        "t":"Variable",
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
        "t":"Literal",
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
        "t":"AppInfija",
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
        "t":"Variable",
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
        "t":"AppInfija",
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
        "t":"Signo",
        "en":ubicación,
        "valor":"Positivo"
      }
    if self.salida.startswith('Negative'):
      self.AvanzarSalida(len('Negative'))
      ubicación = self.parsearUbicación()
      self.cierraParen()
      return {
        "t":"Signo",
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
        "t":"LiteralNúmero",
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