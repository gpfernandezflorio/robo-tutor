# -*- coding: utf-8 -*-

from utils import rutaAlServidor

v = {"a": 0, "n": 0, "r": 0, "v": 0} # Celda vacía
r = {"a": 0, "n": 0, "r": 1, "v": 0} # Celda con una roja
a = {"a": 1, "n": 0, "r": 0, "v": 0} # Celda con una azul
g = {"a": 0, "n": 0, "r": 0, "v": 1} # Celda con una verde (no puedo usar 'v' porque ya la usé para la celda vacía)
n = {"a": 0, "n": 1, "r": 0, "v": 0} # Celda con una negra
def c(a,n,r,v): # celda con ...
  return {"a": a, "n": n, "r": r, "v": v}
def a_s(x): # Celda con varias azules
  return c(x,0,0,0)
def ns(x): # Celda con varias negras
  return c(0,x,0,0)
def rs(x): # Celda con varias rojas
  return c(0,0,x,0)
def gs(x): # Celda con varias verdes
  return c(0,0,0,x)
def ed(h,d=0,a=0): # Edificio con h pisos, d departamentos por piso y a ambientes por departamento
  return c(0,0,h,1)
def rt(l): # Ruta con l lomos de burro
  return c(0,0,1,2*l)
def duplicarTablero(b):
  return list(map(lambda col: duplicarColumna(col), b))
def duplicarColumna(col):
  return list(map(lambda x: c(x["a"], x["n"], x["r"], x["v"]), col))
def fs(h,a): # Carpeta del FS con h hermanas siguientes y a archivos
  return c(h+1,0,a,0)
def abrirArchivosB(b):
  return list(map(abrirArchivosCol, b))
def abrirArchivosCol(col):
  return list(map(lambda x: c(x["a"], 0, x["r"], x["r"]), col))
iniFs = [[v,v,v,v,v,fs(0,2)],[fs(0,2),fs(1,3),v,v,fs(2,1),fs(3,4)],[v,fs(0,3),fs(0,8),fs(1,3),fs(2,4),fs(0,2)],[v,fs(0,4),v,fs(0,2),v,v],[v,v,fs(0,1),fs(1,4),v,v],[v,v,v,v,v,v]]
def agregarRojas(b,k):
  b2 = duplicarTablero(b)
  b2[3][2]["r"] = b2[3][2]["r"] + k
  return b2
def e(p,n): # Enemigo de Gobi en piso p de nivel n
  return c(p,n,0,0)
def gobi(z): # Gobi
  return c(z,0,0,0)
def gobiData(t,a): # Data de Gobi con t pisos totales y piso actual a
  return c(0,0,t,a)
def iniGobi_2_3(a,z): # Tablero inicial Gobi de 4x4x4 en piso a (con Gobi en 2-3-z)
  return [[gobiData(4,a),v,v,v],[v,v,v,v],[v,v,v,gobi(z)],[v,v,v,v]]
def iniGobi_0_1(a,z): # Tablero inicial Gobi de 4x4x4 en piso a (con Gobi en 0-1-z)
  return [[gobiData(4,a),gobi(z),v,v],[v,v,v,v],[v,v,v,v],[v,v,v,v]]
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

def ayuda(texto):
  return '<span style="color:blue;font-weight:bold;">' + texto + '</span>'
def resaltado(texto):
  return '<span style="color:red;font-weight:bold;">' + texto + '</span>'
enPapel = resaltado("EN PAPEL")
importante = resaltado("Importante")
recordar = resaltado("¡Recordar!")
biblioteca = ayuda("BIBLIOTECA")
pista = ayuda("PISTA")

def img(ruta):
  return "Ver imagen en <a href='https://aulas.gobstones.org/pluginfile.php/39068/mod_resource/content/18/P5.%20Expresiones%20y%20tipos.pdf' target='_blank'>la guía</a>."
  # return '<img src="'+rutaAlServidor()+'/servidor/cursos/unq_inpr/'+ruta+'"></img>'

def código(c):
  return '<div style="background-color:#eee;border:solid 2px black;padding:3px;font-weight:bold;"><code>' + c + '</code></div>'

def superGobi64_1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"SuperGobi64_1",
    "nombre":"Súper Gobi 64 - Parte 1",
    "enunciado":"En el popular videojuego Súper Gobi 64 controlamos a Gobi en un escenario 3D. Vamos a programar este videojuego en Gobstones. Para ello, un grupo de ingenieros logró implementar una ingeniosa representación de un tablero 3D sobre el tablero 2D de Gobstones. En esta representación contamos con varios tableros de Gobstones llamados pisos. Obviamente esa represetanción es súper secreta así que no podemos verla pero podemos trabajar con las primitivas de representación. Además del comando Mover, que permite mover el cabezal sobre el plano, tenemos dispoibles Subir y Bajar que mueven el cabezal hacia arriba y hacia abajo, respectivamente. De forma análoga, se agregan puedeSubir y puedeBajar que funcionan como puedeMover pero para arriba y abajo, respectivamente. Tampoco sabemos cómo se representa Gobi pero tenemos disponibles las funciones estáGobiAcá y estáGobiEnEstePiso. Implementar el procedimiento IrAGobi que posicione el cabezal sobre Gobi.",
    "pre":"program{IrAGobi()}procedure Subir() {if (not puedeSubir()) {BOOM(\"No se puede subir más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Poner(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}procedure Bajar() {if (not puedeBajar()) {BOOM(\"No se puede bajar más\")}x := aux_x();y := aux_y()IrAlBorde(Sur)IrAlBorde(Oeste)Sacar(Verde)repeat(x) { Mover(Este) }repeat(y) { Mover(Norte) }}function puedeSubir() {return(aux_pisoActual()<aux_pisoMaximo())}function puedeBajar() {return(aux_pisoActual()>1)}function estáGobiAcá() {return(nroBolitas(Azul)==aux_pisoActual() && not hayBolitas(Negro))}function aux_x() {x:=0;while(puedeMover(Oeste)) {Mover(Oeste)x:=x+1}return(x)}function aux_y() {y:=0;while(puedeMover(Sur)) {Mover(Sur)y:=y+1}return(y)}function aux_pisoActual() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Verde))}function aux_pisoMaximo() {IrAlBorde(Sur)IrAlBorde(Oeste)return(nroBolitas(Rojo))}function estáGobiEnEstePiso() {IrAPrimeraCeldaEnRecorridoAl_YAl_(Norte, Este);while(haySiguienteCeldaEnRecorridoAl_YAl_(Norte, Este) && not estáGobiAcá()) {PasarASiguienteCeldaEnRecorridoAl_YAl_(Norte, Este)}return(estáGobiAcá())}procedure IrAPrimeraCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {IrAlBorde(opuesto(dirPrincipal));IrAlBorde(opuesto(dirSecundaria))}function haySiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {return(puedeMover(dirPrincipal)||puedeMover(dirSecundaria))}procedure PasarASiguienteCeldaEnRecorridoAl_YAl_(dirPrincipal, dirSecundaria) {if (puedeMover(dirPrincipal)) {Mover(dirPrincipal)} else {IrAlBorde(opuesto(dirPrincipal));Mover(dirSecundaria)}}",
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
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[r]]}
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(2)],[ns(2),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(1),ns(2)],[ns(2),ns(2)]]}
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
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[r]]}
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(1)],[v,ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[r,ns(1)],[v,ns(2)]]}
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,v],[ns(1),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[r,v],[ns(1),ns(2)]]}
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(1)],[ns(1),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(1),ns(1)],[ns(1),ns(2)]]}
    },{
      "t0":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[v,ns(2)],[ns(2),ns(2)]]},
      "tf":{"head":[1,0],"width":3,"height":2,"board":[[v,v],[rt(2),ns(2)],[ns(2),ns(2)]]}
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
      "tf":{"head":[1,0],"width":4,"height":2,"board":[[v,v],[rs(2),v],[ns(103),ns(71)],[ns(98),ns(66)]]}
    },{
      "t0":{"head":[1,0],"width":5,"height":2,"board":[[v,v],[rs(3),v],[ns(98),v],[ns(103),v],[ns(98),v]]},
      "tf":{"head":[1,0],"width":5,"height":2,"board":[[v,v],[rs(3),v],[ns(98),ns(66)],[ns(103),ns(71)],[ns(98),ns(66)]]}
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
      "tf":{"head":[3,1],"width":5,"height":3,"board":[[v,v,v],[v,ed(2),v],[v,ed(3),v],[v,ed(4),v],[v,v,v]]}
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
      "tf":{"head":[],"width":8,"height":8,"board":[[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a],[a,r,a,r,a,r,a,r],[r,a,r,a,r,a,r,a]]}
    }],
    "disponible":{"desde":fecha}
  }

def rosa_de_los_vientos(fecha):
  return {
    "tipo":"CODIGO",
    "id":"RosaVientos",
    "nombre":"Rosa de los vientos",
    "enunciado":"Escribir el procedimiento PonerRosaDeLosVientos que ponga una rosa de los vientos al rededor de la celda actual. Para representar una rosa de los vientos centrada en una celda hay que poner una bolita roja en cada una de las cuatro celdas lindantes.",
    "pre":"program {PonerRosaDeLosVientos()}",
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[v,r,v],[r,v,r],[v,r,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def rtas_opción_multiple_n(opciones, correcta):
  return rtas_opción_multiple_i(opciones, correcta-1)

def rtas_opción_multiple_i(opciones, correcta):
  resultado = []
  for i in range(len(opciones)):
    resultado.append({
      "texto":"<p>" + str(opciones[i][0]) + "</p>",
      # "devolucion":opciones[i][1],
      "puntaje":"1" if i==correcta else "0"
    })
  return resultado

def guia1_ej1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia1_ej1",
    "nombre":"1. Reemplazando bolitas",
    "enunciado":["Escribir un programa que reemplace",{"tex":"^1"}," una bolita de color Roja con otra de color Verde en la celda actual.<br><br>1: Por reemplazo nos referimos al efecto observado, aunque no exista ningún comando para hacer reemplazos directamente"],
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[r,v,v],[v,r,v],[v,a,v]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[r,v,v],[v,g,v],[v,a,v]]}
    },{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[r,v,v],[v,c(4,5,3,2),v],[v,a,v]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[r,v,v],[v,c(4,5,2,3),v],[v,a,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia1_ej2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia1_ej2",
    "nombre":"2. Moviendo bolitas",
    "enunciado":["Escribir un programa que mueva",{"tex":"^2"}," una bolita de color Negro de la celda actual a la celda vecina al Este, dejando el cabezal en la celda lindante al Este.<br><br>2: Nuevamente nos referimos al efecto observado."],
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[r,v,v],[v,c(4,5,3,2),a],[v,c(4,5,3,2),v]]},
      "tf":{"head":[2,1],"width":3,"height":3,"board":[[r,v,v],[v,c(4,4,3,2),a],[v,c(4,6,3,2),v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia1_ej3(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia1_ej3",
    "nombre":"3. Poniendo en vecinas",
    "enunciado":["Escribir un programa que ponga una bolita de color Azul en la celda vecina al Norte de la actual",{"tex":"^3"},"<br><br>3: ¿Qué sucede sí no aclaramos la posición final del cabezal? Debería quedar en la misma celda que donde comenzó."],
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[r,v,v],[v,c(4,5,3,2),c(4,5,3,2)],[v,a,v]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[r,v,v],[v,c(4,5,3,2),c(5,5,3,2)],[v,a,v]]}
    }],
    "disponible":{"desde":fecha}
  }

textos1_5 = [
  "(1) No es un propósito, sino una descripción del funcionamiento. Para ser un propósito no debe preocuparse de los estados intermedios, solamente de la transformación final.",
  "(2) Es un propósito incompleto ya que no establece los colores de las bolitas que se agregan. El propósito debe establecer con precisión la transformación esperada.",
  "(3) Es una enunciación correcta del propósito. El orden en que se agregan las bolitas es irrelevante, siempre que la celda actual finalice con una más de cada uno de los colores indicados.",
  "(4) Es un propósito incompleto, ya que no establece dónde se agregan las bolitas en cuestión. El propósito debe establecer con precisión la transformación esperada.",
  "(5) Es una forma incorrecta de indicar la transformación esperada. Utiliza un lenguaje que sugiere un pensamiento operacional (o sea, centrado en las acciones individuales antes que en la transformación esperada)."
]

