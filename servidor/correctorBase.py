from procesos import ejecutarConTimeout

def timeoutDefault():
  return 1

class Corrector(object):
  def __init__(self):
    self.globalPre = ""

  def AdaptarResultado(self, resultadoEjecucion, code, code_run, aridad):
    pass

  def validaciónFinal(self, run, resultadoEjecucion):
    if resultadoEjecucion["errcode"] != 0:
      return {"resultado":"NO"}
    return None

  def corregir(self, jsonObj, v):
    run_data = jsonObj["ejercicio"]["run_data"] if "run_data" in jsonObj["ejercicio"] else {}
    if (type(run_data) != type([])):
      run_data = [run_data]
    code = {
      "pre":self.globalPre,
      "src":jsonObj["src"]
    }
    if (v):
      print(code["src"])
    # Análisis calidad
    resultadoAnalisisCodigo = self.Analizar(jsonObj)
    if not(resultadoAnalisisCodigo is None):
      return resultadoAnalisisCodigo
    ## Timeout
    timeout = jsonObj["ejercicio"]["timeout"] if ("timeout" in jsonObj["ejercicio"]) else timeoutDefault()
    lineasAdicionales = code["pre"].count("\n")
    ## Código
    if "pre" in jsonObj["ejercicio"]:
      code["pre"] = jsonObj["ejercicio"]["pre"] + "\n"
      lineasAdicionales = lineasAdicionales + jsonObj["ejercicio"]["pre"].count("\n") + 1
    ## Ejecuciones
    duraciones = []
    for run in run_data:
      self.InicializarRun(run)
      code_run = {
        "pre":code["pre"],
        "post":"\n"
        "lineasAdicionales":lineasAdicionales
      }
      ## Inicialización
      if "pre" in run:
        code_run["pre"] = code_run["pre"] + "\n\n" + run["pre"]
        code_run["lineasAdicionales"] = code_run["lineasAdicionales"] + run["pre"].count("\n") + 2
      self.AgregarCódigoVariablesDefinidas(run, jsonObj, code_run)
      ## Aridad de funciones correcta
      aridad = None
      if "aridad" in run:
        aridad = run["aridad"]
      elif "aridad" in jsonObj["ejercicio"]:
        aridad = jsonObj["ejercicio"]["aridad"]
      if not (aridad is None):
        self.AgregarCódigoAridadFunciones(aridad, code_run)
      ## Resultado
      if "post" in jsonObj["ejercicio"]:
        code_run["post"] += "\n\n" + jsonObj["ejercicio"]["post"]
      if "post" in run:
        code_run["post"] += "\n\n" + run["post"]
      if "assert" in run:
        self.AgregarCódigoResultado(code_run, run["assert"])
      ## Ejecución del código entregado
      code_run["pre"] += "\n\n"
      code_run["lineasAdicionales"] = code_run["lineasAdicionales"] + 2
      f = open(self.ruta, 'w')
      f.write(code_run["pre"] + code["src"] + code_run["post"])
      f.close()
      resultadoEjecucion = ejecutarConTimeout(self.comando, timeout)
      if resultadoEjecucion["resultado"] == "TIMEOUT":
        return {"resultado":"Except", "error":"La ejecución demoró más de lo permitido"}
      duraciones.append(resultadoEjecucion["duracion"])
      self.AdaptarResultado(resultadoEjecucion, code, code_run, aridad)
      ## Buscar errores
      if len(resultadoEjecucion["falla"]) > 0:
        if (v):
          print(resultadoEjecucion["falla"])
        fallaReal = self.buscarFalla(resultadoEjecucion["falla"], code, code_run)
        if not (fallaReal is None):
          return {"resultado":"Except", "error":fallaReal}
      ## Validación final
      validaciónFinal = self.validaciónFinal(run, resultadoEjecucion)
      if not (validaciónFinal is None):
        return validaciónFinal
    return {"resultado":"OK","duracion":sum(duraciones)/len(duraciones)}