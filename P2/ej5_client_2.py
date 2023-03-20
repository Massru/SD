import socket
import os

direccion_servidor = ('localhost', 1026)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(direccion_servidor)

imagen = input(s.recv(1024).decode("utf-8") + " ")
s.send(imagen.encode("utf-8"))

if imagen.endswith(".jpg"):

    ruta = os.getcwd()

    s.send(ruta.encode("utf-8"))

    with open(imagen, 'rb') as f:
        datos = f.read()

    s.send(datos)
    s.send(b'\xe2\x90\x84')

else:
    print("El archivo no es una imagen .jpg")


s.close()