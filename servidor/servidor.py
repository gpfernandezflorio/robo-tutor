from admin import admin_reset
from data import dame_cursos, tryLogin, dame_data_cuestionario, intentoCodigo, respuestaCuestionario, open_ej

mensajesServidor = {
  "POST":{
    "open":open_ej,
    "code":intentoCodigo,
    "answer":respuestaCuestionario,
    "login":tryLogin,
    "cursos":dame_cursos,
    "reset":admin_reset
  },
  "GET_STARTS":{
    "cuestionario":dame_data_cuestionario
  },
  "FILE":{
    "":"../index.html",
    "index.html":"../index.html",
    # "admin":"admin.html",
    "favicon.ico":"../favicon.ico"
  },
  "FILE_STARTS":{
    "csv":lambda x : 'locales/' + x + '.csv'
  }
}