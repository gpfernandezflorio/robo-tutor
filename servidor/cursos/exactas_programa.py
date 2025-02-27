# -*- coding: utf-8 -*-

figus_1_cantidadNecesaria = {
  "tipo":"CODIGO",
  "id":"Figus1",
  "nombre":"Figus 1",
  "enunciado":"Sabiendo que está definida la función <code>dado(cantidadDeCaras)</code>, que al invocarla devuelve un número entre <code>0</code> y <code>cantidadDeCaras-1</code>, inclusive, implementar la función <code>cantidadDeFigusNecesaria(tamanioAlbum)</code> que genere un álbum de tamaño <code>tamanioAlbum</code>, simule su llenado y devuelva la cantidad de figuritas que se debieron adquirir para completarlo.",
  "aridad":{"cantidadDeFigusNecesaria":1},
  "pre":"k=-1\ndef dado(cantidadDeCaras):\n  global k\n  k = (k+1) % len(tiradas)\n  return tiradas[k] % cantidadDeCaras",
  "run_data":[{
    "pre":"tiradas = [0,1,2,3,4,5]",
    "assert":"cantidadDeFigusNecesaria(6) == 6"
  }, {
    "pre":"tiradas = [0,1,2,0,1,2,3,4,3,5]",
    "assert":"cantidadDeFigusNecesaria(6) == 10"
  }, {
    "pre":"tiradas = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7]",
    "assert":"cantidadDeFigusNecesaria(8) == 19"
  }]
}

figus_2_promedio = {
  "tipo":"CODIGO",
  "id":"Figus2",
  "nombre":"Figus 2",
  "enunciado":"Teniendo ya definda la función <code>cantidadDeFigusNecesaria</code> del ejercicio anterior, implementar la función <code>cantidadDeFigusPromedio(tamanioAlbum,cantidadDeRepeticiones)</code> que tome por parámetros el tamaño del álbum (<code>tamanioAlbum</code>) y la cantidad de repeticiones que queremos hacer (<code>cantidadDeRepeticiones</code>). Debe devolver por medio de la instrucción <code>return</code> el promedio de los valores obtenidos a lo largo de las <code>cantidadDeRepeticiones</code> simulaciones realizadas para completar un álbum de tamaño <code>tamanioAlbum</code>.",
  "aridad":{"cantidadDeFigusPromedio":2},
  "pre":"k=-1\ndef cantidadDeFigusNecesaria(tamanioAlbum):\n  global k\n  k = (k+1) % len(llenados)\n  return llenados[k]",
  "run_data":[{
    "pre":"llenados = [18,16,11,12,10,16,14,12,13,15]",
    "assert":"abs(cantidadDeFigusPromedio(6,10) - 13.7) < 0.1"
  }, {
    "pre":"llenados = [8,10,11,12,10,16,14,12,10,15,8,10,11,12,10,16,14,12,10,15]",
    "assert":"abs(cantidadDeFigusPromedio(6,20) - 11.8) < 0.1"
  }, {
    "pre":"llenados = [18,17,21,22,30,26,24,32,30,25]",
    "assert":"abs(cantidadDeFigusPromedio(8,10) - 24.5) < 0.1"
  }]
}

figus_3_esperanza = {
  "tipo":"CODIGO",
  "id":"Figus3",
  "nombre":"Figus 3",
  "enunciado":"Implementar una función llamada <code>cantidadDeFigusEsperada</code> que tenga por parámetro el tamaño del álbum (<code>tamanioAlbum</code>). Debe devolver la cantidad esperada que propone la matemática, presentada en la fórmula (1).",
  "aridad":{"cantidadDeFigusEsperada":1},
  "run_data":[{
    "assert":"abs(cantidadDeFigusEsperada(3) - 5.5) < 0.1"
  }, {
    "assert":"abs(cantidadDeFigusEsperada(6) - 14.7) < 0.1"
  }]
}

