# Cada regla es una función que toma como argumentos:
# - el analizador sintáctico del lenguaje (AnalizadorPython, AnalizadorGobstones, etc.)
# - el AST
# - el código (como un string)
# - la regla (un objeto cuyos campos son los atributos de la regla)
# y devuelve una lista de hallazgos (vacía si no hay ninguno) donde cada hallazgo es un objeto con los campos 'msg' (el mensaje a mostrar), 'línea' (la línea donde se encontró el hallazgo) y 'columna' (la columna donde se encontró el hallazgo)

def reglaComandosAnidados(analizador, AST, código, regla):
  máximaAnidacion = regla["max"] if "max" in regla else 1
  return buscarNodosCon_YGenerar_(analizador, AST,
    lambda nodo : analizador.es_UnComandoCompuesto(nodo) and analizador.nivelAnidaciónComandos_(nodo) >= máximaAnidacion,
    lambda nodo : "No está bueno anidar comandos compuestos"
  )

def reglaUnComandoPorLinea(analizador, AST, código, regla):
  return []

def reglaIndentacion(analizador, AST, código, regla):
  return []

REGLAS = {
  "NEST_CMD":reglaComandosAnidados,
  "CMD_X_LINE":reglaUnComandoPorLinea,
  "INDENT":reglaIndentacion
}

conceptos = [
  [ "REP_SIMPLE",
    (lambda analizador, AST, código, regla, nodo : (analizador.es_RepeticiónSimple(nodo))),
    "No está permitido usar repetición simple"
  ]
]

def reglaConcepto(concepto, analizador, AST, código, regla):
  return concepto[2] if concepto[1](analizador, AST, código, regla) else None

def buscarNodosCon_YGenerar_(analizador, AST, fVal, fMsg):
  resultado = []
  if fVal(AST):
    resultado.append({
      "msg":fMsg(AST),
      "línea":analizador.líneaDeNodo_(AST),
      "columna":analizador.columnaDeNodo_(AST)
    })
  for nodo in analizador.hijosDeNodo_(AST):
    resultado += buscarNodosCon_YGenerar_(analizador, nodo, fVal, fMsg)
  return resultado

for concepto in conceptos:
  REGLAS["CONCEPT_" + concepto[0]] = lambda analizador, AST, código, regla : buscarNodosCon_YGenerar_(analizador, AST,
    lambda nodo : concepto[1](analizador, AST, código, regla, nodo), lambda nodo : concepto[2]
  )