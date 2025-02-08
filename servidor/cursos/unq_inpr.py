# -*- coding: utf-8 -*-

v = {"a": 0, "r": 0, "n": 0, "v": 0} # Celda vacía
r = {"a": 0, "r": 1, "n": 0, "v": 0} # Celda con una roja
a = {"a": 1, "r": 0, "n": 0, "v": 0} # Celda con una azul
def rs(x): # Celda con varias rojas
    return {"a": 0, "r": x, "n": 0, "v": 0}
def ns(x): # Celda con varias negras
    return {"a": 0, "r": 0, "n": x, "v": 0}
def ed(h,d=0,a=0): # Edificio con h pisos, d departamentos por piso y a ambientes por departamento
    return {"a": 0, "r": h, "n": 0, "v": 1}
def rt(l): # Ruta con l lomos de burro
    return {"a": 0, "r": 1, "n": 0, "v": 2*l}
def duplicarTablero(b):
    return list(map(lambda c: duplicarColumna(c), b))
def duplicarColumna(c):
    return list(map(lambda x: {"a": x["a"], "r": x["r"], "n": x["n"], "v": x["v"]}, c))
def fs(h,a): # Carpeta del FS con h hermanas siguientes y a archivos
    return {"a": h+1, "r": a, "n": 0, "v": 0}
def abrirArchivosB(b):
    return list(map(abrirArchivosC, b))
def abrirArchivosC(c):
    return list(map(lambda x: {"a": x["a"], "r": x["r"], "n": 0, "v": x["r"]}, c))
iniFs = [[v,v,v,v,v,fs(0,2)],[fs(0,2),fs(1,3),v,v,fs(2,1),fs(3,4)],[v,fs(0,3),fs(0,8),fs(1,3),fs(2,4),fs(0,2)],[v,fs(0,4),v,fs(0,2),v,v],[v,v,fs(0,1),fs(1,4),v,v],[v,v,v,v,v,v]]
def agregarRojas(b,k):
    b2 = duplicarTablero(b)
    b2[3][2]["r"] = b2[3][2]["r"] + k
    return b2
def e(p,n): # Enemigo de Gobi en piso p de nivel n
    return {"a": p, "r": 0, "n": n, "v": 0}
def gobiData(t,a): # Data de Gobi con t pisos totales y piso actual a
    return {"a": 0, "r": t, "n": 0, "v": a}
def iniGobi(a): # Tablero inicial Gobi en piso a
    return [[gobiData(4,a),v,e(2,1),v,e(3,7),v],[v,v,e(2,5),v,e(2,8),e(3,6)],[v,e(2,4),v,e(2,4),e(3,4),v],[e(3,6),e(2,6),e(2,2),e(2,5),e(3,10),e(2,3)],[v,v,e(2,4),e(2,1),e(3,5),v],[v,v,e(2,3),e(3,6),e(2,8),e(3,5)]]

'''
    head: [columna, fila]
    board: [col0, col1, ... coln]
        coli: [celda0, celda1, ... celdan]
'''