figus_4_chance = {
  "tipo":"CODIGO",
  "id":"Figus4",
  "nombre":"Figus 4",
  "enunciado":"Implemente una funcion llamada <code>chanceDeCompletarAlbum(resultados, cantidadMaxima)</code> donde <code>resultados</code> representa una lista con la cantidad de figuritas que tuvimos que comprar para llenar el album, mientras que <code>cantidadMaxima</code> denota la canditad máxima de de figus que podemos comprar. Debe devolver las chances de completar un álbum pudiendo comprar a lo sumo <code>cantidadMaxima</code> figuritas. Utilizando la lista <code>resultados</code>, calcular el cociente entre la cantidad de veces que <code>cantidadMaxima</code> sirve para completar el álbum, dividido la cantidad de elementos que hay en <code>resultados</code>.",
  "aridad":{"chanceDeCompletarAlbum":2},
  "run_data":[{
    "assert":"abs(chanceDeCompletarAlbum([3,5,12,14], 10) - 0.5) < 0.1"
  }, {
    "assert":"abs(chanceDeCompletarAlbum([3,5,12,14,30], 20) - 0.8) < 0.1"
  }, {
    "assert":"abs(chanceDeCompletarAlbum([3,5,12,14,30], 6) - 0.6) < 0.1"
  }]
}

figus_5_simulacion_chance = {
  "tipo":"CODIGO",
  "id":"Figus5",
  "nombre":"Figus 5",
  "enunciado":"Implementar la función <code>chanceSimulada(tamanioAlbum,cantidadMaxima,cantidadDeRepeticiones)</code> que tome por parámetros el tamaño del álbum (<code>tamanioAlbum</code>) la cantidad máxima de figus que se pueden comprar (<code>cantidadMaxima</code>) y la cantidad de repeticiones que queremos hacer (<code>cantidadDeRepeticiones</code>). Debe devolver por medio de la instrucción <code>return</code> la chance de completar un álbum de tamaño <code>tamanioAlbum</code>, si puedo compar a lo suma <code>cantidadMaxima</code>, calculada por medio de una simulación de <code>cantidadDeRepeticiones</code> llenados de álbum. Como en el primer ejercicio, está definida la función <code>dado(cantidadDeCaras)</code>, que al invocarla devuelve un número entre <code>0</code> y <code>cantidadDeCaras-1</code>, inclusive",
  "aridad":{"chanceSimulada":3},
  "pre":"k=-1\ndef dado(cantidadDeCaras):\n  global k\n  k = (k+1) % len(tiradas)\n  return tiradas[k] % cantidadDeCaras",
  "run_data":[{
    "pre":"tiradas = [0,1,2,3,4,5,0,0,0,0,0,0,0]",
    "assert":"abs(chanceSimulada(6,8,2) - 0.5) < 0.1"
  }, {
    "pre":"tiradas = [0,0,1,1,2,2,0,0,1,1,2,2,0,0,1,1,2,2,0,0,1,1,2,3]",
    "assert":"abs(chanceSimulada(4,6,4) - 0.25) < 0.1"
  }]
}

AsignacionesYListas2023I = {
  "tipo":"CUESTIONARIO",
  "id":"AsignacionesYListas",
  "file_moodle":"exactas_programa_2023_I/AsignacionesYListas.xml"
}

ListasYFigus2023I = {
  "tipo":"CUESTIONARIO",
  "id":"ListasYFigus",
  "file_moodle":"exactas_programa_2023_I/ListasYFigus.xml"
}

Funciones2023I = {
  "tipo":"CUESTIONARIO",
  "id":"Funciones",
  "file_moodle":"exactas_programa_2023_I/Funciones.xml"
}

CiclosYCondiciones2023I = {
  "tipo":"CUESTIONARIO",
  "id":"CiclosYCondiciones",
  "file_moodle":"exactas_programa_2023_I/CiclosYCondiciones.xml"
}

CiclosYFigus2023I = {
  "tipo":"CUESTIONARIO",
  "id":"CiclosYFigus",
  "file_moodle":"exactas_programa_2023_I/CiclosYFigus.xml"
}

MasFunciones2023I = {
  "tipo":"CUESTIONARIO",
  "id":"MasFunciones",
  "file_moodle":"exactas_programa_2023_I/MasFunciones.xml"
}

