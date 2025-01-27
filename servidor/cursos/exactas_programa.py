# -*- coding: utf-8 -*-

figus_1_cantidadNecesaria = {
  "nombre":"Figus 1",
  "enunciado":"Sabiendo que está definida la función dado(cantidadDeCaras), que al invocarla devuelve un número entre 0 y cantidadDeCaras-1, inclusive, implementar la función cantidadDeFigusNecesaria(tamanioAlbum) que genere un álbum de tamaño tamanioAlbum, simule su llenado y devuelva la cantidad de figuritas que se debieron adquirir para completarlo.",
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
  "enunciado":"Teniendo ya definda la función cantidadDeFigusNecesaria del ejercicio anterior, implementar la función cantidadDeFigusPromedio(tamanioAlbum,cantidadDeRepeticiones) que tome por parámetros el tamaño del álbum (tamanioAlbum) y la cantidad de repeticiones que queremos hacer (cantidadDeRepeticiones). Debe devolver por medio de la instrucción return el promedio de los valores obtenidos a lo largo de las cantidadDeRepeticiones simulaciones realizadas para completar un álbum de tamaño tamanioAlbum.",
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
  "enunciado":"Implementar una función llamada cantidadDeFigusEsperada que tenga por parámetro el tamaño del álbum (tamanioAlbum). Debe devolver la cantidad esperada que propone la matemática, presentada en la fórmula (1).",
  "aridad":{"cantidadDeFigusEsperada":1},
  "run_data":[{
    "post":"abs(cantidadDeFigusEsperada(3) - 5.5) < 0.1"
  }, {
    "post":"abs(cantidadDeFigusEsperada(6) - 14.7) < 0.1"
  }]
}

figus_4_chance = {
  "nombre":"Figus 4",
  "enunciado":"Implemente una funcion llamada chanceDeCompletarAlbum(resultados, cantidadMaxima) donde resultados representa una lista con la cantidad de figuritas que tuvimos que comprar para llenar el album, mientras que cantidadMaxima denota la canditad máxima de de figus que podemos comprar. Debe devolver las chances de completar un álbum pudiendo comprar a lo sumo cantidadMaxima figuritas. Utilizando la lista resultados, calcular el cociente entre la cantidad de veces que cantidadMaxima sirve para completar el álbum, dividido la cantidad de elementos que hay en resultados.",
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
  "enunciado":"Implementar la función chanceSimulada(tamanioAlbum,cantidadMaxima,cantidadDeRepeticiones) que tome por parámetros el tamaño del álbum (tamanioAlbum) la cantidad máxima de figus que se pueden comprar (cantidadMaxima) y la cantidad de repeticiones que queremos hacer (cantidadDeRepeticiones). Debe devolver por medio de la instrucción return la chance de completar un álbum de tamaño tamanioAlbum, si puedo compar a lo suma cantidadMaxima, calculada por medio de una simulación de cantidadDeRepeticiones llenados de álbum. Como en el primer ejercicio, está definida la función dado(cantidadDeCaras), que al invocarla devuelve un número entre 0 y cantidadDeCaras-1, inclusive",
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

CURSOS = {
  "exactas_programa_2023_I":{
    "nombre":"Exactas Programa Invierno 2023",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    "ejs":[figus_1_cantidadNecesaria,figus_2_promedio,figus_3_esperanza,figus_4_chance,figus_5_simulacion_chance]
  },
  "exactas_programa_2025_V":{
    "nombre":"Exactas Programa Verano 2025",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    "ejs":[]
  }
}