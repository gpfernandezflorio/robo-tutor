# -*- coding: utf-8 -*-

import io, os, json
import datetime
import requests
from users import loginValido, cargarUsuariosEnCurso, usuarioEnCurso, cursosUsuario, rolesEnCurso
from corrector import run_code, timeoutDefault, mostrar_excepcion
from cursos.cursos import cargarCuestionarioMoodle, organizarPreguntasYRespuestas
from fechas import fueraDeFecha

# CURSOS:
from cursos.unq_inpr import CURSOS as cursos_unq_inpr
from cursos.exactas_programa import CURSOS as cursos_exactas_programa
from cursos.taller_programacion import CURSOS as cursos_taller_programacion

CURSOS = {}

for c in cursos_unq_inpr:
  CURSOS[c] = cursos_unq_inpr[c]

for c in cursos_exactas_programa:
  CURSOS[c] = cursos_exactas_programa[c]

for c in cursos_taller_programacion:
  CURSOS[c] = cursos_taller_programacion[c]

LOCAL_DIR = 'locales'
if not os.path.isdir(LOCAL_DIR):
  os.mkdir(LOCAL_DIR)

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
      resultado[curso] = {
        "info":CURSOS_publico[curso]["info"],
        "permisos": roles_y_permisos(curso, usuario)
      }
  if 'dataEjs' in jsonObj:
    agregarDataEjs(usuario, resultado)
  return resultado

def roles_y_permisos(curso, usuario):
  resultado = {}
  for rol in rolesEnCurso(usuario, curso):
    resultado[rol] = permisosRol(curso, rol)
  return resultado

'''permisos:
  TODO: puede hacer todo excepto desmatricularse (equivalente a una lista con todos los demás, excepto SALIR)
  VER: puede ver todo el contenido, más allá de las restricciones
  VER_BAJOREGLAS: puede ver el contenido pero sólo si cumple las restricciones
  EDITAR_CONTENIDO: puede editar el contenido del curso (las actividades, las secciones, etc)
  EDITAR_ROLES: puede editar los roles existentes
  MATRICULAR_<ROL>: puede matricular y desmatricular usuarios con el rol ROL (uno por cada rol)
  HACER: puede realizar las actividades
  SALIR: puede desmatricularse
'''

rolesPorDefecto = {
  "Administrador":"TODO",
  "Docente":["VER","EDITAR_CONTENIDO","HACER","MATRICULAR_Estudiante"],
  "Estudiante":["VER_BAJOREGLAS","HACER"]
}

def rolesCurso(curso):
  resultado = []
  if curso in CURSOS:
    curso = CURSOS[curso]
    resultado = curso['roles'] if 'roles' in curso else rolesPorDefecto
  return resultado

def permisosRol(curso, rol):
  resultado = []
  roles = rolesCurso(curso)
  if rol in roles:
    resultado = roles[rol]
  return resultado

def tienePermisoUsuario(usuario, curso, que):
  for rol in rolesEnCurso(usuario, curso):
    if tienePermisoRol(rol, curso, que):
      return True
  return False

def tienePermisoRol(rol, curso, que):
  permisos = permisosRol(curso, rol)
  return (permisos == "TODO" and que != "SALIR") or (permisos != "TODO" and que in permisos)

CURSOS_publico = {}

informacionPrivadaEjercicio = ["pre","run_data","aridad","timeout"]
informacionPublicaEjercicio = ["id","nombre","visible","disponible",
  "enunciado","base","pidePrograma"] # pidePrograma es público porque lo usa el cliente para armar el mensaje de error
def esconderInformacionSensibleEjercicio(ejercicio):
  ejercicioPublico = {"tipo":"CODIGO"}
  for k in ejercicio:
    if k in informacionPublicaEjercicio:
      ejercicioPublico[k] = ejercicio[k]
  # Agrego un timeout para que el cliente sepa cuánto esperar al servidor
  ejercicioPublico["timeoutTotal"] = 2 + (ejercicio["timeout"] if "timeout" in ejercicio else timeoutDefault()) * (len(ejercicio["run_data"]) if "run_data" in ejercicio else 1)
  return ejercicioPublico

informacionPrivadaCuestionario = ["preguntas","file_moodle","data_moodle"]
informacionPublicaCuestionario = ["id","nombre","visible","disponible",
  "solo_preguntas","solo_respuestas","puedenReintentar","puedenSaltearPreguntas","puedenRetroceder"]
