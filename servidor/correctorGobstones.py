import os, json
from correctorBase import Corrector
from analizador import analizarGobstones
from utils import mostrar_excepcion

class CorrectorGobstones(Corrector):
  def __init__(self):
    super().__init__()
    self.ruta = "src.txt"
    self.comando = "node /rtTest/gbs/dist/gobstones-lang run -l es -i src.txt -b"

  def Analizar(self, código, reglas, extras):
    resultadoAnalisisCodigo = analizarGobstones(código, reglas, extras)
    if not(resultadoAnalisisCodigo is None):
      if resultadoAnalisisCodigo["resultado"] == "Except":
        errorMsg = resultadoAnalisisCodigo["errorMsg"] \
          if ("errorMsg" in resultadoAnalisisCodigo) \
          else buscar_falla_gobstones(resultadoAnalisisCodigo["error"], extras["desde"]-1)
        return {"resultado":"Except", "error":errorMsg}
    return resultadoAnalisisCodigo

  def InicializarRun(self, run, ruta):
    ## Tablero inicial
    tablero = run["t0"] if "t0" in run else tablero_default()
    f = open(os.path.join(ruta, 'board.jboard'), 'w')
    f.write(json.dumps(tablero))
    f.close()

  def AgregarCódigoVariablesDefinidas(self, run, jsonObj, code_run):
    pass

  def AgregarCódigoAridadFunciones(self, aridad, code_run):
    pass

  def AgregarCódigoResultado(self, code_run, assertCode):
    pass

  def buscarFalla(self, falla, code, code_run):
    return buscar_falla_gobstones(falla, code_run["lineasAdicionales"])

  def validaciónFinal(self, run, resultadoEjecucion, v):
    try:
      salida = json.loads(resultadoEjecucion["salida"])
    except Exception as e:
      if (v):
        mostrar_excepcion(e)
      return {"resultado":"Except", "error":str(e)}
    ## Validar tablero final
    if "tf" in run:
      tablero_esperado = run["tf"]
      tablero_obtenido = salida
      if (v):
        print(tablero_esperado)
        print(tablero_obtenido)
      if not (tablero_valido(tablero_esperado) and tablero_valido(tablero_obtenido)):
        return {"resultado":"Error", "error":"Error en el ejercicio (POST:tablero válido)"}
      cabezal_esperado = tablero_esperado["head"]
      cabezal_obtenido = tablero_obtenido["head"]
      if not (cabezal_valido(cabezal_esperado) and cabezal_valido(cabezal_obtenido)):
        return {"resultado":"Error", "error":"Error en el ejercicio (POST:cabezal)"}
      if not mismo_cabezal(cabezal_esperado, cabezal_obtenido):
        return {"resultado":"NO"}
      if not (tablero_esperado["width"] == tablero_obtenido["width"] and tablero_esperado["height"] == tablero_obtenido["height"]):
        return {"resultado":"Error", "error":"Error en el ejercicio (POST:dimensiones)"}
      tablero_esperado = tablero_esperado["board"]
      tablero_obtenido = tablero_obtenido["board"]
      if not (len(tablero_esperado) == len(tablero_obtenido)):
        return {"resultado":"Error", "error":"Error en el ejercicio (POST:tablero final)"}
      for x in range(len(tablero_esperado)):
        columna_esperada = tablero_esperado[x]
        columna_obtenida = tablero_obtenido[x]
        if not (len(columna_esperada) == len(columna_obtenida)):
          return {"resultado":"Error", "error":"Error en el ejercicio (POST:columna final)"}
        for y in range(len(columna_esperada)):
          if not misma_celda(columna_esperada[y], columna_obtenida[y]):
            return {"resultado":"NO"}
    return None

correctorGobstones = CorrectorGobstones()

def tablero_valido(t):
  return all(map(lambda x : x in t, ["head","width","height","board"]))

def cabezal_valido(h):
  return len(h) == 2 or len(h) == 0

def mismo_cabezal(h1, h2):
  return len(h1) == 0 or (h1[0] == h2[0] and h1[1] == h2[1])

def misma_celda(c1, c2):
  return c1["a"] == c2["a"] and c1["r"] == c2["r"] and c1["n"] == c2["n"] and c1["v"] == c2["v"]

def tablero_default():
  return {
    "head":[0,0],
    "width":4,
    "height":4,
    "board":list(map(lambda x : columna_default(), [1,2,3,4]))
  }

def columna_default():
  return list(map(lambda x : celda_vacia(), [1,2,3,4]))

def celda_vacia():
  return {
    "a":0,
    "r":0,
    "n":0,
    "v":0
  }

def buscar_falla_gobstones(s, n):
  falla = "?"
  for l in s.split('\n'):
    if l.startswith('br [Error]: ') or l.startswith('Pr [Error]: '):
      falla = l[12:]
    elif l.startswith('    _line: '):
      linea = int(l[11:-1]) - n
      if linea > 0:
        falla = LimpiarNúmerosDeLínea(falla, n) + "\nLínea: " + str(linea)
      return falla
  print(s) # ¿error?
  return falla

def LimpiarNúmerosDeLínea(texto, n):
  res = ""
  j = 0
  i = texto.find("(?):")
  while i >= 0 and i < len(texto) - 4:
    res += texto[j:i]
    fI = texto.find(":", i+4)
    if fI >= i+5:
      l = int(texto[i+4:fI])
      if l > 0:
        res += ("la línea " + str(l-n)) if l > n else "(?)"
      else:
        res += "(?)"
    else:
      res += "(?)"
    j = texto.find(" ", fI)
    i = -1 if (j < 0) else texto.find("(?):", j)
  res += texto[j:] if (j >= 0) else ""
  return res