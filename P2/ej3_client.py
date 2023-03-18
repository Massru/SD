import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
direccion_servidor = ('localhost', 1025)
s.connect(direccion_servidor)

ficheros = os.listdir()
print(ficheros)

print(s.recv(1024).decode("utf-8"))

archivo = input()

with open(archivo, 'r') as f:
    contenido = f.read

s.sendall(contenido)

s.recv(1024).decode("utf-8")

