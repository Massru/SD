import socket

direccion_servidor = ('127.0.0.1', 1024)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)


s.connect(direccion_servidor)

response = s.recv(1024)

while True:
    mensaje = input()
    s.send(str.encode(mensaje))
    if mensaje != 'desconectar':
        response = s.recv(1024)
        print(response.decode('utf-8'))
    else:
        break

s.close()