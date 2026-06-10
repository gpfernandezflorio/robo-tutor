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
    "":"../../campus/index.html",
    "index.html":"../../campus/index.html",
    "settings.js":"../../campus/settings.js",
    "campus.css":"../../campus/campus.css",
    "campus.js":"../../campus/campus.js",
    # "admin":"admin.html",
    "favicon.ico":"../../campus/favicon.ico"
  },
  "FILE_STARTS":{
    "csv":lambda x : 'locales/' + x + '.csv',
    "include":lambda x : '../../campus/include/' + x,
    "img":lambda x : '../../campus/img/' + x
  }
}
