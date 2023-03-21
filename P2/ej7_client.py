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

        archivo = input(s.recv(1024).decode("utf-8"))
        s.send(archivo.encode("utf-8"))

        if s.recv(1024).decode("utf-8") == 'No existe':
            raise ValueError("Archivo no encontrado")
        else:
            datos = s.recv(1024)
            while True:
                chunk = s.recv(1024)
                find = chunk.find(b'\xe2\x90\x84')
                if find != -1:
                    datos += chunk[:find]
                    break
                datos += chunk

    elif opcion == '2':

        ficheros = s.recv(1024)
        ficheros = pickle.loads(ficheros)

        i = 0
        while i < len(ficheros):
            print(ficheros[i])
            i += 1

    elif opcion == '3':

        archivo = input("Archivo que quiere subir: ")

        i = 0
        existe = False
        while i < len(os.listdir()):
            if archivo == os.listdir()[i]:
                existe = True
            i += 1
            
        if existe != True:
            s.send("No existe".encode("utf-8"))
            raise ValueError("Archivo no encontrado")
        else:
            with open(archivo, 'rb') as f:
                datos = f.read()
                
            s.sendall(datos)
            s.send(b'\xe2\x90\x84')
        
    else:

        print("Opción no válida")
        break

    opcion = input(mensaje)
    s.send(opcion.encode("utf-8"))


s.close()