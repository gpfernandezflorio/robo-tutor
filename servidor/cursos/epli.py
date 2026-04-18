q = [{
  "tipo":"SOLO_TEXTO",
  "titulo":"Enunciado",
  "pregunta":["Hola, esta es la primera pregunta:",{"md":"# T1\n\n## T2\n\n ```acá hay código```"},"FIN"]
},{
  "tipo":"SLIDER",
  "titulo":"Pregunta con slider",
  "pregunta":["¿Qué opinás de este ejercicio?",{"md":"# T1\n\n## T2\n\n ```acá hay código```"},"FIN"],
  "rango":{"desde":1,"hasta":5,"paso":1}
},{
  "tipo":"SOLO_TEXTO",
  "titulo":"Enunciado",
  "pregunta":"¡GRACIAS!"
}]

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
    "actividades":[
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q0",
        "nombre":"Calificación de ejercicios de programación",
        "puedenReintentar":False,
        "puedenSaltearPreguntas":False,
        "puedenRetroceder":False,
        "preguntas":[q[0],q[1],q[2]],
        "visible":{"usuariosSi":"estudiante_ficticio"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q1",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"alanrodas@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q2",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"maurosalina85@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q3",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"Federico.Cherchyk@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q4",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"alan.nicolas.rodriguez@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q5",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"cuococarlos@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q6",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"martin.sauczuk@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q7",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"pablo.g.marrero@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q8",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"vdecristofolo@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q9",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"sabaliauskaspablo@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q10",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"pablotobia@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q11",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"duglas.espanol@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q12",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"eugeniocalcena@gmail.com"}
       },
       {
        "tipo":"CUESTIONARIO",
        "id":"progreval_q13",
        "nombre":"Calificación de ejercicios de programación",
        "preguntas":[q[0]],
        "visible":{"usuariosSi":"juliatroilo@gmail.com"}
       }
    ]
  }
}