def esconderInformacionSensibleCuestionario(cuestionario):
  cuestionarioPublico = {"tipo":"CUESTIONARIO"}
  for k in cuestionario:
    if k in informacionPublicaCuestionario:
      cuestionarioPublico[k] = cuestionario[k]
  return cuestionarioPublico

informacionPublicaCurso = ['nombre','descripcion','anio','edicion','responsable','institucion','lenguaje','lenguaje_display']
informacionPrivadaCurso = ['actividades','planilla','roles'] # actividades es privada porque la trato aparte (hay que ocultar la información sensible)
def esconderInformacionSensibleCurso(curso):
  cursoPublico = {
    "info":{}
  }
  for k in curso:
    if k in informacionPublicaCurso:
      cursoPublico["info"][k] = curso[k]
  cursoPublico["todas_las_actividades"] = []
  if "actividades" in curso:
    for actividad in curso["actividades"]:
      if actividad["tipo"] == "CODIGO":
        cursoPublico["todas_las_actividades"].append(esconderInformacionSensibleEjercicio(actividad))
      elif actividad["tipo"] == "CUESTIONARIO":
        if "file_moodle" in actividad:
          cargarCuestionarioMoodle(actividad)
        organizarPreguntasYRespuestas(actividad)
        cursoPublico["todas_las_actividades"].append(esconderInformacionSensibleCuestionario(actividad))
      else: # LINK o SECCION
        cursoPublico["todas_las_actividades"].append(actividad)
  return cursoPublico

def cargarUsuarios(c):
  archivo = f"matricula/{c}.json"
  if os.path.isfile(archivo):
    f = open(archivo, 'r')
    matricula = json.loads(f.read())
    f.close()
    cargarUsuariosEnCurso(matricula, c, rolesCurso(c))

for c in CURSOS:
  CURSOS_publico[c] = esconderInformacionSensibleCurso(CURSOS[c])
  cargarUsuarios(c)

def tryLogin(jsonObj, verb):
  curso = None
  respuesta = {'resultado':"Falla"}
  if 'curso' in jsonObj:
    curso = jsonObj['curso']
  if 'usuario' in jsonObj and 'contrasenia' in jsonObj:
    usuario = jsonObj['usuario']
    contrasenia = jsonObj['contrasenia']
    if loginValido(usuario, contrasenia, curso):
      if "actividad" in jsonObj and not actividadHabilitada(usuario, curso, jsonObj["actividad"]):
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
          if 'dataEjs' in jsonObj or "actividad" in jsonObj:
            agregarDataEjs(usuario, respuesta['cursos'], jsonObj)
  return respuesta

def agregarDataEjs(usuario, cursos, jsonObj={}):
  if "actividad" in jsonObj:
    # Ya verifiqué que la actividad está habilitada
    for curso in cursos:
      if "todas_las_actividades" in CURSOS_publico[curso]:
        ej = elementoDeId(CURSOS_publico[curso]["todas_las_actividades"], jsonObj["actividad"])
        if not (ej is None):
          if not ("actividades" in cursos[curso]):
            cursos[curso]["actividades"] = []
          cursos[curso]["actividades"].append(ej)
  else:
    for curso in cursos:
      if "todas_las_actividades" in CURSOS_publico[curso]:
        if not ("actividades" in cursos[curso]):
          cursos[curso]["actividades"] = []
        cursos[curso]["actividades"] += versionesParaMostrar(usuario, curso)

def elementoDeId(lista, id):
  for elemento in lista:
    if elemento["id"] == id:
      return elemento
  return None

def actividadHabilitada(usuario, curso, actividad):
  return habilitacionId(usuario, curso, actividad) == "HABILITADA"

# Puede devolver HABILITADA, DESHABILITADA, OCULTA o INEXISTENTE
def habilitacionId(usuario, curso, actividad):
  if curso is None or not (curso in CURSOS_publico):
    return "INEXISTENTE"
  actividad = elementoDeId(CURSOS_publico[curso]["todas_las_actividades"], actividad)
  if actividad is None:
    return "INEXISTENTE"
  return habilitacion(usuario, curso, actividad)

