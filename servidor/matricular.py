pasosAEjecutar = { # Cambiar los booleanos de este objeto para decidir qué pasos ejecutar (ver la descripción de cada paso en los comentarios de main).
  1:True,
  2:True,
  3:True,
  4:True
}

archivoDelSistema = 'usersDB.json'

# Importante, para usar cuentas de GMail:
  # https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833
mensaje = '''
Hola,

El campus REDA se encuentra en https://reda-ar.github.io/campus/.

Tus credenciales son:
Usuario: MAIL
Contraseña: CLAVE

Saludos.
'''

def main(): # Cómo usar este archivo: 
  # 0: Conseguir un archivo con la lista de nombres de usuarios de un curso.
  archivoUsuariosCurso = "matricula/exactas_programa_2025_V_TM.json"
  # 1: Ejecutar FiltrarEstudiantesExistentes para obtener en un nuevo archivo sólo los usuarios que no están en el sistema.
  if (pasosAEjecutar[1]):
    FiltrarEstudiantesExistentes(
      archivoUsuariosCurso, # Un objeto con roles y en cada rol una lista con los nombres de los usuarios del curso que tienen ese rol. Ej: {"docente:["estudiante_fictio@gmail.com", ...], "estudiante":[...]}
      "nuevosUsuarios.json" # Una lista con los usuarios en el archivo anterior pero quitando a los usuarios que ya estaban antes en el sistema
    )
  # 2: Ejecutar GenerarClaves para obtener un nuevo archivo con las contraseñas de cada nuevo usuario.
  if (pasosAEjecutar[2]):
    GenerarClaves(
      "nuevosUsuarios.json", # La lista con los nombres de los usuarios que no están en el sistema. Ej: ["estudiante_fictio@gmail.com", ...]
      "usuariosConClaves.json" # Un objeto cuyas claves son los nombres del archivo anterior y sus valores los objetos que los representan,
        # incluyendo sus contraseñas (por ahora eso es todo). Ej: {"estudiante_fictio@gmail.com":{"contrasenia":"123456"}, ...}
    )
  # 3: Ejecutar AgregarUsuariosAlSistema para agregar a los nuevos usuarios y sus contraseñas al sistema.
  if (pasosAEjecutar[3]):
    AgregarUsuariosAlSistema(
      "usuariosConClaves.json" # Un objeto cuyas claves son nombres de usuarios y sus valores los objetos que los representan,
        # incluyendo sus contraseñas (por ahora eso es todo). Ej: {"estudiante_fictio@gmail.com":{"contrasenia":"123456"}, ...}
    )
  # 4: Ejecutar MandarMailsConClave para mandarles por mail a los nuevos usuarios sus contraseñas.
    # NOTA: No me está funcionando desde Python así que mejor genero un csv para importar en Google Spreadsheets y usar Appscripts para mandar los mails.
  if (pasosAEjecutar[4]):
    MandarMailsConClave(
      "usuariosConClaves.json", # Un objeto cuyas claves son nombres de usuarios y sus valores los objetos que los representan,
        # incluyendo sus contraseñas (por ahora eso es todo). Ej: {"estudiante_fictio@gmail.com":{"contrasenia":"123456"}, ...}
      "usuariosConClaves.csv" # Un csv para importar en Google Spreadsheets y usar Appscripts para mandar los mails.
    )

def contenidoArchivo(ruta):
  # PRE: el archivo existe
  f = open(ruta, 'r')
  contenido = json.loads(f.read())
  f.close()
  return contenido

def EscribirJson(ruta, contenido):
  EscribirArchivo(ruta, json.dumps(contenido))

def EscribirArchivo(ruta, contenido):
  f = open(ruta, 'w')
  f.write(contenido)
  f.close()

def todosLosUsuarios():
  if os.path.isfile(archivoDelSistema):
    return contenidoArchivo(archivoDelSistema)
  return {}

def FiltrarEstudiantesExistentes(archivoEntrada, archivoSalida):
  # archivoEntrada tiene que ser un json con los roles y, en cada rol una lista de strings correspondientes a los nombres de usuario (sus mails)
  if not os.path.isfile(archivoEntrada):
    print("Error: no se encuentra el archivo " + archivoEntrada)
    exit()
  usuariosCurso = []
  obj = contenidoArchivo(archivoEntrada)
  if not isinstance(obj, dict):
    print("Error: se esperaba un diccionario en el archivo " + archivoEntrada)
    exit()
  for rol in obj:
    if not isinstance(obj[rol], list):
      print("Error: se esperaba una lista en cada campo del archivo " + archivoEntrada)
      exit()
    usuariosCurso = usuariosCurso + obj[rol]
  for u in usuariosCurso:
    if not isinstance(u, str):
      print("Error: se esperaba que todos los elementos de la lista sean strings en el archivo " + archivoEntrada)
      exit()
  usuariosAnteriores = todosLosUsuarios()
  nuevosUsuarios = []
  usuariosYaExistentes = []
  for u in usuariosCurso:
    if u in usuariosAnteriores:
      usuariosYaExistentes.append(u)
    else:
      nuevosUsuarios.append(u)
  print("Se detectaron los siguientes usuarios nuevos:")
  for u in nuevosUsuarios:
    print("    " + u)
  print("Se detectaron los siguientes usuarios ya existentes:")
  for u in usuariosYaExistentes:
    print("    " + u)
  EscribirJson(archivoSalida, nuevosUsuarios)
  print("Nuevos usuarios guardados en " + archivoSalida)

