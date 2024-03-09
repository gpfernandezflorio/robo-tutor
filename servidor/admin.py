import os, sys

PSW = "secuenciadepasos"

def admin_reset(jsonObj, v):
  if not ("psw" in jsonObj) or jsonObj["psw"] != PSW:
    return {"resultado":"Error", "error":"Contraseña incorrecta"}
  args = ""
  if "i" in jsonObj:
    args = " " + str(jsonObj["i"])
  py = sys.executable.split('/')[-1]
  os.chdir('..')
  # os.system(py + " main.py")
  from subprocess import Popen
  Popen(py + " main.py" + args, universal_newlines=True, shell=True)
  os.chdir('servidor')
  return {"resultado":"OK"}