superGobi64_2 = {
  "id":"SuperGobi64_2",
  "nombre":"Súper Gobi 64 - Parte 2",
  "enunciado":"En el ejercicio anterior mencionamos que, además de Gobi, en el tablero 3D hay enemigos. Cada enemigo tiene un color y nivel de poder. Algunos de estos enemigos son jefes. Para completar un nivel, Gobi debe derrotar a todos los jefes. Escribir la función cantidadDeJefesEnEstePiso que describe la cantidad de jefes que hay en el piso actual. Los jefes son aquellos enemigos que tienen al menos un minion de cada color. Los minions también son enemigos pero para que un enemigo sea minion de un jefe tiene que pasar que su poder sea menor, que estén en el mismo piso y que estén en la misma fila o en la misma columna. Notar que un mismo enemigo puede ser minion de más de un jefe y que los jefes pueden a su vez ser minions de otros jefes más fuertes. Además de todas las primitivas dadas en el ejercico anterior se cuenta también con hayEnemigo, poderDelEnemigo y colorDelEnemigo.",
  "pre":"program {repeat(cantidadDeJefesEnEstePiso()){Poner(Rojo)}}procedure Subir() {if (not puedeSubir()) {BOOM(\"No se puede subir más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Poner(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}procedure Bajar() {if (not puedeBajar()) {BOOM(\"No se puede bajar más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Sacar(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}function puedeSubir() {return(aux_pisoActual()<aux_pisoMaximo())}function puedeBajar() {return(aux_pisoActual()>1)}function estáGobi() {return(nroBolitas(Azul)==aux_pisoActual() && not hayBolitas(Negro))}function hayEnemigo() {return(nroBolitas(Azul)==aux_pisoActual() && hayBolitas(Negro))}function poderDelEnemigo() {if (not hayBolitas(Negro) ||nroBolitas(Azul)/=aux_pisoActual() ) {BOOM(\"No hay enemigo aquí\")}return(nroBolitas(Negro))}function colorDelEnemigo() {if (not hayBolitas(Negro) ||nroBolitas(Azul)/=aux_pisoActual() ) {BOOM(\"No hay enemigo aquí\")}return(choose Rojo when (nroBolitas(Negro) mod 4 == 1) Azul when (nroBolitas(Negro) mod 4 == 2) Negro when (nroBolitas(Negro) mod 4 == 3) Verde otherwise)}function aux_x() {x:=0;while(puedeMover(Oeste)) {Mover(Oeste)x:=x+1}return(x)}function aux_y() {y:=0;while(puedeMover(Sur)) {Mover(Sur)y:=y+1}return(y)}function aux_pisoActual() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Verde))}function aux_pisoMaximo() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Rojo))}",
  "run_data":[{
    "tablero":{"head":[3,2],"width":6,"height":6,"board":iniGobi(2)},
    "post":{"head":[3,2],"width":6,"height":6,"board":agregarRojas(iniGobi(2),3)}
  },{
    "tablero":{"head":[3,2],"width":6,"height":6,"board":iniGobi(3)},
    "post":{"head":[3,2],"width":6,"height":6,"board":agregarRojas(iniGobi(3),1)}
  }]
}

gobFS_1 = {
  "id":"GobFS_1",
  "nombre":"GobFS - Parte 1",
  "enunciado":"-",
  "pre":"procedure IrALaCarpetaRaízDelFS() {IrAlBorde(Norte)IrAlBorde(Oeste)}function quedanCarpetasPorRecorrerEnElFS() {return (tieneCarpetasInternas() || hayCarpetasSuperioresSinRecorrer())}procedure PasarALaSiguienteCarpetaDelFS() {if (tieneCarpetasInternas()) {Mover(Este)} else {while (not hayCarpetasHermanasSinRecorrer()) {IrACarpetaSuperior()}IrACarpetaHermanaSiguiente()}}procedure IrAPrimerArchivoEnCarpetaActual() {Poner(Verde)}function quedanArchivosPorRecorrerEnCarpetaActual() {return (nroBolitas(Verde) < nroBolitas(Rojo))}procedure PasarAlSiguienteArchivoEnCarpetaActual() {Poner(Verde)}procedure ActualizarFechaEnArchivoActual() {}function tieneCarpetasInternas() {res := False if (puedeMover(Este)) {Mover(Este) res := nroBolitas(Azul) > 0}return (res)}function hayCarpetasHermanasSinRecorrer() {return (nroBolitas(Azul) > 1)}function hayCarpetasSuperioresSinRecorrer() {while (not esLaCarpetaRaízDelFS() && not hayCarpetasHermanasSinRecorrer()) {IrACarpetaSuperior()}return(hayCarpetasHermanasSinRecorrer())}procedure IrACarpetaSuperior() {while (not esPrimeraCarpeta()) {IrACarpetaHermanaAnterior()}Mover(Oeste)}procedure IrACarpetaHermanaSiguiente() {Mover(Sur)while(not hayBolitas(Azul)) {Mover(Sur)}}procedure IrACarpetaHermanaAnterior() {Mover(Norte)while(not hayBolitas(Azul)) {Mover(Norte)}}function esLaCarpetaRaízDelFS() {return(not puedeMover(Norte) && not puedeMover(Oeste))}function esPrimeraCarpeta() {Mover(Oeste)return(hayBolitas(Azul))}",
  "base":'''program {
  PROCEDIMIENTO1()
}

procedure PROCEDIMIENTO1() {
  /*
    Propósito: ?
    Precondiciones: ?
    Observaciones: Es un recorrido de procesamiento sobre
      las carpetas del FS, actualizando la fecha de los
      archivos en cada carpeta.
  */
  // Ir al primer elemento
  while(/* quedan elementos por recorrer */) {
    PROCEDIMIENTO2()
    // Pasar al siguiente elemento
  }
  PROCEDIMIENTO2()
}

procedure PROCEDIMIENTO2() {
  /*
    Propósito: ?
    Precondiciones: ?
    Observaciones: Es un recorrido de procesamiento sobre
      los archivos de la carpeta actual, actualizando la
      fecha de cada uno.
  */
  // Ir al primer elemento
  while(/* quedan elementos por recorrer */) {
    // Procesar elemento actual
    // Pasar al siguiente elemento
  }
  // Procesar último elemento (caso de borde)
}''',
  "run_data":[{
    "tablero":{"head":[3,2],"width":6,"height":6,"board":iniFs},
    "post":{"head":[],"width":6,"height":6,"board":abrirArchivosB(iniFs)}
  }],
  "pidePrograma": True
}

