mensajeComandosCompuestosAnidados = "No está bueno anidar comandos compuestos"
mensajeMásDeUnComandoPorLínea = "No está bueno escribir más de un comando por línea"
mensajeIndentaciónSubordinada = "Ojo con la indentación: una línea subordinada debería tener mayor indentación que su línea superior"

def mensajeConceptoNoPermitido(concepto):
  return "No está permitido usar " + concepto
def primitivaNoPermitida(nombre):
  return "No está permitido usar '" + nombre + "'"

mensajeRepeticiónSimpleNoPermitida = mensajeConceptoNoPermitido("repetición simple")
mensajeImportarNoPermitido = "No está permitido importar módulos"
mensajeExcepcionesNoPermitidas = "No está permitido generar excepciones"
mensajeTimeout = "La ejecución demoró más de lo permitido"

def mensajeFaltaDefinición(nombre):
  return "No se encuentra la definición de " + nombre
def mensajeFallaParámetros(nombre, parámetrosEsperados, parámetrosReales):
  return "La función " + nombre + " debería tener " + str(parámetrosEsperados) + " parámetros pero tiene " + str(parámetrosReales)

def fMsg(msg, x):
  res = ""
  for m in msg:
    res += str(x) if m is None else m
  return res

mensajeMenosDeUno = "Menos de 1"
mensajeMásDeMenosUno = "Más de menos 1"
mensajeDebeSerNum = ["Debería ser un número (y ",None," no es un número)"]
mensajeNoDebeSerNeg = ["No debería ser negativo (",None," es negativo)"]
mensajeNoDebeSerPos = ["No debería ser positivo (",None," es positivo)"]