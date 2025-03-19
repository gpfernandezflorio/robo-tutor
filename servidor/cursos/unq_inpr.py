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
def g(z): # Gobi
  return {"a": z, "r": 0, "n": 0, "v": 0}
def gobiData(t,a): # Data de Gobi con t pisos totales y piso actual a
  return {"a": 0, "r": t, "n": 0, "v": a}
def iniGobi_2_3(a,z): # Tablero inicial Gobi de 4x4x4 en piso a (con Gobi en 2-3-z)
  return [[gobiData(4,a),v,v,v],[v,v,v,v],[v,v,v,g(z)],[v,v,v,v]]
def iniGobi_0_1(a,z): # Tablero inicial Gobi de 4x4x4 en piso a (con Gobi en 0-1-z)
  return [[gobiData(4,a),g(z),v,v],[v,v,v,v],[v,v,v,v],[v,v,v,v]]
def iniGobi_2(a): # Tablero inicial Gobi de 6x6x4 en piso a (sin Gobi, sólo enemigos)
  return [[gobiData(4,a),v,e(2,1),v,e(3,7),v],[v,v,e(2,5),v,e(2,8),e(3,6)],[v,e(2,4),v,e(2,4),e(3,4),v],[e(3,6),e(2,6),e(2,2),e(2,5),e(3,10),e(2,3)],[v,v,e(2,4),e(2,1),e(3,5),v],[v,v,e(2,3),e(3,6),e(2,8),e(3,5)]]

'''
    head: [columna, fila]
    board: [col0, col1, ... coln]
        coli: [celda0, celda1, ... celdan]
            celdai: {a: , n: , r: , v: }
'''

'''
  Gobi:
    En la celda 0-0, con bolitas verdes el piso actual y con rojas el piso máximo.
    Cada personaje se representa en un celda con tantas bolitas azules como el piso en el que se encuentra.
    La cantidad de bolitas negras determina el personaje. Si es 0 es Gobi si no, un enemigo cuyo nivel es la cantidad de bolitas negras y su color es ese número módulo 4.
'''
def superGobi64_1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"SuperGobi64_1",
    "nombre":"Súper Gobi 64 - Parte 1",
    "enunciado":"En el popular videojuego Súper Gobi 64 controlamos a Gobi en un escenario 3D. Vamos a programar este videojuego en Gobstones. Para ello, un grupo de ingenieros logró implementar una ingeniosa representación de un tablero 3D sobre el tablero 2D de Gobstones. En esta representación contamos con varios tableros de Gobstones llamados pisos. Obviamente esa represetanción es súper secreta así que no podemos verla pero podemos trabajar con las primitivas de representación. Además del comando Mover, que permite mover el cabezal sobre el plano, tenemos dispoibles Subir y Bajar que mueven el cabezal hacia arriba y hacia abajo, respectivamente. De forma análoga, se agregan puedeSubir y puedeBajar que funcionan como puedeMover pero para arriba y abajo, respectivamente. Tampoco sabemos cómo se representa Gobi pero tenemos disponibles las funciones estáGobiAcá y estáGobiEnEstePiso. Implementar el procedimiento IrAGobi que posicione el cabezal sobre Gobi.",
    "pre":"program{IrAGobi()}procedure Subir() {if (not puedeSubir()) {BOOM(\"No se puede subir más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Poner(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}procedure Bajar() {if (not puedeBajar()) {BOOM(\"No se puede bajar más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Sacar(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}function puedeSubir() {return(aux_pisoActual()<aux_pisoMaximo())}function puedeBajar() {return(aux_pisoActual()>1)}function estáGobiAcá() {return(nroBolitas(Azul)==aux_pisoActual() && not hayBolitas(Negro))}function aux_x() {x:=0;while(puedeMover(Oeste)) {Mover(Oeste)x:=x+1}return(x)}function aux_y() {y:=0;while(puedeMover(Sur)) {Mover(Sur)y:=y+1}return(y)}function aux_pisoActual() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Verde))}function aux_pisoMaximo() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Rojo))}function estáGobiEnEstePiso() {IrAPrimeraCeldaEnRecorridoAl_YAl_(Norte, Este);while(haySiguienteCeldaEnRecorridoAl_YAl_(Norte, Este) && !estáGobiAcá()) {PasarASiguienteCeldaEnRecorridoAl_YAl_(Norte, Este)}return(estáGobiAcá())}procedure IrAPrimeraCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {IrAlBorde(opuesto(dirPrincipal));IrAlBorde(opuesto(dirSecundaria))}function haySiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {return(puedeMover(dirPrincipal)||puedeMover(dirSecundaria))}procedure PasarASiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {if (puedeMover(dirPrincipal)) {Mover(dirPrincipal)} else {IrAlBorde(opuesto(dirPrincipal));Mover(dirSecundaria)}}",
    "run_data":[{
      "t0":{"head":[2,2],"width":4,"height":4,"board":iniGobi_2_3(1,1)},
      "tf":{"head":[2,3],"width":4,"height":4,"board":iniGobi_2_3(1,1)}
    },{
      "t0":{"head":[3,0],"width":4,"height":4,"board":iniGobi_2_3(3,2)},
      "tf":{"head":[2,3],"width":4,"height":4,"board":iniGobi_2_3(2,2)}
    },{
      "t0":{"head":[3,0],"width":4,"height":4,"board":iniGobi_0_1(3,2)},
      "tf":{"head":[0,1],"width":4,"height":4,"board":iniGobi_0_1(2,2)}
    },{
      "t0":{"head":[1,0],"width":4,"height":4,"board":iniGobi_0_1(1,3)},
      "tf":{"head":[0,1],"width":4,"height":4,"board":iniGobi_0_1(3,3)}
    }],
    "disponible":{"desde":fecha}
  }

