import socket
import os



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
direccion_servidor = ('localhost', 1025)
s.connect(direccion_servidor)

mensaje = s.recv(1024)
archivo = input(mensaje.decode("utf-8"))
s.send(archivo.encode("utf-8"))

with open(archivo, 'rb') as f:
    data = f.read()


existe = s.recv(1024).decode("utf-8")


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