def GenerarClaves(archivoEntrada, archivoSalida):
  # archivoEntrada tiene que ser un json con una lista de strings correspondientes a los nombres de usuario (sus mails)
  if not os.path.isfile(archivoEntrada):
    print("Error: no se encuentra el archivo " + archivoEntrada)
    exit()
  nuevosUsuarios = contenidoArchivo(archivoEntrada)
  if not isinstance(nuevosUsuarios, list):
    print("Error: se esperaba una lista en el archivo " + archivoEntrada)
    exit()
  for u in nuevosUsuarios:
    if not isinstance(u, str):
      print("Error: se esperaba que todos los elementos de la lista sean strings en el archivo " + archivoEntrada)
      exit()
  usuariosAnteriores = todosLosUsuarios()
  for u in nuevosUsuarios:
    if u in usuariosAnteriores:
      print("Error: en el archivo " + archivoEntrada + " aparece el usuario " + u + " pero este ya existe en la base de datos actual")
      exit()
  nuevosUsuariosConClave = {}
  for u in nuevosUsuarios:
    nuevosUsuariosConClave[u] = {"contrasenia":claveAleatoria()}
  EscribirJson(archivoSalida, nuevosUsuariosConClave)
  print("Nuevos usuarios con sus claves guardados en " + archivoSalida)

def AgregarUsuariosAlSistema(archivoEntrada):
  # archivoEntrada tiene que ser un json con un objeto cuyas claves son los nombres de los usuarios y sus valores son los objetos que los representan
  usuariosAnteriores = todosLosUsuarios()
  nuevosUsuarios = contenidoArchivo(archivoEntrada)
  for u in nuevosUsuarios:
    usuariosAnteriores[u] = nuevosUsuarios[u]
  EscribirJson(archivoDelSistema, usuariosAnteriores)
  print("Nuevos usuarios de " + archivoEntrada + " agregados al sistema")

def MandarMailsConClave(archivoEntrada, archivoSalida):
  # archivoEntrada tiene que ser un json con un objeto cuyas claves son los nombres de los usuarios y sus valores son los objetos que los representan
  destinatarios = contenidoArchivo(archivoEntrada)
  mailsAMandar = []
  for d in destinatarios:
  #   mailsAMandar.append(mailPara(d, destinatarios[d]))
  # MandarMails(mailsAMandar)
  # print("Enviados los mails con las claves a los usuarios de " + archivoEntrada)
      mailsAMandar.append(d + '\t' + destinatarios[d]["contrasenia"])
  EscribirArchivo(archivoSalida, "mail\tclave\n" + "\n".join(mailsAMandar))
  print("Creado el csv con los nuevos usuarios en " + archivoSalida)

def mailPara(destinatario, informacionAdicional):
  nuevoMail = EmailMessage()
  nuevoMail.set_content(mensajePara(destinatario, informacionAdicional))
  nuevoMail['Subject'] = "Credenciales para el campus REDA"
  nuevoMail['To'] = destinatario
  return nuevoMail

def mensajePara(destinatario, informacionAdicional):
  return mensaje.replace("MAIL", destinatario).replace("CLAVE", informacionAdicional["contrasenia"])

def MandarMails(mailsAMandar):
  from dotenv import load_dotenv
  load_dotenv()
  CUENTA = os.getenv("CUENTA")
  CONTRASENIA = os.getenv("CONTRASENIA")
  SMTP = os.getenv("SMTP")
  PORT = os.getenv("PORT")

  context = ssl.create_default_context()
  with smtplib.SMTP(SMTP, PORT) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(CUENTA, CONTRASENIA)
    for mail in mailsAMandar:
      mail['From'] = CUENTA
      server.sendmail(CUENTA, mail['To'], mail.as_string())

caracteres = "123456789qwertyupasdfghkzxcvbnmMNBVCXZLKJHGFDSAQWERTYUP"
def claveAleatoria():
  clave = ""
  i=0
  while i < random.randint(14,19):
    clave = clave + caracteres[random.randint(0,len(caracteres)-1)]
    i += 1
  return clave

import os, json
# from email.message import EmailMessage
# import smtplib, ssl
import random

if __name__ == '__main__':
  main()
