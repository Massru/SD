import socket

direccion_servidor = ('127.0.0.1', 1024)

s = socket.socket()

s.connect(direccion_servidor)

response = s.recv(1024)

while True:
    mensaje = input()
    s.send(str.encode(mensaje))
    if mensaje != 'exit':
        response = s.recv(1024)
        print(response.decode('utf-8'))
    else:
        break

s.close()