def superGobi64_2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"SuperGobi64_2",
    "nombre":"Súper Gobi 64 - Parte 2",
    "enunciado":"En el ejercicio anterior mencionamos que, además de Gobi, en el tablero 3D hay enemigos. Cada enemigo tiene un color y nivel de poder. Algunos de estos enemigos son jefes. Para completar un nivel, Gobi debe derrotar a todos los jefes. Escribir la función cantidadDeJefesEnEstePiso que describe la cantidad de jefes que hay en el piso actual. Los jefes son aquellos enemigos que tienen al menos un minion de cada color. Los minions también son enemigos pero para que un enemigo sea minion de un jefe tiene que pasar que su poder sea menor, que estén en el mismo piso y que estén en la misma fila o en la misma columna. Notar que un mismo enemigo puede ser minion de más de un jefe y que los jefes pueden a su vez ser minions de otros jefes más fuertes. Además de todas las primitivas dadas en el ejercico anterior se cuenta también con hayEnemigo, poderDelEnemigo y colorDelEnemigo.",
    "pre":"program {repeat(cantidadDeJefesEnEstePiso()){Poner(Rojo)}}procedure Subir() {if (not puedeSubir()) {BOOM(\"No se puede subir más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Poner(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}procedure Bajar() {if (not puedeBajar()) {BOOM(\"No se puede bajar más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Sacar(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}function puedeSubir() {return(aux_pisoActual()<aux_pisoMaximo())}function puedeBajar() {return(aux_pisoActual()>1)}function estáGobiAcá() {return(nroBolitas(Azul)==aux_pisoActual() && not hayBolitas(Negro))}function hayEnemigo() {return(nroBolitas(Azul)==aux_pisoActual() && hayBolitas(Negro))}function poderDelEnemigo() {if (not hayBolitas(Negro) ||nroBolitas(Azul)/=aux_pisoActual() ) {BOOM(\"No hay enemigo aquí\")}return(nroBolitas(Negro))}function colorDelEnemigo() {if (not hayBolitas(Negro) ||nroBolitas(Azul)/=aux_pisoActual() ) {BOOM(\"No hay enemigo aquí\")}return(choose Rojo when (nroBolitas(Negro) mod 4 == 1) Azul when (nroBolitas(Negro) mod 4 == 2) Negro when (nroBolitas(Negro) mod 4 == 3) Verde otherwise)}function aux_x() {x:=0;while(puedeMover(Oeste)) {Mover(Oeste)x:=x+1}return(x)}function aux_y() {y:=0;while(puedeMover(Sur)) {Mover(Sur)y:=y+1}return(y)}function aux_pisoActual() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Verde))}function aux_pisoMaximo() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Rojo))}",
    "run_data":[{
      "t0":{"head":[3,2],"width":6,"height":6,"board":iniGobi_2(2)},
      "tf":{"head":[3,2],"width":6,"height":6,"board":agregarRojas(iniGobi_2(2),3)}
    },{
      "t0":{"head":[3,2],"width":6,"height":6,"board":iniGobi_2(3)},
      "tf":{"head":[3,2],"width":6,"height":6,"board":agregarRojas(iniGobi_2(3),1)}
    }],
    "disponible":{"desde":fecha}
  }

