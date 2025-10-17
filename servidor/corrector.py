# -*- coding: utf-8 -*-

import json
from analizador import analizarPython, analizarGobstones
from procesos import ejecutarConTimeout
from utils import mostrar_excepcion

def run_code(jsonObj, v):
  if (not ("src" in jsonObj)):
    if (v):
      print("Falta src")
    return {"resultado":"Error", "error":"Falta src"}
  if (not ("lenguaje" in jsonObj)):
    if (v):
      print("Falta lenguaje")
    return {"resultado":"Error", "error":"Falta lenguaje"}
  if (jsonObj["lenguaje"] == "Python"):
    resultado = run_python(jsonObj, v)
  elif (jsonObj["lenguaje"] == "Gobstones"):
    resultado = run_gobstones(jsonObj, v)
  else:
    if (v):
      print(jsonObj["lenguaje"])
    return {"resultado":"Error", "error":"Lenguaje desconocido: " + jsonObj["lenguaje"]}
  return resultado

def run_python(jsonObj, v):
  run_data = jsonObj["ejercicio"]["run_data"] if "run_data" in jsonObj["ejercicio"] else {}
  if (type(run_data) != type([])):
    run_data = [run_data]
  code = {
    "pre":"",
    "src":jsonObj["src"]
  }
  if (v):
    print(code["src"])
  ## Código
  resultadoAnalisisCodigo = analizarPython(code["src"], jsonObj["analisisCodigo"])
  if not(resultadoAnalisisCodigo is None):
    return resultadoAnalisisCodigo
  timeout = jsonObj["ejercicio"]["timeout"] if ("timeout" in jsonObj["ejercicio"]) else timeoutDefault()
  lineasAdicionales = 0
  if "pre" in jsonObj["ejercicio"]:
    code["pre"] = jsonObj["ejercicio"]["pre"] + "\n"
    lineasAdicionales = lineasAdicionales + jsonObj["ejercicio"]["pre"].count("\n") + 1
  ## Ejecuciones
  duraciones = []
  for run in run_data:
    code_run = {
      "pre":code["pre"],
      "post":"\n"
    }
    lineasAdicionales_run = lineasAdicionales
    ## Inicialización
    if "pre" in run:
      code_run["pre"] = code_run["pre"] + "\n\n" + run["pre"]
      lineasAdicionales_run = lineasAdicionales_run + run["pre"].count("\n") + 2
    ## Variables definidas
    defs = []
    if "def" in run:
      defs = run["def"]
    elif "def" in jsonObj["ejercicio"]:
      defs = jsonObj["ejercicio"]["def"]
    if (type(defs) != type([])):
      defs = [defs]
    for d in defs:
      code_run["post"] += "\ntry:\n  eval('" + d + "')\nexcept Exception as e:\n  print('DEF " + d + "')\n  exit(1)"
    ## Aridad de funciones correcta
    aridad = None
    if "aridad" in run:
      aridad = run["aridad"]
    elif "aridad" in jsonObj["ejercicio"]:
      aridad = jsonObj["ejercicio"]["aridad"]
    if not (aridad is None):
      code_run["pre"] = "import inspect\n\n" + code_run["pre"]
      lineasAdicionales_run = lineasAdicionales_run + 2
      for f in aridad:
        verificacion_aridad = "\n\n" + "try:\n  args = len(inspect.getfullargspec(eval('" + f + "')).args)\n  if (args != " + str(aridad[f]) + "):\n    print('ARGS " + f + " ' + str(args) + ' [" + str(aridad[f]) + "]')\n    exit(1)\nexcept NameError as e:\n  print('DEF " + f + "')\n  exit(1)\nexcept Exception as e:\n  print('ARGS Err')\n  print(e)\n  exit(1)"
        code_run["post"] += verificacion_aridad
    ## Resultado
    if "post" in jsonObj["ejercicio"]:
      code_run["post"] += "\n\n" + jsonObj["ejercicio"]["post"]
    if "post" in run:
      code_run["post"] += "\n\n" + run["post"]
    if "assert" in run:
      code_run["post"] += "\n\n" + "if (" + run["assert"] + "):\n  exit(0)\nelse:\n  exit(1)"
    ## Ejecución del código entregado
    code_run["pre"] += "\n\n"
    lineasAdicionales_run = lineasAdicionales_run + 2
    f = open('src.py', 'w')
    f.write(code_run["pre"] + code["src"] + code_run["post"])
    f.close()
    resultadoEjecucion = ejecutarConTimeout("python3 src.py", timeout)
    if resultadoEjecucion["resultado"] == "TIMEOUT":
      return {"resultado":"Except", "error":"La ejecución demoró más de lo permitido"}
    duraciones.append(resultadoEjecucion["duracion"])
    if len(resultadoEjecucion["falla"]) > 0:
      if (v):
        print(resultadoEjecucion["falla"])
      fallaReal = buscar_falla_python(resultadoEjecucion["falla"], lineasAdicionales_run, len(code["src"].split("\n")))
      if not (fallaReal is None):
        return {"resultado":"Except", "error":fallaReal}
    if resultadoEjecucion["errcode"] != 0:
      return {"resultado":"NO"}
  return {"resultado":"OK","duracion":sum(duraciones)/len(duraciones)}

def run_gobstones(jsonObj, v):
  run_data = jsonObj["ejercicio"]["run_data"] if "run_data" in jsonObj["ejercicio"] else {}
  if (type(run_data) != type([])):
    run_data = [run_data]
  code = jsonObj["src"]
  if (v):
    print(code)
  timeout = jsonObj["ejercicio"]["timeout"] if ("timeout" in jsonObj["ejercicio"]) else timeoutDefault()
  lineasAdicionales = 0
  if "pre" in jsonObj["ejercicio"]:
    code = jsonObj["ejercicio"]["pre"] + "\n\n" + code
    lineasAdicionales = lineasAdicionales + jsonObj["ejercicio"]["pre"].count("\n") + 2
  ## Código
  f = open('src.txt', 'w')
  f.write(code)
  f.close()
  resultadoAnalisisCodigo = analizarGobstones(code, jsonObj["analisisCodigo"])
  if not(resultadoAnalisisCodigo is None):
    if "falla" in resultadoAnalisisCodigo:
      return {"resultado":"Except", "error":buscar_falla_gobstones(resultadoAnalisisCodigo["falla"], lineasAdicionales)}
    return resultadoAnalisisCodigo
  ## Ejecuciones
  duraciones = []
  for run in run_data:
    lineasAdicionales_run = lineasAdicionales
    ## Tablero inicial
    tablero = run["t0"] if "t0" in run else tablero_default()
    f = open('board.jboard', 'w')
    f.write(json.dumps(tablero))
    f.close()
    resultadoEjecucion = ejecutarConTimeout("node gobstones-lang/dist/gobstones-lang run -l es -i src.txt -b", timeout)
    if resultadoEjecucion["resultado"] == "TIMEOUT":
      return {"resultado":"Except", "error":"La ejecución demoró más de lo permitido"}
    duraciones.append(resultadoEjecucion["duracion"])
    if len(resultadoEjecucion["falla"]) > 0:
      return {"resultado":"Except", "error":buscar_falla_gobstones(resultadoEjecucion["falla"], lineasAdicionales_run)}
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
  return {"resultado":"OK","duracion":sum(duraciones)/len(duraciones)}

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
        falla = falla + "\nLínea: " + str(linea)
      return falla
  # print(s)
  return falla

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

def timeoutDefault():
  return 1
