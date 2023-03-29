import socket

direccion_servidor = ('localhost', 1024)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

s.connect(direccion_servidor)

while True:
    mensaje = input(">> ")

    s.sendall(mensaje.encode("utf-8"))

    if mensaje == 'desconectar':
        s.close()
        break

    respuesta = s.recv(1024).decode("utf-8")

    print(respuesta)

s.close()