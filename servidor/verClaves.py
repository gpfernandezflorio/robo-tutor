archivoDelSistema = 'usersDB.json'

def main(archivoUsuariosCurso):
  if not os.path.isfile(archivoUsuariosCurso):
    print("Error: no se encuentra el archivo " + archivoUsuariosCurso)
    return
  usuariosCurso = []
  obj = contenidoArchivo(archivoUsuariosCurso)
  if not isinstance(obj, dict):
    print("Error: se esperaba un diccionario en el archivo " + archivoUsuariosCurso)
    exit()
  for rol in obj:
    if not isinstance(obj[rol], list):
      print("Error: se esperaba una lista en cada campo del archivo " + archivoUsuariosCurso)
      exit()
    usuariosCurso = usuariosCurso + obj[rol]
  for u in usuariosCurso:
    if not isinstance(u, str):
      print("Error: se esperaba que todos los elementos de la lista sean strings en el archivo " + archivoUsuariosCurso)
      exit()
  usuariosExistentes = todosLosUsuarios()
  for u in usuariosCurso:
    if u in usuariosExistentes:
      print(u + "\t" + usuariosExistentes[u]["contrasenia"])
    else:
      print("ERROR: no se encuentra el usuario " + u + " en la base de datos")
      exit(1)

def contenidoArchivo(ruta):
  # PRE: el archivo existe
  f = open(ruta, 'r')
  contenido = json.loads(f.read())
  f.close()
  return contenido

def todosLosUsuarios():
  if os.path.isfile(archivoDelSistema):
    return contenidoArchivo(archivoDelSistema)
  return {}

import os, sys, json

if __name__ == '__main__':
  if len(sys.argv) == 2:
    main(sys.argv[1])
  else:
    print("Error: se espera exactamente un argumento (la ruta al archivo de matrícula)")