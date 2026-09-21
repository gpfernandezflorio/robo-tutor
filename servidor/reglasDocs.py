from msg import *

''' Regla general de documentación, valida varias cosas según los datos de 'regla':
  * 'pos' : ANTES | [DENTRO] - posición en la que se espera que se defina la documentación (antes de la declaración o dentro de ella).
'''
def reglaDocumentación(analizador, AST, código, regla):
  hallazgos = []
  declaraciones = analizador.nodosDeTipo_(AST, analizador.tiposDefiniciones())
  pos = regla['pos'] if ('pos' in regla) else 'DENTRO'
  líneasDeCódigo = [""] + código.split("\n")
  for declaración in declaraciones:
    hallazgos += hallazgosDocEn(analizador, declaración, AST, líneasDeCódigo, regla, pos)
  return hallazgos

def hallazgosDocEn(analizador, nodoDeclaración, AST, líneasDeCódigo, regla, pos):
  documentación = documentaciónEn(analizador, nodoDeclaración, AST, líneasDeCódigo, pos)
  # print(">>")
  # print(documentación.replace(" ", ".").replace("\n", "\\n"))
  # print("<<")
  # analizador.MostrarAST(nodoDeclaración)
  if soloEspaciosYSaltosDeLínea(documentación):
    return [{
      "msg":mensajeContratosFaltantes,
      "línea":analizador.líneaDeNodo_(nodoDeclaración),
      "columna":analizador.columnaDeNodo_(nodoDeclaración)
    }]
  return []

def documentaciónEn(analizador, nodoDeclaración, AST, líneasDeCódigo, pos):
  doc = ""
  if pos == 'DENTRO':
    nodoEnCuerpo = analizador.nodoEnCuerpoDeDeclaración(nodoDeclaración)
    if not (nodoEnCuerpo is None):
      fL = analizador.líneaDeNodo_(nodoEnCuerpo)
      fC = analizador.columnaDeNodo_(nodoEnCuerpo)
      (iL, iC) = analizador.inicioCuerpoDeclaración(nodoDeclaración, líneasDeCódigo)
      # print(iL)
      # print(iC)
      # print(fL)
      # print(fC)
      doc += códigoEntre(líneasDeCódigo, iL, iC, fL, fC)
  else: # pos == 'ANTES'
    fL = analizador.líneaDeNodo_(nodoDeclaración)
    fC = analizador.columnaDeNodo_(nodoDeclaración)
    hermanaMayor = analizador.nodoHermanaMayorDe_(nodoDeclaración)
    (iL, iC) = (1,1) if (hermanaMayor is None) else (analizador.líneaFinDeNodo_(hermanaMayor),analizador.columnaFinDeNodo_(hermanaMayor))
    # print(iL)
    # print(iC)
    # print(fL)
    # print(fC)
    doc += códigoEntre(líneasDeCódigo, iL, iC, fL, fC)
  return doc

def códigoEntre(líneasDeCódigo, iL, iC, fL, fC):
  doc = ""
  if iL == fL:
    if fC >= iC:
      doc += líneasDeCódigo[iL][(iC-1):(fC-1)]
  elif fL > iL:
    doc += líneasDeCódigo[iL][(iC-1):]
    for l in range(iL+1, fL):
      doc += "\n" + líneasDeCódigo[l]
    if fC > 1:
      doc += "\n" + líneasDeCódigo[fL][:(fC-1)]
  return doc

def soloEspaciosYSaltosDeLínea(texto):
  for c in texto:
    if not (c in [" ","\n"]):
      return False
  return True