OperadoresLogicos2023I = {
  "tipo":"CUESTIONARIO",
  "id":"OperadoresLogicos",
  "file_moodle":"exactas_programa_2023_I/OperadoresLogicos.xml"
}

def AsignacionesYListas2025V(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"AsignacionesYListas",
    "file_moodle":"exactas_programa_2025_V/Asignaciones y Listas.xml",
    "visible":{"desde":fecha}
  }

def ListasYFigus2025V(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"ListasYFigus",
    "file_moodle":"exactas_programa_2025_V/Listas y Figus.xml",
    "visible":{"desde":fecha}
  }

def Funciones2025V(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"Funciones",
    "file_moodle":"exactas_programa_2025_V/Funciones.xml",
    "visible":{"desde":fecha}
  }

def CiclosYCondiciones2025V(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"CiclosYCondiciones",
    "file_moodle":"exactas_programa_2025_V/Ciclos y Condiciones.xml",
    "visible":{"desde":fecha}
  }

def CiclosYFigus2025V(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"CiclosYFigus",
    "file_moodle":"exactas_programa_2025_V/Ciclos y Figus.xml",
    "visible":{"desde":fecha}
  }

def MasFunciones2025V(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"MasFunciones",
    "file_moodle":"exactas_programa_2025_V/Mas Funciones.xml",
    "visible":"NO"
  }

def OperadoresLogicos2025V(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"OperadoresLogicos",
    "file_moodle":"exactas_programa_2025_V/Operadores Logicos.xml",
    "visible":{"desde":fecha}
  }

def figus_sin_funciones(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Figus_sf_1",
    "nombre":"Figus, versión 0",
    "enunciado":"Sabiendo que está disponible la función <code>randint(inf, sup)</code>, que devuelve un número entero aleatorio entre <code>inf</code> y <code>sup</code> (ambos incluídos), escribir un código en el que:<br/>- Se genere una variable <code>album</code>, que represente a un álbum de 6 figuritas vacío.<br/>- Se genere una variable <code>contador</code>, para contar el total de figuritas compradas para llenar el álbum.<br/>-  Se defina un ciclo que repita el mismo procedimiento hasta que el album se llene (todos los elementos sean 1). El procedimiento debe consistir en:<br/>1. Generar una variable <code>figu</code> que reciba un número aleatorio entre 0 y 5.<br/>2. Pegar la figu, es decir, poner un 1 en la posición que corresponda del album.<br/>3. Contar la figu, es decir, incrementar la variable <code>contador</code>.",
    "pre":"k=-1\ndef randint(inf, sup):\n  global k\n  k = (k+1) % len(tiradas)\n  return inf + (tiradas[k] % (sup+1-inf))",
    "def":["album","contador","figu"],
    "run_data":[{
      "pre":"tiradas = [6,1,2,3,4,5]",
      "assert":"contador == 6 and type(album) == type([]) and len(album) == 6 and len(list(filter(lambda x : x==1, album))) == 6"
    }, {
      "pre":"tiradas = [0,1,2,0,1,2,3,4,3,5]",
      "assert":"contador == 10 and type(album) == type([]) and len(album) == 6 and len(list(filter(lambda x : x==1, album))) == 6"
    }],
    "visible":{"desde":fecha}
  }

