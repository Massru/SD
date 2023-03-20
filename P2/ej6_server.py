import socket
import os
import pickle
import shutil

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(direccion_servidor)

print("Me quedo a la espera")

mensaje, addr = s.recvfrom(1024)

print(mensaje.decode("utf-8"))

s.sendto("¿Que operacion quiere realizar? ".encode("utf-8"), addr)

operacion, addr = s.recvfrom(1024)

while True:

    if operacion.decode("utf-8") == 'exit':

        break

    if operacion.decode("utf-8") == 'ls':

        ficheros = os.listdir()
        directorio = pickle.dumps(ficheros)
        s.sendto(directorio, addr)

    if operacion.decode("utf-8").startswith("rm"):

        archivo, addr = s.recvfrom(1024)
        archivo = archivo.decode("utf-8")
        os.remove(archivo)
        s.sendto("Archivo borrado correctamente".encode("utf-8"), addr)

    if operacion.decode("utf-8").startswith("move"):

        origen, addr = s.recvfrom(1024)
        destino, addr = s.recvfrom(1024)
        shutil.move(origen.decode("utf-8"), destino.decode("utf-8"))
        s.sendto("Archivo movido correctamente".encode("utf-8"), addr)

    if operacion.decode("utf-8").startswith("cd"):

        dir, addr = s.recvfrom(1024)
        dir = dir.decode("utf-8")

        i = 0
        existe = False
        if dir == '..':
            existe = True        
        while i < len(os.listdir()):
            if dir == os.listdir()[i]:
                existe = True
            i += 1

        if existe == True:
            os.chdir(dir)
            s.sendto("Directorio de trabajo cambiado correctamente".encode("utf-8"), addr)

        else:
            raise ValueError("Directorio no encontrado")
        
    if operacion.decode("utf-8").startswith("write"):

        archivo, addr = s.recvfrom(1024)
        texto, addr = s.recvfrom(1024)

        with open(archivo.decode("utf-8"), 'w') as f:
            f.write(texto.decode("utf-8"))
            
        s.sendto("Archivo creado correctamente".encode("utf-8"), addr)


    s.sendto("¿Que operacion quiere realizar? ".encode("utf-8"), addr)

    operacion, addr = s.recvfrom(1024)

s.close()