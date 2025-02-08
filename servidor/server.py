# -*- coding: utf-8 -*-

import os, io
import sys
import threading

try: # python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except:
    pass

import json
import socket
from corrector import run_code, open_ej
from admin import admin_reset
from data import dame_cursos, tryLogin, dame_data_cuestionario, respuestaCuestionario

try: # python 3
    from http.server import BaseHTTPRequestHandler, HTTPServer
    moduloHTTPServer = HTTPServer
    moduloHTTPRequest = BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
except: # python 2
    import BaseHTTPServer
    moduloHTTPServer = BaseHTTPServer.HTTPServer
    moduloHTTPRequest = BaseHTTPServer.BaseHTTPRequestHandler
    from SocketServer import ThreadingMixIn

servidorAC = None
MODO_WEB = False
verb = False

def launch_server(ip='localhost', port=8000, v=False):
    global verb
    verb = v
    MODO_WEB = ip != 'localhost'

    if (MODO_WEB):
        print('Launch WEB Server ' + ip + ":" + str(port))
    else:
        print('Launch LOCAL Server ' + ip + ":" + str(port))
    sys.stdout.flush()
    run(ip, port)

class HandlerAC(moduloHTTPRequest):
    def _set_response(self, n=200, headers={'Content-type':'text/html'}):
        self.send_response(n)
        self.send_header('Cache-Control', 'no-cache')
        for h in headers:
            self.send_header(h, headers.get(h))
        self.cors_headers()
        self.end_headers()

    def cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.cors_headers()
        self.end_headers()

    def do_GET(self):
        ruta = self.path.split("?")[0]
        if (ruta == "/" or ruta == "/index.html"):
            self.archivoStatico('../index.html')
        # elif (ruta == "/admin"):
        #     self.archivoStatico('admin.html')
        elif (ruta.startswith("/csv/")):
            self.archivoStatico('locales/' + ruta[4:] + '.csv')
        elif (ruta.startswith("/cuestionario/")):
            self.responder(dame_data_cuestionario(ruta[14:]))
        elif (ruta == "/favicon.ico"):
            self.archivoStatico('../favicon.ico')
        else:
            self.error("[GET] Ruta {} inválida".format(self.path))

    def do_PUT(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        put_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        jsonObject = json.loads(put_data)
        self.error("[PUT] Ruta {} inválida".format(self.path))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        jsonObject = json.loads(post_data)
        if (self.path == "/open"):
            self.responder(open_ej(jsonObject, verb))
        elif (self.path == "/code"):
            self.responder(run_code(jsonObject, verb))
        elif (self.path == "/answer"):
            self.responder(respuestaCuestionario(jsonObject))
        elif (self.path == "/login"):
            self.responder(tryLogin(jsonObject, verb))
        elif (self.path == "/cursos"):
            self.responder(dame_cursos(jsonObject))
        elif (self.path == "/reset"):
            self.responder(admin_reset(jsonObject, verb))
        else:
            self.error("[POST] Ruta {} inválida".format(self.path))

    def error(self, msg):
        print(msg)
        self._set_response(404, {})

    def responder(self, jsonObject):
        self._set_response(200, {'Content-Type': 'application/json'})
        datos = json.dumps(jsonObject, ensure_ascii=False)
        try: # python 3
            self.wfile.write(bytes(datos, 'utf-8'))
        except: # python 2
            self.wfile.write(datos.decode())

    def archivoStatico(self, ruta):
        if (os.path.isfile(ruta)):
            self._set_response(200, {'Content-type':tipo_archivo(ruta)})
            # f = io.open(ruta, mode='r', encoding='utf-8')
            f = io.open(ruta, mode='rb')
            self.wfile.write(f.read())
            f.close()
        else:
            self._set_response(404)
            print("Archivo {} no econtrado".format(self.path))

class ServerAC(ThreadingMixIn, moduloHTTPServer):
    """ This class allows to handle requests in separated threads.
        No further content needed, don't touch this. """

def run(host, port):
    global servidorAC
    servidorAC = ServerAC((host, port), HandlerAC)
    seguirSirviendo = True
    while(seguirSirviendo):
      try:
          servidorAC.serve_forever()
      except KeyboardInterrupt:
          seguirSirviendo = False
      except Exception as e:
          mostrar_excepcion(e)
    close_server()
    print('Exit...\n')

def close_server():
    print("CLOSE")
    servidorAC.server_close()
    exit()

def mi_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    return s.getsockname()[0]

def tipo_archivo(filename):
    # if filename[-4:] == '.css':
    #     return 'text/css'
    # if filename[-5:] == '.json':
    #     return 'application/json'
    # if filename[-3:] == '.js':
    #     return 'application/javascript'
    if filename[-4:] == '.ico':
        return 'image/x-icon'
    # if filename[-4:] == '.svg':
    #     return 'image/svg+xml'
    if filename[-4:] == '.csv':
        return 'text/csv'
    return 'text/html'

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Server')
    parser.add_argument('-v', dest="v", default=False, type=bool, help='Modo verborrágico.')
    parser.add_argument('-p', dest="PORT", default=8000, type=int, help='Puerto')
    args = parser.parse_args()
    PORT = (int(os.environ['PORT']) if 'PORT' in os.environ else args.PORT)
    launch_server(mi_ip(), PORT, args.v)
