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
  # print(nodoDeclaración.keys())
  documentación = documentaciónEn(analizador, nodoDeclaración, AST, líneasDeCódigo, pos)
  # print(">>")
  # print(documentación.replace(" ", ".").replace("\n", "\\n"))
  # print("<<")
  # analizador.MostrarAST(nodoDeclaración)
  return []

def documentaciónEn(analizador, nodoDeclaración, AST, líneasDeCódigo, pos):
  doc = ""
  if pos == 'DENTRO':
    hijos = analizador.hijosDeNodo_(nodoDeclaración)
    if len(hijos) > 0:
      primerHijo = hijos[0]
      if analizador.es_UnComandoParcial(primerHijo):
        nietos = analizador.hijosDeNodo_(primerHijo)
        if len(nietos) > 0:
          primerHijo = nietos[0]
      fL = analizador.líneaDeNodo_(primerHijo)
      fC = analizador.columnaDeNodo_(primerHijo)
      (iL, iC) = analizador.inicioCuerpoDeclaración(nodoDeclaración, líneasDeCódigo)
      # print(iL)
      # print(iC)
      # print(fL)
      # print(fC)
      if iL == fL:
        if fC >= iC:
          doc += líneasDeCódigo[iL][(iC-1):(fC-1)]
      elif fL > iL:
        doc += líneasDeCódigo[iL][(iC-1):]
        for l in range(iL+1, fL):
          doc += "\n" + líneasDeCódigo[l]
        if fC > 1:
          doc += "\n" + líneasDeCódigo[fL][:(fC-1)]
  else: # pos == 'ANTES'
    pass # TODO
  return doc