def gobFS_1(fecha):
  return {
    "tipo":"CODIGO",
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
      "t0":{"head":[3,2],"width":6,"height":6,"board":iniFs},
      "tf":{"head":[],"width":6,"height":6,"board":abrirArchivosB(iniFs)}
    }],
    "pidePrograma": True,
    "disponible":{"desde":fecha}
  }

def rutera_1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Rutera1",
    "nombre":"Rutera - parte 1",
    "enunciado":"La empresa de construcción Rutera S.A. estaba encargada de construir una ruta que cruzara el país de Este a Oeste. Como la presidenta de la compañía aprobó Intro decidió que la construcción siga el esquema top-down y comenzó implementando el procedimiento ContruirRutaHaciaEl_DeLargo_. Sin embargo, al hacer división en subtareas, no pudieron realizar el procedimiento ConstruirSegmentoDeRuta que construye en la celda actual un segmento de ruta. El problema con el que se encontraron es que desde el ministerio les solicitaron que aquellos segmentos que transiten por ciudades tuvieran un lomo de burro. Ayudar a Rutera escribiendo el procedimiento que les falta teniendo en cuenta que un segmento de ruta se representa con una bolita roja y un lomo de burro se representa con dos bolitas verdes. Decimos que un segmento de ruta transita por una ciudad si hay al menos un edificio en alguna de las celdas lindantes a la celda del segmento en cuestión. Para esto se puede utilizar la función primitiva hayEdificioAl_ que dada una dirección indica si hay una celda lindante con algún edificio en dicha dirección.",
    "pre":"program{ConstruirSegmentoDeRuta()}function hayEdificioAl_(d) {h := False;if (puedeMover(d)) {Mover(d)h := hayBolitas(Negro)}return (h)}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[r]]},
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(2)],[ns(2),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(1),ns(2)],[ns(2),ns(2)]]},
    }],
    "disponible":{"desde":fecha}
  }

def rutera_2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Rutera2",
    "nombre":"Rutera - parte 2",
    "enunciado":"El ministerio decidió cambiar la reglamentación y ahora es necesario que en cada segmento haya un lomo de burro por cada dos edificios que dicho segmento atraviesa. Reescribir el procedimiento ConstruirSegmentoDeRuta para que cumpla la nueva reglamentación. Recordar que un segmento de ruta se representa con una bolita roja y un lomo de burro se representa con dos bolitas verdes. La función primitiva ahora es cantidadDeEdificiosAl_ que dada una dirección describe la cantidad de edificios lindantes (es decir, que están en una celda a distancia uno) en dicha dirección.",
    "pre":"program{ConstruirSegmentoDeRuta()}function cantidadDeEdificiosAl_(d){h := 0;if (puedeMover(d)) {Mover(d)h := nroBolitas(Negro)}return(h)}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[r]]},
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(1)],[v,ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[r,ns(1)],[v,ns(2)]]},
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,v],[ns(1),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[r,v],[ns(1),ns(2)]]},
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(1)],[ns(1),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(1),ns(1)],[ns(1),ns(2)]]},
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(2)],[ns(2),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(2),ns(2)],[ns(2),ns(2)]]},
    }],
    "disponible":{"desde":fecha}
  }

