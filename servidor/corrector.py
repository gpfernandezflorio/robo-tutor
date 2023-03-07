def run_code(jsonObj, v):
    if ("src" in jsonObj):
        code = jsonObj["src"]
        if (v):
            print(code)
        try:
            exec(code)
        except Exception as e:
            if (v):
                mostrar_excepcion(e)
            return {"resultado":"Except", "error":str(e)}
        return {"resultado":"OK"}
    return {"resultado":"Error", "error":"Falta src"}

def mostrar_excepcion(e):
    res = str(e)
    tb = e.__traceback__
    while not (tb is None):
        res += "\n" + tb.tb_frame.f_code.co_filename + ":" + tb.tb_frame.f_code.co_name + " " + str(tb.tb_lineno)
        tb = tb.tb_next
    return res