def habilitacion(usuario, curso, actividad):
  if tienePermisoUsuario(usuario, curso, "VER"):
    if tienePermisoUsuario(usuario, curso, "HACER"):
      return "HABILITADA"
    return "DESHABILITADA"
  if "visible" in actividad:
    if actividad["visible"] == "NO":
      return "OCULTA"
    if fueraDeFecha(actividad["visible"]):
      return "OCULTA"
  if "disponible" in actividad:
    if actividad["disponible"] == "NO":
      return "DESHABILITADA"
    if fueraDeFecha(actividad["disponible"]):
      return "DESHABILITADA"
  if actividad["tipo"] == "CODIGO":
    return ejercicioHabilitado(usuario, actividad)
  elif actividad["tipo"] == "CUESTIONARIO":
    return cuestionarioHabilitado(usuario, actividad)
  elif actividad["tipo"] == "LINK":
    return linkHabilitado(usuario, actividad)
  elif actividad["tipo"] == "SECCION":
    return seccionHabilitada(usuario, actividad)
  return "INEXISTENTE"

def ejercicioHabilitado(usuario, ejercicio):
  # Acá se puede verificar si el usuario ya lo resolvió y no lo puede resolver otra vez
  return "HABILITADA"

def cuestionarioHabilitado(usuario, cuestionario):
  # Acá se puede verificar si el usuario ya lo respondió y no lo puede responder otra vez
  return "HABILITADA"

def linkHabilitado(usuario, cuestionario):
  # Acá se puede verificar ... ?
  return "HABILITADA"

def seccionHabilitada(usuario, cuestionario):
  # Acá se puede verificar si hay contenido habilitado en la sección
  return "HABILITADA"

def dame_data_cuestionario(ruta):
  respuesta = {'resultado':"Falla"}
  data = ruta.split("/")
  if len(data) == 2:
    curso = data[0]
    if curso in CURSOS_publico:
      curso = CURSOS_publico[curso]
      if "todas_las_actividades" in curso:
        cuestionario = elementoDeId(curso["todas_las_actividades"], data[1])
        if not (cuestionario is None):
          respuesta["resultado"] = "OK"
          respuesta["cuestionario"] = {
            "nombre": cuestionario["nombre"],
            "preguntas": cuestionario["solo_preguntas"]
          }
  return respuesta

def respuestaCuestionario(jsonObj, verb):
  resultado = {'resultado':"Falla"}
  if all(map(lambda x : x in jsonObj, ['usuario', 'contrasenia', 'curso', 'actividad', 'nPregunta', 'respuesta'])):
    usuario = jsonObj['usuario']
    contrasenia = jsonObj['contrasenia']
    curso = jsonObj['curso']
    if loginValido(usuario, contrasenia, curso):
      cuestionario = jsonObj['actividad']
      if actividadHabilitada(usuario, curso, cuestionario):
        cuestionario = elementoDeId(CURSOS[curso]["actividades"], cuestionario)
        nPregunta = jsonObj['nPregunta']
        if "preguntas" in cuestionario and nPregunta < len(cuestionario["preguntas"]):
          pregunta = cuestionario["preguntas"][nPregunta]
          respuesta = jsonObj['respuesta']
          devolucion = validarRespuesta(pregunta, respuesta)
          resultado["resultado"] = "OK"
          resultado["devolucion"] = devolucion
          jsonObj['actividad'] = jsonObj['actividad'] + "." + str(jsonObj['nPregunta']+1)
          jsonObj['respuesta'] = str(respuesta+1) if type(respuesta) == int else respuesta
          jsonObj['resultado'] = ("OK" if devolucion['correcto'] else "NO") if 'correcto' in devolucion else "-"
          jsonObj['duracion'] = "-"
          commit(jsonObj, verb)
  return resultado

def intentoCodigo(jsonObj, verb):
  resultado = {'resultado':"Falla"}
  if all(map(lambda x : x in jsonObj, ['usuario', 'contrasenia', 'curso', 'actividad'])):
    usuario = jsonObj['usuario']
    contrasenia = jsonObj['contrasenia']
    curso = jsonObj['curso']
    if loginValido(usuario, contrasenia, curso):
      ejercicio = jsonObj['actividad']
      if actividadHabilitada(usuario, curso, ejercicio):
        jsonObj["ejercicio"] = elementoDeId(CURSOS[curso]["actividades"], ejercicio)
        jsonObj["analisisCodigo"] = reglasDeAnalisisDeCodigo(jsonObj, CURSOS[curso])
        resultado = run_code(jsonObj, verb)
  # else: # Ejercicio libre o usuario anónimo:
  #   resultado = run_code(jsonObj)
  if resultado["resultado"] != "Falla" and "usuario" in jsonObj:
    if ("duracion" in resultado):
      jsonObj["duracion"] = "{:.2f}".format(resultado["duracion"])
      del resultado["duracion"]
    else:
      jsonObj["duracion"] = "-"
    jsonObj["respuesta"] = jsonObj["src"]
    jsonObj["resultado"] = mostrar_resultado(resultado)
    commit(jsonObj, verb)
  return resultado

