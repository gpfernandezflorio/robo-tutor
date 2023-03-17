# -*- coding: utf-8 -*-

from subprocess import PIPE, Popen
import signal
import inspect
import json
import os

def run_code(jsonObj, v):
    if (not ("src" in jsonObj)):
        if (v):
            print("Falta src")
        return {"resultado":"Error", "error":"Falta src"}
    if (not ("lenguaje" in jsonObj)):
        if (v):
            print("Falta lenguaje")
        return {"resultado":"Error", "error":"Falta lenguaje"}
    if (jsonObj["lenguaje"] == "Python"):
        return run_python(jsonObj, v)
    elif (jsonObj["lenguaje"] == "Gobstones"):
        return run_gobstones(jsonObj, v)
    else:
        if (v):
            print(jsonObj["lenguaje"])
        return {"resultado":"Error", "error":"Lenguaje desconocido: " + jsonObj["lenguaje"]}

def run_python(jsonObj, v):
    run_data = jsonObj["run_data"] if "run_data" in jsonObj else {}
    if (type(run_data) != type([])):
        run_data = [run_data]
    code = jsonObj["src"]
    if (v):
        print(code)
    for run in run_data:
        ## Inicialización
        if "pre" in run:
            try:
                exec(run["pre"])
            except Exception as e:
                if (v):
                    mostrar_excepcion(e)
                return {"resultado":"Error", "error":"Error en el ejercicio"}
        ## Ejecución del código entregado
        try:
            signal.alarm(1)
            exec(code)
            signal.alarm(0)
        except Exception as e:
            signal.alarm(0)
            if (v):
                mostrar_excepcion(e)
            return {"resultado":"Except", "error":str(e)}
        ## Variables definidas
        if "def" in run:
            defs = run["def"]
            if (type(defs) != type([])):
                defs = [defs]
            for d in defs:
                try:
                    eval(d)
                except Exception as e:
                    if (v):
                        mostrar_excepcion(e)
                    return {"resultado":"Falla"}
        ## Aridad de funciones correcta
        if "aridad" in run:
            aridad = run["aridad"]
            for f in aridad:
                try:
                    if (len(inspect.getfullargspec(eval(f)).args) != aridad[f]):
                        return {"resultado":"Falla"}
                except Exception as e:
                    if (v):
                        mostrar_excepcion(e)
                    return {"resultado":"Falla"}
        ## Validación final
        if "post" in run:
            try:
                resultado = eval(run["post"])
            except Exception as e:
                if (v):
                    mostrar_excepcion(e)
                return {"resultado":"Error", "error":"Error en el ejercicio"}
            if (not resultado):
                return {"resultado":"Falla"}
    return {"resultado":"OK"}

def run_gobstones(jsonObj, v):
    run_data = jsonObj["run_data"] if "run_data" in jsonObj else {}
    if (type(run_data) != type([])):
        run_data = [run_data]
    code = jsonObj["src"]
    if (v):
        print(code)
    if "pre" in jsonObj:
        code += jsonObj["pre"]
    ## Código
    f = open('src.txt', 'w')
    f.write(code)
    f.close()
    for run in run_data:
        ## Tablero inicial
        tablero = run["tablero"] if "tablero" in run else tablero_default()
        f = open('board.jboard', 'w')
        f.write(json.dumps(tablero))
        f.close()
        try:
            signal.alarm(1)
            salida, falla = ejecutar("node gobstones-lang/dist/gobstones-lang run -l es -i src.txt -b")
            signal.alarm(0)
        except Exception as e:
            signal.alarm(0)
            if (v):
                mostrar_excepcion(e)
            return {"resultado":"Except", "error":str(e)}
        if len(falla) > 0:
            return {"resultado":"Except", "error":buscar_falla_gobstones(falla)}
        try:
            salida = json.loads(salida)
        except Exception as e:
            if (v):
                mostrar_excepcion(e)
            return {"resultado":"Except", "error":str(e)}
        ## Validar tablero final
        if "post" in run:
            tablero_esperado = run["post"]
            tablero_obtenido = salida
            if not tablero_valido(tablero_esperado) and tablero_valido(tablero_obtenido):
                return {"resultado":"Error", "error":"Error en el ejercicio"}
            cabezal_esperado = tablero_esperado["head"]
            cabezal_obtenido = tablero_obtenido["head"]
            if not cabezal_valido(cabezal_esperado) and cabezal_valido(cabezal_obtenido):
                return {"resultado":"Error", "error":"Error en el ejercicio"}
            if not mismo_cabezal(cabezal_esperado, cabezal_obtenido):
                return {"resultado":"Falla"}
            if not tablero_esperado["width"] == tablero_obtenido["width"] and tablero_esperado["height"] == tablero_obtenido["height"]:
                return {"resultado":"Error", "error":"Error en el ejercicio"}
            tablero_esperado = tablero_esperado["board"]
            tablero_obtenido = tablero_obtenido["board"]
            if not len(tablero_esperado) == len(tablero_obtenido):
                return {"resultado":"Error", "error":"Error en el ejercicio"}
            for x in range(len(tablero_esperado)):
                columna_esperada = tablero_esperado[x]
                columna_obtenida = tablero_obtenido[x]
                if not len(columna_esperada) == len(columna_obtenida):
                    return {"resultado":"Error", "error":"Error en el ejercicio"}
                for y in range(len(columna_esperada)):
                    if not misma_celda(columna_esperada[y], columna_obtenida[y]):
                        return {"resultado":"Falla"}
    return {"resultado":"OK"}

def handler_timeout(s, f):
    raise Exception("La ejecución demoró más de 1 segundo")

signal.signal(signal.SIGALRM, handler_timeout)

def ejecutar(cmd):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return p.communicate()

def tablero_valido(t):
    return all(["head","width","height","board"].map(lambda x : x in t))

def cabezal_valido(h):
    return len(h) == 2

def mismo_cabezal(h1, h2):
    return h1[0] == h2[0] and h1[1] == h2[1]

def misma_celda(c1, c2):
    return c1["a"] == c2["a"] and c1["r"] == c2["r"] and c1["n"] == c2["n"] and c1["v"] == c2["v"]

def tablero_default():
    return {
        "head":[0,0],
        "width":4,
        "height":4,
        "board":list(map(lambda x : columna_default(), [1,2,3,4]))
    }

def columna_default():
    return list(map(lambda x : celda_vacia(), [1,2,3,4]))

def celda_vacia():
    return {
        "a":0,
        "r":0,
        "n":0,
        "v":0
    }

def buscar_falla_gobstones(s):
    for l in s.split('\n'):
        if l.startswith('br [Error]: ') or l.startswith('Pr [Error]: '):
            return l[12:]
    print(s)
    return "?"

def mostrar_excepcion(e):
    res = str(e)
    tb = e.__traceback__
    while not (tb is None):
        res += "\n" + tb.tb_frame.f_code.co_filename + ":" + tb.tb_frame.f_code.co_name + " " + str(tb.tb_lineno)
        tb = tb.tb_next
    print(e)
