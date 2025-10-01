import os, io, json

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

def failCallback(data):
  if not os.path.isdir(carpetaFallos):
      os.mkdir(carpetaFallos)
  nombreArchivo = lambda x : os.path.join(carpetaFallos, "r" + str(x) + ".json")
  i=1
  while os.path.isfile(nombreArchivo(i)):
      i += 1
  f = io.open(nombreArchivo(i), mode='w', encoding='utf-8')
  f.write(json.dumps(data))
  f.close()