from correctorBase import Corrector
from analizador import analizarPython

class CorrectorPython(Corrector):
  def __init__(self):
    self.ruta = "src.py"
    self.comando = "python3 src.py"

  def Analizar(self, jsonObj):
    return analizarPython(jsonObj["src"], jsonObj["analisisCodigo"])

  def InicializarRun(self, run):
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
      code_run["post"] += "\ntry:\n  eval('" + d + "')\nexcept Exception as e:\n  print('DEF " + d + "')\n  exit(1)"

  def AgregarCódigoAridadFunciones(self, aridad, code_run):
    code_run["pre"] = "import inspect\n\n" + code_run["pre"]
    code_run["lineasAdicionales"] = code_run["lineasAdicionales"] + 2
    for f in aridad:
      verificacion_aridad = "\n\n" + "try:\n  args = len(inspect.getfullargspec(eval('" + f + "')).args)\n  if (args != " + str(aridad[f]) + "):\n    print('ARGS " + f + " ' + str(args) + ' [" + str(aridad[f]) + "]')\n    exit(1)\nexcept NameError as e:\n  print('DEF " + f + "')\n  exit(1)\nexcept Exception as e:\n  print('ARGS Err')\n  print(e)\n  exit(1)"
      code_run["post"] += verificacion_aridad

  def AgregarCódigoResultado(self, code_run, assertCode):
    code_run["post"] += "\n\n" + "if (" + assertCode + "):\n  exit(0)\nelse:\n  exit(1)"

  def buscarFalla(self, falla, code, code_run):
    return buscar_falla_python(falla, code_run["lineasAdicionales"], len(code["src"].split("\n")))

correctorPython = CorrectorPython()

def buscar_falla_python(s, n, m):
  falla = None
  linea = None
  tb = []
  for l in s.split('\n'):
    if l.startswith('  File "'):
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
          return "No se pueden correr los tests"
        falla = falla + "\nLínea: " + str(linea)
        if len(tb) > 1:
          falla = falla + "\n\nLlamados:" + "".join(tb)
      return falla
  return falla

def esLineaIgnorable(l):
  return l.startswith('Traceback') or l.startswith('  ') or l.startswith('/') or 'src.py' in l or len(l) < 2