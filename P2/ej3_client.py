import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
direccion_servidor = ('localhost', 1025)
s.connect(direccion_servidor)

ficheros = os.listdir()
print(ficheros)

print(s.recv(1024).decode("utf-8"))

archivo = input()

i = 0
coincide = False
while i < len(ficheros):
    if archivo == ficheros[i]:
        coincide = True
    i += 1

if coincide == True:
    with open(archivo, 'rb') as f:
        contenido = f.read()

    s.sendall(contenido)

    contenido_invertido = s.recv(1024)

    with open('invertido.txt', 'wb') as f:
        f.write(contenido_invertido)

    print('Recibido archivo invertido')
    print('El tamaño es ' + str(s.recv(1024).decode("utf-8")) + ' B')

else:
    print('Archivo no encontrado')

s.close()

