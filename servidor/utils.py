import os, io, json
import requests

URL_FORM_AVISOS = "1FAIpQLSf1kS-KBU5lDGZ2LsXUYOjBz5TCm39ngQASMsco2MNKWqAgBQ"
CAMPO_FORM_AVISOS = "370539263"

def mapear(f, l):
  return list(map(f, l))

def algunoCumple(f, l):
  for i in l:
    if f(i):
      return True
  return False

def aplanar(ls):
  nl = []
  for l in ls:
    for x in l:
      nl.append(x)
  return nl

def singularSiEsta(x):
  return [] if (x is None) else [x]

def texto_excepcion(e):
  res = str(e)
  tb = e.__traceback__
  while not (tb is None):
    res += "\n" + tb.tb_frame.f_code.co_filename + ":" + tb.tb_frame.f_code.co_name + " " + str(tb.tb_lineno)
    tb = tb.tb_next
  return res

def mostrar_excepcion(e):
  print(texto_excepcion(e))

carpetaFallos = "FAIL"

def failCallback(dataFile,FILENAME="r"):
  if FILENAME in ["_loadJson","_readData"]:
    return # No vale la pena registrarlos
  if not os.path.isdir(carpetaFallos):
    os.mkdir(carpetaFallos)
  nombreArchivo = lambda x : os.path.join(carpetaFallos, FILENAME + "_" + str(x) + ".json")
  i=1
  while os.path.isfile(nombreArchivo(i)):
    i += 1
  f = io.open(nombreArchivo(i), mode='w', encoding='utf-8')
  f.write(json.dumps(dataFile))
  f.close()
  dataForm = {}
  dataForm["entry." + CAMPO_FORM_AVISOS] = "[RT] bug " + str(i) + ((": " + dataFile["e"]) if ("e" in dataFile) else ".") + (("\n\nReportado por: " + dataFile["json"]["usuario"]) if (("json" in dataFile) and ("usuario" in dataFile["json"])) else "")
  requests.post("https://docs.google.com/forms/d/e/" + URL_FORM_AVISOS + "/formResponse", data = dataForm)