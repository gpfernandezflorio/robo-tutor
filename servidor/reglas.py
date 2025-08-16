# Cada regla es una función que toma como argumentos:
# - el analizador sintáctico del lenguaje (AnalizadorPython, AnalizadorGobstones, etc.)
# - el AST
# - el código (como un string)
# - la regla (un objeto cuyos campos son los atributos de la regla)
# y devuelve None en caso de que el código cumpla la regla o un string en caso de que no (el string es el mensaje que se le muestra al usuario)

def reglaComandosAnidados(analizador, AST, codigo, regla):
  maximaAnidacion = regla["max"] if "max" in regla else 1
  return "No está bueno anidar comandos compuestos" if analizador.nivelesAnidacionComandos(AST) > maximaAnidacion else None

def reglaUnComandoPorLinea(analizador, AST, codigo, regla):
  return None

def reglaIndentacion(analizador, AST, codigo, regla):
  return None

REGLAS = {
  "NEST_CMD":reglaComandosAnidados,
  "CMD_X_LINE":reglaUnComandoPorLinea,
  "INDENT":reglaIndentacion
}