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

contenido_invertido = contenido[::-1]

with open('invertido.txt', 'wb') as f:
    f.write(contenido_invertido)

tamanno = os.stat('invertido.txt').st_size

s_cliente.sendall(contenido_invertido)
s_cliente.sendall(str(tamanno).encode("utf-8"))


s_cliente.close()
s_servidor.close()