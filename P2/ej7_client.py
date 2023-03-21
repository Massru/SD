import socket
import os
import pickle

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(direccion_servidor)

mensaje = s.recv(1024).decode("utf-8")
opcion = input(mensaje)
print("\n")
s.send(opcion.encode("utf-8"))

while True:

    if opcion == '4':
        break
    elif opcion == '1':
        break
    elif opcion == '2':

        ficheros = s.recv(1024)
        ficheros = pickle.loads(ficheros)

        i = 0
        while i < len(ficheros):
            print(ficheros[i])
            i += 1

    elif opcion == '3':
        break
    else:
        print("Opción no válida")
        break

    opcion = input(mensaje)
    s.send(opcion.encode("utf-8"))


s.close()