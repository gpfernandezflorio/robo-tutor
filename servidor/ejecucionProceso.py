import os, sys, pwd
from subprocess import Popen
import signal
import resource

USER_RT = 'rtTest'
MEM_MAX_MB = 10 * 1024
MEM_MAX_KB = MEM_MAX_MB * 1024
MEM_MAX_B =  MEM_MAX_KB * 1024

class Runner(object):
  def __init__(self):
    self.proceso_en_ejecucion = None
  def run(self, comandoAEjecutar, fOut, fErr, ruta):
    # print(comandoAEjecutar)
    self.proceso_en_ejecucion = Popen(comandoAEjecutar, stdout=fOut, stderr=fErr, universal_newlines=True, shell=True
      , preexec_fn=lambda: inicialización(ruta)
      # , user=USER_RT
    )
    return self.proceso_en_ejecucion
  def end(self):
    if not (self.proceso_en_ejecucion is None):
      try:
        os.killpg(os.getpgid(self.proceso_en_ejecucion.pid), signal.SIGTERM)
        self.proceso_en_ejecucion.kill()
        self.proceso_en_ejecucion.terminate()
      except Exception as e:
        pass
      self.proceso_en_ejecucion = None

def handler_timeout(runner):
  runner.end()

def inicialización(ruta):
  os.chdir(ruta)
  if LOCAL:
    return
  os.setsid()
  # os.system("ulimit -v " + str(MEM_MAX_KB))
  resource.setrlimit(resource.RLIMIT_AS, (MEM_MAX_B, MEM_MAX_B))
  resource.setrlimit(resource.RLIMIT_RSS, (MEM_MAX_B, MEM_MAX_B))
  # resource.setrlimit(resource.RLIMIT_STACK, (MEM_MAX_B, MEM_MAX_B))
  # resource.setrlimit(resource.RLIMIT_DATA, (MEM_MAX_B, MEM_MAX_B))
  user_info = pwd.getpwnam(USER_RT)
  os.setgid(user_info.pw_gid)
  os.setuid(user_info.pw_uid)

def LanzarComando(cmd, ruta, RUTA_STDOUT, RUTA_STDERR, timeout):
  runner = Runner()
  if not (timeout is None):
    signal.signal(signal.SIGALRM, lambda s, f: handler_timeout(runner))
    signal.alarm(timeout)
  fOut = open(RUTA_STDOUT,'w')
  fErr = open(RUTA_STDERR,'w')
  comandoAEjecutar = cmd
  # comandoAEjecutar = "sudo -u " + USER_RT + " " + comandoAEjecutar
  errcode = runner.run(comandoAEjecutar, fOut, fErr, ruta).wait()
  if not (timeout is None):
    signal.alarm(0)
  fOut.close()
  fErr.close()
  exit(errcode)

LOCAL = False

if __name__ == '__main__':
  cmd = sys.argv[1][1:-1]
  ruta = sys.argv[2]
  LOCAL = sys.argv[3] == "LOCAL"
  timeout = int(sys.argv[4]) if len(sys.argv) > 4 else None
  RUTA_STDOUT = os.path.join(ruta, 'stdout.out')
  RUTA_STDERR = os.path.join(ruta, 'stderr.out')
  LanzarComando(cmd, ruta, RUTA_STDOUT, RUTA_STDERR, timeout)
