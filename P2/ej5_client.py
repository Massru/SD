import socket
import os

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(direccion_servidor)

imagen = input(s.recv(1024).decode("utf-8") + " ")
s.send(imagen.encode("utf-8"))

if imagen.endswith(".jpg"):

    ruta = os.path.abspath(imagen)

    s.send(ruta.encode("utf-8"))

else:
    print("El archivo no es una imagen .jpg")


s.close()