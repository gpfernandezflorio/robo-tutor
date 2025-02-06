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
      respuesta["cursos"] = {}
      respuesta["resultado"] = "OK"
      respuesta["cursos"] = cursosDeUsuario(usuario)
  return respuesta

def cursosDeUsuario(usuario):
  resultado = {}
  for curso in CURSOS_publico:
    if usuarioEnCurso(usuario, curso):
      resultado[curso] = CURSOS_publico[curso]
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
  cursoPublico = {}
  for k in curso:
    if k in informacionPublicaCurso:
      cursoPublico[k] = curso[k]
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
      respuesta['resultado'] = "OK"
      respuesta['usuario'] = usuario
      respuesta['contrasenia'] = contrasenia
      if not (curso is None):
        respuesta['cursos'] = {}
        respuesta['cursos'][curso] = CURSOS_publico[curso]
        respuesta['curso'] = curso
      else:
        respuesta['cursos'] = cursosDeUsuario(usuario)
  return respuesta
