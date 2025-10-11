import os, io
import json
import ssl
import threading

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

from utils import mostrar_excepcion, texto_excepcion

CONFIG = {"DATA":{}}

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
    CONFIG["DATA"] = {"metodo":"OPTIONS","path":self.path}
    self.send_response(200, "ok")
    self.cors_headers()
    self.end_headers()

  def do_GET(self):
    CONFIG["DATA"] = {"metodo":"GET","path":self.path}
    try:
      ruta = self.path.split("?")[0]
      for msg in CONFIG["msgs"]["GET"]:
        if (ruta == "/" + msg):
          self.responder(CONFIG["msgs"]["GET"][msg](CONFIG["verb"]))
          return
      for msg in CONFIG["msgs"]["GET_STARTS"]:
        if (ruta.startswith("/" + msg + "/")):
          self.responder(CONFIG["msgs"]["GET_STARTS"][msg](ruta[2+len(msg):]))
          return
      for msg in CONFIG["msgs"]["FILE"]:
        if (ruta == "/" + msg):
          self.archivoStatico(CONFIG["msgs"]["FILE"][msg])
          return
      for msg in CONFIG["msgs"]["FILE_STARTS"]:
        if (ruta.startswith("/" + msg + "/")):
          self.archivoStatico(CONFIG["msgs"]["FILE_STARTS"][msg](ruta[2+len(msg):]))
          return
      self.error("[GET] Ruta {} inválida".format(self.path))
    except Exception as e:
      CONFIG["DATA"]["e"] = texto_excepcion(e)
      CONFIG["fail"](CONFIG["DATA"])

  def do_PUT(self):
    CONFIG["DATA"] = {"metodo":"PUT","path":self.path}
    try:
      content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
      put_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
    except Exception as e:
      CONFIG["DATA"]["e"] = texto_excepcion(e)
      CONFIG["fail"](CONFIG["DATA"],"_readData")
      return
    try:
      jsonObject = json.loads(put_data)
    except Exception as e:
      CONFIG["DATA"]["e"] = texto_excepcion(e)
      CONFIG["fail"](CONFIG["DATA"],"_loadJson")
      return
    try:
      CONFIG["DATA"]["json"] = jsonObject
      self.error("[PUT] Ruta {} inválida".format(self.path))
    except Exception as e:
      CONFIG["DATA"]["e"] = texto_excepcion(e)
      CONFIG["fail"](CONFIG["DATA"])

  def do_POST(self):
    CONFIG["DATA"] = {"metodo":"POST","path":self.path}
    try:
      content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
      post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
    except Exception as e:
      CONFIG["DATA"]["e"] = texto_excepcion(e)
      CONFIG["fail"](CONFIG["DATA"],"_readData")
      return
    try:
      jsonObject = json.loads(post_data)
    except Exception as e:
      CONFIG["DATA"]["e"] = texto_excepcion(e)
      CONFIG["fail"](CONFIG["DATA"],"_loadJson")
      return
    try:
      CONFIG["DATA"]["json"] = jsonObject
      for msg in CONFIG["msgs"]["POST"]:
        if (self.path == "/" + msg):
          self.responder(CONFIG["msgs"]["POST"][msg](jsonObject, CONFIG["verb"]))
          return
      self.error("[POST] Ruta {} inválida".format(self.path))
    except Exception as e:
      CONFIG["DATA"]["e"] = texto_excepcion(e)
      CONFIG["fail"](CONFIG["DATA"])

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

class Servidor(object):
  def run(self, host, port, msgs, failCallback, verb):
    for k in ["GET","GET_STARTS","FILE","FILE_STARTS","POST","PUT"]:
      if not (k in msgs):
        msgs[k] = {}
    CONFIG["msgs"] = msgs
    CONFIG["fail"] = failCallback
    CONFIG["verb"] = verb
    self.servidor = ServerAC((host, port), HandlerAC)
    if ("CERT" in os.environ) and ("KEY" in os.environ):
      context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
      context.load_cert_chain(certfile=os.environ["CERT"], keyfile=os.environ["KEY"])
      context.set_ciphers("@SECLEVEL=1:ALL")
      self.servidor.socket = context.wrap_socket(self.servidor.socket, server_side=True)
    seguirSirviendo = True
    while(seguirSirviendo):
      try:
        self.servidor.serve_forever()
      except KeyboardInterrupt:
        seguirSirviendo = False
      except Exception as e:
        mostrar_excepcion(e)
    self.cerrar()
    print('Exit...\n')
  
  def cerrar(self):
    print("CLOSE")
    self.servidor.server_close()
    exit()