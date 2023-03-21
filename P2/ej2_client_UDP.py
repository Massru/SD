import socket
import argparse
import os


archivo = input('Introduce nombre del archivo: ')

with open(archivo, 'rb') as f:
    data = f.read()
    tamanno = len(data)

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccion_servidor = ('localhost', 1111)

s_udp.sendto(archivo.encode("utf-8"), direccion_servidor)
mensaje, addr = s_udp.recvfrom(1024)

if mensaje.decode("utf-8") == 'Archivo existente, ¿desea sobreescribir? s/n':

    respuesta = input(mensaje.decode("utf-8") + ': ')
    s_udp.sendto(respuesta.encode("utf-8"), direccion_servidor)

    s_udp.sendto(str(tamanno).encode("utf-8"), direccion_servidor)
    s_udp.sendto(data, direccion_servidor)

    fin, addr = s_udp.recvfrom(1024)
    print(fin.decode("utf-8"))

else:

    s_udp.sendto(str(tamanno).encode("utf-8"), direccion_servidor)
    s_udp.sendto(data, direccion_servidor)

    fin, addr = s_udp.recvfrom(1024)
    print(fin.decode("utf-8"))

os.remove(archivo)


s_udp.close()
