import socket
import os

direccion_servidor = ('localhost', 1025)

s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_servidor.bind(direccion_servidor)
s_servidor.listen(1)
print('Me quedo a la espera')

s_cliente, direccion_cliente = s_servidor.accept()

s_cliente.send('Nombre del archivo que quiere invertir :'.encode("utf-8"))

contenido = s_cliente.recv(1024)

i = len(contenido)

with open('invertido.txt', 'w') as f:
    f.write('')

while i > 0:
    with open('invertido.txt', 'a') as f:
        f.write(contenido[i])

tamanno = os.stat('invertido.txt').st_size

s_cliente.send('El tamaño del archivo son ' + str(tamanno) + ' B'.encode("utf-8"))