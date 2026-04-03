# SERVER = "http://192.168.0.11:8050" # LOCAL
SERVER = "http://157.92.26.79:8060" # RT

import requests
import json

todosLosIntentos = []

def nombreRepeticiónSimple():
  return "repetición simple"

def idConMayus():
  return "un identificador con mayúsculas"

def errorFaltaDef(q, l):
  return "Se esperaba una definición (de programa, función, procedimiento, o tipo). Se encontró: "+q+".\nLínea: "+str(l)

def errorFaltaPrograma():
  return 'El código debe tener una definición de "program { ... }".'

def errorSacar(c, l):
  return "No se puede sacar una bolita de color "+c+": no hay bolitas de ese color.\nLínea: "+str(l)

def errorLlaveNoCierra(l):
  return 'Se encontró una llave abierta "{" pero nunca se cierra.\nLínea: '+str(l)

def errorProcNoDef(n):
  return 'El procedimiento "'+n+'" no está definido.'

def errorDobleDefProc(n, d1, d2):
  return 'El procedimiento "'+n+'" está definido dos veces: en '+("(?)" if (d1 is None) else ("la línea "+str(d1)))+" y en la línea "+str(d2)+"\nLínea: "+str(d2)

def errorTimeout():
  return "La ejecución demoró más de lo permitido"

def errorNombre(n):
  return "No está permitido usar '"+n+"'"

def errorImport():
  return "No está permitido importar módulos"

def errorRaise():
  return "No está permitido generar excepciones"

def errorConcepto(n):
  return "No está permitido usar "+n

def calidadNest():
  return "No está bueno anidar comandos compuestos"

