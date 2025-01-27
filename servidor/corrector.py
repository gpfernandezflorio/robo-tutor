# -*- coding: utf-8 -*-

import datetime
from subprocess import Popen
import select
import requests
import signal
import json
import io, os

from data import dameEjercicio, informacionPrivada, timeoutDefault

LOCAL_FILE = 'local.csv'

proceso_en_ejecucion = None

if not os.path.isfile(LOCAL_FILE):
  f = io.open(LOCAL_FILE, mode='w')
  f.write("ts,dni,src,res,ej")
  f.close()

def open_ej(jsonObj, v):
  jsonObj["src"] = "."
  jsonObj["resultado"] = "OPEN"
  commit(jsonObj, v)

def completarDataEjercicio(jsonObj):
  ejercicio = None
  if ("curso" in jsonObj) and ("ejercicio" in jsonObj):
    ejercicio = dameEjercicio(jsonObj["curso"], jsonObj["ejercicio"])
  elif "ejercicio" in jsonObj:
    ejercicio = jsonObj["ejercicio"]
  if not (ejercicio is None):
    for k in informacionPrivada:
      if k in ejercicio:
        jsonObj[k] = ejercicio[k]
      elif k in jsonObj:
        del jsonObj[k]

def run_code(jsonObj, v):
  if (not ("src" in jsonObj)):
    if (v):
      print("Falta src")
    return {"resultado":"Error", "error":"Falta src"}
  if (not ("lenguaje" in jsonObj)):
    if (v):
      print("Falta lenguaje")
    return {"resultado":"Error", "error":"Falta lenguaje"}
  completarDataEjercicio(jsonObj)
  if (jsonObj["lenguaje"] == "Python"):
    resultado = run_python(jsonObj, v)
  elif (jsonObj["lenguaje"] == "Gobstones"):
    resultado = run_gobstones(jsonObj, v)
  else:
    if (v):
      print(jsonObj["lenguaje"])
    return {"resultado":"Error", "error":"Lenguaje desconocido: " + jsonObj["lenguaje"]}
  if ("dni" in jsonObj):
    jsonObj["resultado"] = mostrar_resultado(resultado)
    commit(jsonObj, v)
  return resultado

def run_python(jsonObj, v):
  global proceso_en_ejecucion
  run_data = jsonObj["run_data"] if "run_data" in jsonObj else {}
  if (type(run_data) != type([])):
    run_data = [run_data]
  code = jsonObj["src"]
  timeout = jsonObj["timeout"] if ("timeout" in jsonObj) else timeoutDefault()
  if (v):
    print(code)
  cm = verificarCodigoMaliciosoPython(code)
  if not (cm is None):
    return {"resultado":"EVIL", "error":cm}
  lineasAdicionales = 0
  codigoPre = prePython() + "\n\n"
  lineasAdicionales = codigoPre.count('\n')
  code = codigoPre + code
  if "pre" in jsonObj:
    code = jsonObj["pre"] + "\n\n" + code
    lineasAdicionales = lineasAdicionales + jsonObj["pre"].count("\n") + 2
  for run in run_data:
    code_run = code
    lineasAdicionales_run = lineasAdicionales
    ## Inicialización
    if "pre" in run:
      code_run = run["pre"] + "\n\n" + code_run
      lineasAdicionales_run = lineasAdicionales_run + run["pre"].count("\n") + 2
    ## Variables definidas
    if "def" in run:
      defs = run["def"]
      if (type(defs) != type([])):
        defs = [defs]
      for d in defs:
        code_run = code_run + "try:\n  eval(" + d + ")\nexcept Exception as e:\n  print('DEF " + d + "')"
    ## Aridad de funciones correcta
    aridad = None
    if "aridad" in run:
      aridad = run["aridad"]
    elif "aridad" in jsonObj:
      aridad = jsonObj["aridad"]
    if not (aridad is None):
      code_run = "import inspect\n\n" + code_run
      lineasAdicionales_run = lineasAdicionales_run + 2
      for f in aridad:
        verificacion_aridad = "\n\n" + "try:\n  args = len(inspect.getfullargspec(eval('" + f + "')).args)\n  if (args != " + str(aridad[f]) + "):\n    print('ARGS " + f + "' + str(args) + '[" + str(aridad[f]) + "]')\nexcept Exception as e:\n  print('ARGS Err')\n  print(e)"
        code_run = code_run + verificacion_aridad
    ## Resultado
    if "post" in run:
      code_run = code_run + "\n\n" + "if (" + run["post"] + "):\n  exit(0)\nelse:\n  exit(1)"
    ## Ejecución del código entregado
    f = open('src.py', 'w')
    f.write(code_run)
    f.close()
    signal.alarm(timeout)
    errcode, salida, falla = ejecutar("python3 src.py")
    signal.alarm(0)
    if proceso_en_ejecucion is None:
      return {"resultado":"Except", "error":"La ejecución demoró más de lo permitido"}
    else:
      proceso_en_ejecucion = None
    if len(falla) > 0:
      if (v):
        print(falla)
      return {"resultado":"Except", "error":buscar_falla_python(falla, lineasAdicionales_run)}
    if errcode != 0:
      return {"resultado":"Falla"}
  return {"resultado":"OK"}