def figus_de_verdad_1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Figus_dv_1",
    "nombre":"Figus, de verdad (1)",
    "enunciado":"Sabiendo que está definida la función <code>dadoDe_Caras(cantidadDeCaras)</code>, que al invocarla devuelve un número entre <code>0</code> y <code>cantidadDeCaras-1</code>, inclusive, implementar la función <code>cuantas_figus(figus_total)</code> que reciba la cantidad total de figuritas de un álbum (<code>figus_total</code>), realice la simulación de llenado y devuelva la cantidad de figuritas que fue necesario comprar para llenar el álbum. Se asume que las figuritas se compran de a una. Escribir un ciclo controlado por un contador <code>j</code> en el que la función se corra 1000 veces para un álbum de 6 figuritas y se calcule el promedio de figuritas necesarias para llenar el álbum en esas 1000 pruebas. Este promedio debe almacenarse en una variable de nombre <code>promedio</code>.",
    "pre":"k=-1\ndef dadoDe_Caras(cantidadDeCaras):\n  global k\n  k = (k+1) % len(tiradas)\n  return tiradas[k] % cantidadDeCaras",
    "aridad":{"cuantas_figus":1},
    "def":["promedio","j"],
    "run_data":[{
      "pre":"tiradas = [0,1,2,3,4,5]",
      "assert":"j == 1000 and promedio == 6"
    }, {
      "pre":"tiradas = [0,6,1,7,2,2,3,3,4,4,5]",
      "assert":"j == 1000 and promedio == 11 and cuantas_figus(8) == 11"
    }, {
      "pre":"tiradas = [0,1,2,3,4,5,6,0,1,1,2,2,3,7,4,5]",
      "assert":"j == 1000 and promedio == 8 and cuantas_figus(8) == 14"
    }],
    "visible":{"desde":fecha}
  }

def figus_de_verdad_2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Figus_dv_2",
    "nombre":"Figus, de verdad (2)",
    "enunciado":"Sabiendo que está definida la función <code>dadoDe_Caras(cantidadDeCaras)</code>, que al invocarla devuelve un número entre <code>0</code> y <code>cantidadDeCaras-1</code>, inclusive, implementar las siguientes funciones:<br/>(a) <code>cuantas_figus(album)</code>: debe recibir una lista <code>album</code> y simular el llenado, asumiendo que se compran figuritas de a una. Debe devolver la cantidad de figuritas que fue necesario comprar.<br/>(b) <code>limpiar_album(album)</code>: debe recibir una lista <code>album</code> y llenarla de ceros (reiniciar el álbum).<br/>(c) <code>promedio(figus_total, n_albumes)</code>: debe recibir dos números, crear un álbum de <code>figus_total</code> casilleros y definir un contador <code>cantidad</code> en el que se acumule la cantidad de figus compradas. Luego, realizar un ciclo de <code>n_albumes</code> pasos en el que:<br/>1. Se limpie el album usando la función <code>limpiar_album</code>,<br/>2. Se llene el album usando la función <code>cuantas_figus</code> y<br/>3. Se sume a <code>cantidad</code> el número de figuritas necesarias para llenar el álbum.<br/>Finalmente, debe devolver el promedio de figuritas necesarias para llenar un álbum (<code>cantidad / n_albumes</code>).",
    "aridad":{"cuantas_figus":1,"limpiar_album":1,"promedio":2},
    "pre":"k=-1\ndef dadoDe_Caras(cantidadDeCaras):\n  global k\n  k = (k+1) % len(tiradas)\n  return tiradas[k] % cantidadDeCaras",
    "run_data":[{
      "pre":"a1 = [1]*6\na2 = [1]*10\na3 = [1]*150",
      "post":"limpiar_album(a1)\nlimpiar_album(a2)\nlimpiar_album(a3)",
      "assert":"all(a1[i] == 0 for i in range(len(a1))) and all(a2[i] == 0 for i in range(len(a2))) and all(a3[i] == 0 for i in range(len(a3)))"
    }, {
      "pre":"tiradas = [0,1,2,3,4,5]",
      "assert":"cuantas_figus([0]*6) == 6 and abs(promedio(6,4) - 6) < 0.1"
    }, {
      "pre":"tiradas = [0,6,1,7,2,8,3,9,4,10,5,11]",
      "assert":"cuantas_figus([0]*6) == 11 and cuantas_figus([0]*10) == 12"
    }, {
      "pre":"tiradas = [0,1,2,3,0,0,1,1,2,2,3,3,3,3,2,2,2,1,1,1,0]",
      "assert":"abs(promedio(4,3) - 7) < 0.1 and abs(promedio(4,6) - 7) < 0.1"
    }],
    "visible":{"desde":fecha}
  }