def validarRespuesta(pregunta, respuesta):
  resultado = {}
  if pregunta["tipo"] == "OPCION_MULTIPLE":
    # respuesta es un número
    respuesta = pregunta["respuestas"][respuesta]
    if "puntaje" in respuesta:
      resultado["correcto"] = respuesta["puntaje"] == "1"
    if "devolucion" in respuesta:
      resultado["texto"] = respuesta["devolucion"]
  return resultado

def open_ej(jsonObj, v):
  # usuario, curso y actividad ya vienen
  jsonObj["respuesta"] = "OPEN"
  jsonObj["resultado"] = "-"
  jsonObj["duracion"] = "-"
  commit(jsonObj, v)
  return {'resultado':"OK"}

def mostrar_resultado(resultado):
  r = resultado["resultado"]
  if "error" in resultado:
    r += " - " + resultado["error"].split("\n")[0]
  return r

entries = ["usuario","actividad","respuesta","resultado","duracion"]

def commit(jsonObj, v):
  if "ejercicio" in jsonObj:
    if type(jsonObj["ejercicio"]) == type({}):
      jsonObj["ejercicio"] = jsonObj["ejercicio"]["id"]
  else:
    jsonObj["ejercicio"] = "-"
  data_form = {}
  data_csv = [str(datetime.datetime.now())]
  for x in entries:
    data_form[x] = jsonObj[x]
    data_csv.append(limpiar_csv(jsonObj[x].replace('"','""')))
  cursos = []
  if "curso" in jsonObj:
    cursos = [jsonObj["curso"]]
  else:
    cursos = cursosUsuario(jsonObj["usuario"])
  for curso in cursos:
    guardarLocal(",".join(data_csv), curso)
    guardarDrive(data_form, curso, v)

def guardarDrive(data, curso, v):
  planillaCurso = planillaDeCurso(curso)
  if not (planillaCurso is None):
    dataParaCurso = {}
    for x in planillaCurso["campos"]:
      dataParaCurso["entry." + planillaCurso["campos"][x]] = data[x]
    submit("https://docs.google.com/forms/d/e/" + planillaCurso["url"] + "/formResponse",
      dataParaCurso, data["usuario"], v
    )

def submit(url, data, dni, v):
  try:
    requests.post(url, data = data)
  except Exception as e:
    if (v):
      mostrar_excepcion(e)
    print("ERROR " + dni)

def guardarLocal(s, curso):
  archivo = os.path.join(LOCAL_DIR, curso + ".csv")
  f = None
  if os.path.isfile(archivo):
    f = io.open(archivo, mode='a')
  else:
    f = io.open(archivo, mode='w')
    f.write("ts,usuario,actividad,respuesta,resultado,d")
  f.write("\n" + s)
  f.close()

def limpiar_csv(s):
  return '"' + s + '"' if ("," in s) or ("\n" in s) else s

def planillaDeCurso(curso):
  if curso in CURSOS:
    curso = CURSOS[curso]
    if 'planilla' in curso:
      return curso['planilla']
  return None

def versionesParaMostrar(usuario, curso):
  lista = []
  for actividad in CURSOS_publico[curso]["todas_las_actividades"]:
    estado = habilitacion(usuario, curso, actividad)
    if estado == "HABILITADA":
      lista.append(actividad)
    elif estado == "DESHABILITADA":
      actividadDeshabilitada = {}
      for k in ['tipo','id','nombre','disponible']:
        actividadDeshabilitada[k] = actividad[k]
      actividadDeshabilitada["activa"] = "NO"
      lista.append(actividadDeshabilitada)
  return lista

def reglasDeAnalisisDeCodigo(jsonObj, curso):
  ejercicio = jsonObj["ejercicio"]
  reglas = []
  if "analisisCodigo" in ejercicio:
    reglas += ejercicio["analisisCodigo"]
  if "analisisCodigo" in curso:
    reglas += curso["analisisCodigo"]
  return reglas