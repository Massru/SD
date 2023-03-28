import socket

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Soy el cliente".encode("utf-8"), direccion_servidor)

mensaje, addr = s.recvfrom(1024)

nombre = input(mensaje.decode("utf-8"))

s.sendto(nombre.encode("utf-8"), direccion_servidor)

ayuda, addr = s.recvfrom(1024)

print(ayuda.decode("utf-8"))

respuesta = input()

s.sendto(respuesta.encode("utf-8"), direccion_servidor)

while respuesta != 'exit':

    contestacion , addr = s.recvfrom(1024)

    print(contestacion.decode("utf-8"))

    print(ayuda.decode("utf-8"))

    respuesta = input()

    s.sendto(respuesta.encode("utf-8"), direccion_servidor)

s.close()
print("Desconexión realizada")