def diezmil_1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"diezmil_1",
    "nombre":"Diezmil (1)",
    "enunciado":"Sabiendo que está definida la función <code>dado(cantidadDeCaras)</code>, que al invocarla devuelve un número entre <code>0</code> y <code>cantidadDeCaras-1</code>, inclusive, implementar la función <code>tirar_cubilete()</code> que no reciba parámetros y devuelva una lista de 5 casilleros con números al azar entre 1 y 6.",
    "aridad":{"tirar_cubilete":0},
    "pre":"k=-1\ndef dado(cantidadDeCaras):\n  global k\n  k = (k+1) % len(tiradas)\n  return tiradas[k] % cantidadDeCaras",
    "post":"cubilete = tirar_cubilete()",
    "run_data":[{
      "pre":"tiradas = [2]",
      "assert":"len(cubilete) == 5 and all([(cubilete[i] >= 1 and cubilete[i] <= 6) for i in range(5)]) and all([cubilete[i] == cubilete[i+1] for i in range(4)])"
    }, {
      "pre":"tiradas = [2,5,2,5,1]",
      "assert":"len(cubilete) == 5 and all([(cubilete[i] >= 1 and cubilete[i] <= 6) for i in range(5)])"
    }, {
      "pre":"tiradas = [4,3,2,1,0]",
      "assert":"len(cubilete) == 5 and all([(cubilete[i] >= 1 and cubilete[i] <= 6) for i in range(5)]) and all([cubilete[i] != cubilete[i+1] for i in range(4)])"
    }],
    "visible":{"desde":fecha}
  }

def diezmil_2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"diezmil_2",
    "nombre":"Diezmil (2)",
    "enunciado":"Implementar la función <code>puntos_por_unos(cubilete)</code> que reciba una lista de cinco dados y devuelva el puntaje que aportan los unos que aparecen en el cubilete. Las reglas son: cada 1 suma 100 puntos, pero tres unos suman 1000 y 5 unos suman 10000. De este modo, al cubilete <code>[1,2,3,1,1]</code> le corresponden 1000 puntos, pero al cubilete <code>[1,1,6,1,1]</code> le corresponden 1100 puntos.",
    "aridad":{"puntos_por_unos":1},
    "run_data":[{
      "pre":"cubilete = [1,5,5,5,5]",
      "assert":"puntos_por_unos(cubilete) == 100 and cubilete == [1,5,5,5,5]"
    }, {
      "pre":"cubilete = [1,1,5,5,5]",
      "assert":"puntos_por_unos(cubilete) == 200 and cubilete == [1,1,5,5,5]"
    }, {
      "pre":"cubilete = [1,1,1,5,5]",
      "assert":"puntos_por_unos(cubilete) == 1000 and cubilete == [1,1,1,5,5]"
    }, {
      "pre":"cubilete = [1,1,1,1,5]",
      "assert":"puntos_por_unos(cubilete) == 1100 and cubilete == [1,1,1,1,5]"
    }, {
      "pre":"cubilete = [1,1,1,1,1]",
      "assert":"puntos_por_unos(cubilete) == 10000 and cubilete == [1,1,1,1,1]"
    }],
    "visible":{"desde":fecha}
  }

def diezmil_3(fecha):
  return {
    "tipo":"CODIGO",
    "id":"diezmil_3",
    "nombre":"Diezmil (3)",
    "enunciado":"Implementar la función <code>acumular_puntajes(puntos_jugada,puntos_totales)</code>. Se espera que los argumentos <code>puntos_jugada</code> y <code>puntos_totales</code> sean listas de la misma longitud. La función debe sumar casillero a casillero ambas listas y acumular el resulado en <code>puntos_totales</code> y no debe devolver nada.",
    "aridad":{"acumular_puntajes":2},
    "run_data":[{
      "pre":"jugada = [1000,50,1150,200]\ntotales = [5500,1750,2100,3500]",
      "assert":"acumular_puntajes(jugada,totales) is None and jugada == [1000,50,1150,200] and totales == [6500,1800,3250,3700]"
    }, {
      "pre":"jugada = [150,250,300]\ntotales = [350,1100,2350]",
      "assert":"acumular_puntajes(jugada,totales) is None and jugada == [150,250,300] and totales == [500,1350,2650]"
    }],
    "visible":{"desde":fecha}
  }

