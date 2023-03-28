import socket
import os
import pickle

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Soy el cliente".encode("utf-8"), direccion_servidor)

pregunta, direccion_servidor = s.recvfrom(1024)

operacion = input(pregunta.decode("utf-8"))

s.sendto(operacion.encode("utf-8"), direccion_servidor)

while True:

    if operacion == 'exit':

        break    

    if operacion == 'ls':

        directorio, direccion_servidor = s.recvfrom(1024)
        ficheros = pickle.loads(directorio)
        print(ficheros)

    if operacion.startswith("rm"):

        archivo = operacion.split()
        s.sendto(archivo[len(archivo)-1].encode("utf-8"), direccion_servidor)
        confirmacion, direccion_servidor = s.recvfrom(1024)
        print(confirmacion.decode("utf-8"))

    if operacion.startswith("move"):

        directorios = operacion.split()
        s.sendto(directorios[len(directorios)-2].encode("utf-8"), direccion_servidor)
        s.sendto(directorios[len(directorios)-1].encode("utf-8"), direccion_servidor)        
        confirmacion, direccion_servidor = s.recvfrom(1024)
        print(confirmacion.decode("utf-8"))

    if operacion.startswith("cd"):

        dir_trabajo = operacion.split()
        s.sendto(dir_trabajo[len(dir_trabajo)-1].encode("utf-8"), direccion_servidor)
        confirmacion, direccion_servidor = s.recvfrom(1024)
        print(confirmacion.decode("utf-8"))

    if operacion.startswith("write"):

        dividir = operacion.split(' ', 2)

        s.sendto(dividir[1].encode("utf-8"), direccion_servidor)
        s.sendto(dividir[2].encode("utf-8"), direccion_servidor)

        confirmacion, direccion_servidor = s.recvfrom(1024)
        print(confirmacion.decode("utf-8"))


    pregunta, direccion_servidor = s.recvfrom(1024)

    operacion = input(pregunta.decode("utf-8"))

    s.sendto(operacion.encode("utf-8"), direccion_servidor)

s.close()