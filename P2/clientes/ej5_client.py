import socket
import os

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

s.connect(direccion_servidor)

mensaje = s.recv(1024).decode("utf-8")

imagen = input(mensaje)

if imagen.endswith(".jpg"):

    s.send(imagen.encode("utf-8"))

    datos = s.recv(1024)
    while True:
        chunk = s.recv(1024)
        find = chunk.find(b'\xe2\x90\x84')
        if find != -1:
            datos += chunk[:find]
            break
        datos += chunk

    with open(imagen, 'wb')  as f:
        f.write(datos)



else:
    print("El archivo no es un jpg")

s.close()