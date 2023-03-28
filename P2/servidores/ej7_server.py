import socket
import os
import pickle

direccion_servidor = ('localhost', 1025)

s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_servidor.bind(direccion_servidor)
s_servidor.listen(1)

s_cliente, direccion_cliente = s_servidor.accept()

mensaje = '\n------------------------------------\n1. Buscar fichero\n2. Listar ficheros\n3. Subir fichero\n4. Salir\n------------------------------------\nSeleccione una opcion: '

s_cliente.send(mensaje.encode("utf-8"))
opcion = s_cliente.recv(1024).decode("utf-8")

while True:

    if opcion == '4':

        break
    
    elif opcion == '1':

        s_cliente.send("Archivo que quiere recibir: ".encode("utf-8"))
        archivo = s_cliente.recv(1024).decode("utf-8")

        i = 0
        existe = False
        while i < len(os.listdir()):
            if archivo == os.listdir()[i]:
                existe = True
            i += 1

        if existe != True:
            s_cliente.send("No existe".encode("utf-8"))
            raise ValueError("Archivo no encontrado")
        else:
            s_cliente.send("existe".encode("utf-8"))
            with open(archivo, 'rb') as f:
                datos = f.read()

            s_cliente.sendall(datos)
            s_cliente.send(b'\xe2\x90\x84')


    elif opcion == '2':

        directorio = os.listdir()

        i = 0
        ficheros = []
        while i < len(directorio):
            if os.path.isfile(directorio[i]) == True:
                ficheros.append(directorio[i])
            i += 1

        ficheros_bytes = pickle.dumps(ficheros)
        s_cliente.send(ficheros_bytes)

    elif opcion == '3':

        archivo = s_cliente.recv(1024).decode("utf-8")

        if archivo == 'No existe':
            raise ValueError("Error en el cliente, archivo no encontrado")
        else:
            datos = s_cliente.recv(1024)
            while True:
                chunk = s_cliente.recv(1024)
                find = chunk.find(b'\xe2\x90\x84')
                if find != -1:
                    datos += chunk[:find]
                    break
                datos += chunk

            with open(archivo, 'wb') as f:
                f.write(datos)

    else:
        
        print("Opción no válida")
        break

    opcion = s_cliente.recv(1024).decode("utf-8")


s_cliente.close()
s_servidor.close()