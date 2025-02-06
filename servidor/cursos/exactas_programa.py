# -*- coding: utf-8 -*-

from cursos.cursos import cargarCuestionarioMoodle, organizarPreguntasYRespuestas

figus_1_cantidadNecesaria = {
  "nombre":"Figus 1",
  "enunciado":"Sabiendo que está definida la función <code>dado(cantidadDeCaras)</code>, que al invocarla devuelve un número entre <code>0</code> y <code>cantidadDeCaras-1</code>, inclusive, implementar la función <code>cantidadDeFigusNecesaria(tamanioAlbum)</code> que genere un álbum de tamaño <code>tamanioAlbum</code>, simule su llenado y devuelva la cantidad de figuritas que se debieron adquirir para completarlo.",
  "aridad":{"cantidadDeFigusNecesaria":1},
  "pre":"k=-1\ndef dado(cantidadDeCaras):\n  global k\n  k = (k+1) % len(tiradas)\n  return tiradas[k]",
  "run_data":[{
    "pre":"tiradas = [0,1,2,3,4,5]",
    "post":"cantidadDeFigusNecesaria(6) == 6"
  }, {
    "pre":"tiradas = [0,1,2,0,1,2,3,4,3,5]",
    "post":"cantidadDeFigusNecesaria(6) == 10"
  }, {
    "pre":"tiradas = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7]",
    "post":"cantidadDeFigusNecesaria(8) == 19"
  }]
}

figus_2_promedio = {
  "nombre":"Figus 2",
  "enunciado":"Teniendo ya definda la función <code>cantidadDeFigusNecesaria</code> del ejercicio anterior, implementar la función <code>cantidadDeFigusPromedio(tamanioAlbum,cantidadDeRepeticiones)</code> que tome por parámetros el tamaño del álbum (<code>tamanioAlbum</code>) y la cantidad de repeticiones que queremos hacer (<code>cantidadDeRepeticiones</code>). Debe devolver por medio de la instrucción <code>return</code> el promedio de los valores obtenidos a lo largo de las <code>cantidadDeRepeticiones</code> simulaciones realizadas para completar un álbum de tamaño <code>tamanioAlbum</code>.",
  "aridad":{"cantidadDeFigusPromedio":2},
  "pre":"k=-1\ndef cantidadDeFigusNecesaria(tamanioAlbum):\n  global k\n  k = (k+1) % len(llenados)\n  return llenados[k]",
  "run_data":[{
    "pre":"llenados = [18,16,11,12,10,16,14,12,13,15]",
    "post":"abs(cantidadDeFigusPromedio(6,10) - 13.7) < 0.1"
  }, {
    "pre":"llenados = [8,10,11,12,10,16,14,12,10,15,8,10,11,12,10,16,14,12,10,15]",
    "post":"abs(cantidadDeFigusPromedio(6,20) - 11.8) < 0.1"
  }, {
    "pre":"llenados = [18,17,21,22,30,26,24,32,30,25]",
    "post":"abs(cantidadDeFigusPromedio(8,10) - 24.5) < 0.1"
  }]
}

figus_3_esperanza = {
  "nombre":"Figus 3",
  "enunciado":"Implementar una función llamada <code>cantidadDeFigusEsperada</code> que tenga por parámetro el tamaño del álbum (<code>tamanioAlbum</code>). Debe devolver la cantidad esperada que propone la matemática, presentada en la fórmula (1).",
  "aridad":{"cantidadDeFigusEsperada":1},
  "run_data":[{
    "post":"abs(cantidadDeFigusEsperada(3) - 5.5) < 0.1"
  }, {
    "post":"abs(cantidadDeFigusEsperada(6) - 14.7) < 0.1"
  }]
}

figus_4_chance = {
  "nombre":"Figus 4",
  "enunciado":"Implemente una funcion llamada <code>chanceDeCompletarAlbum(resultados, cantidadMaxima)</code> donde <code>resultados</code> representa una lista con la cantidad de figuritas que tuvimos que comprar para llenar el album, mientras que <code>cantidadMaxima</code> denota la canditad máxima de de figus que podemos comprar. Debe devolver las chances de completar un álbum pudiendo comprar a lo sumo <code>cantidadMaxima</code> figuritas. Utilizando la lista <code>resultados</code>, calcular el cociente entre la cantidad de veces que <code>cantidadMaxima</code> sirve para completar el álbum, dividido la cantidad de elementos que hay en <code>resultados</code>.",
  "aridad":{"chanceDeCompletarAlbum":2},
  "run_data":[{
    "post":"abs(chanceDeCompletarAlbum([3,5,12,14], 10) - 0.5) < 0.1"
  }, {
    "post":"abs(chanceDeCompletarAlbum([3,5,12,14,30], 20) - 0.8) < 0.1"
  }, {
    "post":"abs(chanceDeCompletarAlbum([3,5,12,14,30], 6) - 0.6) < 0.1"
  }]
}