def rtas1_5(correcta, devoluciones):
  opciones = []
  for i in range(5):
    opciones.append([textos1_5[i], devoluciones[i]])
  return rtas_opción_multiple_n(opciones, correcta)

def guia1_ej5(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"guia1_ej5",
    "nombre":"5. Analizando propósitos",
    "preguntas":[{
      "tipo":"SOLO_TEXTO",
      "titulo":"Enunciado",
      "pregunta":enPapel+" Dado el siguiente programa:"+código("program {<br>&nbsp;&nbsp;Poner(Verde)<br>&nbsp;&nbsp;Sacar(Verde)<br>&nbsp;&nbsp;Poner(Azul)<br>&nbsp;&nbsp;Poner(Rojo)<br>}")+"Diversos estudiantes realizaron propuestas para redactar su propósito, y también un profesor realizó explicaciones sobre cada una de estas propuestas. Asociar cada propuesta de propósito para el mismo (indicadas con las letras A, B, etc.) con la explicación que resulta correcta para dicha propuesta (indicadas con los números 1, 2, etc.)."
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"A",
      "pregunta":"Poner una bolita azul y luego una roja en la celda actual.",
      "respuestas":rtas1_5(5, ["","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"B",
      "pregunta":"Agregar una bolita azul y una roja.",
      "respuestas":rtas1_5(4, ["","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"C",
      "pregunta":"Pone una bolita verde y luego la saca, para a continuación poner una bolita azul y una roja.",
      "respuestas":rtas1_5(1, ["","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"D",
      "pregunta":"Agregar una bolita roja y una bolita azul en la celda actual.",
      "respuestas":rtas1_5(3, ["","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"E",
      "pregunta":"Agregar dos bolitas en la celda actual.",
      "respuestas":rtas1_5(2, ["","","","",""])
    }],
    "disponible":{"desde":fecha}
  }

def guia1_ej6a(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia1_ej6a",
    "nombre":"6. Cuadrados verdes (a)",
    "enunciado":["Escribir el siguiente programa:<br>uno que ponga un cuadrado",{"tex":"^4"}," de tamaño 3 con bolitas de color verde, con centro en la celda inicial (dejando el cabezal en dicha celda al finalizar).<br><br>4: Un cuadrado consiste en una secuencia de celdas que tienen al menos una bolita de un determinado color, y que se extienden de forma vertical la misma cantidad de celdas que en horizontal."],
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[g,g,g],[g,g,g],[g,g,g]]}
    },{
      "t0":{"head":[2,2],"width":4,"height":4,"board":[[v,v,g,v],[v,v,v,v],[a,v,v,v],[v,v,v,v]]},
      "tf":{"head":[2,2],"width":4,"height":4,"board":[[v,v,g,v],[v,g,g,g],[a,g,g,g],[v,g,g,g]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia1_ej6b(fecha):
  b = c(0,0,0,2) # Celda con dos bolitas verdes
  return {
    "tipo":"CODIGO",
    "id":"guia1_ej6b",
    "nombre":"6. Cuadrados verdes (b)",
    "enunciado":"Escribir el siguiente programa:<br>uno que saque un cuadrado de tamaño 3 con bolitas de color verde (saca una bolita de cada celda), siendo la celda inicial el centro del cuadrado, dejando el cabezal en dicha celda al finalizar.",
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[g,g,g],[g,g,g],[g,g,g]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v]]}
    },{
      "t0":{"head":[2,2],"width":4,"height":4,"board":[[v,v,g,v],[v,g,g,g],[a,g,g,g],[v,g,g,g]]},
      "tf":{"head":[2,2],"width":4,"height":4,"board":[[v,v,g,v],[v,v,v,v],[a,v,v,v],[v,v,v,v]]}
    },{
      "t0":{"head":[2,2],"width":4,"height":4,"board":[[v,v,g,v],[v,g,b,g],[a,g,g,g],[v,g,g,b]]},
      "tf":{"head":[2,2],"width":4,"height":4,"board":[[v,v,g,v],[v,v,g,v],[a,v,v,v],[v,v,v,g]]}
    }],
    "disponible":{"desde":fecha}
  }

textos1_8 = [
  "(1) Es una precondición incorrecta, pues al no establecer dónde debe ubicarse el cabezal hay tableros de ese tamaño que no sirven.",
  "(2) Es una precondición correcta, pues establece las condiciones mínimas necesarias para que el programa funcione, y define con precisión el conjunto de tableros iniciales que sirven.",
  "(3) Es otra forma de enunciar correctamente la precondición: todos los tableros del conjunto que la satisfacen sirven, y todos los que no la satisfacen no sirven. Sin embargo, especificar las dimensiones del tablero es innecesario, pues son las distancias a los bordes lo relevante para que el programa no falle.",
  "(4) Es una precondición correcta pero insuficiente, pues todos los tableros que la satisfacen sirven, pero hay muchos tableros que sirven que no la satisfacen.",
  "(5) Es una precondición insuficiente, pues es demasiado vaga y no permite determinar cuáles son los tableros que sirven.",
  "(6) No es una precondición, sino una aclaración. Una precondición debe hablar sobre los tableros iniciales y no sobre el dominio del problema.",
  "(7) No es una precondición, sino una explicación de la tarea. Una precondición debe hablar sobre los tableros iniciales y no sobre las características de lo que se va a realizar."
]

def rtas1_8(correcta, devoluciones):
  opciones = []
  for i in range(7):
    opciones.append([textos1_8[i], devoluciones[i]])
  return rtas_opción_multiple_n(opciones, correcta)

def guia1_ej8(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"guia1_ej8",
    "nombre":"8. Analizando precondiciones",
    "preguntas":[{
      "tipo":"SOLO_TEXTO",
      "titulo":"Enunciado",
      "pregunta":enPapel+" La solución propuesta por diversos estudiantes para el punto c. del ejercicio anterior (Poner un rectángulo de bolitas Negras cuyo tamaño sea 3 filas y 5 columnas, centrado en la celda actual.) fue corregida por los docentes. Sin embargo, las correcciones se mezclaron, y hay que juntar cada corrección con su precondición correspondiente."
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"A",
      "pregunta":"Debe haber al menos una celda al Norte y otra al Sur, y dos celdas al Este y otras dos al Oeste de la celda actual.",
      "respuestas":rtas1_8(2, ["","","","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"B",
      "pregunta":"El rectángulo va a representar a una ventana en el dibujo de una casa.",
      "respuestas":rtas1_8(6, ["","","","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"C",
      "pregunta":"El tablero debe tener 3 o más filas, y 5 o más columnas, y el cabezal debe estar al menos a una celda de distancia de los bordes Norte y Sur, y a dos celdas de distancia de los bordes Este y Oeste.",
      "respuestas":rtas1_8(3, ["","","","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"D",
      "pregunta":"Debe haber lugar suficiente en las direcciones adecuadas.",
      "respuestas":rtas1_8(5, ["","","","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"E",
      "pregunta":"Se van a colocar 35 bolitas de color Negro.",
      "respuestas":rtas1_8(7, ["","","","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"F",
      "pregunta":"El tablero debe tener 3 filas y 5 columnas y el cabezal estar ubicado en el centro del mismo.",
      "respuestas":rtas1_8(4, ["","","","","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"G",
      "pregunta":"El tablero debe ser de 3 filas por 5 columnas.",
      "respuestas":rtas1_8(1, ["","","","","","",""])
    }],
    "disponible":{"desde":fecha}
  }

def guia1_ej10(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia1_ej10",
    "nombre":"10. Arcoiris",
    "enunciado":enPapel+" Escribir un programa que ponga un \"arco iris\", poniendo una bolita Azul en la celda actual, una Negra en la celda siguiente al Este, una Roja en la siguiente al Este, y una Verde en la siguiente al Este, dejando el cabezal en la celda inicial.",
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":6,"height":3,"board":[[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v]]},
      "tf":{"head":[1,1],"width":6,"height":3,"board":[[v,v,v],[v,a,v],[v,n,v],[v,r,v],[v,g,v],[v,v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia1_ej11(fecha):
  u = c(1,1,1,1) # Celda con una de cada color
  return {
    "tipo":"CODIGO",
    "id":"guia1_ej11",
    "nombre":"11. Sacando un cuadrado",
    "enunciado":"Escriba un programa que saque del tablero un cuadrado multicolor de dos celdas de lado, donde la celda actual representa el vértice inferior izquierdo del mismo. Recuerde escribir primero el contrato del programa, y luego el código. Considere las siguientes preguntas como guía para escribir su programa:<br>&nbsp;a. ¿Qué hace el programa? (Determina el propósito del programa)<br>&nbsp;b. ¿Cuándo funciona tal cual se espera? (Determina la precondición del programa)<br>&nbsp;c. ¿Cómo lo hace? (Determina el código del programa)",
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":4,"height":4,"board":[[v,v,v,v],[v,u,u,v],[v,u,u,v],[v,v,v,v]]},
      "tf":{"head":[1,1],"width":4,"height":4,"board":[[v,v,v,v],[v,v,v,v],[v,v,v,v],[v,v,v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia1(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia1",
    "nombre":"Práctica 1 - Programas y Contratos",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(1, 38997, "25/P1.%20Programas%20y%20Contratos.pdf"),
      guia1_ej1(fechaInicio),
      guia1_ej2(fechaInicio),
      guia1_ej3(fechaInicio),
      guia1_ej5(fechaInicio),
      guia1_ej6a(fechaInicio),
      guia1_ej6b(fechaInicio),
      guia1_ej8(fechaInicio),
      guia1_ej10(fechaInicio),
      guia1_ej11(fechaInicio)
    ]
  }

def guia2_ej2a(fecha):
  b = c(0,1,1,0) # Celda con una negra y una roja
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej2a",
    "nombre":"2. Por arriba (a)",
    "enunciado":"Escribir un procedimiento DibujarRectánguloRojoYNegroDe5x3() cuyo contrato es el siguiente:"+código("procedure DibujarRectánguloRojoYNegroDe5x3()<br>&nbsp;/*<br>&nbsp;&nbsp;PROPÓSITO: Poner un rectángulo sólido de 5 celdas de ancho y 3 celdas de alto. Desde la celda actual hacia el Este y hacia el Norte.<br>&nbsp;&nbsp;PRECONDICIONES:<br>&nbsp;&nbsp;&nbsp;* Hay al menos 4 celdas al Este y 2 celdas al Norte de la celda actual.<br>&nbsp;&nbsp;&nbsp;* Las celdas contenidas en el rectángulo de 5x3 desde la celda actual hacia el Este y hacia el Norte están vacías.<br>&nbsp;*/")+importante+" La metodología a seguir que se debe aplicar es la siguiente. En primer lugar, pensar una estrategia; se sugiere pensar una estrategia que involucre poner líneas de 5 celdas de ancho. Luego se debe definir primero el contrato de un procedimiento llamado <code>DibujarLíneaRojaYNegraDeTamaño5HaciaElEste()</code> que exprese la subtarea sugerida. Para completar el ejercicio, se debe utilizar este procedimiento auxiliar en la codificación del procedimiento pedido, <code>DibujarRectánguloRojoYNegroDe5x3()</code>. El código del procedimiento auxiliar no es parte de este inciso, sino del siguiente.<br><br><b>Nota</b>: no incluir la definición del procedimiento <code>DibujarLíneaRojaYNegraDeTamaño5HaciaElEste()</code> al enviar este ejercicio.",
    "pre":"program{ DibujarRectánguloRojoYNegroDe5x3() }\nprocedure DibujarLíneaRojaYNegraDeTamaño5HaciaElEste() {\n  repeat(4){Poner(Rojo) Poner(Negro) Mover(Este)}\n  Poner(Rojo) Poner(Negro)\n  repeat(4) {Mover(Oeste)}}",
    "base":"procedure DibujarRectánguloRojoYNegroDe5x3() {\n  /*\n  PROPÓSITO: Poner un rectángulo sólido de 5 celdas de ancho y 3\n   celdas de alto. Desde la celda actual hacia el Este y hacia el Norte.\n  PRECONDICIONES:\n   * Hay al menos 4 celdas al Este y 2 celdas al Norte de la celda\n    actual.\n   * Las celdas contenidas en el rectángulo de 5x3 desde la celda\n    actual hacia el Este y hacia el Norte están vacías.\n  */\n  ",
    "run_data":[{
      "t0":{"head":[1,1],"width":7,"height":5,"board":[[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]]},
      "tf":{"head":[1,1],"width":7,"height":5,"board":[[v,v,v,v,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,v,v,v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej2b(fecha):
  b = c(0,1,1,0) # Celda con una negra y una roja
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej2b",
    "nombre":"2. Por arriba (b)",
    "enunciado":"Escribir el procedimiento <code>DibujarLíneaRojaYNegraDeTamaño5HaciaElEste()</code> que quedó pendiente del ítem anterior.<br>"+importante+" Para ello, se debe seguir la misma metodología que en el caso anterior: en primer lugar pensar una estrategia, luego definir los contratos de los procedimientos que expresan las subtareas, y por último codificar el procedimiento pedido usando dichas subtareas (sin su código). Se sugiere que la estrategia involucre a subtareas llamadas <code>PonerUnaNegraYUnaRoja()</code> y <code>Mover4VecesAlOeste()</code>.<br><br><b>Nota</b>: no incluir las definiciones de los procedimientos <code>PonerUnaNegraYUnaRoja()</code> y <code>Mover4VecesAlOeste()</code> al enviar este ejercicio.",
    "pre":"program{ DibujarRectánguloRojoYNegroDe5x3() }\nprocedure DibujarRectánguloRojoYNegroDe5x3() {\n  repeat(2){DibujarLíneaRojaYNegraDeTamaño5HaciaElEste() Mover(Norte)}\n  DibujarLíneaRojaYNegraDeTamaño5HaciaElEste()\n  repeat(2) {Mover(Sur)}}\nprocedure PonerUnaNegraYUnaRoja() {Poner(Negro) Poner(Rojo)}\nprocedure Mover4VecesAlOeste() {repeat(4) {Mover(Oeste)}}",
    "base":"procedure DibujarLíneaRojaYNegraDeTamaño5HaciaElEste() {\n  /*\n  PROPÓSITO: ...\n  PRECONDICIONES: ...\n  */\n  ",
    "run_data":[{
      "t0":{"head":[1,1],"width":7,"height":5,"board":[[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]]},
      "tf":{"head":[1,1],"width":7,"height":5,"board":[[v,v,v,v,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,v,v,v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej2c(fecha):
  b = c(0,1,1,0) # Celda con una negra y una roja
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej2c",
    "nombre":"2. Por arriba (c)",
    "enunciado":"Escribir los procedimientos <code>PonerUnaNegraYUnaRoja()</code> y <code>Mover4VecesAlOeste()</code> que quedaron pendientes del ejercicio anterior. En este caso, los procedimientos se pueden expresar fácilmente utilizando comandos primitivos, por lo que no es necesario comenzar pensando en posibles subtareas.",
    "pre":"program{ DibujarRectánguloRojoYNegroDe5x3() }\nprocedure DibujarRectánguloRojoYNegroDe5x3() {\n  repeat(2){DibujarLíneaRojaYNegraDeTamaño5HaciaElEste() Mover(Norte)}\n  DibujarLíneaRojaYNegraDeTamaño5HaciaElEste()\n  repeat(2) {Mover(Sur)}}\nprocedure DibujarLíneaRojaYNegraDeTamaño5HaciaElEste() {\n  repeat(4) {PonerUnaNegraYUnaRoja() Mover(Este)}\n  PonerUnaNegraYUnaRoja()\n  Mover4VecesAlOeste()\n}",
    "base":"procedure PonerUnaNegraYUnaRoja() {\n  /*\n  PROPÓSITO: ...\n  PRECONDICIONES: ...\n  */\n  \n\nprocedure Mover4VecesAlOeste() {\n  /*\n  PROPÓSITO: ...\n  PRECONDICIONES: ...\n  */\n  ",
    "run_data":[{
      "t0":{"head":[1,1],"width":7,"height":5,"board":[[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]]},
      "tf":{"head":[1,1],"width":7,"height":5,"board":[[v,v,v,v,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,b,b,b,v],[v,v,v,v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

e2_3 = "En el ejercicio anterior se trabajó con una metodología conocida como <em>top-down</em>: se comienza desde el problema, y se lo va descomponiendo en tareas cada vez más pequeñas, hasta llegar al uso de comandos primitivos. En este ejercicio vamos a proponer la estrategia inversa, <em>bottom-up</em>: primero se escriben los procedimientos elementales, y luego se van armando procedimientos cada vez más complejos, hasta construir uno que resuelva el problema original.<br>Escribir el siguiente procedimiento. Recuerde escribir los contratos correspondientes.<br><br>"

def guia2_ej3a(fecha):
  u = c(1,1,1,1) # Celda con una de cada color
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej3a",
    "nombre":"3. Por abajo (a)",
    "enunciado":e2_3+"<code>PonerUnaDeCada()</code> que ponga una bolita de cada color en la celda actual.",
    "pre":"program { PonerUnaDeCada() }",
    "run_data":[{
      "t0":{"head":[1,1],"width":3,"height":3,"board":[[a,v,v],[v,v,v],[v,v,r]]},
      "tf":{"head":[1,1],"width":3,"height":3,"board":[[a,v,v],[v,u,v],[v,v,r]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej3b(fecha):
  u = c(1,1,1,1) # Celda con una de cada color
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej3b",
    "nombre":"3. Por abajo (b)",
    "enunciado":e2_3+"<code>Mover3VecesAlOeste()</code> que mueva el cabezal tres celdas hacia el Oeste.",
    "pre":"program { Mover3VecesAlOeste() }",
    "run_data":[{
      "t0":{"head":[4,3],"width":6,"height":6,"board":[
        [v,r,v,a,v,u],[v,u,g,v,a,r],[v,v,u,u,v,v],[a,n,v,g,g,v],[r,v,r,a,v,u],[v,n,v,g,v,v]
      ]},
      "tf":{"head":[1,3],"width":6,"height":6,"board":[
        [v,r,v,a,v,u],[v,u,g,v,a,r],[v,v,u,u,v,v],[a,n,v,g,g,v],[r,v,r,a,v,u],[v,n,v,g,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej3c(fecha):
  u = c(1,1,1,1) # Celda con una de cada color
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej3c",
    "nombre":"3. Por abajo (c)",
    "enunciado":e2_3+"<code>DibujarLíneaMulticolorDeLargo4()</code> que ponga una línea de cuatro celdas hacia el Este en la que cada celda tenga una bolita de cada color. El cabezal debe quedar en la celda inicial. Para ello, debe reutilizar los procedimientos <code>PonerUnaDeCada()</code> y <code>Mover3VecesAlOeste()</code> (realizados en ejercicios anteriores).<br><br><b>Nota</b>: no incluir las definiciones de los procedimientos <code>PonerUnaDeCada()</code> y <code>Mover3VecesAlOeste()</code> al enviar este ejercicio.",
    "pre":"program { DibujarLíneaMulticolorDeLargo4() }\nprocedure PonerUnaDeCada() { Poner(Rojo) Poner(Verde) Poner(Azul) Poner(Negro) }\nprocedure Mover3VecesAlOeste() { repeat(3) { Mover(Oeste) } }",
    "run_data":[{
      "t0":{"head":[1,3],"width":6,"height":6,"board":[
        [v,r,v,a,v,u],[v,u,g,v,a,r],[v,v,u,v,v,v],[a,n,v,v,g,v],[r,v,r,v,v,u],[v,n,v,g,v,v]
      ]},
      "tf":{"head":[1,3],"width":6,"height":6,"board":[
        [v,r,v,a,v,u],[v,u,g,u,a,r],[v,v,u,u,v,v],[a,n,v,u,g,v],[r,v,r,u,v,u],[v,n,v,g,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej3d(fecha):
  u = c(1,1,1,1) # Celda con una de cada color
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej3d",
    "nombre":"3. Por abajo (d)",
    "enunciado":[e2_3+"<code>DibujarCuadradoMulticolorDeLado4()</code> que ponga un cuadrado sólido de 4",{"tex":"\\times"},"4 celdas en la que cada celda tenga una bolita de cada color. El cabezal debe quedar en la celda inicial. Para ello, debe reutilizar el procedimiento <code>DibujarLíneaMulticolorDeLargo4()</code>.<br><br><b>Nota</b>: no incluir la definición del procedimiento <code>DibujarLíneaMulticolorDeLargo4()</code> al enviar este ejercicio."],
    "pre":"program { DibujarCuadradoMulticolorDeLado4() }\nprocedure DibujarLíneaMulticolorDeLargo4() {\n  repeat(3) { PonerUnaDeCada() Mover(Este) }\n  PonerUnaDeCada()\n  Mover3VecesAlOeste()\n}\nprocedure PonerUnaDeCada() { Poner(Rojo) Poner(Verde) Poner(Azul) Poner(Negro) }\nprocedure Mover3VecesAlOeste() { repeat(3) { Mover(Oeste) } }",
    "run_data":[{
      "t0":{"head":[1,1],"width":6,"height":6,"board":[
        [v,r,v,a,v,u],[v,v,v,v,v,a],[g,v,v,v,v,v],[v,v,v,v,v,v],[u,v,v,v,v,v],[v,n,v,g,v,v]
      ]},
      "tf":{"head":[1,1],"width":6,"height":6,"board":[
        [v,r,v,a,v,u],[v,u,u,u,u,a],[g,u,u,u,u,v],[v,u,u,u,u,v],[u,u,u,u,u,v],[v,n,v,g,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej4(fecha):
  b = c(0,5,9,1) # Un azulejo
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej4",
    "nombre":"4. Guarda de azulejos",
    "enunciado":"Construir un procedimiento <code>PonerGuardaDe5Azulejos()</code>, que arme una \"guarda\" horizontal de 5 azulejos (como las que decoran las paredes). Cada azulejo está conformado por 1 bolita verde, 5 negras y 9 rojas. La posición final del cabezal no es relevante.<br>Recordar seguir una metodología adecuada para la construcción del código: <b>COMENZAR</b> por escribir el contrato completo del procedimiento, luego pensar las subtareas necesarias y darles un nombre adecuado, escribir el contrato de las subtareas, <b>LUEGO</b> el código del procedimiento pedido en términos de las subtareas, y <b>FINALMENTE</b>, realizar el código de las subtareas siguiendo la misma metodología (que denominamos metodología de construcción de programas <em>top-down</em>).",
    "pre":"program { PonerGuardaDe5Azulejos() }",
    "run_data":[{
      "t0":{"head":[1,2],"width":6,"height":6,"board":[
        [v,r,v,a,v,b],[v,v,v,v,v,a],[g,v,v,v,v,v],[v,v,v,v,v,v],[b,v,v,v,v,v],[v,n,v,g,v,v]
      ]},
      "tf":{"head":[],"width":6,"height":6,"board":[
        [v,r,v,a,v,b],[v,v,b,v,v,a],[g,v,b,v,v,v],[v,v,b,v,v,v],[b,v,b,v,v,v],[v,n,b,g,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej5(fecha):
  D = a_s(24)
  M = rs(3)
  A = gs(1976)
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej5",
    "nombre":"5.  Día de la Memoria",
    "enunciado":"Utilizando bolitas pueden representarse diversos elementos; un ejemplo de esto es la posibilidad de representar una fecha. Una fecha que los argentinos deberíamos recordar, para no repetirla jamás, es el 24 de marzo de 1976, hoy constituido como Día de la Memoria por la Verdad y la Justicia en Argentina.<br>Hacer un procedimiento <code>RegistrarElDíaDeLaMemoria()</code> que<ul><li>en la celda actual, ponga 24 bolitas Azules, que representan el día,</li><li> en la celda lindante al Este de la actual, ponga 3 bolitas Rojas, que representan el mes, y</li><li>en la celda lindante al Este de la anterior, ponga 1976 bolitas Verdes, representando el año.</li></ul>Recordar que la solución completa incluye la documentación: propósito, precondición y parámetros, los cuales deben ser escritos <b>ANTES</b> de escribir el código.<br>"+importante+": La solución se puede realizar íntegramente utilizando los conceptos vistos en la materia hasta el momento, y no se requieren herramientas adicionales. No debe utilizar conceptos aún no vistos en la teoría para solucionar el problema.",
    "pre":"program { RegistrarElDíaDeLaMemoria() }",
    "run_data":[{
      "t0":{"head":[2,2],"width":6,"height":6,"board":[
        [v,r,v,a,v,r],[v,v,v,v,v,a],[g,v,v,v,v,v],[v,v,v,v,v,v],[a,v,v,v,v,v],[v,n,v,g,v,v]
      ]},
      "tf":{"head":[2,2],"width":6,"height":6,"board":[
        [v,r,v,a,v,r],[v,v,v,v,v,a],[g,v,D,v,v,v],[v,v,M,v,v,v],[a,v,A,v,v,v],[v,n,v,g,v,v]
      ]}
    }],
    "analisisCodigo":[
      {"key":"CONCEPT_REP_SIMPLE"}
    ],
    "disponible":{"desde":fecha}
  }

def guia2_ej6(fecha):
  b = c(0,5,9,1) # Un azulejo
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej6",
    "nombre":"6. Guarda de azulejos en L",
    "enunciado":"Hacer un procedimiento <code>PonerGuardaEnL()</code>, que arme una guarda en L como muestra la figura (ver figura en <a href='https://aulas.gobstones.org/pluginfile.php/39015/mod_resource/content/22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf' target='_blank'>la guía</a>), dejando el cabezal en la posición inicial.<br>¿Pensaste en reutilizar el procedimiento definido antes, o empezaste a escribirlo de nuevo? Dado que ahora se cuenta con la subtarea definida en el ejercicio anterior, la metodología <em>top-down</em> se puede enriquecer con la reutilización de procedimientos ya realizados; esto puede hacer que ciertas divisiones en subtareas, que permiten esa reutilización, sean más sencillas que otras.",
    "pre":"program { PonerGuardaEnL() }",
    "run_data":[{
      "t0":{"head":[1,2],"width":6,"height":6,"board":[
        [v,r,v,a,v,b],[v,v,v,v,v,a],[g,v,v,v,v,v],[v,v,v,v,v,v],[b,v,v,v,v,v],[v,n,v,g,v,v]
      ]},
      "tf":{"head":[1,2],"width":6,"height":6,"board":[
        [v,r,v,a,v,b],[v,v,b,b,b,a],[g,v,b,v,v,v],[v,v,b,v,v,v],[b,v,v,v,v,v],[v,n,v,g,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def e2_7(e):
  return enPapel+" Escribir un programa para cumplir con el propósito que se indica más adelante. Para ello, deben utilizarse los procedimientos indicados a continuación."+código("procedure DibujarBase()<br>&nbsp;&nbsp;/*<br>&nbsp;&nbsp;PROPÓSITO: Dibuja una base de pirámide de 5 celdas de lado<br>&nbsp;&nbsp;PRECONDICIONES:<br>&nbsp;&nbsp;&nbsp;&nbsp;* La celda actual debe estar vacía<br>&nbsp;&nbsp;&nbsp;&nbsp;* Debe haber cuatro celdas vacías al Este del cabezal<br>&nbsp;&nbsp;*/<br>procedure DibujarMedio()<br>&nbsp;&nbsp;/* PROPÓSITO: Dibuja un sector del medio de pirámide de 3 celdas de lado<br>&nbsp;&nbsp;PRECONDICIONES:<br>&nbsp;&nbsp;&nbsp;&nbsp;* La celda actual debe estar vacía<br>&nbsp;&nbsp;&nbsp;&nbsp;* Debe haber dos celdas vacías al Este del cabezal<br>&nbsp;&nbsp;*/<br>procedure DibujarPunta()<br>&nbsp;&nbsp;/*<br>&nbsp;&nbsp;PROPÓSITO: Dibuja una punta de pirámide<br>&nbsp;&nbsp;PRECONDICIONES:<br>&nbsp;&nbsp;&nbsp;&nbsp;* La celda actual debe estar vacía<br>&nbsp;&nbsp;*/")+recordar+" Para cada ítem que sigue debe comenzarse redactando el contrato correspondiente, y de ser necesario, se deben definir subtareas para construir su solución, expresándolas mediante procedimientos (y en ese caso se deben escribir primero los contratos de los mismos y utilizarlos <b>ANTES</b> de dar su código).<br><br>" + e + "<br><br><b>Nota</b>: Para enviar, asumir que los dibujos se deben realizar siempre desde la celda actual hacia el Este y hacia el Norte."

def guia2_ej7a(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej7a",
    "nombre":"7. Las pirámides de Gobstones (a)",
    "enunciado":e2_7("Una pirámide."),
    "pre":"procedure DibujarBase() {\n  repeat(4){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(4){Mover(Oeste)}\n}\nprocedure DibujarMedio() {\n  repeat(2){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(2){Mover(Oeste)}\n}\nprocedure DibujarPunta() {Poner(Negro)}",
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,0],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]},
      "tf":{"head":[1,0],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[n,v,v,v,v,v],[n,n,v,v,v,v],[n,n,n,v,v,v],[n,n,v,v,v,v],[n,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]}
    },{
      "t0":{"head":[7,1],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]},
      "tf":{"head":[7,1],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,n,v,v,v,v],[v,n,n,v,v,v],[v,n,n,n,v,v],[v,n,n,v,v,v],[v,n,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej7b(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej7b",
    "nombre":"7. Las pirámides de Gobstones (b)",
    "enunciado":e2_7("Una pirámide invertida."),
    "pre":"procedure DibujarBase() {\n  repeat(4){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(4){Mover(Oeste)}\n}\nprocedure DibujarMedio() {\n  repeat(2){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(2){Mover(Oeste)}\n}\nprocedure DibujarPunta() {Poner(Negro)}",
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,1],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]},
      "tf":{"head":[1,1],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,n,v,v],[v,v,n,n,v,v],[v,n,n,n,v,v],[v,v,n,n,v,v],[v,v,v,n,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]}
    },{
      "t0":{"head":[7,1],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]},
      "tf":{"head":[7,1],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,n,v,v],[v,v,n,n,v,v],[v,n,n,n,v,v],[v,v,n,n,v,v],[v,v,v,n,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej7c(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej7c",
    "nombre":"7. Las pirámides de Gobstones (c)",
    "enunciado":e2_7("Una pirámide estirada a lo alto (con dos segmentos de cada uno)."),
    "pre":"procedure DibujarBase() {\n  repeat(4){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(4){Mover(Oeste)}\n}\nprocedure DibujarMedio() {\n  repeat(2){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(2){Mover(Oeste)}\n}\nprocedure DibujarPunta() {Poner(Negro)}",
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,0],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]},
      "tf":{"head":[1,0],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[n,n,v,v,v,v],[n,n,n,n,v,v],[n,n,n,n,n,n],[n,n,n,n,v,v],[n,n,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej7d(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej7d",
    "nombre":"7. Las pirámides de Gobstones (d)",
    "enunciado":e2_7("Una pirámide gigante (con 11 bloques de base y 6 bloques de altura, donde cada segmento es dos celdas más chico que el que tiene debajo). Para esto deben reutilizarse los procedimientos implementados en los puntos a. y b.<br>"+pista+": una pirámide gigante se puede conseguir con 4 pirámides comunes, si se las ubica con cuidado."),
    "pre":"procedure DibujarBase() {\n  repeat(4){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(4){Mover(Oeste)}\n}\nprocedure DibujarMedio() {\n  repeat(2){Poner(Negro) Mover(Este)}\n  Poner(Negro)\n  repeat(2){Mover(Oeste)}\n}\nprocedure DibujarPunta() {Poner(Negro)}",
    "pidePrograma": True,
    "run_data":[{
      "t0":{"head":[1,0],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]},
      "tf":{"head":[1,0],"width":12,"height":6,"board":[
        [v,v,v,v,v,v],[n,v,v,v,v,v],[n,n,v,v,v,v],[n,n,n,v,v,v],[n,n,n,n,v,v],[n,n,n,n,n,v],
        [n,n,n,n,n,n],[n,n,n,n,n,v],[n,n,n,n,v,v],[n,n,n,v,v,v],[n,n,v,v,v,v],[n,v,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def e2_8(e):
  return "En este ejercicio, se usará el tablero para <b><em>representar un bosque</em></b>. Cada celda representa a una <b><em>parcela</em></b>. Cada <b><em>bolita verde representa un árbol</em></b>. Cada <b><em>bolita roja representa una semilla</em></b>. Una <b><em>bolita negra representa una bomba</em></b>. Una <b><em>bolita azul representa una unidad de nutrientes</em></b>.<br>Escribir el siguiente procedimiento de representación, que hace lo que su nombre indica. Trabaja sobre la celda actual."+código(e+"()")

def guia2_ej8a(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8a",
    "nombre":"8. El bosque, parte 1 (a)",
    "enunciado":e2_8("PonerUnaSemilla"),
    "pre":"program {PonerUnaSemilla()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[r]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(4)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej8b(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8b",
    "nombre":"8. El bosque, parte 1 (b)",
    "enunciado":e2_8("PonerUnÁrbol"),
    "pre":"program {PonerUnÁrbol()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[g]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(4)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej8c(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8c",
    "nombre":"8. El bosque, parte 1 (c)",
    "enunciado":e2_8("PonerUnaBomba"),
    "pre":"program {PonerUnaBomba()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[n]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[ns(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[ns(4)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej8d(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8d",
    "nombre":"8. El bosque, parte 1 (d)",
    "enunciado":e2_8("PonerUnNutriente"),
    "pre":"program {PonerUnNutriente()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[a_s(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a_s(4)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej8e(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8e",
    "nombre":"8. El bosque, parte 1 (e)",
    "enunciado":e2_8("SacarUnaSemilla"),
    "pre":"program {SacarUnaSemilla()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[r]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(2)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej8f(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8f",
    "nombre":"8. El bosque, parte 1 (f)",
    "enunciado":e2_8("SacarUnÁrbol"),
    "pre":"program {SacarUnÁrbol()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[g]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(2)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej8g(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8g",
    "nombre":"8. El bosque, parte 1 (g)",
    "enunciado":e2_8("SacarUnaBomba"),
    "pre":"program {SacarUnaBomba()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[n]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[ns(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[ns(2)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej8h(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej8h",
    "nombre":"8. El bosque, parte 1 (h)",
    "enunciado":e2_8("SacarUnNutriente"),
    "pre":"program {SacarUnNutriente()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[a]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[a_s(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a_s(2)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2_ej9(fecha):
  T = rs(3) # Número 3
  S = rs(6) # Número 6
  N = rs(9) # Número 9
  D = rs(12) # Número 12
  return {
    "tipo":"CODIGO",
    "id":"guia2_ej9",
    "nombre":"9. Reloj Analógico",
    "enunciado":["Dibujar un reloj analógico de agujas en un tablero cuadriculado puede ser un desafío. Una simplificación posible sería representar solamente algunos de los números que aparecen en el mismo: el 12 arriba, el 3 a la derecha, el 9 a la izquierda y el 6 abajo.<br>Construir un procedimiento <code>DibujarRelojAnalógicoSimplificado()</code>, que ponga los números del reloj tal como se indicó, alrededor del casillero actual. El tamaño del reloj será de 2 celdas de \"radio\" (suponiendo que miramos al reloj como un círculo).<br>Utilizar el comando <code>DibujarRelojAnalógicoSimplificado()</code> en un tablero inicial vacío de 5",{"tex":"\\times"},"5 con la celda inicial en el centro del mismo, es el siguiente: (ver imagen en <a href='https://aulas.gobstones.org/pluginfile.php/39015/mod_resource/content/22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf' target='_blank'>la guía</a>).<br>"+recordar+" Escribir el contrato en primer lugar, y en caso de utilizar división en subtareas, en seguir la metodología <em>top-down</em> para las mismas (primero su nombre y su contrato, usarlas, y recién luego definirlas con la misma metodología)."],
    "pre":"program {DibujarRelojAnalógicoSimplificado()}",
    "run_data":[{
      "t0":{"head":[2,2],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[2,2],"width":5,"height":5,"board":[
        [v,v,N,v,v],[v,v,v,v,v],[S,v,v,v,D],[v,v,v,v,v],[v,v,T,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia2(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia2",
    "nombre":"Práctica 2 - Procedimientos y estrategia de solución",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(2, 39015, "22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf"),
      guia2_ej2a(fechaInicio),
      guia2_ej2b(fechaInicio),
      guia2_ej2c(fechaInicio),
      guia2_ej3a(fechaInicio),
      guia2_ej3b(fechaInicio),
      guia2_ej3c(fechaInicio),
      guia2_ej3d(fechaInicio),
      guia2_ej4(fechaInicio),
      guia2_ej5(fechaInicio),
      guia2_ej6(fechaInicio),
      guia2_ej7a(fechaInicio),
      guia2_ej7b(fechaInicio),
      guia2_ej7c(fechaInicio),
      guia2_ej7d(fechaInicio),
      guia2_ej8a(fechaInicio),
      guia2_ej8b(fechaInicio),
      guia2_ej8c(fechaInicio),
      guia2_ej8d(fechaInicio),
      guia2_ej8e(fechaInicio),
      guia2_ej8f(fechaInicio),
      guia2_ej8g(fechaInicio),
      guia2_ej8h(fechaInicio),
      guia2_ej9(fechaInicio)
    ]
  }

def guia3_ej1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej1",
    "nombre":"1. Moviendo tres veces al Norte",
    "enunciado":"Escribir un procedimiento <code>Mover3VecesAlNorte()</code> que mueva el cabezal tres posiciones al Norte de la actual.",
    "pre":"program {Mover3VecesAlNorte()}",
    "run_data":[{
      "t0":{"head":[3,0],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[3,3],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia3_ej2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej2",
    "nombre":"2. Moviendo tres veces al Este",
    "enunciado":"Escribir un procedimiento <code>Mover3VecesAlEste()</code> que mueva el cabezal tres posiciones al Este de la actual.",
    "pre":"program {Mover3VecesAlEste()}",
    "run_data":[{
      "t0":{"head":[0,3],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[3,3],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia3_ej3(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej3",
    "nombre":"3. Y ahora para algo completamente distinto",
    "enunciado":"Escribir un procedimiento <code>Poner6DeColorNegro()</code> que ponga 6 bolitas de color Negro en la celda actual.",
    "pre":"program {Poner6DeColorNegro()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[ns(2)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[ns(8)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia3_ej4(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej4",
    "nombre":"4. Y 6 Verdes",
    "enunciado":"Escribir un procedimiento <code>Poner6DeColorVerde()</code> que ponga 6 bolitas de color Verde en la celda actual.",
    "pre":"program {Poner6DeColorVerde()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(1)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(7)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia3_ej5(fecha):
  b = c(0,1,1,0) # Celda con una negra y una roja
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej5",
    "nombre":"5. Dibujando un rectángulo con repeticiones",
    "enunciado":"Escribir un procedimiento <code>DibujarRectánguloRojoYNegroDe5x3()</code> que dibuje un rectángulo sólido de 5 celdas de largo por 3 de alto, similar al realizado en <b><em>\"<a href='https://aulas.gobstones.org/pluginfile.php/39015/mod_resource/content/22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf' target='_blank'>P2. 2. Por Arriba</a>\"</em></b>, pero esta vez, utilice repetición para solucionar el problema.",
    "pre":"program {DibujarRectánguloRojoYNegroDe5x3()}",
    "run_data":[{
      "t0":{"head":[0,2],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[0,2],"width":5,"height":5,"board":[
        [v,v,b,b,b],[v,v,b,b,b],[v,v,b,b,b],[v,v,b,b,b],[v,v,b,b,b]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia3_ej6(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej6",
    "nombre":"6. Pintando el tablero",
    "enunciado":"Escribir un procedimiento <code>PintarElTableroDeAzul()</code> que, asumiendo que el tablero tiene 10 celdas de largo y 7 celdas de alto, pinte absolutamente todo el tablero con bolitas azules, dejando exactamente una bolita azul en cada celda. No es relevante la posición final del cabezal.<br>"+importante+": Recuerde que la estrategia de solución debe quedar clara a partir de la lectura del código. Use subtareas con nombres apropiados para dicho objetivo.",
    "pre":"program {PintarElTableroDeAzul()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":10,"height":7,"board":[
        [v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],
        [v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v]
      ]},
      "tf":{"head":[],"width":10,"height":7,"board":[
        [a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a]
      ]}
    },{
      "t0":{"head":[4,6],"width":10,"height":7,"board":[
        [v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],
        [v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v]
      ]},
      "tf":{"head":[],"width":10,"height":7,"board":[
        [a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],
        [a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a],[a,a,a,a,a,a,a]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia3(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia3",
    "nombre":"Práctica 3 - Repeticiones Simples",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(3, 39034, "23/P3.%20Repeticiones%20Simples.pdf"),
      guia3_ej1(fechaInicio),
      guia3_ej2(fechaInicio),
      guia3_ej3(fechaInicio),
      guia3_ej4(fechaInicio),
      guia3_ej5(fechaInicio),
      guia3_ej6(fechaInicio)
    ]
  }

def guia4_ej1(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej1",
    "nombre":"1. Moviendo tres veces a donde quieras",
    "enunciado":"Escribir un procedimiento <code>Mover3VecesAl_(direcciónAMover)</code> que dada una dirección <em><code>direcciónAMover</code></em> mueva el cabezal tres posiciones en dicha dirección.<br>"+recordar+" No olvidar escribir el contrato del procedimiento ANTES de realizar el código (y que los parámetros son parte del mismo).",
    "run_data":[{
      "pre":"program {Mover3VecesAl_(Este)}",
      "t0":{"head":[1,1],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[4,1],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    },{
      "pre":"program {Mover3VecesAl_(Sur)}",
      "t0":{"head":[3,3],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[3,0],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej2",
    "nombre":"2. Y 6 de lo que quieras",
    "enunciado":"Escribir un procedimiento <code>Poner6DeColor_(colorAPoner)</code> que dado un color <em><code>colorAPoner</code></em> ponga 6 bolitas del color dado.",
    "run_data":[{
      "pre":"program {Poner6DeColor_(Rojo)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(6)]]}
    },{
      "pre":"program {Poner6DeColor_(Verde)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(3)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(9)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej3(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej3",
    "nombre":"3. Moviendo y poniendo",
    "enunciado":"Escribir un procedimiento <code>Poner_Al_(colorAPoner, direcciónDondePoner)</code> que dado un color <em><code>colorAPoner</code></em> y una dirección <em><code>direcciónDondePoner</code></em>, ponga una bolita del color dado en la celda vecina en la dirección dada, dejando el cabezal en dicha celda.",
    "run_data":[{
      "pre":"program {Poner_Al_(Rojo,Norte)}",
      "t0":{"head":[0,0],"width":2,"height":2,"board":[[v,v],[v,v]]},
      "tf":{"head":[0,1],"width":2,"height":2,"board":[[v,r],[v,v]]}
    },{
      "pre":"program {Poner_Al_(Azul,Oeste)}",
      "t0":{"head":[1,1],"width":2,"height":2,"board":[[v,v],[v,v]]},
      "tf":{"head":[0,1],"width":2,"height":2,"board":[[v,a],[v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej4(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej4",
    "nombre":"4. Reemplazando colores",
    "enunciado":"Escribir <code>ReemplazarUnaDe_Por_(colorAReemplazar, colorPorElCualReemplazar)</code>, un procedimiento que dado un primer color <em><code>colorAReemplazar</code></em> y un segundo color <em><code>colorPorElCualReemplazar</code></em>, reemplaza una bolita del primer color por una del segundo color (en la celda actual).",
    "run_data":[{
      "pre":"program {ReemplazarUnaDe_Por_(Rojo,Azul)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(3,1,6,2)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(4,1,5,2)]]}
    },{
      "pre":"program {ReemplazarUnaDe_Por_(Verde,Negro)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(3,1,6,2)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(3,2,6,1)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej7(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej7",
    "nombre":"7. Multi Arcoiris",
    "enunciado":"Utilizando el procedimiento <code>Pintar3Puntos_</code> definido en el ejercicio anterior (ver el enunciado en <a href='https://aulas.gobstones.org/pluginfile.php/39050/mod_resource/content/21/P4.%20Para%CC%81metros.pdf' target='_blank'>la guía</a>), construir el procedimiento <code>PintarArcoiris()</code> que ponga el tablero de la derecha cuando el tablero inicial es el de la izquierda (ver imágenes de los tableros en <a href='https://aulas.gobstones.org/pluginfile.php/39050/mod_resource/content/21/P4.%20Para%CC%81metros.pdf' target='_blank'>la guía</a>). ¡A no ser como Nova, y empezar escribiendo el contrato!<br><br><b>Nota</b>: no incluir la definición del procedimiento <code>Pintar3Puntos_(colorPunto)</code> al enviar este ejercicio.",
    "pre":"program {PintarArcoiris()}\nprocedure Pintar3Puntos_(c){\n  Poner(c)\n  repeat(3) {Mover(Este)}\n  Poner(c)\n  repeat(3) {Mover(Este)}\n  Poner(c)\n  repeat(6) {Mover(Oeste)}\n}",
    "run_data":[{
      "t0":{"head":[1,1],"width":10,"height":3,"board":[
        [v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v],[v,v,v]
      ]},
      "tf":{"head":[1,1],"width":10,"height":3,"board":[
        [v,v,v],[v,n,v],[v,a,g],[v,r,v],[v,n,v],[v,a,g],[v,r,v],[v,n,v],[v,a,g],[v,r,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej8(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej8",
    "nombre":"8. Y ahora, muchas Rojas",
    "enunciado":"Escribir un procedimiento <code>Poner_DeColorRojo(cantidadAPoner)</code> que dado un número <em><code>cantidadAPoner</code></em>, ponga tantas bolitas como se indica de color Rojo en la celda actual.",
    "run_data":[{
      "pre":"program {Poner_DeColorRojo(2)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(2)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(4)]]}
    },{
      "pre":"program {Poner_DeColorRojo(7)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(4)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(11)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej9(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej9",
    "nombre":"9. Poner de a muchas",
    "enunciado":biblioteca+" Escribir un procedimiento <code>Poner_DeColor_(cantidadAPoner, colorAPoner)</code> que dado un número <em><code>cantidadAPoner</code></em> y un color <em><code>colorAPoner</code></em>, ponga tantas bolitas como se indica del color dado en la celda actual.",
    "run_data":[{
      "pre":"program {Poner_DeColor_(3,Verde)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(4)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(7)]]}
    },{
      "pre":"program {Poner_DeColor_(8,Azul)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[a_s(1)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a_s(9)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej10(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej10",
    "nombre":"10. Moviendo tantas veces como quieras a donde quieras",
    "enunciado":biblioteca+" Escribir <code>Mover_VecesAl_(cantidadAMover, direcciónAMover)</code>, un procedimiento que dado un número <em><code>cantidadAMover</code></em> y una dirección <em><code>direcciónAMover</code></em> mueva el cabezal tantas veces como la dada en dicha dirección.",
    "run_data":[{
      "pre":"program {Mover_VecesAl_(2,Norte)}",
      "t0":{"head":[1,1],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[1,3],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    },{
      "pre":"program {Mover_VecesAl_(4,Oeste)}",
      "t0":{"head":[4,4],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[0,4],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej11(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej11",
    "nombre":"11. Sacar de a muchas",
    "enunciado":biblioteca+" Escribir un procedimiento <code>Sacar_DeColor_(cantidadASacar, colorASacar)</code> que dado un número <em><code>cantidadASacar</code></em> y un color <em><code>colorASacar</code></em>, saque tantas bolitas como se indica del color dado en la celda actual.",
    "run_data":[{
      "pre":"program {Sacar_DeColor_(2,Negro)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[ns(5)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[ns(3)]]}
    },{
      "pre":"program {Sacar_DeColor_(3,Rojo)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(8)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(5)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej12(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej12",
    "nombre":"12. Yendo a una esquina",
    "enunciado":biblioteca+" Escribir un procedimiento <code>IrAEsquinaAl_Y_(primeraDirección, segundaDirección)</code> que dadas dos direcciones posiciona el cabezal en la esquina en dichas direcciones.",
    "run_data":[{
      "pre":"program {IrAEsquinaAl_Y_(Sur,Este)}",
      "t0":{"head":[2,2],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[4,0],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    },{
      "pre":"program {IrAEsquinaAl_Y_(Norte,Oeste)}",
      "t0":{"head":[1,3],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[0,4],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej13(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej13",
    "nombre":"13. Escribiendo fechas",
    "enunciado":"Construir un procedimiento <code>EscribirFechaConDía_Mes_Año_(día, mes, año)</code>, que permita representar cualquier fecha dados el día, mes y año (como números). La representación debe ser la misma utilizada en el ejercicio anterior donde se registró el Día de la Memoria (ver enunciado en <a href='https://aulas.gobstones.org/pluginfile.php/39015/mod_resource/content/22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf' target='_blank'>la guía 2</a>): Azul para el día, Rojo para el mes y Verde para el año, en tres celdas hacia el Este.<br><br>"+recordar+" Debe comenzarse por escribir el contrato; en este caso puede resultar útil escribir también una observación con la representación a utilizar.",
    "run_data":[{
      "pre":"program {EscribirFechaConDía_Mes_Año_(2,6,11)}",
      "t0":{"head":[1,1],"width":4,"height":2,"board":[[v,v],[v,v],[v,v],[v,v]]},
      "tf":{"head":[1,1],"width":4,"height":2,"board":[[v,v],[v,a_s(2)],[v,rs(6)],[v,gs(11)]]}
    },{
      "pre":"program {EscribirFechaConDía_Mes_Año_(9,3,8)}",
      "t0":{"head":[1,1],"width":4,"height":2,"board":[[v,v],[v,v],[v,v],[v,v]]},
      "tf":{"head":[1,1],"width":4,"height":2,"board":[[v,v],[v,a_s(9)],[v,rs(3)],[v,gs(8)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej14(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej14",
    "nombre":"14. Listado de fechas",
    "enunciado":"Construir un programa que escriba un listado vertical con las siguientes fechas:<ul><li>Inicio de la reforma universitaria.</li><li>Reglamentación del voto femenino en Argentina.</li><li>Fecha en la que ocurrieron los hechos conmemorados en el Día Internacional de los Trabajadores.</li><li>Creación del Ministerio de Ciencia y Tecnología argentino</li><li>Primera conmemoración del Día de la Mujer.</li></ul>¿Es necesario pensar procedimientos para escribir cada una de las fechas o sirve algo de lo realizado con anterioridad?",
    "pidePrograma":True,
    "run_data":[{
      "t0":{"head":[0,4],"width":3,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[0,4],"width":3,"height":5,"board":[
        [a_s(19), a_s(10),  a,        a_s(23),  a_s(15)],
        [rs(3),   rs(12),   rs(5),    rs(9),    rs(6)],
        [gs(1911),gs(2007), gs(1886), gs(1947), gs(1918)]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej15(fecha):
  T = rs(3) # Número 3
  S = rs(6) # Número 6
  N = rs(9) # Número 9
  D = rs(12) # Número 12
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej15",
    "nombre":"15. Reloj analógico simplificado generalizado",
    "enunciado":"Generalizar el ejercicio del reloj analógico simplificado de la práctica 2 (ver el enunciado en <a href='https://aulas.gobstones.org/pluginfile.php/39015/mod_resource/content/22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf' target='_blank'>la guía</a>) para que se pueda pasar el radio como argumento. O sea, se le pide escribir un procedimiento <code>DibujarRelojAnalógicoSimplificadoDeRadio_(radio)</code> que ponga los números del reloj como en el programa original, pero donde el radio recibido por parámetro indica la distancia al centro del reloj: mientras más grande es el radio, más alejados están los números del centro.<br>Por ejemplo, el programa del ejercicio anterior podría obtenerse invocando al procedimiento con el comando <code>DibujarRelojAnalógicoSimplificadoDeRadio_(2)</code>.",
    "run_data":[{
      "pre":"program {DibujarRelojAnalógicoSimplificadoDeRadio_(1)}",
      "t0":{"head":[2,2],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[2,2],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,N,v,v],[v,S,v,D,v],[v,v,T,v,v],[v,v,v,v,v]
      ]}
    },{
      "pre":"program {DibujarRelojAnalógicoSimplificadoDeRadio_(2)}",
      "t0":{"head":[2,2],"width":5,"height":5,"board":[
        [v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v],[v,v,v,v,v]
      ]},
      "tf":{"head":[2,2],"width":5,"height":5,"board":[
        [v,v,N,v,v],[v,v,v,v,v],[S,v,v,v,D],[v,v,v,v,v],[v,v,T,v,v]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def e4_18(e):
  return "Continuaremos representando el bosque que comenzamos en la práctica 2 (ver el enunciado en <a href='https://aulas.gobstones.org/pluginfile.php/39015/mod_resource/content/22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf' target='_blank'>la guía</a>). Esta vez queremos ser capaces de poner o sacar múltiples elementos de una sola vez.<br><br>"+importante+": para realizar este ejercicio se espera haya realizado la parte 1 de <a href='https://aulas.gobstones.org/pluginfile.php/39015/mod_resource/content/22/P2.%20Procedimientos%20y%20Estrategias%20de%20Solucio%CC%81n.pdf' target='_blank'>la Práctica 2</a>. Si aún no lo hizo, se recomienda volver y realizar el mismo previo a solucionar el ejercicio actual."+código(e)

def guia4_ej18a(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej18a",
    "nombre":"18. El bosque, parte 2 (a)",
    "enunciado":e4_18("Poner_Semillas(cantidadDeSemillasAPoner)"),
    "run_data":[{
      "pre":"program {Poner_Semillas(3)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(1)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(4)]]}
    },{
      "pre":"program {Poner_Semillas(1)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(8)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(9)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej18b(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej18b",
    "nombre":"18. El bosque, parte 2 (b)",
    "enunciado":e4_18("Sacar_Semillas(cantidadDeSemillasASacar)"),
    "run_data":[{
      "pre":"program {Sacar_Semillas(2)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(2)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    },{
      "pre":"program {Sacar_Semillas(4)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[rs(5)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[rs(1)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej18c(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej18c",
    "nombre":"18. El bosque, parte 2 (c)",
    "enunciado":e4_18("Poner_Árboles(cantidadDeÁrbolesAPoner)"),
    "run_data":[{
      "pre":"program {Poner_Árboles(4)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(2)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(6)]]}
    },{
      "pre":"program {Poner_Árboles(2)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(5)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(7)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej18d(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej18d",
    "nombre":"18. El bosque, parte 2 (d)",
    "enunciado":e4_18("Sacar_Árboles(cantidadDeÁrbolesASacar)"),
    "run_data":[{
      "pre":"program {Sacar_Árboles(5)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(5)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    },{
      "pre":"program {Sacar_Árboles(1)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[gs(8)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[gs(7)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej18e(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej18e",
    "nombre":"18. El bosque, parte 2 (e)",
    "enunciado":e4_18("Poner_Nutrientes(cantidadDeNutrientesAPoner)"),
    "run_data":[{
      "pre":"program {Poner_Nutrientes(1)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a]]}
    },{
      "pre":"program {Poner_Nutrientes(8)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[a_s(2)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a_s(10)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4_ej18f(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia4_ej18f",
    "nombre":"18. El bosque, parte 2 (f)",
    "enunciado":e4_18("Sacar_Nutrientes(cantidadDeNutrientesASacar)"),
    "run_data":[{
      "pre":"program {Sacar_Nutrientes(3)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[a_s(9)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a_s(6)]]}
    },{
      "pre":"program {Sacar_Nutrientes(4)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[a_s(8)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[a_s(4)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia4(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia4",
    "nombre":"Práctica 4 - Parámetros",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(4, 39050, "21/P4.%20Para%CC%81metros.pdf"),
      guia4_ej1(fechaInicio),
      guia4_ej2(fechaInicio),
      guia4_ej3(fechaInicio),
      guia4_ej4(fechaInicio),
      guia4_ej7(fechaInicio),
      guia4_ej8(fechaInicio),
      guia4_ej9(fechaInicio),
      guia4_ej10(fechaInicio),
      guia4_ej11(fechaInicio),
      guia4_ej12(fechaInicio),
      guia4_ej13(fechaInicio),
      guia4_ej14(fechaInicio),
      guia4_ej15(fechaInicio),
      guia4_ej18a(fechaInicio),
      guia4_ej18b(fechaInicio),
      guia4_ej18c(fechaInicio),
      guia4_ej18d(fechaInicio),
      guia4_ej18e(fechaInicio),
      guia4_ej18f(fechaInicio)
    ]
  }

TIPOS5_1 = [
  "Color",      # 0
  "Dirección",  # 1
  "Número",     # 2
  "Error"       # 3
]

EXPRESIONES5_1 = {
  "a":"nroBolitas(Negro) + nroBolitas(Azul)",
  "b":"opuesto(opuesto(Este))",
  "c":"nroBolitas(siguiente(Azul))",
  "d":"2 * nroBolitas(colorAImitar)"
}

def expresión5_1(e):
  return EXPRESIONES5_1[e]

def preguntas5_1(q,e,t):
  return q+' de la expresión <code>'+expresión5_1(e)+'</code> en el tablero ('+t+'):<br>'+img('5.1.'+t+'.png')

def preguntas5_1_tipos(e,t):
  return preguntas5_1("Tipo",e,t)

def preguntas5_1_valores(e,t):
  return preguntas5_1("Valor",e,t) + (preguntas5_1_d() if e=="d" else "")

def preguntas5_1_d():
  return "<br>Para este último supondremos que la expresión aparece dentro del cuerpo del procedimiento con el siguiente contrato:"+ \
    código("procedure PonerElDobleDe_QueDe_(colorAPoner, colorAImitar)<br>"+ \
      "&nbsp;&nbsp;/*<br>&nbsp;&nbsp;&nbsp;&nbsp;PROPÓSITO: Poner bolitas del color **colorAPoner** en una cantidad que sea el doble de las que hay del color **colorAImitar** en la celda actual.<br>"+ \
      "&nbsp;&nbsp;&nbsp;&nbsp;PARÁMETROS:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* colorAPoner : Color - color del que se pondrán bolitas.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* colorAImitar : Color - color del que se mirará cuántas bolitas hay en la celda actual.<br>"+ \
      "&nbsp;&nbsp;&nbsp;&nbsp;PRECONDICIONES:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Ninguna<br>&nbsp;&nbsp;*/")+ \
    "Y del cual sabemos fue invocado como:"+código("PonerElDobleDe_QueDe_(Rojo, Verde)")

def rtas5_1_tipos(correcta, devoluciones):
  opciones = []
  for i in range(len(TIPOS5_1)):
    opciones.append([TIPOS5_1[i], devoluciones[i]])
  return rtas_opción_multiple_i(opciones, correcta)

def guia5_ej1(fecha):
  return {
    "tipo":"CUESTIONARIO",
    "id":"guia5_ej1",
    "nombre":"1. Mis primeras expresiones",
    "preguntas":[{
      "tipo":"SOLO_TEXTO",
      "titulo":"Enunciado",
      "pregunta":enPapel+" Indicar el valor y el tipo que representan las expresiones dadas en los ítems en cada uno de los tableros A , B y C, suponiendo definido un procedimiento con el contrato dado al final."
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"a. (A) Tipo",
      "pregunta":preguntas5_1_tipos("a","A"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"a. (A) Valor",
      "pregunta":preguntas5_1_valores("a","A"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""]
      ], 3)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"a. (B) Tipo",
      "pregunta":preguntas5_1_tipos("a","B"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"a. (B) Valor",
      "pregunta":preguntas5_1_valores("a","B"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""]
      ], 8)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"a. (C) Tipo",
      "pregunta":preguntas5_1_tipos("a","C"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"a. (C) Valor",
      "pregunta":preguntas5_1_valores("a","C"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""]
      ], 0)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"b. (A) Tipo",
      "pregunta":preguntas5_1_tipos("b","A"),
      "respuestas":rtas5_1_tipos(1, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"b. (A) Valor",
      "pregunta":preguntas5_1_valores("b","A"),
      "respuestas":rtas_opción_multiple_i([
        ["Norte",""],
        ["Sur",""],
        ["Este",""],
        ["Oeste",""],
        ["Error",""]
      ], 2)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"b. (B) Tipo",
      "pregunta":preguntas5_1_tipos("b","B"),
      "respuestas":rtas5_1_tipos(1, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"b. (B) Valor",
      "pregunta":preguntas5_1_valores("b","B"),
      "respuestas":rtas_opción_multiple_i([
        ["Norte",""],
        ["Sur",""],
        ["Este",""],
        ["Oeste",""],
        ["Error",""]
      ], 2)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"b. (C) Tipo",
      "pregunta":preguntas5_1_tipos("b","C"),
      "respuestas":rtas5_1_tipos(1, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"b. (C) Valor",
      "pregunta":preguntas5_1_valores("b","C"),
      "respuestas":rtas_opción_multiple_i([
        ["Norte",""],
        ["Sur",""],
        ["Este",""],
        ["Oeste",""],
        ["Error",""]
      ], 2)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"c. (A) Tipo",
      "pregunta":preguntas5_1_tipos("c","A"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"c. (A) Valor",
      "pregunta":preguntas5_1_valores("c","A"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""],
        ["Error",""]
      ], 0)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"c. (B) Tipo",
      "pregunta":preguntas5_1_tipos("c","B"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"c. (B) Valor",
      "pregunta":preguntas5_1_valores("c","B"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""],
        ["Error",""]
      ], 4)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"c. (C) Tipo",
      "pregunta":preguntas5_1_tipos("c","C"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"c. (C) Valor",
      "pregunta":preguntas5_1_valores("c","C"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""],
        ["Error",""]
      ], 0)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"d. (A) Tipo",
      "pregunta":preguntas5_1_tipos("d","A"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"d. (A) Valor",
      "pregunta":preguntas5_1_valores("d","A"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""],
        ["Error",""]
      ], 6)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"d. (B) Tipo",
      "pregunta":preguntas5_1_tipos("d","B"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"d. (B) Valor",
      "pregunta":preguntas5_1_valores("d","B"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""],
        ["Error",""]
      ], 8)
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"d. (C) Tipo",
      "pregunta":preguntas5_1_tipos("d","C"),
      "respuestas":rtas5_1_tipos(2, ["","","",""])
    },{
      "tipo":"OPCION_MULTIPLE",
      "titulo":"d. (C) Valor",
      "pregunta":preguntas5_1_valores("d","C"),
      "respuestas":rtas_opción_multiple_i([
        [0,""],
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        [11,""],
        [12,""],
        ["Error",""]
      ], 0)
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej2(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej2",
    "nombre":"2. Moviendo según me indican las bolitas",
    "enunciado":"Escribir el procedimiento <code>Mover_SegúnColor_(dirección,color)</code>, que mueve el cabezal en la dirección dada tantas celdas como bolitas de color dado hay en la celda actual. Como ejemplos se ofrecen los resultados de evaluar el comando <code>Mover_SegúnColor_(Este, Negro)</code>, en diferentes tableros iniciales (ver imágenes en <a href='https://aulas.gobstones.org/pluginfile.php/39068/mod_resource/content/18/P5.%20Expresiones%20y%20tipos.pdf' target='_blank'>la guía</a>).<br><br>"+importante+":  En el último caso, como la celda no tiene bolitas negras (o sea tiene 0 bolitas negras), entonces el cabezal se mueve 0 celdas hacia el Este (O sea, no se mueve). Para probar correctamente su código, pruebe pasando como argumento otras direcciones y colores.",
    "run_data":[{
      "pre":"program {Mover_SegúnColor_(Norte, Negro)}",
      "t0":{"head":[0,0],"width":1,"height":5,"board":[[ns(3),v,v,v,v]]},
      "tf":{"head":[0,3],"width":1,"height":5,"board":[[ns(3),v,v,v,v]]}
    },{
      "pre":"program {Mover_SegúnColor_(Sur, Verde)}",
      "t0":{"head":[0,4],"width":1,"height":5,"board":[[v,v,v,v,gs(4)]]},
      "tf":{"head":[0,0],"width":1,"height":5,"board":[[v,v,v,v,gs(4)]]}
    }],
    "disponible":{"desde":fecha}
  }

def e5_3(e):
  return "En este ejercicio continuaremos con nuestro bosque, esta vez colocando semillas y árboles en la celda lindante hacia alguna dirección, y dejando el cabezal en la celda inicial."+código(e+"<br>// deja el cabezal en la celda inicial")

def guia5_ej3a(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej3a",
    "nombre":"3. El bosque, parte 3 (a)",
    "enunciado":e5_3("Poner_SemillasAl_(cantidadDeSemillas, direcciónAPoner)"),
    "run_data":[{
      "pre":"program {Poner_SemillasAl_(3,Norte)}",
      "t0":{"head":[0,0],"width":1,"height":2,"board":[[v,v]]},
      "tf":{"head":[0,0],"width":1,"height":2,"board":[[v,rs(3)]]}
    },{
      "pre":"program {Poner_SemillasAl_(2,Oeste)}",
      "t0":{"head":[1,1],"width":2,"height":2,"board":[[v,rs(2)],[v,rs(5)]]},
      "tf":{"head":[1,1],"width":2,"height":2,"board":[[v,rs(4)],[v,rs(5)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej3b(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej3b",
    "nombre":"3. El bosque, parte 3 (b)",
    "enunciado":e5_3("Sacar_ÁrbolesAl_(cantidadDeÁrboles, direcciónASacar)"),
    "run_data":[{
      "pre":"program {Sacar_ÁrbolesAl_(3,Sur)}",
      "t0":{"head":[0,1],"width":2,"height":2,"board":[[gs(7),rs(3)],[v,v]]},
      "tf":{"head":[0,1],"width":2,"height":2,"board":[[gs(4),rs(3)],[v,v]]}
    },{
      "pre":"program {Sacar_ÁrbolesAl_(1,Este)}",
      "t0":{"head":[0,1],"width":2,"height":2,"board":[[v,rs(2)],[v,gs(2)]]},
      "tf":{"head":[0,1],"width":2,"height":2,"board":[[v,rs(2)],[v,gs(1)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej3c(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej3c",
    "nombre":"3. El bosque, parte 3 (c)",
    "enunciado":e5_3("Sacar_SemillasEnDiagonalAl_Y_(cantidadDeSemillas, primeraDirDiagonal, segundaDirDiagonal)"),
    "run_data":[{
      "pre":"program {Sacar_SemillasEnDiagonalAl_Y_(3,Norte,Este)}",
      "t0":{"head":[0,0],"width":2,"height":2,"board":[[v,v],[v,rs(5)]]},
      "tf":{"head":[0,0],"width":2,"height":2,"board":[[v,v],[v,rs(2)]]}
    },{
      "pre":"program {Sacar_SemillasEnDiagonalAl_Y_(6,Oeste,Sur)}",
      "t0":{"head":[1,1],"width":2,"height":2,"board":[[rs(9),v],[v,v]]},
      "tf":{"head":[1,1],"width":2,"height":2,"board":[[rs(3),v],[v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej3d(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej3d",
    "nombre":"3. El bosque, parte 3 (d)",
    "enunciado":e5_3("Sacar_ÁrbolesEnDiagonalHorariaAl_(cantidadDeÁrboles, direcciónDiagonal)<br>// la diagonal horaria de una dirección es aquella dada por la dirección y su dirección siguiente.<br>// Ej. la diagonal horaria de Norte es Norte-Este, la de Sur es Sur-Oeste."),
    "run_data":[{
      "pre":"program {Sacar_ÁrbolesEnDiagonalHorariaAl_(3,Norte)}",
      "t0":{"head":[0,0],"width":2,"height":2,"board":[[v,v],[v,gs(5)]]},
      "tf":{"head":[0,0],"width":2,"height":2,"board":[[v,v],[v,gs(2)]]}
    },{
      "pre":"program {Sacar_ÁrbolesEnDiagonalHorariaAl_(6,Sur)}",
      "t0":{"head":[1,1],"width":2,"height":2,"board":[[gs(9),v],[v,v]]},
      "tf":{"head":[1,1],"width":2,"height":2,"board":[[gs(3),v],[v,v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej4(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej4",
    "nombre":"4. La banda de la gloriosa River Plate",
    "enunciado":"Escribir <code>DibujarLaBandaGloriosaDeAncho_(ancho)</code> que dibuja una banda diagonal de color Rojo de cuatro celdas de alto y de tantas celdas de largo como indique el parámetro ancho (dibujando hacia arriba y hacia la derecha). El procedimiento debe poder ser ejecutado en tableros en donde la banda entra justa en el tablero como se muestra a continuación (ver figura en <a href='https://aulas.gobstones.org/pluginfile.php/39068/mod_resource/content/18/P5.%20Expresiones%20y%20tipos.pdf' target='_blank'>la guía</a>).<br>La imágen muestra el resultado de ejecutar el procedimiento como <code>DibujarLaBandaGloriosaDeAncho_(6)</code>, con el cabezal posicionado en la esquina Sur-Oeste del tablero al inicio.<br>"+importante+": Si la banda tiene 6 celdas de largo, el argumento pasado debe ser 6, no 5. Tenga en cuenta que deberá utilizar expresiones en algún lugar de su código para solucionar el problema.",
    "run_data":[{
      "pre":"program {DibujarLaBandaGloriosaDeAncho_(1)}",
      "t0":{"head":[0,0],"width":1,"height":4,"board":[[v,v,v,v]]},
      "tf":{"head":[0,0],"width":1,"height":4,"board":[[r,r,r,r]]}
    },{
      "pre":"program {DibujarLaBandaGloriosaDeAncho_(3)}",
      "t0":{"head":[1,1],"width":4,"height":7,"board":[
        [v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v],[v,v,v,v,v,v,v]
      ]},
      "tf":{"head":[1,1],"width":4,"height":7,"board":[
        [v,v,v,v,v,v,v],[v,r,r,r,r,v,v],[v,v,r,r,r,r,v],[v,v,v,r,r,r,r]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej5a(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej5a",
    "nombre":"5. ¡A la batalla!, parte 1 (a)",
    "enunciado":"Suponiendo que se está programando un juego donde en las celdas del tablero se representan Soldados (los aliados con una bolita de color Negro y los enemigos con una bolita de color Rojo por cada soldado), escribir el siguiente procedimiento:<br><br><code>EnviarAliadosParaDuplicarEnemigos()</code>, que agrega soldados aliados en la celda actual en cantidad suficiente para que haya el doble de aliados que de soldados enemigos.",
    "pre":"program {EnviarAliadosParaDuplicarEnemigos()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(0,0,0,0)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(0,0,0,0)]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(0,0,10,0)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(0,20,10,0)]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(0,4,8,0)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(0,16,8,0)]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(0,6,4,0)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(0,8,4,0)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej5b(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej5b",
    "nombre":"5. ¡A la batalla!, parte 1 (b)",
    "enunciado":"Suponiendo que se está programando un juego donde en las celdas del tablero se representan Soldados (los aliados con una bolita de color Negro y los enemigos con una bolita de color Rojo por cada soldado), escribir el siguiente procedimiento:<br><br><code>PelearLaBatalla()</code>, que simula una batalla, suponiendo que hay suficiente cantidad de soldados aliados como para ganar la batalla. Durante una batalla, 2 soldados enemigos pelean contra 3 soldados aliados y todos mueren. Por ejemplo, si hay 6 enemigos y 10 aliados, mueren los 6 enemigos y 9 de los aliados; si hay 10 enemigos y 21 aliados, mueren los 10 enemigos y 15 soldados aliados.<br>"+pista+": ¿Qué cuenta hay que hacer para saber cuántos soldados aliados morirán?",
    "pre":"program {PelearLaBatalla()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(0,0,0,0)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(0,0,0,0)]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(0,10,6,0)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(0,1,0,0)]]}
    },{
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(0,21,10,0)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(0,6,0,0)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej6(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej6",
    "nombre":"6. Sacando todas las de un color",
    "enunciado":biblioteca+" Escribir un procedimiento <code>SacarTodasLasDeColor_(colorASacar)</code>, que quite de la celda actual todas las bolitas del color indicado por el parámetro.<br>"+pista+": Considerar utilizar el procedimiento <code>Sacar_DeColor_</code>, definido en la práctica anterior. ¿Qué argumentos se le deberían pasar?",
    "run_data":[{
      "pre":"program {SacarTodasLasDeColor_(Rojo)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(10,10,10,10)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[c(10,10,0,10)]]}
    },{
      "pre":"program {SacarTodasLasDeColor_(Azul)}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej7(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej7",
    "nombre":"7. ¿Y si vaciamos la celda?",
    "enunciado":biblioteca+" Escribir un procedimiento <code>VaciarCelda()</code> que quite de la celda actual todas las bolitas de todos los colores, dejando la celda vacía.",
    "run_data":[{
      "pre":"program {VaciarCelda()}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[c(10,10,10,10)]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    },{
      "pre":"program {VaciarCelda()}",
      "t0":{"head":[0,0],"width":1,"height":1,"board":[[v]]},
      "tf":{"head":[0,0],"width":1,"height":1,"board":[[v]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej8(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej8",
    "nombre":"8. La banda ahora es para todos",
    "enunciado":"Los hinchas de otros clubes se quejaron de que la banda que hicimos solo vale para River, y quieren poder hacer otras bandas. Escribir entonces <code>DibujarBandaDeAlto_YAncho_DeColor_(alto, ancho, color)</code> que dibuja una banda diagonal con los parámetros dados.<br>"+importante+": Nuevamente, debe seguir funcionando el código para casos de borde.",
    "run_data":[{
      "pre":"program {DibujarBandaDeAlto_YAncho_DeColor_(6,1,Verde)}",
      "t0":{"head":[0,0],"width":1,"height":6,"board":[[v,v,v,v,v,v]]},
      "tf":{"head":[0,0],"width":1,"height":6,"board":[[g,g,g,g,g,g]]}
    },{
      "pre":"program {DibujarBandaDeAlto_YAncho_DeColor_(2,4,Azul)}",
      "t0":{"head":[1,1],"width":5,"height":6,"board":[
        [v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v],[v,v,v,v,v,v]
      ]},
      "tf":{"head":[1,1],"width":5,"height":6,"board":[
        [v,v,v,v,v,v],[v,a,a,v,v,v],[v,v,a,a,v,v],[v,v,v,a,a,v],[v,v,v,v,a,a]
      ]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5_ej9(fecha):
  return {
    "tipo":"CODIGO",
    "id":"guia5_ej9",
    "nombre":"9. Aprendiendo a leer y escribir",
    "enunciado":"Hacer el procedimiento PasarPalabraActualAMayúsculas() que suponiendo que en la fila actual se codifica una palabra en minúsculas usando bolitas, ponga la misma palabra en mayúsculas en la fila al Norte.<ul><li>Cada letra se representa con una cantidad diferente de bolitas negras, según un código numérico llamado ASCII.</li><li>En la celda más al Oeste de la fila actual se codifica la cantidad de letras de la palabra, usando bolitas rojas.</li><li>La primera letra de la palabra está en la celda lindante al Este de la que contiene la cantidad de letras.</li><li>En el código ASCII si las letras mayúsculas se codifican con un número N entonces la misma letra minúscula se representa con N+32 (ej. la ‘a’ minúsculas se representa con el número 97 y la ‘A’ mayúsculas, con el 65).</li><li>El cabezal se encuentra en la celda más al Oeste de una fila donde hay una palabra representada.</li></ul>"+importante+": ¿Cómo comenzar la resolución? En cada procedimiento, ¿qué parte debe escribirse primero?",
    "pre":"program {PasarPalabraActualAMayúsculas()}",
    "run_data":[{
      "t0":{"head":[0,0],"width":3,"height":2,"board":[[rs(2),v],[ns(103),v],[ns(98),v]]},
      "tf":{"head":[0,0],"width":3,"height":2,"board":[[rs(2),v],[ns(103),ns(71)],[ns(98),ns(66)]]}
    },{
      "t0":{"head":[0,0],"width":4,"height":2,"board":[[rs(3),v],[ns(98),v],[ns(103),v],[ns(98),v]]},
      "tf":{"head":[0,0],"width":4,"height":2,"board":[[rs(3),v],[ns(98),ns(66)],[ns(103),ns(71)],[ns(98),ns(66)]]}
    }],
    "disponible":{"desde":fecha}
  }

def guia5(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia5",
    "nombre":"Práctica 5 - Expresiones y Tipos",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(5, 39068, "18/P5.%20Expresiones%20y%20tipos.pdf"),
      guia5_ej1(fechaInicio),
      guia5_ej2(fechaInicio),
      guia5_ej3a(fechaInicio),
      guia5_ej3b(fechaInicio),
      guia5_ej3c(fechaInicio),
      guia5_ej3d(fechaInicio),
      guia5_ej4(fechaInicio),
      guia5_ej5a(fechaInicio),
      guia5_ej5b(fechaInicio),
      guia5_ej6(fechaInicio),
      guia5_ej7(fechaInicio),
      guia5_ej8(fechaInicio),
      guia5_ej9(fechaInicio)
    ]
  }

def guia6(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia6",
    "nombre":"Práctica 6 - Alternativas Condicionales",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(6, 39086, "25/P6.%20Alternativas%20Condicionales.pdf"),
    ]
  }

def guia7(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia7",
    "nombre":"Práctica 7 - Funciones Simples",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(7, 39099, "23/P7.%20Funciones%20simples.pdf"),
    ]
  }

def guia8(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia8",
    "nombre":"Práctica 8 - Repetición Condicional y Recorridos",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(8, 39117, "19/P8.%20Repetici%C3%B3n%20condicional%2C%20recorridos.pdf"),
    ]
  }

def guia9(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia9",
    "nombre":"Práctica 9 - Variables y Funciones con Procesamiento",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(9, 39139, "18/P9.%20Variables%20y%20Funciones%20con%20Procesamiento.pdf"),
    ]
  }

def guiaI1(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guiaI1",
    "nombre":"Práctica integradora de Recorridos",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía("I1", 39223, "7/Gobs-Man%20%28Recorridos%29.pdf"),
    ]
  }

def guiaI2(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guiaI2",
    "nombre":"Práctica integradora de Funciones Simples y Con Procesamiento, Alternativa de Expresiones y Variables",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía("I2", 39222, "4/Ms.%20Gobs-Man%20%28Funciones%20simples%20y%20con%20procesamiento%29%20%5B2023-04-24%5D.pdf"),
    ]
  }

def guia10(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia10",
    "nombre":"Práctica 10 - Tipos de Datos Personalizados",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(10, 39158, "19/P10.%20Tipos%20Personalizado.pdf"),
    ]
  }

def guia11(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia11",
    "nombre":"Práctica 11 - Listas",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía(11, 39180, "11/P11.%20Listas.pdf"),
    ]
  }

def guiaI3(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guiaI3",
    "nombre":"Ejercicios Integradores",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía("I3", 39230, "8/Pr%C3%A1ctica%2011%20-%20Ejercicios%20Integradores%20%5B2023-11-06%5D.pdf"),
    ]
  }

def guiaI4(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guiaI4",
    "nombre":"Práctica integradora de Registros y Listas",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía("I4", 39229, "3/Comidas%20Gobianas%20%5B2023-11-06%5D.pdf"),
    ]
  }

def guiaI5(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guiaI5",
    "nombre":"Compumundo Hiper Mega Red",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      linkGuía("I5", 39228, "2/Compumundo%20Hiper%20Mega%20Red%20%5B2023-11-06%5D.pdf"),
    ]
  }

def linkGuía(n, mId, l):
  return {
    "tipo":"LINK",
    "id":"linkGuia" + str(n),
    "nombre":"Guía en pdf",
    "url":"https://aulas.gobstones.org/pluginfile.php/" + str(mId) + "/mod_resource/content/" + l
  }

CURSOS = {
  "inpr_unq_2026_s1":{
    "nombre":"Introducción a la Programación - UNQ (2026s1)",
    "anio":"2026",
    "edicion":"Primer Semestre",
    "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Informática, Tecnicatura en Programación Informática y Licenciatura en Bioinformática de la Universidad Nacional de Quilmes",
    "responsable":{
      "nombre":"Equipo de Intro",
      "contacto":"tpi-doc-inpr (AT) listas.unq.edu.ar"
    },
    "institucion":"Universidad Nacional de Quilmes (UNQ)",
    "lenguaje":"Gobstones",
    "lenguaje_display":"none",
    "analisisCodigo":[
      # {"key":"CMD_X_LINE"},
      # {"key":"INDENT"},
      {"key":"NEST_CMD","max":1}
    ],
    "actividades":[
      guia1("16/3/2026-8:00"),
      guia2("23/3/2026-8:00"),
      guia3("30/3/2026-8:00"),
      guia4("30/3/2026-8:00"),
      guia5("6/4/2026-8:00"),
      guia6("13/4/2026-8:00"),
      guia7("13/4/2026-8:00"),
      guia8("20/4/2026-8:00"),
      guia9("27/4/2026-8:00"),
      guiaI1("4/5/2026-8:00"),
      guiaI2("4/5/2026-8:00"),
      guia10("11/5/2026-8:00"),
      guia11("18/5/2026-8:00"),
      guiaI3("1/6/2026-8:00"),
      guiaI4("1/6/2026-8:00"),
      guiaI5("1/6/2026-8:00")
    ],
    "planilla":{
      "url":"1FAIpQLScBYC_P5dbFA0v9e-GDTw65KMFn5PIM9IX0jZmHSTUXdyW5oA",
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
  # "inpr_unq_2025_s1":{
  #   "nombre":"Introducción a la Programación - UNQ (2025s1)",
  #   "anio":"2025",
  #   "edicion":"Primer Semestre",
  #   "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Informática, Tecnicatura en Programación Informática y Licenciatura en Bioinformática de la Universidad Nacional de Quilmes",
  #   "responsable":{
  #     "nombre":"Equipo de Intro",
  #     "contacto":"tpi-doc-inpr (AT) listas.unq.edu.ar"
  #   },
  #   "institucion":"Universidad Nacional de Quilmes (UNQ)",
  #   "lenguaje":"Gobstones",
  #   "lenguaje_display":"none",
  #   "analisisCodigo":[
  #     {"key":"CMD_X_LINE"},
  #     {"key":"INDENT"},
  #     {"key":"NEST_CMD","max":1}
  #   ],
  #   "actividades":[
  #     rosa_de_los_vientos("21/3/2025"),
  #     ajedrez_1("28/3/2025"),
  #     escalera_1("4/4/2025"),
  #     mayusculas_recargado("11/4/2025"),
  #     rutera_1("18/4/2025"),
  #     rutera_2("18/4/2025"),
  #     superGobi64_1("25/4/2025"),
  #     gobFS_1("2/5/2025"),
  #     superGobi64_2("9/5/2025")
  #   ],
  #  "planilla":{
  #    "url":"1FAIpQLSeJRA1urVZ81AhWS73Z66G0p_hAujXLR6hirdc3cVq3LuKAtw",
  #    "campos":{
  #      "usuario":"9867257",
  #      "actividad":"1165966175",
  #      "respuesta":"1778184894",
  #      "resultado":"1496208069",
  #      "duracion":"1460244707"
  #    }
  #  }
  # }
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
