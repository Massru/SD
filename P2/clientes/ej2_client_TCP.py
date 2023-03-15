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
    respuesta = input(existe + ': ').encode("utf-8")
    s.send(respuesta)

    if respuesta.decode("utf-8") == 's':
        s.sendall(data)
        s.send(b'\xe2\x90\x84')    
        os.remove(archivo)
    if respuesta.decode("utf-8") == 'n':
        print("Transferencia cancelada")

else:
    s.sendall(data)
    s.send(b'\xe2\x90\x84')

    os.remove(archivo)

confirmacion = s.recv(1024).decode("utf-8")
print(confirmacion)

