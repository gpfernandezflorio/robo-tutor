# -*- coding: utf-8 -*-

import os
import sys

try: # python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except:
    pass

import socket
from servidor import mensajesServidor
from utils import failCallback, EjecutarLocal

## SERVER_LIBRARY
from server_httpServer import Servidor # HTTPServer

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
    Servidor().run(ip, port, mensajesServidor, failCallback, verb)
    print('Exit...\n')

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
    parser.add_argument('-l', dest="LOCAL", default=False, type=bool, help='Ejecución local')
    args = parser.parse_args()
    PORT = (int(os.environ['PORT']) if 'PORT' in os.environ else args.PORT)
    if args.LOCAL:
      print("\n\n || LOCAL ||\n\n")
      print("ATENCIÓN: estás ejecutando el servidor en [[MODO LOCAL]] (pensado principalmente para hacer pruebas).")
      print("Para correrlo en modo real, volvé a ejecutarlo sin el flag '-l'.\n")
      EjecutarLocal()
    else:
      print("\n\n || REAL ||\n\n")
      print("ATENCIÓN: estás ejecutando el servidor en [[MODO REAL]] (el que debería estar corriendo en el servidor real).")
      print("Si querés hacer pruebas, volvé a ejecutarlo con el flag '-l'.\n")
    launch_server(mi_ip(), PORT, args.v)
