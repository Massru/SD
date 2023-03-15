import socket
import os

ficheros = os.listdir()
direccion_servidor = ('localhost', 1025)

s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_servidor.bind(direccion_servidor)
s_servidor.listen(1)
print("Nos quedamos a la espera")

s_cliente, direccion_cliente = s_servidor.accept()

s_cliente.send("Nombre del archivo que quiere mandar: ".encode("utf-8"))

archivo = s_cliente.recv(1024).decode("utf-8")

i = 0
existe = False
while i < len(ficheros):
    if archivo == ficheros[i]:
        existe = True
    i += 1

if existe == True:
    s_cliente.send("Archivo existente, ¿desea sobreescribir? s/n".encode("utf-8"))
    respuesta = s_cliente.recv(1024).decode("utf-8")
    if respuesta == 'n':
        print('No se sobreescribira')
    if respuesta == 's':
        print('Se sobreescribe')

        data = b''
        while True:
            chunk = s_cliente.recv(1024)
            find = chunk.find(b'\xe2\x90\x84')
            if find != -1:
                data += chunk[:find]
                break
            data += chunk

        with open(archivo, 'wb') as f:
            f.write(data)

else:
    data = b''
    while True:
        chunk = s_cliente.recv(1024)
        find = chunk.find(b'\xe2\x90\x84')
        if find != -1:
            data += chunk[:find]
            break
        data += chunk

    with open(archivo, 'wb') as f:
        f.write(data)

s_cliente.send("Archivo recibido".encode("utf-8"))