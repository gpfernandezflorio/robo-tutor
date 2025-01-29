# -*- coding: utf-8 -*-

import os, json

USUARIOS = {}

if os.path.isfile('usersDB.json'):
  f = open('usersDB.json', 'r')
  USUARIOS = json.loads(f.read())
  f.close()

def guardarUsuarios():
  f = open('usersDB.json', 'w')
  f.write(json.dumps(USUARIOS))
  f.close()

def existeUsuario(nombre):
  return nombre in USUARIOS

def crearUsuario(nombre):
  USUARIOS[nombre] = {'contrasenia':generarContrasenia(), 'cursos':[]}

def usuarioEnCurso(nombre, curso):
  return curso in USUARIOS[nombre]['cursos']

def matricular(nombre, curso):
  USUARIOS[nombre]['cursos'].append(curso)

def cargarUsuariosEnCurso(listaDeUsuarios, curso):
  for usuario in listaDeUsuarios:
    if not existeUsuario(usuario):
      crearUsuario(usuario)
    if not usuarioEnCurso(usuario, curso):
      matricular(usuario, curso)
  guardarUsuarios()

def generarContrasenia():
  return '123456'

def contraseniaUsuario(nombre):
  return USUARIOS[nombre]['contrasenia']

def loginValido(usuario, contrasenia, curso=None):
  return existeUsuario(usuario) and contraseniaUsuario(usuario) == contrasenia and (curso is None or usuarioEnCurso(usuario, curso))

def cursosUsuario(nombre):
  return USUARIOS[nombre]['cursos']