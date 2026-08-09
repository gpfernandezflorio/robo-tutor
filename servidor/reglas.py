# Cada regla es una función que toma como argumentos:
# - el analizador sintáctico del lenguaje (AnalizadorPython, AnalizadorGobstones, etc.)
# - el AST
# - el código (como un string)
# - la regla (un objeto cuyos campos son los atributos de la regla)
# y devuelve una lista de hallazgos (vacía si no hay ninguno) donde cada hallazgo es un objeto con los campos 'msg' (el mensaje a mostrar), 'línea' (la línea donde se encontró el hallazgo) y 'columna' (la columna donde se encontró el hallazgo)

from msg import *

def reglaComandosAnidados(analizador, AST, código, regla):
  # Verifica que la profundidad de anidación de comandos no supere el umbral 'max'.
  máximaAnidacion = regla["max"] if "max" in regla else 1
  return buscarNodosCon_YGenerar_(analizador, AST,
    lambda nodo : analizador.es_UnComandoCompuesto(nodo) and analizador.nivelAnidaciónComandos_(nodo) >= máximaAnidacion,
    lambda nodo : mensajeComandosCompuestosAnidados
  )

def reglaUnComandoPorLinea(analizador, AST, código, regla):
  # Verifica que no haya dos o más comandos en la misma línea.
  líneasConflictivas = {}
  nodoAnterior = None
  líneaAnterior = 0
  for nodo in analizador.nodosDeTipo_(AST, analizador.tiposComandos()):
    nuevaLínea = analizador.líneaDeNodo_(nodo)
    if líneaAnterior > 0 and not (nodoAnterior is None):
      if (líneaAnterior == nuevaLínea and not (líneaAnterior in líneasConflictivas)):
        líneasConflictivas[líneaAnterior] = {
          "msg":mensajeMásDeUnComandoPorLínea,
          "línea":líneaAnterior,
          "columna":analizador.columnaDeNodo_(nodo)
        }
    nodoAnterior = nodo
    líneaAnterior = nuevaLínea
  resultado = []
  for l in líneasConflictivas:
    resultado.append(líneasConflictivas[l])
  return resultado


def reglaIndentacionPorAnidación(analizador, AST, código, regla):
  # Verifica que la indentación de cada línea anidada sea mayor a la línea del nodo que la contiene.
  return reglaIndentacionPorAnidaciónDesde(analizador, AST, código, regla, 0, -1)

def reglaIndentacionPorAnidaciónDesde(analizador, nodo, código, regla, n, i):
  resultado = []
  líneaActual = analizador.líneaDeNodo_(nodo)
  indentaciónActual = i
  if líneaActual != n:
    columnaActual = analizador.columnaDeNodo_(nodo)
    indentaciónActual = indentaciónHasta(código, líneaActual, columnaActual)
    if indentaciónActual <= i:
      resultado.append({
          "msg":mensajeIndentaciónSubordinada,
          "línea":líneaActual,
          "columna":columnaActual
        })
  for nodoHijo in analizador.hijosDeNodo_(nodo):
    resultado += reglaIndentacionPorAnidaciónDesde(analizador, nodoHijo, código, regla, líneaActual,
      indentaciónActual if analizador.es_NodoSubordinadoDe_(nodoHijo, nodo) else i
    )
  return resultado


def indentaciónHasta(código, nLínea, nColumna):
  línea = código.split("\n")[nLínea-1]
  i = 0
  while i < (nColumna-1) and esIndentación(línea[i]):
    i += 1
  return i

def esIndentación(caracter):
  return caracter == " " or caracter == "\t"

def reglaNombresProhibidos(analizador, AST, código, regla):
  # Verifica que no se usen identificadores con nombre en 'nombres'.
  return nodosDeNombresProhibidosEnAST(analizador, AST, regla["nombres"] if "nombres" in regla else [])

REGLAS = {
  "NEST_CMD":reglaComandosAnidados,
  "CMD_X_LINE":reglaUnComandoPorLinea,
  "INDENT_NEST":reglaIndentacionPorAnidación,
  "NAME_VOID":reglaNombresProhibidos
}

conceptos = [ # Cada uno verifica que no se use el concepto en cuestión.
  [ "REP_SIMPLE",
    (lambda analizador, AST, código, regla, nodo : (analizador.es_RepeticiónSimple(nodo))),
    mensajeRepeticiónSimpleNoPermitida
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

def nodosDeNombresProhibidosEnAST(analizador, AST, nombres):
  todosLosNombres = nombres if (type(nombres) == type([])) else [nombres]
  return buscarNodoDeTipo_Con_(analizador, AST, analizador.tiposNombre(),
    lambda nodo : analizador.nombreNodo_(nodo) in todosLosNombres,
    lambda nodo : analizador.nombreNodo_(nodo)
  )

def buscarNodoDeTipo_Con_(analizador, AST, tipo, fVal, fMsg):
  return buscarNodosCon_YGenerar_(analizador, AST,
    lambda nodo : analizador.es_NodoDeTipo_(nodo, tipo) and fVal(nodo),
    lambda nodo : primitivaNoPermitida(fMsg(nodo))
  )

def buscarNodoImportEnAST(analizador, AST):
  return buscarNodosCon_YGenerar_(analizador, AST,
    lambda nodo : analizador.es_NodoImport(nodo),
    lambda nodo : mensajeImportarNoPermitido
  )

def buscarNodoRaiseEnAST(analizador, AST):
  return buscarNodosCon_YGenerar_(analizador, AST,
    lambda nodo : analizador.es_NodoExcepción(nodo),
    lambda nodo : mensajeExcepcionesNoPermitidas
  )

for concepto in conceptos:
  REGLAS["CONCEPT_" + concepto[0]] = lambda analizador, AST, código, regla : buscarNodosCon_YGenerar_(analizador, AST,
    lambda nodo : concepto[1](analizador, AST, código, regla, nodo), lambda nodo : concepto[2]
  )