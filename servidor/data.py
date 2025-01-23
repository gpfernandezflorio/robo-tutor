# -*- coding: utf-8 -*-

from cursos.unq_inpr import CURSOS as cursos_unq_inpr
from cursos.exactas_programa import CURSOS as cursos_exactas_programa

def dame_cursos(verb):
  return CURSOS

CURSOS = {"cursos":{}}

for c in cursos_unq_inpr:
  CURSOS["cursos"][c] = cursos_unq_inpr[c]

for c in cursos_exactas_programa:
  CURSOS["cursos"][c] = cursos_exactas_programa[c]