cursos = [{
  "id":"inpr_unq_2026_s1",
  "l":"Gobstones",
  "ejs":[{
    "id":"guia1_ej1",
    "i":[{"src":"","res":"NO"},
      {"src":"Sacar(Rojo)\nPoner(Verde)","res":"Except","error":errorFaltaDef(idConMayus(), 1)},
      {"src":"program{}","res":"NO"},
      {"src":"program{Sacar(Verde)}","res":"Except","error":errorSacar("Verde", 1)},
      {"src":"program{\nSacar(Verde)\n}","res":"Except","error":errorSacar("Verde", 2)},
      {"src":"program{\nSacar(Rojo)\nPoner(Verde)\n}","res":"OK"},
      {"src":"program{\nPoner(Verde)\nSacar(Rojo)\n}","res":"OK"}
    ]
  },{
    "id":"guia2_ej2a",
    "i":[{"src":"procedure DibujarRectánguloRojoYNegroDe5x3() {","res":"Except","error":errorLlaveNoCierra(1)},
      {"src":"procedure DibujarRectánguloRojoYNegroDe5x3() {}","res":"NO"},
      {"src":"procedure DibujarRectánguloRojoYNegroDe5x3() {\nDibujarLíneaRojaYNegraDeTamaño5HaciaElEste()\n}","res":"NO"},
      {"src":"procedure DibujarRectánguloRojoYNegroDe5x3() {\nDibujarLíneaRojaYNegraDeTamaño5HaciaElEste()\n}\n"+\
        "procedure DibujarLíneaRojaYNegraDeTamaño5HaciaElEste(){}",
        "res":"Except","error":errorDobleDefProc("DibujarLíneaRojaYNegraDeTamaño5HaciaElEste", None, 4)
      },
      {"src":"procedure A(){}\n\nprocedure A(){}","res":"Except","error":errorDobleDefProc("A", 1, 3)}
    ]
  },{
    "id":"guia2_ej5",
    "i":[{"src":"","res":"Except","error":errorProcNoDef("RegistrarElDíaDeLaMemoria")},
      {"src":"procedure RegistrarElDíaDeLaMemoria() {\n  repeat(24) {Poner(Azul)}\n  repeat(3) {Poner(Rojo)}\n  repeat(1976) {Poner(Verde)}\n}",
        "res":"Calidad","error":errorConcepto(nombreRepeticiónSimple())
      },
      {"src":"procedure RegistrarElDíaDeLaMemoria() {\n  PonerDía()\n  PonerMes()\n  PonerAño()\n}\n\n" +\
        "procedure PonerDía() {repeat(24){Poner(Azul)}}\n\n" +\
        "procedure PonerMes() {repeat(3){Poner(Rojo)}}\n\n" +\
        "procedure PonerAño() {repeat(1976){Poner(Verde)}}",
        "res":"Calidad","error":errorConcepto(nombreRepeticiónSimple())
      },
      {"src":"procedure RegistrarElDíaDeLaMemoria() {\n  Poner20A()Poner4A()Mover(Este)\n  Poner3R()Mover(Este)\n"+\
        "  Poner1000V()Poner900V()Poner70V()Poner6V()\n  Mover(Oeste)Mover(Oeste)\n}\n\n" +\
        "procedure Poner20A() {Poner10A()Poner10A()}\n\n" +\
        "procedure Poner10A() {Poner4A()Poner4A()Poner2A()}\n\n" +\
        "procedure Poner4A() {Poner2A()Poner2A()}\n\n" +\
        "procedure Poner2A() {Poner(Azul)Poner(Azul)}\n\n" +\
        "procedure Poner3R() {Poner(Rojo)Poner(Rojo)Poner(Rojo)}\n\n" +\
        "procedure Poner1000V() {Poner500V()Poner500V()}\n\n" +\
        "procedure Poner900V() {Poner500V()Poner100V()Poner100V()Poner100V()Poner100V()}\n\n" +\
        "procedure Poner500V() {Poner100V()Poner100V()Poner100V()Poner100V()Poner100V()}\n\n" +\
        "procedure Poner100V() {Poner50V()Poner50V()}\n\n" +\
        "procedure Poner70V() {Poner50V()Poner10V()Poner10V()}\n\n" +\
        "procedure Poner50V() {Poner10V()Poner10V()Poner10V()Poner10V()Poner10V()}\n\n" +\
        "procedure Poner10V() {Poner5V()Poner5V()}\n\n" +\
        "procedure Poner6V() {Poner5V()Poner(Verde)}\n\n" +\
        "procedure Poner5V() {Poner(Verde)Poner(Verde)Poner(Verde)Poner(Verde)Poner(Verde)}",
        "res":"OK"
      }
    ]
  },{
    "id":"guia2_ej7a",
    "i":[{"src":"","res":"Except","error":errorFaltaPrograma()},
      {"src":"procedure DibujarBase() {}","res":"Except","error":errorDobleDefProc("DibujarBase",None,1)},
      {"src":"program {DibujarBase()}","res":"NO"},
      {"src":"program {\nDibujarBase()Mover(Este)Mover(Norte)\nDibujarMedio()Mover(Este)Mover(Norte)\nDibujarPunta()\n" +\
        "Mover(Oeste)Mover(Oeste)Mover(Sur)Mover(Sur)\n}","res":"OK"
      }
    ]
  },{
    "id":"guia5_ej2",
    "i":[{"src":"procedure Mover_SegúnColor_(d,c) {\n  repeat(nroBolitas(c)) {Mover(d)}\n}","res":"OK"}
    ]
  },{
    "id":"guia5_ej5b",
    "i":[{"src":"procedure PelearLaBatalla() {\nrepeat(nroBolitas(Rojo) div 2) {\nE()\n}\n}\n\nprocedure E() {\n" +\
      "Sacar(Rojo)Sacar(Rojo)\nSacar(Negro)Sacar(Negro)Sacar(Negro)\n}","res":"OK"}
    ]
  },{
    "id":"guia5_ej8",
    "i":[{"src":"procedure DibujarBandaDeAlto_YAncho_DeColor_(h,w,c){\nrepeat(w-1) {\nL(h,c) Mover(Este)Mover(Norte)\n}\n" +\
        "L(h,c)\nrepeat(w-1) {Mover(Oeste)Mover(Sur)}\n}\n\nprocedure L(h,c) {\n  repeat(h-1) {Poner(c)Mover(Norte)}\n  Poner(c)" +\
        "\n  repeat(h-1) {Mover(Sur)}\n}","res":"OK"},
      {"src":"procedure DibujarBandaDeAlto_YAncho_DeColor_(h,w,c){\nrepeat(w-1) {\n  repeat(h-1) {Poner(c)Mover(Norte)}\n  Poner(c)" +\
        "\n  repeat(h-1) {Mover(Sur)}\nMover(Este)Mover(Norte)\n}\n  repeat(h-1) {Poner(c)Mover(Norte)}\n  Poner(c)" +\
        "\n  repeat(h-1) {Mover(Sur)}\nrepeat(w-1) {Mover(Oeste)Mover(Sur)}\n}","res":"Calidad","error":calidadNest()}
    ]
  },{
    "id":"guia5_ej9",
    "i":[{"src":"procedure PasarPalabraActualAMayúsculas() {\nrepeat(nroBolitas(Rojo)) {\nMover(Este)\n" +\
        "Poner_AlNorte(nroBolitas(Negro)-32)\n}\nIrAlBorde(Oeste)\n}\n\nprocedure Poner_AlNorte(k) {\nMover(Norte)\n" +\
        "repeat (k) {Poner(Negro)}\nMover(Sur)\n}","res":"OK"},
    ]
  }]
},{
  "id":"alc_prueba",
  "l":"Python",
  "ejs":[{
    "id":"error_relativo",
    "i":[{"src":"def error_relativo(x,y):\n  return 0","res":"NO"},
      {"src":"while True:\n  pass","res":"Except","error":errorTimeout()},
      {"src":"print(1)","res":"EVIL","error":errorNombre("print")},
      {"src":"exit(1)","res":"EVIL","error":errorNombre("exit")},
      {"src":"import os","res":"EVIL","error":errorImport()},
      {"src":"raise 'X'","res":"EVIL","error":errorRaise()},
      {"src":"__import__('os')","res":"EVIL","error":errorNombre("__import__")},
      {"src":"().__class__","res":"EVIL","error":errorNombre("__class__")}
    ]
  }]
}]

