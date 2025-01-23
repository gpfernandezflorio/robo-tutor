# -*- coding: utf-8 -*-

from cursos.unq_inpr import CURSOS as cursos_unq_inpr
from cursos.exactas_programa import CURSOS as cursos_exactas_programa

def dame_cursos():
  return CURSOS_publico

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

CURSOS_publico = {"cursos":{}}

informacionPrivada = ["pre","run_data"]
informacionPublica = ["nombre","enunciado","base","pidePrograma"] # pidePrograma es público porque lo usa el cliente para armar el mensaje de error
def esconderInformacionSensibleEjercicio(ejercicio):
  ejercicioPublico = {}
  for k in ejercicio:
    if k in informacionPublica:
      ejercicioPublico[k] = ejercicio[k]
  return ejercicioPublico

def esconderInformacionSensibleCurso(curso):
  cursoPublico = {}
  for k in curso:
    if k != "ejs":
      cursoPublico[k] = curso[k]
  cursoPublico["ejs"] = []
  for ej in curso["ejs"]:
    if not ("mostrar" in ej) or ej["mostrar"]:
      cursoPublico["ejs"].append(esconderInformacionSensibleEjercicio(ej))
  return cursoPublico

for c in CURSOS:
  CURSOS_publico["cursos"][c] = esconderInformacionSensibleCurso(CURSOS[c])