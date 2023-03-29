import socket

direccion_servidor = ('localhost', 1024)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

s.connect(direccion_servidor)

print("Esperando mensaje del cliente 1")

while True:
    respuesta = s.recv(1024).decode("utf-8")

    print(respuesta)

    mensaje = input(">> ")

    s.sendall(mensaje.encode("utf-8"))

    if mensaje == 'desconectar':
        s.close()
        break


s.close()