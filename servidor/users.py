# -*- coding: utf-8 -*-

import os, json

USUARIOS = {}

CURSOS_POR_USUARIO = {}

if os.path.isfile('usersDB.json'):
  f = open('usersDB.json', 'r')
  USUARIOS = json.loads(f.read())
  f.close()

def existeUsuario(nombre):
  return nombre in USUARIOS

def usuarioEnCurso(nombre, curso, rol=None):
  if (nombre in CURSOS_POR_USUARIO) and (curso in CURSOS_POR_USUARIO[nombre]):
    return rol is None or rol in CURSOS_POR_USUARIO[nombre][curso]
  return False

def matricular(nombre, curso, rol):
  if not (nombre in CURSOS_POR_USUARIO):
    CURSOS_POR_USUARIO[nombre] = {curso:[rol]}
  elif not (curso in CURSOS_POR_USUARIO[nombre]):
    CURSOS_POR_USUARIO[nombre][curso] = [rol]
  else:
    CURSOS_POR_USUARIO[nombre][curso].append(rol)

def cargarUsuariosEnCurso(matricula, curso, roles):
  for rol in roles:
    if rol in matricula:
      for usuario in matricula[rol]:
        if not usuarioEnCurso(usuario, curso, rol):
          matricular(usuario, curso, rol)

def contraseniaUsuario(nombre):
  return USUARIOS[nombre]['contrasenia']

def loginValido(usuario, contrasenia, curso=None):
  return existeUsuario(usuario) and contraseniaUsuario(usuario) == contrasenia and (curso is None or usuarioEnCurso(usuario, curso))

def cursosUsuario(nombre):
  if nombre in CURSOS_POR_USUARIO:
    return CURSOS_POR_USUARIO[nombre].keys()
  else:
    return []

def rolesEnCurso(usuario, curso):
  if usuario in CURSOS_POR_USUARIO and curso in CURSOS_POR_USUARIO[usuario]:
    return CURSOS_POR_USUARIO[usuario][curso]
  return []
