# -*- coding: utf-8 -*-

from cursos.unq_inpr import CURSOS as cursos_unq_inpr

def dame_cursos(verb):
  return CURSOS

CURSOS = {"cursos":{}}

for c in cursos_unq_inpr:
  CURSOS["cursos"][c] = cursos_unq_inpr[c]