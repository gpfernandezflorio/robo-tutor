from correctorBase import Corrector
from analizador import analizarPython
from msg import *

class CorrectorPython(Corrector):
  def __init__(self):
    super().__init__()
    self.ruta = "src.py"
    self.comando = "python3 src.py"
    self.globalPost = "import sys"

  def Analizar(self, código, reglas, extras):
    return analizarPython(código, reglas, extras)

  def InicializarRun(self, run, ruta):
    pass

  def AgregarCódigoVariablesDefinidas(self, run, jsonObj, code_run):
    defs = []
    if "def" in run:
      defs = run["def"]
    elif "def" in jsonObj["ejercicio"]:
      defs = jsonObj["ejercicio"]["def"]
    if (type(defs) != type([])):
      defs = [defs]
    for d in defs:
      code_run["post"] += "\ntry:\n  eval('" + d + "')\nexcept Exception as e:\n  print('DEF " + d + "', file=sys.stderr)\n  exit(1)"

  def AgregarCódigoAridadFunciones(self, aridad, code_run):
    code_run["pre"] = "import inspect\n\n" + code_run["pre"]
    code_run["lineasAdicionales"] = code_run["lineasAdicionales"] + 2
    for f in aridad:
      verificacion_aridad = "\n\n" + "try:\n  args = len(inspect.getfullargspec(eval('" + f + "')).args)\n  if (args != " + str(aridad[f]) + "):\n    print('ARGS " + f + " ' + str(args) + ' " + str(aridad[f]) + "', file=sys.stderr)\n    exit(1)\nexcept NameError as e:\n  print('DEF " + f + "', file=sys.stderr)\n  exit(1)\nexcept Exception as e:\n  print('ARGS Err', file=sys.stderr)\n  print(e, file=sys.stderr)\n  exit(1)"
      code_run["post"] += verificacion_aridad

  def AgregarCódigoResultado(self, code_run, assertCode):
    code_run["post"] += "\n\n" + "if (" + assertCode + "):\n  exit(0)\nelse:\n  exit(1)"

  def AgregarCódigoEvaluación(self, code_run, evalObj):
    nombreVariableRes = "res" # nombreSeguro(code_run, evalObj, ...)
    code_run["post"] += "\n\n" + nombreVariableRes + " = " + evalObj["expr"]
    if "vals" in evalObj:
      for res in evalObj["vals"]:
        code_run["post"] += "\nif (" + nombreVariableRes + " == " + res + "):\n  "
        code_run["post"] += "exit(0)" \
          if (evalObj["vals"][res] == "OK") \
          else ("print('NO " + evalObj["vals"][res] + "', file=sys.stderr)\n  exit(1)")
      code_run["post"] += "\nelse:\n  exit(1)"
    elif "checks" in evalObj:
      for check in evalObj["checks"]:
        code_run["post"] += "\nif (" + check["fVal"](nombreVariableRes) + "):\n  "
        msg = ""
        if type(check["msg"]) == type(""):
          msg = check["msg"]
        else:
          for m in check["msg"]:
            msg += "' + str(" + nombreVariableRes + ") + '" if m is None else m
        code_run["post"] += "exit(0)" \
          if (msg == "OK") \
          else ("print('NO " + msg + "', file=sys.stderr)\n  exit(1)")
      code_run["post"] += "\nelse:\n  exit(1)"

  def buscarFalla(self, falla, code, code_run):
    return buscar_falla_python(falla, code_run["lineasAdicionales"], len(code["src"].split("\n")))

correctorPython = CorrectorPython()

def buscar_falla_python(s, n, m):
  linea = None
  tb = []
  for l in s.split('\n'):
    if l.startswith("NO "):
      return {"resultado":"NO", "mensaje":l[3:]}
    elif l.startswith("DEF "):
      return {"resultado":"NO", "mensaje":mensajeFaltaDefinición(l[4:])}
    elif l == "ARGS Err":
      pass # ¿Qué hago acá?
    elif l.startswith("ARGS "):
      info = l[5:].split(" ")
      return {"resultado":"NO", "mensaje":mensajeFallaParámetros(
        info[0], int(info[2]), int(info[1])
      )}
    elif l.startswith('  File "'):
      inicio = l.find('src.py", line ')
      if inicio > 0:
        inicio = inicio + 14
        fin = l.find(",", inicio)
        nlinea = int(l[inicio:fin] if fin > 0 else l[inicio:])
        if nlinea > n:
          linea = nlinea - n
          if fin > 0 and not ("<module>" in l[fin:]):
            tb.insert(0, "\n > " + l[fin + 5:] + " (línea " + str(linea) + ")")
    if not esLineaIgnorable(l):
      falla = l
      if not (linea is None):
        if linea > m: # la falla está en el código que ejecuta el test!
          return {"resultado":"Except", "error":"No se pueden correr los tests"}
        falla = falla + "\nLínea: " + str(linea)
        if len(tb) > 1:
          falla = falla + "\n\nLlamados:" + "".join(tb)
      return {"resultado":"Except", "error":falla}
  return None

def esLineaIgnorable(l):
  return l.startswith('Traceback') or l.startswith('  ') or l.startswith('/') or 'src.py' in l or len(l) < 2