# -*- coding: utf-8 -*-

import os
from subprocess import Popen
import time

def ejecutarConTimeout(comando, timeout, ruta):
  inicio = time.time()
  errcode, salida, falla = ejecutar(comando, ruta, timeout)
  duracion = time.time() - inicio
  if duracion > timeout:
    return {"resultado":"TIMEOUT"}
  return {
    "resultado":"OK",
    "errcode":errcode,
    "salida":salida,
    "falla":falla,
    "duracion":duracion
  }

def ejecutar(cmd, ruta, timeout=None):
  RUTA_STDOUT = os.path.join(ruta, 'stdout.out')
  RUTA_STDERR = os.path.join(ruta, 'stderr.out')
  comandoAEjecutar = [
    "python3",
    "ejecucionProceso.py",
    '"'+cmd+'"',
    ruta
  ]
  if not (timeout is None):
    comandoAEjecutar.append(str(timeout))
  ejecucion = Popen(comandoAEjecutar)
  errcode = ejecucion.wait()
  stdout = ""
  stderr = ""
  fOut = open(RUTA_STDOUT,'r')
  for line in fOut.read():
    stdout += line
  fOut.close()
  fErr = open(RUTA_STDERR,'r')
  for line in fErr.read():
    stderr += line
  fErr.close()
  return errcode, stdout, stderr