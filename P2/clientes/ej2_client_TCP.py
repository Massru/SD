import socket
import os



direccion_servidor = ('localhost', 1025)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(direccion_servidor)

mensaje = s.recv(1024)
archivo = input(mensaje.decode("utf-8"))
s.send(archivo.encode("utf-8"))

existe = s.recv(1024).decode("utf.8")

with open(archivo, 'rb') as f:
    data = f.read()

if existe == 'Archivo existente, ¿desea sobreescribir? s/n':
    respuesta = input(existe + ': ')

    s.sendall(data)
    s.send(b'\xe2\x90\x84')    

else:
    s.sendall(data)
    s.send(b'\xe2\x90\x84')

confirmacion = s.recv(1024).decode("utf-8")
print(confirmacion)

os.remove(archivo)