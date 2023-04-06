v = {"a": 0, "r": 0, "n": 0, "v": 0} # Celda vacía
r = {"a": 0, "r": 1, "n": 0, "v": 0} # Celda con una roja
a = {"a": 1, "r": 0, "n": 0, "v": 0} # Celda con una azul
def rs(x): # Celda con varias rojas
    return {"a": 0, "r": x, "n": 0, "v": 0}
def ns(x): # Celda con varias negras
    return {"a": 0, "r": 0, "n": x, "v": 0}
def ed(h,d=0,a=0): # Edificio con h pisos, d departamentos por piso y a ambientes por departamento
    return {"a": 0, "r": h, "n": 0, "v": 1}

def dame_cursos(verb):
    return {"cursos":{
        "inpr_unq_2023_s1":{
            "nombre":"Introducción a la Programación - UNQ (2023s1)",
            "lenguaje":"Gobstones",
            "lenguaje_display":"none",
            "ejs":[
              {
                "nombre":"Presente 10/4",
                "enunciado":"-",
                "pre":"program{...}",
                "run_data":[]
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
