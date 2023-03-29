import socket

direccion_servidor = ('localhost', 1024)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Cliente 1".encode("utf-8"), direccion_servidor)

while True:
    mensaje = input(">> ")
    s.sendto(mensaje.encode("utf-8"), direccion_servidor)

    if mensaje == 'desconectar':
        break

    respuesta, direccion_servidor = s.recvfrom(1024)
    respuesta = respuesta.decode("utf-8")
    print(respuesta)


s.close()