def mayusculas_recargado(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Mayusculas",
    "nombre":"Aprendiendo a leer y escribir, recargado",
    "enunciado":"El ejercicio \"Aprendiendo a leer y escribir\" pero sin suponer que la palabra comienza sobre el borde Oeste (podría comenzar en cualquier celda).",
    "pre":"program {PasarPalabraActualAMayúsculas()}",
    "run_data":[{
      "t0":{"head":[1,0],"width":4,"height":2,"board":[[v,v],[rs(2),v],[ns(103),v],[ns(98),v]]},
      "tf":{"head":[1,0],"width":4,"height":2,"board":[[v,v],[rs(2),v],[ns(103),ns(71)],[ns(98),ns(66)]]},
    },{
      "t0":{"head":[1,0],"width":5,"height":2,"board":[[v,v],[rs(3),v],[ns(98),v],[ns(103),v],[ns(98),v]]},
      "tf":{"head":[1,0],"width":5,"height":2,"board":[[v,v],[rs(3),v],[ns(98),ns(66)],[ns(103),ns(71)],[ns(98),ns(66)]]},
    }],
    "disponible":{"desde":fecha}
  }

def escalera_1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Escalera_1",
    "nombre":"Ciudad Escalera - Parte 1",
    "enunciado":"Escribir un programa que construya una ciudad escalera de tamaño 3 desde la celda actual hacia el Oeste. El cabezal debe finalizar sobre el edificio más alto de la ciudad construida.\n\nUna ciudad es sólo una hilera de edificios consecutivos y su tamaño es la cantidad de edificios que tiene. Decimos que una ciudad es \"escalera\" si al recorrerla de Oeste a Este, el primero de sus edificios tiene dos pisos de altura y cada uno de los demás tiene un piso de altura más que el edificio anterior.\n\nCada edificio ocupa una celda del tablero y se representa con una bolita verde y tantas bolitas rojas como pisos este tenga.",
    "pre":"",
    "run_data":[{
      "t0":{"head":[3,1],"width":5,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v]]},
      "tf":{"head":[3,1],"width":5,"height":3,"board":[[v,v,v],[v,ed(2),v],[v,ed(3),v],[v,ed(4),v],[v,v,v]]},
    }],
    "pidePrograma": True,
    "disponible":{"desde":fecha}
  }

def ajedrez_1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"Ajedrez_1",
    "nombre":"Ajedrez - Parte 1",
    "enunciado":"Suponiendo que se encuentran definidos los procedimientos PintarBlanco y PintarNegro que pintan la celda actual de blanco y de negro respectivamente, escribir el procedimiento PintarTableroDeAjedrez que, suponiendo que el tablero tiene exactamente 8 filas y 8 columnas, pinte todo el tablero como un tablero de ajedrez. Tener en cuenta que este procedimiento debe funcionar sin importar la ubicación inicial del cabezal y no se pide que este finalice en alguna ubicación en particular",
    "pre":"procedure PintarBlanco(){Poner(Rojo)}\nprocedure PintarNegro(){Poner(Azul)}\nprogram {PintarTableroDeAjedrez()}",
    "run_data":[{
      "t0":{"head":[5,6],"width":8,"height":8,"board":[[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v],[v,v,v,v,v,v,v,v]]},
      "tf":{"head":[],"width":8,"height":8,"board":[[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a]]},
    }],
    "disponible":{"desde":fecha}
  }

