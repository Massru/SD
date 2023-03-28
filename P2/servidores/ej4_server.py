import socket

direccion_servidor = ('localhost', 1025)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(direccion_servidor)

print("Me quedo a la espera")

mensaje, addr = s.recvfrom(1024)

s.sendto("¡Bienvenido! ¿Cuál es su nombre para que pueda dirigirme a usted? ".encode("utf-8"), addr)

nombre, addr = s.recvfrom(1024)

s.sendto(str(nombre.decode("utf-8")).encode("utf-8") + ", ¿en qué puedo ayudarte? ('exit' para salir)".encode("utf-8"), addr)

respuesta, addr = s.recvfrom(1024)

while respuesta.decode("utf-8") != 'exit':

    if respuesta.decode("utf-8") == '¿Cuándo empiezan las clases este curso?' :
        s.sendto("Debe ponerse en contacto con el servicio de atención de dudas cuya dirección es dudas@ejemplo.com".encode("utf-8"), addr)
    else:
        s.sendto("Lo siento, no puedo ayudar".encode("utf-8"), addr)

    respuesta, addr = s.recvfrom(1024)

s.close()
print("Desconexión realizada")
