import http.server
import ssl
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8443
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('0.0.0.0', PORT), handler)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

print(f'Servindo HTTPS na porta {PORT}')
httpd.serve_forever()
