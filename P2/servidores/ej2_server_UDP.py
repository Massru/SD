import socket
import argparse
import os

ficheros = os.listdir()

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccion_servidor = ('localhost', 1111)
s_udp.bind(direccion_servidor)

print("Me quedo a la espera")

archivo, addr = s_udp.recvfrom(1024)

nombre_archivo = archivo.decode("utf-8")

i = 0
existe = False
while i < len(ficheros):
    if nombre_archivo == ficheros[i]:
        existe = True
    i += 1
    
if existe == True:
    s_udp.sendto("Archivo existente, ¿desea sobreescribir? s/n".encode("utf-8"), addr)
    respuesta, addr = s_udp.recvfrom(1024)
    if respuesta.decode("utf-8") == 'n':
        print('No se sobreescribira')
    if respuesta.decode("utf-8") == 's':
        print('Se sobreescribe')

        tamanno, addr = s_udp.recv(1024)
        data = s_udp.recv(tamanno)
            
        with open(nombre_archivo, 'wb') as f:
            f.write(data)

else:
    s_udp.sendto("El archivo no existe".encode("utf-8"), addr)
    print("El archivo no existe")

    tamanno, addr = s_udp.recv(1024)
    data = s_udp.recv(tamanno)

    with open(nombre_archivo, 'wb') as f:
        f.write(data)

s_udp.sendto("Archivo recibido".encode("utf-8"), addr)

s_udp.close()
