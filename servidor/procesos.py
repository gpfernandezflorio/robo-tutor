# -*- coding: utf-8 -*-

import os, pwd
from subprocess import Popen
import signal
import resource

proceso_en_ejecucion = None

def handler_timeout(s, f):
  global proceso_en_ejecucion
  if not (proceso_en_ejecucion is None):
    try:
      os.killpg(os.getpgid(proceso_en_ejecucion.pid), signal.SIGTERM)
      proceso_en_ejecucion.kill()
      proceso_en_ejecucion.terminate()
    except Exception as e:
      pass
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

RUTA_BASE = '/rtTest'
RUTA_JAIL = os.path.join(RUTA_BASE, 'jail')
USER_RT = 'rtTest'
MEM_MAX_MB = 1024
MEM_MAX_KB = MEM_MAX_MB * 1024
MEM_MAX_B =  MEM_MAX_KB * 1024

def sacarPrivilegios():
  os.setsid()
  # os.system("ulimit -v " + str(MEM_MAX_KB))
  os.chdir(RUTA_JAIL)
  resource.setrlimit(resource.RLIMIT_AS, (MEM_MAX_B, MEM_MAX_B))
  resource.setrlimit(resource.RLIMIT_RSS, (MEM_MAX_B, MEM_MAX_B))
  # resource.setrlimit(resource.RLIMIT_STACK, (MEM_MAX_B, MEM_MAX_B))
  # resource.setrlimit(resource.RLIMIT_DATA, (MEM_MAX_B, MEM_MAX_B))
  # user_info = pwd.getpwnam(USER_RT)
  # os.setgid(user_info.pw_gid)
  # os.setuid(user_info.pw_uid)

def ejecutar(cmd):
  global proceso_en_ejecucion
  fOut = open('stdout.out','w')
  fErr = open('stderr.out','w')
  comandoAEjecutar = cmd
  # comandoAEjecutar = "sudo -u " + USER_RT + " " + comandoAEjecutar
  p = Popen(comandoAEjecutar, stdout=fOut, stderr=fErr, universal_newlines=True, shell=True, preexec_fn=sacarPrivilegios
    # , user=USER_RT
  )
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

def rutaJail(ruta):
  return os.path.join(RUTA_JAIL, ruta)
