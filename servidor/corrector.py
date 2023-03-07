import inspect

def run_code(jsonObj, v):
    if (not ("src" in jsonObj)):
        return {"resultado":"Error", "error":"Falta src"}
    if (not ("lenguaje" in jsonObj)):
        return {"resultado":"Error", "error":"Falta lenguaje"}
    if (jsonObj["lenguaje"] != "Python"):
        return {"resultado":"Error", "error":"Lenguaje desconocido: " + jsonObj["lenguaje"]}
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
            exec(code)
        except Exception as e:
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

def mostrar_excepcion(e):
    res = str(e)
    tb = e.__traceback__
    while not (tb is None):
        res += "\n" + tb.tb_frame.f_code.co_filename + ":" + tb.tb_frame.f_code.co_name + " " + str(tb.tb_lineno)
        tb = tb.tb_next
    print(e)
