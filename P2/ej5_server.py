import socket
import os

direccion_servidor = ('localhost', 1025)

s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_servidor.bind(direccion_servidor)
s_servidor.listen(1)

s_cliente, direccion_cliente = s_servidor.accept()

s_cliente.send("¿Que imagen jpg quiere obtener? ".encode("utf-8"))

imagen = s_cliente.recv(1024)

i = 0
existe = False
ficheros = os.listdir()
print(ficheros)

while i < len(ficheros):
    if imagen == ficheros[i]:
        existe = True
    i += 1

if existe == False:
    raise ValueError("Imagen no encontrada")
else:
    with open(imagen, 'rb') as f:
        datos = f.read()

    s_cliente.sendall(datos)
    s_cliente.send(b'\xe2\x90\x84')

s_cliente.close()
s_servidor.close()