figus_5_simulacion_chance = {
  "nombre":"Figus 5",
  "enunciado":"Implementar la función <code>chanceSimulada(tamanioAlbum,cantidadMaxima,cantidadDeRepeticiones)</code> que tome por parámetros el tamaño del álbum (<code>tamanioAlbum</code>) la cantidad máxima de figus que se pueden comprar (<code>cantidadMaxima</code>) y la cantidad de repeticiones que queremos hacer (<code>cantidadDeRepeticiones</code>). Debe devolver por medio de la instrucción <code>return</code> la chance de completar un álbum de tamaño <code>tamanioAlbum</code>, si puedo compar a lo suma <code>cantidadMaxima</code>, calculada por medio de una simulación de <code>cantidadDeRepeticiones</code> llenados de álbum. Como en el primer ejercicio, está definida la función <code>dado(cantidadDeCaras)</code>, que al invocarla devuelve un número entre <code>0</code> y <code>cantidadDeCaras-1</code>, inclusive",
  "aridad":{"chanceSimulada":3},
  "pre":"k=-1\ndef dado(cantidadDeCaras):\n  global k\n  k = (k+1) % len(tiradas)\n  return tiradas[k]",
  "run_data":[{
    "pre":"tiradas = [0,1,2,3,4,5,0,0,0,0,0,0,0]",
    "post":"abs(chanceSimulada(6,8,2) - 0.5) < 0.1"
  }, {
    "pre":"tiradas = [0,0,1,1,2,2,0,0,1,1,2,2,0,0,1,1,2,2,0,0,1,1,2,3]",
    "post":"abs(chanceSimulada(4,6,4) - 0.25) < 0.1"
  }]
}

AsignacionesYListas2023I = {
  "file_moodle":"exactas_programa_2023_I/AsignacionesYListas.xml"
}

CiclosYCondiciones2023I = {
  "file_moodle":"exactas_programa_2023_I/CiclosYCondiciones.xml"
}

CiclosYFigus2023I = {
  "file_moodle":"exactas_programa_2023_I/CiclosYFigus.xml"
}

Funciones2023I = {
  "file_moodle":"exactas_programa_2023_I/Funciones.xml"
}

ListasYFigus2023I = {
  "file_moodle":"exactas_programa_2023_I/ListasYFigus.xml"
}

MasFunciones2023I = {
  "file_moodle":"exactas_programa_2023_I/MasFunciones.xml"
}

OperadoresLogicos2023I = {
  "file_moodle":"exactas_programa_2023_I/OperadoresLogicos.xml"
}

CURSOS = {
  "exactas_programa_2023_I":{
    "nombre":"Exactas Programa Invierno 2023",
    "anio":"2023",
    "edicion":"Invierno",
    "descripcion":"Curso correspondiente al taller de Python Exactas Programa",
    "responsable":{
      "nombre":"Equipo docente de Exactas Programa",
      "contacto":"exactasprograma (AT) dc.uba.ar"
    },
    "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    "ejs":[figus_1_cantidadNecesaria,figus_2_promedio,figus_3_esperanza,figus_4_chance,figus_5_simulacion_chance],
    "cuestionarios":[AsignacionesYListas2023I,CiclosYCondiciones2023I,CiclosYFigus2023I,Funciones2023I,ListasYFigus2023I,MasFunciones2023I,OperadoresLogicos2023I]
  },
  "exactas_programa_2025_V":{
    "nombre":"Exactas Programa Verano 2025",
    "anio":"2025",
    "edicion":"Verano",
    "descripcion":"Curso correspondiente al taller de Python Exactas Programa",
    "responsable":{
      "nombre":"Equipo docente de Exactas Programa",
      "contacto":"exactasprograma (AT) dc.uba.ar"
    },
    "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    "ejs":[]
  }
}

for c in CURSOS:
  if "cuestionarios" in CURSOS[c]:
    for q in CURSOS[c]["cuestionarios"]:
      if "file_moodle" in q:
        cargarCuestionarioMoodle(q)
      organizarPreguntasYRespuestas(q)
