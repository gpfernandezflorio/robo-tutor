import asyncio
import sys, os

py_version = sys.version_info.major
if py_version != 3:
  print("Ejecutame con python 3")
  exit(0)

py = sys.executable.split('/')[-1]
if not (py in ['python', 'python3']):
  print("Error en la ruta ejecutable: " + py)
  exit(0)

def esEntero(x):
  try:
    int(x)
  except ValueError:
    return False
  return True

def obtener_pid(s):
  for x in s.split(' '):
    if len(x) > 0 and esEntero(x):
      return x
  return None

def kill_previous():
  from subprocess import PIPE, Popen
  p = Popen('ps', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
  out = p.communicate()[0]
  print(out)
  for s in out.split('\n'):
    if s.endswith(py):
      pid = obtener_pid(s)
      if not (pid is None):
        if int(pid) != os.getpid():
          print("kill " + pid)
          os.system("kill -9 " + pid)

async def main():
  process = await asyncio.create_subprocess_exec(py, 'servidor/server.py', '-p80' + str(50+i))
  print(f'subprocess: {process}')

kill_previous()
for i in range(11):
  asyncio.run(main())