superGobi64_1 = {
  "id":"SuperGobi64_1",
  "nombre":"Súper Gobi 64 - Parte 1",
  "enunciado":"-",
  "pre":"program{IrAGobi()}procedure Subir() {}procedure Bajar() {}function puedeSubir() {return(False)}function puedeBajar() {return(False)}function estáGobi() {return(True)}function estáGobiEnEstePiso() {return(True)}procedure IrAPrimeraCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {}function haySiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {return(False)}procedure PasarASiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {}"
}

rutera_1 = {
  "id":"Rutera1",
  "nombre":"Rutera - parte 1",
  "enunciado":"-",
  "pre":"program{ConstruirSegmentoDeRuta()}function hayEdificioAl_(d) {h := False;if (puedeMover(d)) {Mover(d)h := hayBolitas(Negro)}return (h)}",
  "run_data":[{
    "tablero":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
    "post":{"head":[0,0],"width":1,"height":1,"board":[[r]]},
  },{
    "tablero":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(2)],[ns(2),ns(2)]]},
    "post":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(1),ns(2)],[ns(2),ns(2)]]},
  }],
  "mostrar":False
}

rutera_2 = {
  "id":"Rutera2",
  "nombre":"Rutera - parte 2",
  "enunciado":"-",
  "pre":"program{ConstruirSegmentoDeRuta()}function cantidadDeEdificiosAl_(d){h := 0;if (puedeMover(d)) {Mover(d)h := nroBolitas(Negro)}return(h)}",
  "run_data":[{
    "tablero":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
    "post":{"head":[0,0],"width":1,"height":1,"board":[[r]]},
  },{
    "tablero":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(1)],[v,ns(2)]]},
    "post":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[r,ns(1)],[v,ns(2)]]},
  },{
    "tablero":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,v],[ns(1),ns(2)]]},
    "post":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[r,v],[ns(1),ns(2)]]},
  },{
    "tablero":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(1)],[ns(1),ns(2)]]},
    "post":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(1),ns(1)],[ns(1),ns(2)]]},
  },{
    "tablero":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(2)],[ns(2),ns(2)]]},
    "post":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(2),ns(2)],[ns(2),ns(2)]]},
  }],
  "mostrar":False
}

p_3_4 = {
  "id":"P34",
  "nombre":"Presente 3/4",
  "enunciado":"El ejercicio 5 de la práctica 4 pero permitiendo que la palabra no comience sobre el borde Oeste.",
  "pre":"program {PasarPalabraActualAMayúsculas()}",
  "run_data":[{
    "tablero":{"head":[1,0],"width":4,"height":2,"board":[[v,v],[rs(2),v],[ns(103),v],[ns(98),v]]},
    "post":{"head":[1,0],"width":4,"height":2,"board":[[v,v],[rs(2),v],[ns(103),ns(71)],[ns(98),ns(66)]]},
  },{
    "tablero":{"head":[1,0],"width":5,"height":2,"board":[[v,v],[rs(3),v],[ns(98),v],[ns(103),v],[ns(98),v]]},
    "post":{"head":[1,0],"width":5,"height":2,"board":[[v,v],[rs(3),v],[ns(98),ns(66)],[ns(103),ns(71)],[ns(98),ns(66)]]},
  }],
  "mostrar":False
}