linkEncuestaInicial_2025_V = {
  "tipo":"LINK",
  "id":"linkEncuestaInicial",
  "nombre":"Encuesta Inicial",
  "url":"https://docs.google.com/forms/d/e/1FAIpQLSefK1jnPNEanKnKnVxkZNZfFJv0sWRS4ataFyerLZd_fQ47tA/viewform"
}

def linkBloquesFigus1(fecha):
  return {
    "tipo":"LINK",
    "id":"bloquesFigus1",
    "nombre":"Figus Bloques (1)",
    "url":"https://reda-ar.github.io/campus/milanator/?juego=figus0&toolbox=off",
    "visible":{"desde":fecha}
  }

def linkBloquesFigus2(fecha):
  return {
    "tipo":"LINK",
    "id":"bloquesFigus2",
    "nombre":"Figus Bloques (2) (exploratorio)",
    "url":"https://reda-ar.github.io/campus/milanator/?juego=figus",
    "visible":"NO"
  }

def linkBloquesFigus3(fecha):
  return {
    "tipo":"LINK",
    "id":"bloques5Figus3",
    "nombre":"Figu5s Bloques (3) (exploratorio)",
    "url":"https://reda-ar.github.io/campus/milanator/?juego=figus&fix=N",
    "visible":"NO"
  }

def linkBloquesFigus4(fecha):
  return {
    "tipo":"LINK",
    "id":"bloquesFigus4",
    "nombre":"Figus Bloques (4) (exploratorio)",
    "url":"https://reda-ar.github.io/campus/milanator/?juego=figus2",
    "visible":"NO"
  }

def linkComoLaPasaste_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkComoLaPasaste",
    "nombre":"Encuesta cierre Clase 00",
    "url":"https://docs.google.com/forms/d/e/1FAIpQLSdjUo4bpoJ0wYFftUUMs9xh0BfY6wLiKsjbFj5l1HfHVeJ8ZQ/viewform",
    "visible":{"desde":fecha}
  }

def linkDiaposClase00_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkDiapos00",
    "nombre":"Diapositivas Clase 00",
    "url":"https://drive.google.com/file/d/110QruT1EjERsnzYqCveLokIRF5Khqw7h/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkMachete00_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkMachete00",
    "nombre":"Machete Clase 00",
    "url":"https://drive.google.com/file/d/1rbB3bocljMegO8o-X3_rHL30CVo5nI7w/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkDiaposClase01_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkDiapos01",
    "nombre":"Diapositivas Clase 01",
    "url":"https://drive.google.com/file/d/1XMrG_3MsUSMdk61eJTpSK0ceEyKltmds/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkActividad01_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkActividad01",
    "nombre":"Actividad Clase 01",
    "url":"https://drive.google.com/file/d/1iW4qFXydl6-daZ6r5mhnGdYUgqFCiJfL/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkMachete01_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkMachete01",
    "nombre":"Machete Clase 01",
    "url":"https://drive.google.com/file/d/1LvvZefcbwZafA6VDpTen5E5F20luuSEi/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkParaPensar01_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkParaPensar01",
    "nombre":"Para pensar durante el finde",
    "url":"https://drive.google.com/file/d/1OQd1wt5iLhr129ze6dknUY-GkF6lT8Am/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkNotaPenza_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkNotaPenza",
    "nombre":"Nota de Adrián Paenza sobre figuritas",
    "url":"https://drive.google.com/file/d/16RFHGLYCPpMqC8keGVrPaq3DcreegTPM/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkDiaposClase02_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkDiapos02",
    "nombre":"Diapositivas Clase 02",
    "url":"https://drive.google.com/file/d/1I9zwlNctbQdVsUPXMwtQSo-KZEboziZf/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkActividad02_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkActividad02",
    "nombre":"Actividad Clase 02",
    "url":"https://drive.google.com/file/d/1t9wg2InlJoLh6PmtoZdUiaAZe0FLQkPx/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def linkMachete02_2025_V(fecha):
  return {
    "tipo":"LINK",
    "id":"linkMachete02",
    "nombre":"Machete Clase 02",
    "url":"https://drive.google.com/file/d/1mbbt4J5KxzLpDQ25V4TKz27XJlg2RyeO/view?usp=drive_link",
    "visible":{"desde":fecha}
  }

