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

def usuarioEnCurso(nombre, curso):
  return (nombre in CURSOS_POR_USUARIO) and (curso in CURSOS_POR_USUARIO[nombre])

def matricular(nombre, curso):
  if not (nombre in CURSOS_POR_USUARIO):
    CURSOS_POR_USUARIO[nombre] = [curso]
  else:
    CURSOS_POR_USUARIO[nombre].append(curso)

def cargarUsuariosEnCurso(listaDeUsuarios, curso):
  for usuario in listaDeUsuarios:
    if not usuarioEnCurso(usuario, curso):
      matricular(usuario, curso)

def contraseniaUsuario(nombre):
  return USUARIOS[nombre]['contrasenia']

def loginValido(usuario, contrasenia, curso=None):
  return existeUsuario(usuario) and contraseniaUsuario(usuario) == contrasenia and (curso is None or usuarioEnCurso(usuario, curso))

def cursosUsuario(nombre):
  if nombre in CURSOS_POR_USUARIO:
    return CURSOS_POR_USUARIO[nombre]
  else:
    return []