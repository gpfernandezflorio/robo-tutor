from correctorBase import Corrector
from analizador import analizarHaskell

class CorrectorHaskell(Corrector):
  def __init__(self):
    self.ruta = "src.hs"
    self.comando = "echo 'main' | ghci -v0 src.hs"
    self.globalPre = "import System.Exit\n\n"

  def Analizar(self, jsonObj):
    return analizarHaskell(jsonObj["src"], jsonObj["analisisCodigo"])

  def InicializarRun(self, run):
    self.tmpAridad = ""

  def AgregarCódigoVariablesDefinidas(self, run, jsonObj, code_run):
    pass

  def AgregarCódigoAridadFunciones(self, aridad, code_run):
    verificacion_aridad = ""
    code_run["pre"] = "import Data.Typeable\n" + code_run["pre"]
    code_run["lineasAdicionales"] = code_run["lineasAdicionales"] + 1
    for f in aridad:
      verificacion_aridad += '\n  if (((show . typeOf) ' + f + ') /= "' + aridad[f].replace("String","[Char]") + '")\n    then do\n      exitWith (ExitFailure 1)\n    else do\n      return ()'
    self.tmpAridad = verificacion_aridad # la necesito después

  def AgregarCódigoResultado(self, code_run, assertCode):
    code_run["post"] += "\n\nmain :: IO ()\nmain = do" + self.tmpAridad + "\n  if (" + assertCode + ")\n    then do\n      exitSuccess\n    else do\n      exitWith (ExitFailure 1)"

  def AdaptarResultado(self, resultadoEjecucion, code, code_run, aridad):
    # Haskell siempre devuelve errcode 0 y manda el verdadero exitcode a través del campo 'falla'
    AdaptarResultadoHaskell(resultadoEjecucion, code_run["lineasAdicionales"], len(code["src"].split("\n")), aridad)

  def buscarFalla(self, falla, code, code_run):
    return falla # Ya la procesé en AdaptarResultado

correctorHaskell = CorrectorHaskell()

def AdaptarResultadoHaskell(resultadoOriginal, n, m, aridad):
  falla = None
  i = 0
  todasLasLineas = resultadoOriginal["falla"].split('\n')
  resultadoOriginal["falla"] = ""
  if hayFallaDeAridad(todasLasLineas, aridad): # Falló al intentar deducir el tipo de una expresión
    resultadoOriginal["errcode"] = 1
  else:
    for l in todasLasLineas:
      if l == '*** Exception: ExitFailure 1': # No es una falla, es que falló un test
        resultadoOriginal["errcode"] = 1
        break
      elif l.startswith('*** Exception: src.hs:'):
        falla = procesarErrorHaskell(l,22,n,m,todasLasLineas[i+1:])
        break
      elif l.startswith('src.hs:'):
        falla = procesarErrorHaskell(l,7,n,m,todasLasLineas[i+1:])
        break
      i+=1
  if not (falla is None):
    resultadoOriginal["falla"] = falla
  return resultadoOriginal

def procesarErrorHaskell(l,inicio,n,m,otrasLíneas):
  linea = None
  fin = l.find(": ", inicio)
  nlinea = nLineaHaskell(l, inicio, fin)
  if nlinea > n:
    linea = nlinea - n
    if linea > m: # la falla está en el código que ejecuta el test (y no es por la aridad)!
      return "No se pueden correr los tests"
  falla = l[fin+2:] if fin > 0 else "Error desconocido"
  if falla == "error:":
    i=0
    while (i < len(otrasLíneas)) and (otrasLíneas[i] != "  |"):
      falla += " " + limpiarLíneaHaskell(otrasLíneas[i])
      i += 1
  if not (linea is None):
    falla = falla + "\nLínea: " + str(linea)
  return falla.replace("•","\n•")

def limpiarLíneaHaskell(l):
  iSrc = l.find('at src.hs')
  if iSrc < 0:
    iSrc = l.find('src.hs')
  return l[0:(len(l) if iSrc < 0 else iSrc)].strip()

def hayFallaDeAridad(ls, aridad):
  i=1
  for l in ls:
    if esFallaDeAridad(l, aridad, ls[i:]):
      return True
    i+=1
  return False

def esFallaDeAridad(l, aridad, siguientes):
  if not (aridad is None):
    for f in aridad:
      if l.startswith('      In the expression: ((show . typeOf) ' + f + ') /= "') or \
        l.endswith(': error: Variable not in scope: ' + f) or \
        esFallaDeAridadCon(l, f, siguientes):
          return True
  return False

def esFallaDeAridadCon(l, f, siguientes):
  líneaReconstruida = l
  espacios = cantidadDeEspacios(l)
  i=0
  while len(siguientes) > i and cantidadDeEspacios(siguientes[i]) > espacios:
    espacios = cantidadDeEspacios(siguientes[i])
    líneaReconstruida += siguientes[i][espacios-1:]
    i += 1
  return líneaReconstruida.startswith('      In the expression: ((show . typeOf) ' + f + ') /= "')

def cantidadDeEspacios(s):
  i=0
  while i < len(s) and s[i] == ' ':
    i += 1
  return i

def nLineaHaskell(l, i, f):
  if f > i:
    sl = l[i:f]
    dp = sl.find(":")
    if dp > 0:
      return int(sl[:dp])
    if sl.startswith("("):
      c = sl.find(",")
      if c > 0:
        return int(sl[1:c])
  return -1