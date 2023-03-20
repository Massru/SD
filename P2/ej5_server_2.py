import socket
import os

direccion_servidor = ('localhost', 1026)

s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_servidor.bind(direccion_servidor)
s_servidor.listen(1)

s_cliente, direccion_cliente = s_servidor.accept()

s_cliente.send("¿Que imagen jpg quiere enviar?".encode("utf-8"))
imagen = s_cliente.recv(1024).decode("utf-8")

if imagen.endswith(".jpg"):

    ruta = s_cliente.recv(1024).decode("utf-8")

    print(ruta)

    ficheros = os.listdir(ruta)

    i = 0
    existe = False
    while i < len(ficheros):
        if imagen == ficheros[i]:
            existe = True
        i += 1


    if existe != True:
        raise ValueError('Imagen no encontrada')
    else:
        print("Imagen encontrada")

    datos = s_cliente.recv(1024)
    while True:
        chunk = s_cliente.recv(1024)
        find = chunk.find(b'\xe2\x90\x84')
        if find != -1:
            datos += chunk[:find]
            break
        datos += chunk

    with open('copia.jpg', 'wb') as f:
        f.write(datos)
        
else:
    print("El archivo no es una imagen")

s_cliente.close()
s_servidor.close()