def rosa_de_los_vientos(fecha):
  return {
    "tipo":"CODIGO",
    "id":"RosaVientos",
    "nombre":"Rosa de los vientos",
    "enunciado":"Escribir el procedimiento PonerRosaDeLosVientos que ponga un rosa de los vientos al rededor de la celda actual. Para representar una rosa de los vientos centrada en una celda hay que poner una bolita roja en cada una de las cuatro celdas lindantes.",
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[v,r,v],[r,v,r],[v,r,v]]},
    }],
    "disponible":{"desde":fecha}
  }

CURSOS = {
  "inpr_unq_2025_s1":{
    "nombre":"Introducción a la Programación - UNQ (2025s1)",
    "anio":"2025",
    "edicion":"Primer Semestre",
    "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Informática, Tecnicatura en Programación Informática y Licenciatura en Bioinformática de la Universidad Nacional de Quilmes",
    "responsable":{
      "nombre":"Equipo de Intro",
      "contacto":"tpi-doc-inpr (AT) listas.unq.edu.ar"
    },
    "institucion":"Universidad Nacional de Quilmes (UNQ)",
    "lenguaje":"Gobstones",
    "lenguaje_display":"none",
    "actividades":[
      rosa_de_los_vientos("21/3/2025"),
      ajedrez_1("28/3/2025"),
      escalera_1("4/4/2025"),
      mayusculas_recargado("11/4/2025"),
      rutera_1("18/4/2025"),
      rutera_2("18/4/2025"),
      superGobi64_1("25/4/2025"),
      gobFS_1("2/5/2025"),
      superGobi64_2("9/5/2025")
    ],
    "planilla":{
      "url":"1FAIpQLSeJRA1urVZ81AhWS73Z66G0p_hAujXLR6hirdc3cVq3LuKAtw",
      "campos":{
        "usuario":"9867257",
        "actividad":"1165966175",
        "respuesta":"1778184894",
        "resultado":"1496208069",
        "duracion":"1460244707"
      }
    }
  }
  # ,
  # "inpr_unq_2023_s1":{
  #   "nombre":"Introducción a la Programación - UNQ (2023s1)",
  #   "anio":"2023",
  #   "edicion":"Primer Semestre",
  #   "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Informática, Tecnicatura en Programación Informática y Licenciatura en Bioinformática de la Universidad Nacional de Quilmes",
  #   "responsable":{
  #     "nombre":"Equipo de Intro",
  #     "contacto":"tpi-doc-inpr (AT) listas.unq.edu.ar"
  #   },
  #   "institucion":"Universidad Nacional de Quilmes (UNQ)",
  #   "lenguaje":"Gobstones",
  #   "lenguaje_display":"none",
  #   "actividades":[superGobi64_2,gobFS_1,superGobi64_1,rutera_1,rutera_2,p_3_4,p_30_3,ajedrez_1],
  #   "planilla":{
  #     "url":"1FAIpQLScHNF1TFEZrcSLNLYbxxFOHIVPyml9dpZTpqJ_WJSqGPanOAw",
  #     "campos":{
  #       "usuario":"1115080072",
  #       "actividad":"1084236439",
  #       "respuesta":"256509475",
  #       "resultado":"236721452",
  #       "duracion":"1133020774"
  #     }
  #   }
  # },
  # "inpr_unq_2024_s1":{
  #   "nombre":"Introducción a la Programación - UNQ (2024s1)",
  #   "anio":"2024",
  #   "edicion":"Primer Semestre",
  #   "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Informática, Tecnicatura en Programación Informática y Licenciatura en Bioinformática de la Universidad Nacional de Quilmes",
  #   "responsable":{
  #     "nombre":"Equipo de Intro",
  #     "contacto":"tpi-doc-inpr (AT) listas.unq.edu.ar"
  #   },
  #   "institucion":"Universidad Nacional de Quilmes (UNQ)",
  #   "lenguaje":"Gobstones",
  #   "lenguaje_display":"none",
  #   "actividades":[rosa_de_los_vientos,ajedrez_1]
  # }
}