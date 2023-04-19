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
def fs(h,a): # Carpeta del FS con h hermanas siguientes y a archivos
    return {"a": h+1, "r": a, "n": 0, "v": 0}
def abrirArchivosB(b):
    return list(map(abrirArchivosC, b))
def abrirArchivosC(c):
    return list(map(lambda x: {"a": x["a"], "r": x["r"], "n": 0, "v": x["r"]}, c))
iniFs = [[v,v,v,v,v,fs(0,2)],[fs(0,2),fs(1,3),v,v,fs(2,1),fs(3,4)],[v,fs(0,3),fs(0,8),fs(1,3),fs(2,4),fs(0,2)],[v,fs(0,4),v,fs(0,2),v,v],[v,v,fs(0,1),fs(1,4),v,v],[v,v,v,v,v,v]]

'''
    head: [columna, fila]
    board: [col0, col1, ... coln]
        coli: [celda0, celda1, ... celdan]
'''

def dame_cursos(verb):
    return {"cursos":{
        "inpr_unq_2023_s1":{
            "nombre":"Introducción a la Programación - UNQ (2023s1)",
            "lenguaje":"Gobstones",
            "lenguaje_display":"none",
            "ejs":[
              {
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
              },{
                "nombre":"Súper Gobi 64 - Parte 1",
                "enunciado":"-",
                "pre":"program{IrAGobi()}procedure Subir() {}procedure Bajar() {}function puedeSubir() {return(False)}function puedeBajar() {return(False)}function estáGobi() {return(True)}function estáGobiEnEstePiso() {return(True)}procedure IrAPrimeraCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {}function haySiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {return(False)}procedure PasarASiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {}"
              },{
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
              },{
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
              },{
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
              },{
                "nombre":"Presente 30/3",
                "enunciado":"Escribir un programa que construya una ciudad escalera de tamaño 3 desde la celda actual hacia el Oeste. El cabezal debe finalizar sobre el edificio más alto de la ciudad construida.\n\nUna ciudad es sólo una hilera de edificios consecutivos y su tamaño es la cantidad de edificios que tiene. Decimos que una ciudad es \"escalera\" si al recorrerla de Oeste a Este, el primero de sus edificios tiene dos pisos de altura y cada uno de los demás tiene un piso de altura más que el edificio anterior.\n\nCada edificio ocupa una celda del tablero y se representa con una bolita verde y tantas bolitas rojas como pisos este tenga.",
                "pre":"",
                "run_data":[{
                  "tablero":{"head":[3,1],"width":5,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v]]},
                  "post":{"head":[3,1],"width":5,"height":3,"board":[[v,v,v],[v,ed(2),v],[v,ed(3),v],[v,ed(4),v],[v,v,v]]},
                }],
                "pidePrograma": True,
                "mostrar":False
              },{
                "nombre":"Presente 27/3",
                "enunciado":"Suponiendo que se encuentran definidos los procedimientos PintarBlanco y PintarNegro que pintan la celda actual de blanco y de negro respectivamente, escribir el procedimiento PintarTableroDeAjedrez que, suponiendo que el tablero tiene exactamente 8 filas y 8 columnas, pinte todo el tablero como un tablero de ajedrez. Tener en cuenta que este procedimiento debe funcionar sin importar la ubicación inicial del cabezal y no se pide que este finalice en alguna ubicación en particular",
                "pre":"procedure PintarBlanco(){Poner(Rojo)}\nprocedure PintarNegro(){Poner(Azul)}\nprogram {PintarTableroDeAjedrez()}",
                "run_data":[{
                  "tablero":{"head":[5,6],"width":8,"height":8,"board":[[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v]]},
                  "post":{"head":[],"width":8,"height":8,"board":[[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a]]},
                }],
                "mostrar":False
              }
            ]
          }
        }
    }
