# -*- coding: utf-8 -*-

from cursos.cursos import cargarCuestionarioMoodle, organizarPreguntasYRespuestas

AsignacionesYListas2023_1 = {
  "id":"AsignacionesYListas",
  "file_moodle":"taller_programacion_2023_1c/AsignacionesYListas.xml"
}

ListasYFigus2023_1 = {
  "id":"ListasYFigus",
  "file_moodle":"taller_programacion_2023_1c/ListasYFigus.xml"
}

Funciones2023_1 = {
  "id":"Funciones",
  "file_moodle":"taller_programacion_2023_1c/Funciones.xml"
}

CiclosYCondiciones2023_1 = {
  "id":"CiclosYCondiciones",
  "file_moodle":"taller_programacion_2023_1c/CiclosYCondiciones.xml"
}

OperadoresLogicos2023_1 = {
  "id":"OperadoresLogicos",
  "file_moodle":"taller_programacion_2023_1c/OperadoresLogicos.xml"
}

MasFunciones2023_1 = {
  "id":"MasFunciones",
  "file_moodle":"taller_programacion_2023_1c/MasFunciones.xml"
}

Ciclos2023_1 = {
  "id":"Ciclos",
  "file_moodle":"taller_programacion_2023_1c/Ciclos.xml"
}

CorrigiendoCodigo2023_1 = {
  "id":"CorrigiendoCodigo",
  "file_moodle":"taller_programacion_2023_1c/CorrigiendoCodigo.xml"
}

MasFuncionesEP2023_1 = {
  "id":"MasFuncionesEP",
  "file_moodle":"taller_programacion_2023_1c/MasFuncionesEP.xml"
}

CURSOS = {
  "taller_programacion_2023_1c":{
    "nombre":"Taller de Programación - 2023 1C",
    "anio":"2023",
    "edicion":"Primer Cuatrimestre",
    "descripcion":"Curso correspondiente a la materia Taller de Programación de la Universidad de Buenos Aires",
    "responsable":{
      "nombre":"Mariela Sued",
      "contacto":"marielasued (AT) gmail.com"
    },
    "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    "cuestionarios":[AsignacionesYListas2023_1,ListasYFigus2023_1,Funciones2023_1,CiclosYCondiciones2023_1,OperadoresLogicos2023_1,MasFunciones2023_1,Ciclos2023_1,CorrigiendoCodigo2023_1,MasFuncionesEP2023_1]
  }
}

for c in CURSOS:
  if "cuestionarios" in CURSOS[c]:
    for q in CURSOS[c]["cuestionarios"]:
      if "file_moodle" in q:
        cargarCuestionarioMoodle(q)
      organizarPreguntasYRespuestas(q)
