# -*- coding: utf-8 -*-

import os
import sys
try: # python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except:
    pass

import json
import socket
from corrector import run_code

try: # python 3
    from http.server import BaseHTTPRequestHandler, HTTPServer
    moduloHTTPServer = HTTPServer
    moduloHTTPRequest = BaseHTTPRequestHandler
except: # python 2
    import BaseHTTPServer
    moduloHTTPServer = BaseHTTPServer.HTTPServer
    moduloHTTPRequest = BaseHTTPServer.BaseHTTPRequestHandler

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
        if (self.path == "/code"):
            self.responder(run_code(jsonObject, verb))
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

def run(host, port):
    global servidorAC
    servidorAC = moduloHTTPServer((host, port), HandlerAC)
    try:
        servidorAC.serve_forever()
    except KeyboardInterrupt:
        pass
    close_server()
    print('Exit...\n')

def close_server():
    servidorAC.server_close()
    exit()

def mi_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    return s.getsockname()[0]

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Server')
    parser.add_argument('-v', dest="v", default=False, type=bool, help='Modo verborrágico.')
    args = parser.parse_args()
    PORT = (int(os.environ['PORT']) if 'PORT' in os.environ else 8000)
    launch_server(mi_ip(), PORT, args.v)