p_30_3 = {
  "id":"P303",
  "nombre":"Presente 30/3",
  "enunciado":"Escribir un programa que construya una ciudad escalera de tamaño 3 desde la celda actual hacia el Oeste. El cabezal debe finalizar sobre el edificio más alto de la ciudad construida.\n\nUna ciudad es sólo una hilera de edificios consecutivos y su tamaño es la cantidad de edificios que tiene. Decimos que una ciudad es \"escalera\" si al recorrerla de Oeste a Este, el primero de sus edificios tiene dos pisos de altura y cada uno de los demás tiene un piso de altura más que el edificio anterior.\n\nCada edificio ocupa una celda del tablero y se representa con una bolita verde y tantas bolitas rojas como pisos este tenga.",
  "pre":"",
  "run_data":[{
    "tablero":{"head":[3,1],"width":5,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v]]},
    "post":{"head":[3,1],"width":5,"height":3,"board":[[v,v,v],[v,ed(2),v],[v,ed(3),v],[v,ed(4),v],[v,v,v]]},
  }],
  "pidePrograma": True,
  "mostrar":False
}

ajedrez_1 = {
  "id":"Ajedrez_1",
  "nombre":"Ajedrez - Parte 1",
  "enunciado":"Suponiendo que se encuentran definidos los procedimientos PintarBlanco y PintarNegro que pintan la celda actual de blanco y de negro respectivamente, escribir el procedimiento PintarTableroDeAjedrez que, suponiendo que el tablero tiene exactamente 8 filas y 8 columnas, pinte todo el tablero como un tablero de ajedrez. Tener en cuenta que este procedimiento debe funcionar sin importar la ubicación inicial del cabezal y no se pide que este finalice en alguna ubicación en particular",
  "pre":"procedure PintarBlanco(){Poner(Rojo)}\nprocedure PintarNegro(){Poner(Azul)}\nprogram {PintarTableroDeAjedrez()}",
  "run_data":[{
    "tablero":{"head":[5,6],"width":8,"height":8,"board":[[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v]]},
    "post":{"head":[],"width":8,"height":8,"board":[[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a]]},
  }]
}

rosa_de_los_vientos = {
  "id":"RosaVientos",
  "nombre":"Rosa de los vientos",
  "enunciado":"Escribir el procedimiento PonerRosaDeLosVientos que ponga un rosa de los vientos al rededor de la celda actual. Para representar una rosa de los vientos centrada en una celda hay que poner una bolita roja en cada una de las cuatro celdas lindantes.",
  "run_data":[{
    "tablero":{"head":[1,1],"width":3,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v]]},
    "post":{"head":[1,1],"width":3,"height":3,"board":[[v,r,v],[r,v,r],[v,r,v]]},
  }]
}

CURSOS = {
  "inpr_unq_2023_s1":{
    "nombre":"Introducción a la Programación - UNQ (2023s1)",
    "anio":"2023",
    "edicion":"Primer Semestre",
    "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Informática, Tecnicatura en Programación Informática y Licenciatura en Bioinformática de la Universidad Nacional de Quilmes",
    "responsable":{
      "nombre":"Equipo de Intro",
      "contacto":"tpi-doc-inpr (AT) listas.unq.edu.ar"
    },
    "institucion":"Universidad Nacional de Quilmes (UNQ)",
    "lenguaje":"Gobstones",
    "lenguaje_display":"none",
    "ejs":[superGobi64_2,gobFS_1,superGobi64_1,rutera_1,rutera_2,p_3_4,p_30_3,ajedrez_1]
  },
  "inpr_unq_2024_s1":{
    "nombre":"Introducción a la Programación - UNQ (2024s1)",
    "anio":"2024",
    "edicion":"Primer Semestre",
    "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Informática, Tecnicatura en Programación Informática y Licenciatura en Bioinformática de la Universidad Nacional de Quilmes",
    "responsable":{
      "nombre":"Equipo de Intro",
      "contacto":"tpi-doc-inpr (AT) listas.unq.edu.ar"
    },
    "institucion":"Universidad Nacional de Quilmes (UNQ)",
    "lenguaje":"Gobstones",
    "lenguaje_display":"none",
    "ejs":[rosa_de_los_vientos,ajedrez_1]
  }
}