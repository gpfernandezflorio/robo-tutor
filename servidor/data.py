# -*- coding: utf-8 -*-

import os, json
from users import loginValido, cargarUsuariosEnCurso, usuarioEnCurso

# CURSOS:
from cursos.unq_inpr import CURSOS as cursos_unq_inpr
from cursos.exactas_programa import CURSOS as cursos_exactas_programa
from cursos.taller_programacion import CURSOS as cursos_taller_programacion

def dame_cursos(jsonObj):
  respuesta = {'resultado':"Falla"}
  if 'usuario' in jsonObj and 'contrasenia' in jsonObj:
    usuario = jsonObj['usuario']
    contrasenia = jsonObj['contrasenia']
    if loginValido(usuario, contrasenia):
      respuesta["resultado"] = "OK"
      respuesta["cursos"] = cursosDeUsuario(usuario, jsonObj)
  return respuesta

def cursosDeUsuario(usuario, jsonObj):
  resultado = {}
  for curso in CURSOS_publico:
    if usuarioEnCurso(usuario, curso):
      resultado[curso] = {"info":CURSOS_publico[curso]["info"]}
  if 'dataEjs' in jsonObj:
    agregarDataEjs(resultado)
  if 'dataCuestionarios' in jsonObj:
    agregarDataCuestionarios(resultado)
  return resultado

def dameEjercicio(curso, nombreEjercicio):
  if curso in CURSOS:
    for ejercicio in CURSOS[curso]["ejs"]:
      if ejercicio["nombre"] == nombreEjercicio:
        return ejercicio
  return {}

CURSOS = {}

for c in cursos_unq_inpr:
  CURSOS[c] = cursos_unq_inpr[c]

for c in cursos_exactas_programa:
  CURSOS[c] = cursos_exactas_programa[c]

for c in cursos_taller_programacion:
  CURSOS[c] = cursos_taller_programacion[c]

CURSOS_publico = {}

informacionPrivadaEjercicio = ["pre","run_data","aridad","timeout"]
informacionPublicaEjercicio = ["nombre","enunciado","base","pidePrograma"] # pidePrograma es público porque lo usa el cliente para armar el mensaje de error
def esconderInformacionSensibleEjercicio(ejercicio):
  ejercicioPublico = {}
  for k in ejercicio:
    if k in informacionPublicaEjercicio:
      ejercicioPublico[k] = ejercicio[k]
  # Agrego un timeout para que el cliente sepa cuánto esperar al servidor
  ejercicioPublico["timeoutTotal"] = 2 + (ejercicio["timeout"] if "timeout" in ejercicio else timeoutDefault()) * (len(ejercicio["run_data"]) if "run_data" in ejercicio else 1)
  return ejercicioPublico

informacionPrivadaCuestionario = ["preguntas","file_moodle","data_moodle"]
informacionPublicaCuestionario = ["nombre","solo_preguntas","solo_respuestas"]
def esconderInformacionSensibleCuestionario(cuestionario):
  cuestionarioPublico = {}
  for k in cuestionario:
    if k in informacionPublicaCuestionario:
      cuestionarioPublico[k] = cuestionario[k]
  return cuestionarioPublico

informacionPublicaCurso = ['nombre','descripcion','anio','edicion','responsable','institucion','lenguaje','lenguaje_display']
informacionPrivadaCurso = ['ejs','cuestionarios'] # ejs y cuestionarios son privados porque lo trato aparte
def esconderInformacionSensibleCurso(curso):
  cursoPublico = {
    "info":{}
  }
  for k in curso:
    if k in informacionPublicaCurso:
      cursoPublico["info"][k] = curso[k]
  cursoPublico["ejs"] = []
  cursoPublico["cuestionarios"] = []
  if "ejs" in curso:
    for ej in curso["ejs"]:
      if not ("mostrar" in ej) or ej["mostrar"]:
        cursoPublico["ejs"].append(esconderInformacionSensibleEjercicio(ej))
  if "cuestionarios" in curso:
    for cuestionario in curso["cuestionarios"]:
      if not ("mostrar" in cuestionario) or cuestionario["mostrar"]:
        cursoPublico["cuestionarios"].append(esconderInformacionSensibleCuestionario(cuestionario))
  return cursoPublico

