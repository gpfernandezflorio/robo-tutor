linkEncuestaInicial_2026_1C = {
  "tipo":"LINK",
  "id":"linkEncuestaInicial",
  "nombre":"Encuesta Inicial",
  "url":"-" # TODO
}

def guia3(fechaInicio):
  return {
    "tipo":"SECCION",
    "id":"guia3",
    "nombre":"Guía Práctica 3",
    "disponible":{"desde":fechaInicio},
    "actividades":[
      guia3_ej1(fechaInicio)
    ]
  }

def guia3_ej1(fechaInicio):
  return {
    "tipo":"CODIGO",
    "id":"guia3_ej1",
    "nombre":"Guía 3 - Ejercicio 1",
    "lenguaje":"Haskell",
    "enunciado":"Implementar la función parcial <code>f :: Integer -> Integer</code> definida por extensión de la siguiente manera:<br><emph>f(1) = 8</emph><br><emph>f(4) = 131</emph><br><emph>f(16) = 16</emph>",
    "aridad":{"f":"Integer -> Integer"},
    "run_data":[{
      "assert":"f(1)==8"
    },{
      "assert":"f(4)==131"
    },{
      "assert":"f(16)==16"
    }],
    "visible":{"desde":fechaInicio}
  }

CURSOS = {
  "dc_ip_2026_1c":{
    "nombre":"Introducción a la Programación - DC (2026 - 1c)",
    "anio":"2026",
    "edicion":"Primer Cuatrimestre",
    "descripcion":"Curso correspondiente a la materia Introducción a la Programación para las carreras Licenciatura en Ciencias de la Computación y Licenciatura en Ciencias de Datos de la Universidad de Buenos Aires",
    "responsable":{
      "nombre":"Equipo de IP",
      "contacto":"a través del campus de la materia"
    },
    "institucion":"Universidad de Buenos Aires (UBA)",
    "lenguaje_display":"none",
    # "analisisCodigo":[
    #   {"key":"CMD_X_LINE"},
    #   {"key":"INDENT"},
    #   {"key":"NEST_CMD","max":1}
    # ],
    "actividades":[
      linkEncuestaInicial_2026_1C,
      guia3("24/2/2025-8:30")
    ]
  }
}
