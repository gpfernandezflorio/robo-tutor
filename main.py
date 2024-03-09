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

otropy = 'python' if py == 'python3' else 'python3'

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

def a_eliminar(pids, s):
  for p in pids:
    if s.endswith(py + " server.py -p80" + str(50+p)) or s.endswith(otropy + " server.py -p80" + str(50+p)):
      return True
  return False

def kill_previous(pids):
  from subprocess import PIPE, Popen
  p = Popen('ps -x', stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
  out = p.communicate()[0]
  # print(out)
  for s in out.split('\n'):
    if a_eliminar(pids, s):
      pid = obtener_pid(s)
      if not (pid is None):
        if int(pid) != os.getpid():
          print("kill " + pid)
          os.system("kill -9 " + pid)

async def main(i):
  process = await asyncio.create_subprocess_exec(py, 'server.py', '-p80' + str(50+i))
  print(f'subprocess: {process}')

pids = []
if len(sys.argv) > 1:
  for x in sys.argv:
    try:
      p = int(x)
      pids.append(p)
    except ValueError:
      continue
if len(pids) == 0:
  pids = [0,1,2,3,4,5,6,7,8,9,10]

kill_previous(pids)

if len(sys.argv) > 1 and 'x' in sys.argv:
  exit(0)

os.chdir('servidor')
for i in pids:
  asyncio.run(main(i))
