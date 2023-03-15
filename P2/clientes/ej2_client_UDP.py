import socket
import argparse
import os


archivo = input('Introduce nombre del archivo: ')

with open(archivo, 'rb') as f:
    data = f.read()

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccion_servidor = ('localhost', 1025)
s_udp.sendto("Soy el cliente".encode("utf-8"), direccion_servidor)

s_udp.sendto(archivo.encode("utf-8"), direccion_servidor)
mensaje, addr = s_udp.recvfrom(1024)

if mensaje.decode("utf-8") == 'Archivo existente, ¿desea sobreescribir? s/n':

    respuesta = input(mensaje.decode("utf-8") + ': ')
    s_udp.sendto(respuesta.encode("utf-8"), direccion_servidor)

    s_udp.sendall(data)
    s_udp.send(b'\xe2\x90\x84')

    fin, addr = s_udp.recvfrom(1024)
    print(fin.decode("utf-8"))

else:
    s_udp.sendall(data)
    s_udp.send(b'\xe2\x90\x84')

    fin, addr = s_udp.recvfrom(1024)
    print(fin.decode("utf-8"))

os.remove(archivo)


s_udp.close()