def clase0(fecha):
  return {
    "tipo":"SECCION",
    "id":"clase0",
    "nombre":"Clase 00 - Introducción",
    "visible":{"desde":fecha}
  }

def clase1(fecha):
  return {
    "tipo":"SECCION",
    "id":"clase1",
    "nombre":"Clase 01 - Figuritas",
    "visible":{"desde":fecha}
  }

def clase2(fecha):
  return {
    "tipo":"SECCION",
    "id":"clase2",
    "nombre":"Clase 02 - Diez mil",
    "visible":{"desde":fecha}
  }

actividades_2025_V = {
  "TM":[
      linkEncuestaInicial_2025_V,
    clase0("24/2/2025-8:30"),
      linkBloquesFigus1("24/2/2025-8:30"),
      linkBloquesFigus2("24/2/2025-8:30"),
      linkBloquesFigus3("24/2/2025-8:30"),
      linkBloquesFigus4("24/2/2025-8:30"),
      linkComoLaPasaste_2025_V("24/2/2025-12:30"),
      linkDiaposClase00_2025_V("24/2/2025-8:30"),
      AsignacionesYListas2025V("24/2/2025-12:30"),
      ListasYFigus2025V("24/2/2025-12:30"),
      CiclosYFigus2025V("24/2/2025-12:30"),
      figus_sin_funciones("24/2/2025-12:30"),
      linkMachete00_2025_V("24/2/2025-12:30"),
    clase1("26/2/2025-8:30"),
      linkDiaposClase01_2025_V("26/2/2025-8:30"),
      linkActividad01_2025_V("26/2/2025-8:30"),
      CiclosYCondiciones2025V("26/2/2025-12:30"),
      Funciones2025V("26/2/2025-12:30"),
      MasFunciones2025V("26/2/2025-12:30"),
      figus_de_verdad_1("26/2/2025-12:30"),
      figus_de_verdad_2("26/2/2025-12:30"),
      linkMachete01_2025_V("26/2/2025-12:30"),
      linkParaPensar01_2025_V("26/2/2025-12:30"),
      linkNotaPenza_2025_V("26/2/2025-12:30"),
    clase2("28/2/2025-8:30"),
      linkDiaposClase02_2025_V("28/2/2025-8:30"),
      linkActividad02_2025_V("28/2/2025-8:30"),
      OperadoresLogicos2025V("28/2/2025-12:30"),
      diezmil_1("28/2/2025-12:30"),
      diezmil_2("28/2/2025-12:30"),
      diezmil_3("28/2/2025-12:30"),
      linkMachete02_2025_V("28/2/2025-12:30")
  ],
  "TT":[
      linkEncuestaInicial_2025_V,
    clase0("24/2/2025-13:00"),
      linkBloquesFigus1("24/2/2025-13:00"),
      linkBloquesFigus2("24/2/2025-13:00"),
      linkBloquesFigus3("24/2/2025-13:00"),
      linkBloquesFigus4("24/2/2025-13:00"),
      linkComoLaPasaste_2025_V("24/2/2025-17:00"),
      linkDiaposClase00_2025_V("24/2/2025-13:00"),
      AsignacionesYListas2025V("24/2/2025-17:00"),
      ListasYFigus2025V("24/2/2025-17:00"),
      CiclosYFigus2025V("24/2/2025-17:00"),
      figus_sin_funciones("24/2/2025-17:00"),
      linkMachete00_2025_V("24/2/2025-17:00"),
    clase1("26/2/2025-13:00"),
      linkDiaposClase01_2025_V("26/2/2025-13:00"),
      linkActividad01_2025_V("26/2/2025-13:00"),
      CiclosYCondiciones2025V("26/2/2025-17:00"),
      Funciones2025V("26/2/2025-17:00"),
      MasFunciones2025V("26/2/2025-17:00"),
      figus_de_verdad_1("26/2/2025-17:00"),
      figus_de_verdad_2("26/2/2025-17:00"),
      linkMachete01_2025_V("26/2/2025-17:00"),
      linkParaPensar01_2025_V("26/2/2025-17:00"),
      linkNotaPenza_2025_V("26/2/2025-17:00"),
    clase2("28/2/2025-13:00"),
      linkDiaposClase02_2025_V("28/2/2025-13:00"),
      linkActividad02_2025_V("28/2/2025-13:00"),
      OperadoresLogicos2025V("28/2/2025-17:00"),
      diezmil_1("28/2/2025-17:00"),
      diezmil_2("28/2/2025-17:00"),
      diezmil_3("28/2/2025-17:00"),
      linkMachete02_2025_V("28/2/2025-17:00")
  ],
  "TV":[
      linkEncuestaInicial_2025_V,
    clase0("24/2/2025-17:30"),
      linkBloquesFigus1("24/2/2025-17:30"),
      linkBloquesFigus2("24/2/2025-17:30"),
      linkBloquesFigus3("24/2/2025-17:30"),
      linkBloquesFigus4("24/2/2025-17:30"),
      linkComoLaPasaste_2025_V("24/2/2025-21:30"),
      linkDiaposClase00_2025_V("24/2/2025-17:30"),
      AsignacionesYListas2025V("24/2/2025-21:30"),
      ListasYFigus2025V("24/2/2025-21:30"),
      CiclosYFigus2025V("24/2/2025-21:30"),
      figus_sin_funciones("24/2/2025-21:30"),
      linkMachete00_2025_V("24/2/2025-21:30"),
    clase1("26/2/2025-17:30"),
      linkDiaposClase01_2025_V("26/2/2025-17:30"),
      linkActividad01_2025_V("26/2/2025-17:30"),
      CiclosYCondiciones2025V("26/2/2025-21:30"),
      Funciones2025V("26/2/2025-21:30"),
      MasFunciones2025V("26/2/2025-21:30"),
      figus_de_verdad_1("26/2/2025-21:30"),
      figus_de_verdad_2("26/2/2025-21:30"),
      linkMachete01_2025_V("26/2/2025-21:30"),
      linkParaPensar01_2025_V("26/2/2025-21:30"),
      linkNotaPenza_2025_V("26/2/2025-21:30"),
    clase2("28/2/2025-17:30"),
      linkDiaposClase02_2025_V("28/2/2025-17:30"),
      linkActividad02_2025_V("28/2/2025-17:30"),
      OperadoresLogicos2025V("28/2/2025-21:30"),
      diezmil_1("28/2/2025-21:30"),
      diezmil_2("28/2/2025-21:30"),
      diezmil_3("28/2/2025-21:30"),
      linkMachete02_2025_V("28/2/2025-21:30")
  ]
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
    "actividades":[AsignacionesYListas2023I,ListasYFigus2023I,Funciones2023I,figus_1_cantidadNecesaria,figus_2_promedio,figus_3_esperanza,figus_4_chance,figus_5_simulacion_chance,CiclosYCondiciones2023I,CiclosYFigus2023I,MasFunciones2023I,OperadoresLogicos2023I]
  }
}

for turno in actividades_2025_V:
  CURSOS["exactas_programa_2025_V_" + turno] = {
    "nombre":"Exactas Programa Verano 2025 (" + turno + ")",
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
    "actividades":actividades_2025_V[turno],
    "planilla":{
      "url":"1FAIpQLSeUWC_rd9VPapkUy4LsnQrwTqUs3J3U5kuFJMmEk8SUXzPaLQ",
      "campos":{
        "usuario":"9867257",
        "actividad":"1165966175",
        "respuesta":"1778184894",
        "resultado":"1496208069",
        "duracion":"1460244707"
      }
    }
  }
