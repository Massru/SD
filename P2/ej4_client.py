import socket

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Soy el cliente".encode("utf-8"), direccion_servidor)

mensaje, addr = s.recvfrom(1024)

nombre = input(mensaje.decode("utf-8"))

s.sendto(bytes(nombre), direccion_servidor)

mensaje, addr = s.recvfrom(1024)

print(mensaje.decode("utf-8"))

respuesta = input()

s.sendto(bytes(respuesta), direccion_servidor)

contestacion , addr = s.recvfrom(1024)

print(contestacion.decode("utf-8"))

s.close()