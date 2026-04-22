títuloBienvenida = "Comenzando"
# TODO: Explicar en qué consiste el experimento
textoDeBienvenida = "[...]<br>Hacé clic en 'Siguiente' para continuar."
títuloEstímulo = "Calificá este ejercicio"
def textoEstímulo(estímulo):
  return [{'md':estímulo}, "<br>A continuación calificá el ejercicio propuesto en la escala del 1 al 5:"]
títuloJustificación = "Justificá tu respuesta (opcional)"
textoJustificación = 'En el siguiente campo podés complementar tu respuesta justificando el puntaje que le asignaste al ejercicio o agregando cualquier comentario que te parezca pertinente.<br><br>Si no tenés nada que agregar, escribí "-".'
títuloFinalización = "Eso es todo..."
textoDeFinalización = "¡Muchas gracias por particiar!"

todosLosEstímulos = [ # TODO
  "¿Verdadero o falso?\n\n```x = 1```",
  "```\nx = 1\n```",
  "¿Cuánto es 2+2?",
  "# T\n\n## T2\n\nCompletar."
]

def estímulosPara_(i):
  # i es un número entre 1 y la cantidad de sujetos
  return [ # TODO
    todosLosEstímulos[(i-1) % 4]
  ]

sujetos = [
  "alanrodas@gmail.com",                # 1
  "maurosalina85@gmail.com",            # 2
  "Federico.Cherchyk@gmail.com",        # 3
  "alan.nicolas.rodriguez@gmail.com",   # 4
  "cuococarlos@gmail.com",              # 5
  "martin.sauczuk@gmail.com",           # 6
  "pablo.g.marrero@gmail.com",          # 7
  "vdecristofolo@gmail.com",            # 8
  "sabaliauskaspablo@gmail.com",        # 9
  "pablotobia@gmail.com",               # 10
  "duglas.espanol@gmail.com",           # 11
  "eugeniocalcena@gmail.com",           # 12
  "juliatroilo@gmail.com"               # 13
]

def cuestionarioPara_ConEstímulos_(sujeto, estímulos, i):
  preguntas = [{
    "tipo":"SOLO_TEXTO",
    "titulo":títuloBienvenida,
    "pregunta":textoDeBienvenida
  }]
  for estímulo in estímulos:
    preguntas.append({
      "tipo":"SLIDER",
      "titulo":títuloEstímulo,
      "pregunta":textoEstímulo(estímulo),
      "rango":{"desde":1,"hasta":5,"paso":1}
    })
    preguntas.append({
      "tipo":"TEXTO_LIBRE",
      "titulo":títuloJustificación,
      "pregunta":textoJustificación
    })
  preguntas.append({
    "tipo":"SOLO_TEXTO",
    "titulo":títuloFinalización,
    "pregunta":textoDeFinalización
  })
  return {
    "tipo":"CUESTIONARIO",
    "id":"progreval_q" + str(i),
    "nombre":"Calificación de ejercicios de programación",
    "puedenReintentar":False,
    "puedenSaltearPreguntas":False,
    "puedenRetroceder":False,
    "preguntas":preguntas,
    "visible":{"usuariosSi":sujeto}
  }

actividades = [
  cuestionarioPara_ConEstímulos_("estudiante_ficticio", todosLosEstímulos, 0)
]

i = 1
for sujeto in sujetos:
  actividades.append(cuestionarioPara_ConEstímulos_(sujeto, estímulosPara_(i), i))
  i += 1

CURSOS = {
  "progreval2026":{
    "nombre":"-",
    "anio":"-",
    "edicion":"-",
    "descripcion":"-",
    "responsable":{
      "nombre":"-",
      "contacto":"-"
    },
    "institucion":"-",
    "actividades":actividades,
    "planilla":{
      "url":"1FAIpQLScgDso9R1aU0b_IwOtpr6RwhRlma8j52YEZX6bc5SO1pqVkpQ",
      "campos":{
        "usuario":"9867257",
        "actividad":"1165966175",
        "respuesta":"1778184894",
        "resultado":"1496208069",
        "duracion":"1460244707"
      }
    }
  }
}
