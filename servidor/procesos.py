# -*- coding: utf-8 -*-

import os
from subprocess import Popen
import signal

proceso_en_ejecucion = None

def handler_timeout(s, f):
  global proceso_en_ejecucion
  if not (proceso_en_ejecucion is None):
    proceso_en_ejecucion.kill()
    proceso_en_ejecucion = None

signal.signal(signal.SIGALRM, handler_timeout)

def ejecutarConTimeout(comando, timeout):
  global proceso_en_ejecucion
  signal.alarm(timeout)
  errcode, salida, falla = ejecutar(comando)
  duracion = timeout - signal.alarm(0)
  if proceso_en_ejecucion is None:
    return {"resultado":"TIMEOUT"}
  proceso_en_ejecucion = None
  return {
    "resultado":"OK",
    "errcode":errcode,
    "salida":salida,
    "falla":falla,
    "duracion":duracion
  }

def sacarPrivilegios():
  os.setuid(int(os.environ['UID']) if 'UID' in os.environ else 1000)

def ejecutar(cmd):
  global proceso_en_ejecucion
  fOut = open('stdout.out','w')
  fErr = open('stderr.out','w')
  p = Popen(cmd, stdout=fOut, stderr=fErr, universal_newlines=True, shell=True, preexec_fn=sacarPrivilegios)
  proceso_en_ejecucion = p
  errcode = p.wait()
  fOut.close()
  fErr.close()
  stdout = ""
  stderr = ""
  fOut = open('stdout.out','r')
  for line in fOut.read():
      stdout += line
  fOut.close()
  fErr = open('stderr.out','r')
  for line in fErr.read():
      stderr += line
  fErr.close()
  return errcode, stdout, stderr