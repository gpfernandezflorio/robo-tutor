'''
    head: [columna, fila]
    board: [col0, col1, ... coln]
        coli: [celda0, celda1, ... celdan]
            celdai: {a: , n: , r: , v: }
'''

v = {"a": 0, "n": 0, "r": 0, "v": 0} # Celda vacía
r = {"a": 0, "n": 0, "r": 1, "v": 0} # Celda con una roja
a = {"a": 1, "n": 0, "r": 0, "v": 0} # Celda con una azul
g = {"a": 0, "n": 0, "r": 0, "v": 1} # Celda con una verde (no puedo usar 'v' porque ya la usé para la celda vacía)
n = {"a": 0, "n": 1, "r": 0, "v": 0} # Celda con una negra
def c(a,n,r,v): # celda con ...
  return {"a": a, "n": n, "r": r, "v": v}
def a_s(x): # Celda con varias azules
  return c(x,0,0,0)
def ns(x): # Celda con varias negras
  return c(0,x,0,0)
def rs(x): # Celda con varias rojas
  return c(0,0,x,0)
def gs(x): # Celda con varias verdes
  return c(0,0,0,x)
def duplicarTablero(b):
  return list(map(lambda col: duplicarColumna(col), b))
def duplicarColumna(col):
  return list(map(lambda x: c(x["a"], x["n"], x["r"], x["v"]), col))
def agregarRojas(b,k):
  b2 = duplicarTablero(b)
  b2[3][2]["r"] = b2[3][2]["r"] + k
  return b2

def tv(w,h):
  tablero = []
  for c in range(w):
    columna = []
    for r in range(h):
      columna.append(v)
    tablero.append(columna)
  return tablero

def celdaCambiadaPorBooleano(celda, b):
  return c(
    celda["a"], celda["n"], celda["r"] + (0 if b else 1), celda["v"] + (1 if b else 0)
  )

def programParaValidarBoolEnCelda(expresión):
  return "program {Poner(choose Verde when ("+expresión+") Rojo otherwise)}"

def validarBoolEnCelda(expresión, b, celda, pre=""):
  return {
    "pre":pre+programParaValidarBoolEnCelda(expresión),
    "t0":{"head":[0,0],"width":1,"height":1,"board":[[celda]]},
    "tf":{"head":[0,0],"width":1,"height":1,"board":[[
      celdaCambiadaPorBooleano(celda, b)
    ]]}
  }

def validarBoolEnTablero(expresión, b, t0):
  head = t0["head"]
  width = t0["width"]
  height = t0["height"]
  b0 = t0["board"]
  bf = []
  for col in range(width):
    columna = []
    for row in range(height):
      columna.append(celdaCambiadaPorBooleano(b0[col][row],b) if head == [col,row] else b0[col][row])
    bf.append(columna)
  tf = {
    "head":head,
    "width":width,
    "height":height,
    "board":bf
  }
  return {
    "pre":programParaValidarBoolEnCelda(expresión),
    "t0":t0,
    "tf":tf
  }

def celdaCambiadaPorNúmero(celda, n):
  return c(
    celda["a"] + n, celda["n"], celda["r"], celda["v"]
  )

def programParaValidarNumEnCelda(expresión):
  return "program {repeat("+expresión+"){Poner(Azul)}}"

def validarNumEnCelda(expresión, n, celda):
  return {
    "pre":programParaValidarNumEnCelda(expresión),
    "t0":{"head":[0,0],"width":1,"height":1,"board":[[celda]]},
    "tf":{"head":[0,0],"width":1,"height":1,"board":[[celdaCambiadaPorNúmero(celda, n)]]}
  }

def validarNumEnTablero(expresión, n, t0):
  head = t0["head"]
  width = t0["width"]
  height = t0["height"]
  b0 = t0["board"]
  bf = []
  for col in range(width):
    columna = []
    for row in range(height):
      columna.append(celdaCambiadaPorNúmero(b0[col][row],n) if head == [col,row] else b0[col][row])
    bf.append(columna)
  tf = {
    "head":head,
    "width":width,
    "height":height,
    "board":bf
  }
  return {
    "pre":programParaValidarNumEnCelda(expresión),
    "t0":t0,
    "tf":tf
  }

def celdaCambiadaPorColor(celda, claveColor):
  return c(
    celda["a"] + (1 if claveColor == "a" else 0),
    celda["n"] + (1 if claveColor == "n" else 0),
    celda["r"] + (1 if claveColor == "r" else 0),
    celda["v"] + (1 if claveColor == "v" else 0)
  )

def programParaValidarColorEnCelda(expresión):
  return "program {Poner("+expresión+")}"

def validarColorEnCelda(expresión, claveColor, celda):
  return {
    "pre":programParaValidarColorEnCelda(expresión),
    "t0":{"head":[0,0],"width":1,"height":1,"board":[[celda]]},
    "tf":{"head":[0,0],"width":1,"height":1,"board":[[celdaCambiadaPorColor(celda, claveColor)]]}
  }

def validarColorEnTablero(expresión, claveColor, t0):
  head = t0["head"]
  width = t0["width"]
  height = t0["height"]
  b0 = t0["board"]
  bf = []
  for col in range(width):
    columna = []
    for row in range(height):
      columna.append(celdaCambiadaPorColor(b0[col][row],claveColor) if head == [col,row] else b0[col][row])
    bf.append(columna)
  tf = {
    "head":head,
    "width":width,
    "height":height,
    "board":bf
  }
  return {
    "pre":programParaValidarColorEnCelda(expresión),
    "t0":t0,
    "tf":tf
  }

def expresiónDirAColor(expresión):
  return "choose Azul when (("+expresión+")==Norte) Negro when (("+expresión+")==Este) Rojo when (("+expresión+")==Sur) Verde otherwise"

def dirAClaveColor(d):
  return {"N":"a", "E":"n", "S":"r", "O":"v"}[d]

def validarDirEnCelda(expresión, d, celda):
  # Uso colores para codificar las direcciones
  return validarColorEnCelda(expresiónDirAColor(expresión), dirAClaveColor(d), celda)

def validarDirEnTablero(expresión, d, t0):
  # Uso colores para codificar las direcciones
  return validarColorEnTablero(expresiónDirAColor(expresión), dirAClaveColor(d), t0)

def validarTransformaciónCeldaCon(comando,c1,c2):
  return {
    "pre":"program{"+comando+"}",
    "t0":{"head":[0,0],"width":1,"height":1,"board":[[c1]]},
    "tf":{"head":[0,0],"width":1,"height":1,"board":[[c2]]}
  }

def validarTransformaciónCelda(c1,c2):
  return {
    "t0":{"head":[0,0],"width":1,"height":1,"board":[[c1]]},
    "tf":{"head":[0,0],"width":1,"height":1,"board":[[c2]]}
  }

def CambiarCeldaTablero(t, pos, cof):
  if (type(cof) == type(lambda x : x)):
    cof(t["board"][pos[0]][pos[1]])
  else:
    t["board"][pos[0]][pos[1]] = cof