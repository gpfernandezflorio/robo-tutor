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