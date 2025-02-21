import datetime

def fecha(s):
  partes = s.split("-")
  partes_f = partes[0].split("/")
  anio = int(partes_f[2])
  mes = int(partes_f[1])
  dia = int(partes_f[0])
  horas = 0
  minutos = 0
  segundos = 0
  if len(partes) > 1:
    partes_h = partes[1].split(":")
    horas = int(partes_h[0])
    if len(partes_h) > 1:
      minutos = int(partes_h[1])
      if len(partes_h) > 2:
        segundos = int(partes_h[2])
  return datetime.datetime(anio, mes, dia, horas, minutos, segundos)

def fueraDeFecha(obj):
  hoy = datetime.datetime.now()
  if "desde" in obj and esUnaFecha(obj["desde"]) and hoy < fecha(obj["desde"]):
    return True
  if "hasta" in obj and esUnaFecha(obj["hasta"]) and hoy > fecha(obj["hasta"]):
    return True
  return False

def esUnNumero(s):
  return s.isnumeric()

def esUnaFecha(s):
  partes = s.split("-")
  partes_f = partes[0].split("/")
  return len(partes_f) == 3 and esUnNumero(partes_f[0]) and esUnNumero(partes_f[1]) and esUnNumero(partes_f[2])