estudiantes_tm = [

]
estudiantes_grado = [

]
estudiantes_tt = [

]

def tp_final(id, coms, fechas, estudiantes):
  return {
    "tipo":"CUESTIONARIO",
    "id":"tp_final_"+id,
    "nombre":"TP Final - " + coms,
    "puedenReintentar":False,
    "puedenSaltearPreguntas":False,
    "puedenRetroceder":False,
    "preguntas":[{
      "tipo":"MULTI",
      "titulo":"TP Final",
      "contenido":"Ingresá los datos del labo y la pc.",
      "preguntas":[{
        "tipo":"TEXTO_LIBRE",
        "pregunta":"Labo (4 dígitos)"
      },{
        "tipo":"TEXTO_LIBRE",
        "pregunta":"PC dentro del labo (5 dígitos, contando el punto en el medio)"
      }]
    },
    {
      "tipo":"TEXTO_LIBRE",
      "titulo":"TP Final",
      "pregunta":"Copiá y pegá acá tu solución."
    },{
      "tipo":"SOLO_TEXTO",
      "titulo":"TP Final",
      "pregunta":"Respuesta enviada."
    }],
    "disponible":{
      "desde":fechas[0],
      "hasta":fechas[1]
    }#,
    #"visible":{
    #  "usuariosSi":estudiantes
    #}
  }

CURSOS = {
  "pensamiento_computacional_2026_1c":{
    "nombre":"Pensamiento Computacional - 2026 1C",
    "anio":"2026",
    "edicion":"Primer Cuatrimestre",
    "descripcion":"Curso correspondiente a la materia Pensamiento Computacional de la Universidad de Buenos Aires",
    "responsable":{
      "nombre":"Christian Cossio",
      "contacto":"cgcossio (AT) gmail.com"
    },
    "institucion":"Facultad de Ciencias Exactas y Naturales (FCEyN) - UBA",
    "lenguaje":"Python",
    "lenguaje_display":"none",
    "actividades":[
    # {
    #   "tipo":"CODIGO",
    #   "id":"tp_final_tm",
    #   "nombre":"TP Final - Comisiones 290001 a 29003 (viernes mañana)",
    #   "enunciado":"-",
    #   "visible":{"desde":"12/6/2026-7:00","hasta":"12/6/2026-11:30"}
    # },{
    #   "tipo":"CODIGO",
    #   "id":"tp_final_grado",
    #   "nombre":"TP Final - Comisión grado (viernes tarde)",
    #   "enunciado":"-",
    #   "visible":{"desde":"12/6/2026-13:00","hasta":"12/6/2026-17:30"}
    # },{
    #   "tipo":"CODIGO",
    #   "id":"tp_final_tt",
    #   "nombre":"TP Final - Comisiones 290004 y 29005 (sábado tarde)",
    #   "enunciado":"-",
    #   "visible":{"desde":"13/6/2026-13:00","hasta":"13/6/2026-17:30"}
    # }
      # tp_final("prueba","Prueba",["10/6/2026-10:00","14/6/2026-18:00"],["estudiante_ficticio"]),
      tp_final("tm",
        "Comisiones 290001 a 29003 (viernes mañana)",
        ["12/6/2026-7:00","12/6/2026-12:00"],
        estudiantes_tm
      ),
      tp_final("grado",
        "Comisión grado (viernes tarde)",
        ["12/6/2026-13:00","12/6/2026-18:00"],
        estudiantes_grado
      ),
      tp_final("tt",
        "Comisiones 290004 y 29005 (sábado tarde)",
        ["13/6/2026-13:00","13/6/2026-18:00"],
        estudiantes_tt
      )
    ],
    "planilla":{
      "url":"1FAIpQLSeYrKZ_juXRRzPew_77qTMHyw_4LdZ0DXcCSARhpNttSFKJIQ",
      "campos":{
        "usuario":"9867257",
        "ip":"1934148550",
        "actividad":"1165966175",
        "respuesta":"1778184894",
        "resultado":"1496208069",
        "duracion":"1460244707",
      }
    }
  }
}