def run_gobstones(jsonObj, v):
  global proceso_en_ejecucion
  run_data = jsonObj["run_data"] if "run_data" in jsonObj else {}
  if (type(run_data) != type([])):
    run_data = [run_data]
  code = jsonObj["src"]
  timeout = jsonObj["timeout"] if ("timeout" in jsonObj) else timeoutDefault()
  if (v):
    print(code)
  lineasAdicionales = 0
  if "pre" in jsonObj:
    code = jsonObj["pre"] + "\n\n" + code
    lineasAdicionales = lineasAdicionales + jsonObj["pre"].count("\n") + 2
  ## Código
  f = open('src.txt', 'w')
  f.write(code)
  f.close()
  for run in run_data:
    lineasAdicionales_run = lineasAdicionales
    ## Tablero inicial
    tablero = run["tablero"] if "tablero" in run else tablero_default()
    f = open('board.jboard', 'w')
    f.write(json.dumps(tablero))
    f.close()
    signal.alarm(timeout)
    errcode, salida, falla = ejecutar("node gobstones-lang/dist/gobstones-lang run -l es -i src.txt -b")
    signal.alarm(0)
    if proceso_en_ejecucion is None:
      return {"resultado":"Except", "error":"La ejecución demoró más de lo permitido"}
    else:
      proceso_en_ejecucion = None
    if len(falla) > 0:
      return {"resultado":"Except", "error":buscar_falla_gobstones(falla, lineasAdicionales_run)}
    try:
      salida = json.loads(salida)
    except Exception as e:
      if (v):
        mostrar_excepcion(e)
      return {"resultado":"Except", "error":str(e)}
    ## Validar tablero final
    if "post" in run:
      tablero_esperado = run["post"]
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
        return {"resultado":"Falla"}
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
            return {"resultado":"Falla"}
  return {"resultado":"OK"}

def handler_timeout(s, f):
  global proceso_en_ejecucion
  if not (proceso_en_ejecucion is None):
    proceso_en_ejecucion.kill()
    proceso_en_ejecucion = None

signal.signal(signal.SIGALRM, handler_timeout)

def ejecutar(cmd):
  global proceso_en_ejecucion
  fOut = open('stdout.out','w')
  fErr = open('stderr.out','w')
  p = Popen(cmd, stdout=fOut, stderr=fErr, universal_newlines=True, shell=True)
  proceso_en_ejecucion = p
  errcode = p.wait()
  fOut.close()
  fErr.close()
  stdout = ""
  stderr = ""
  fOut = open('stdout.out','r')
  for line in fOut.read():
      stdout += line
  fOut.close()
  fErr = open('stderr.out','r')
  for line in fErr.read():
      stderr += line
  fErr.close()
  return errcode, stdout, stderr

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
      return falla + "\nLínea: " + str(int(l[11:-1]) - n)
  print(s)
  return falla

def buscar_falla_python(s, n):
  falla = "?"
  linea = None
  for l in s.split('\n'):
    if l.startswith('  File "src.py", line'):
      fin = l.find(",", 22)
      nlinea = int(l[22:fin] if fin > 0 else l[22:])
      if nlinea > n:
        linea = str(nlinea - n)
    if not (l.startswith('Traceback') or l.startswith('  ')):
      falla = l
      if not (linea is None):
        falla = falla + "\nLínea: " + linea
      return falla
  return falla

def mostrar_excepcion(e):
  res = str(e)
  tb = e.__traceback__
  while not (tb is None):
    res += "\n" + tb.tb_frame.f_code.co_filename + ":" + tb.tb_frame.f_code.co_name + " " + str(tb.tb_lineno)
    tb = tb.tb_next
  print(e)

def mostrar_resultado(resultado):
  r = resultado["resultado"]
  if "error" in resultado:
    r += " - " + resultado["error"].split("\n")[0]
  return r

form_url = "https://docs.google.com/forms/d/e/1FAIpQLScHNF1TFEZrcSLNLYbxxFOHIVPyml9dpZTpqJ_WJSqGPanOAw/formResponse"
entries = {
  "dni":"1115080072",
  "src":"256509475",
  "resultado":"236721452",
  "ejercicio":"1084236439"
}

def commit(jsonObj, v):
  if "ejercicio" in jsonObj:
    if type(jsonObj["ejercicio"]) == type({}):
      jsonObj["ejercicio"] = jsonObj["ejercicio"]["nombre"]
  else:
    jsonObj["ejercicio"] = "-"
  if "curso" in jsonObj:
    jsonObj["ejercicio"] = jsonObj["curso"] + " : " + jsonObj["ejercicio"]
  data_form = {}
  data_csv = [str(datetime.datetime.now())]
  for x in entries:
    data_form["entry." + entries[x]] = jsonObj[x]
    data_csv.append(limpiar_csv(jsonObj[x].replace('"','""')))
  guardarLocal(",".join(data_csv))
  # submit(form_url, data_form, jsonObj["dni"], v)

def submit(url, data, dni, v):
  try:
    requests.post(url, data = data)
  except Exception as e:
    if (v):
      mostrar_excepcion(e)
    print("ERROR " + dni)

def guardarLocal(s):
  f = io.open(LOCAL_FILE, mode='a')
  f.write("\n" + s)
  f.close()

def limpiar_csv(s):
  return '"' + s + '"' if ("," in s) or ("\n" in s) else s

def prePython():
  return '''def secure_importer(name, globals=None, locals=None, fromlist=(), level=0):
  raise ImportError("No está permitido importar módulos")
__builtins__.__dict__['__import__'] = secure_importer'''

def verificarCodigoMaliciosoPython(codigo):
  if "exit" in codigo:
    return "No está permitido usar 'exit'"
  return None