n = 0
for c in cursos:
  for ej in c["ejs"]:
    n += len(ej["i"])

desde = n # Cambiarlo por un número más chico para ignorar los primeros tests

for c in cursos:
  for ej in c["ejs"]:
    for i in ej["i"]:
      res = {"resultado":i["res"]}
      if "error" in i:
        res["error"] = i["error"]
      todosLosIntentos.append({
        "send":{
          "src":i["src"],
          "lenguaje":c["l"],
          "usuario":"estudiante_ficticio",
          "contrasenia":"123456",
          "curso":c["id"],
          "actividad":ej["id"]
        },
        "res":res
      })

def sendCode(data):
  r = requests.post(SERVER + "/code", data=json.dumps(data))
  return r.json()

def Intentar(intento):
  global n
  print(n)
  resultado = sendCode(intento["send"])
  esperado = intento["res"]
  res = Validar(resultado, esperado)
  if not (res is None):
    print("\n---\n")
    print(intento)
    print("\n---\n")
    print(res)
    exit()
  n -= 1

def Validar(resultado, esperado):
  if resultado["resultado"] == esperado["resultado"]:
    if "error" in esperado:
      if "error" in resultado:
        if resultado["error"] == esperado["error"]:
          return None
        return "Se esperaba que el error fuera '" + esperado["error"] + "' pero es '" + resultado["error"] + "'"
      return "Se esperaba que el resultado tuviera un mensaje de error pero no es así"
    elif "error" in resultado:
      if not ("error" in esperado):
        return "El resultado tiene un mensaje de error que no se esperaba: " + resultado["error"]
    return None
  return "Se esperaba RES=" + esperado["resultado"] + " pero se obtuvo:" + resultado["resultado"] + "\n("+str(resultado)+")"

for intento in todosLosIntentos:
  if desde < n:
    n -= 1
  else:
    Intentar(intento)
