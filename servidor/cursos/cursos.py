import os
import xml.etree.ElementTree as ET
RUTA_RAIZ = "cursos"

def cargarCuestionarioMoodle(cuestionario):
  ruta = cuestionario["file_moodle"]
  tree = ET.parse(os.path.join(RUTA_RAIZ, ruta))
  root = tree.getroot()
  cuestionario["data_moodle"] = {}
  cargarInformacionDeElementoMoodle(cuestionario["data_moodle"], root)
  ordenarLecciones(cuestionario["data_moodle"])
  for campo in cuestionario["data_moodle"]:
    if not (campo in cuestionario):
      cuestionario[campo] = cuestionario["data_moodle"][campo]

def cargarInformacionDeElementoMoodle(cuestionario, elemento):
  if (elemento.tag == "activity"):
    for hijo in elemento:
      cargarInformacionDeElementoMoodle(cuestionario, hijo)
  elif (elemento.tag == "lesson"):
    for hijo in elemento:
      cargarInformacionDeElementoMoodle(cuestionario, hijo)
  elif (elemento.tag == "name"):
    if "nombre" in cuestionario:
      empezarOtraLeccion(cuestionario)
    cuestionario["nombre"] = limpiarXML(elemento.text)
  elif (elemento.tag == "pages"):
    if "preguntas" in cuestionario:
      empezarOtraLeccion(cuestionario)
    preguntas = []
    for hijo in elemento:
      if (hijo.tag == "page"):
        preguntas.append(cargarInformacionPreguntaMoodle(hijo))
    cuestionario["preguntas"] = preguntas

def cargarInformacionPreguntaMoodle(pagina):
  nuevaPregunta = {}
  for elemento in pagina:
    if (elemento.tag == "qtype"):
      nuevaPregunta["tipoMoodle"] = elemento.text
      nuevaPregunta["tipo"] = obtenerTipoPreguntaMoodle(elemento.text)
    elif (elemento.tag == "title"):
      nuevaPregunta["titulo"] = limpiarXML(elemento.text)
    elif (elemento.tag == "contents"):
      nuevaPregunta["pregunta"] = limpiarXML(elemento.text)
    elif (elemento.tag == "answers"):
      respuestas = []
      for hijo in elemento:
        if (hijo.tag == "answer"):
          respuestas.append(cargarInformacionRespuestaMoodle(hijo))
      nuevaPregunta["respuestas"] = respuestas
  return nuevaPregunta

def obtenerTipoPreguntaMoodle(tipoMoodle):
  if tipoMoodle == "20":
    return "SOLO_TEXTO"
  if tipoMoodle == "2" or tipoMoodle == "3":
    return "OPCION_MULTIPLE"
  return "?"

def cargarInformacionRespuestaMoodle(respuesta):
  nuevaRespuesta = {}
  for elemento in respuesta:
    if (elemento.tag == "answer_text"):
      nuevaRespuesta["texto"] = limpiarXML(elemento.text)
    elif (elemento.tag == "response"):
      nuevaRespuesta["devolucion"] = limpiarXML(elemento.text)
    elif (elemento.tag == "score"):
      nuevaRespuesta["puntaje"] = elemento.text
  return nuevaRespuesta

camposLeccion = ["nombre","preguntas"]

def empezarOtraLeccion(cuestionario):
  nuevaLeccion = {}
  for campo in camposLeccion:
    if campo in cuestionario:
      nuevaLeccion[campo] = cuestionario[campo]
      del cuestionario[campo]
  if "lecciones" in cuestionario:
    cuestionario["lecciones"].append(nuevaLeccion)
  else:
    cuestionario["lecciones"] = [nuevaLeccion]

def ordenarLecciones(cuestionario):
  if "lecciones" in cuestionario:
    empezarOtraLeccion(cuestionario)

def limpiarXML(textoOriginal):
  return textoOriginal.replace('&lt;','<').replace('&gt;','>')

informacionPrivadaPregunta = ["respuestas"]
informacionPublicaPregunta = ["titulo","tipo","tipoMoodle","pregunta"]

informacionPrivadaRespuesta = ["devolucion","puntaje"]
informacionPublicaRespuesta = ["texto"]

def organizarPreguntasYRespuestas(cuestionario):
  if "preguntas" in cuestionario:
    cuestionario["solo_preguntas"] = []
    cuestionario["solo_respuestas"] = []
    for pregunta in cuestionario["preguntas"]:
      nuevaPregunta = {}
      nuevoMapaDeRespuestas = []
      for x in informacionPublicaPregunta:
        if x in pregunta:
          nuevaPregunta[x] = pregunta[x]
      if "respuestas" in pregunta:
        for respuesta in pregunta["respuestas"]:
          nuevaRespuesta = {}
          for x in informacionPublicaRespuesta:
            if x in respuesta:
              nuevaRespuesta[x] = respuesta[x]
          nuevoMapaDeRespuestas.append(nuevaRespuesta)
      cuestionario["solo_preguntas"].append(nuevaPregunta)
      cuestionario["solo_respuestas"].append(nuevoMapaDeRespuestas)