def timeoutDefault():
  return 1

def cargarEstudiantes(c):
  archivo = f"estudiantes/{c}.json"
  if os.path.isfile(archivo):
    f = open(archivo, 'r')
    estudiantes = json.loads(f.read())
    f.close()
    cargarUsuariosEnCurso(estudiantes, c)

for c in CURSOS:
  CURSOS_publico[c] = esconderInformacionSensibleCurso(CURSOS[c])
  cargarEstudiantes(c)

def tryLogin(jsonObj, verb):
  curso = None
  respuesta = {'resultado':"Falla"}
  if 'curso' in jsonObj:
    curso = jsonObj['curso']
  if 'usuario' in jsonObj and 'contrasenia' in jsonObj:
    usuario = jsonObj['usuario']
    contrasenia = jsonObj['contrasenia']
    if loginValido(usuario, contrasenia, curso):
      if "ej" in jsonObj and not ejercicioHabilitado(usuario, curso, jsonObj["ej"]):
        respuesta["msg"] = "DISABLE"
      elif "cuestionario" in jsonObj and not cuestionarioHabilitado(usuario, curso, jsonObj["cuestionario"]):
        respuesta["msg"] = "DISABLE"
      else:
        respuesta['resultado'] = "OK"
        respuesta['usuario'] = usuario
        respuesta['contrasenia'] = contrasenia
        if curso is None:
          respuesta['cursos'] = cursosDeUsuario(usuario, jsonObj)
        else:
          respuesta['cursos'] = {curso:{"info":CURSOS_publico[curso]["info"]}}
          respuesta['curso'] = curso
          if 'dataEjs' in jsonObj or "ej" in jsonObj:
            agregarDataEjs(respuesta['cursos'], jsonObj)
          if 'dataCuestionarios' in jsonObj or "cuestionario" in jsonObj:
            agregarDataCuestionarios(respuesta['cursos'], jsonObj)
  return respuesta

def agregarDataEjs(cursos, jsonObj={}):
  if "ej" in jsonObj:
    for curso in cursos:
      if "ejs" in CURSOS_publico[curso]:
        cursos[curso]["ejs"] = []
        ej = elementoDeNombre(CURSOS_publico[curso]["ejs"], jsonObj["ej"])
        if not (ej is None):
          cursos[curso]["ejs"].append(ej)
  else:
    for curso in cursos:
      if "ejs" in CURSOS_publico[curso]:
        cursos[curso]["ejs"] = CURSOS_publico[curso]["ejs"]

def agregarDataCuestionarios(cursos, jsonObj={}):
  if "cuestionario" in jsonObj:
    for curso in cursos:
      if "cuestionarios" in CURSOS_publico[curso]:
        cursos[curso]["cuestionarios"] = []
        cuestionario = elementoDeNombre(CURSOS_publico[curso]["cuestionarios"], jsonObj["cuestionario"])
        if not (cuestionario is None):
          cursos[curso]["cuestionarios"].append(cuestionario)
  else:
    for curso in cursos:
      if "cuestionarios" in CURSOS_publico[curso]:
        cursos[curso]["cuestionarios"] = CURSOS_publico[curso]["cuestionarios"]

def elementoDeNombre(lista, nombre):
  for elemento in lista:
    if elemento["nombre"] == nombre:
      return elemento
  return None

def ejercicioHabilitado(usuario, curso, ejercicio):
  if curso is None or not (curso in CURSOS_publico):
    return False
  if not (ejercicio in CURSOS_publico[curso]):
    return False
  # Acá se puede verificar si la fecha del ejercicio ya pasó o si el usuario ya lo resolvió y no lo puede resolver otra vez
  return True

def cuestionarioHabilitado(usuario, curso, cuestionario):
  if curso is None or not (curso in CURSOS_publico):
    return False
  if not (ejercicio in CURSOS_publico[curso]):
    return False
  # Acá se puede verificar si la fecha del ejercicio ya pasó o si el usuario ya lo resolvió y no lo puede resolver otra vez
  return True
