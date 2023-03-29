import socket

direccion_servidor = ('localhost', 1024)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(direccion_servidor)

cl1, addr1 = s.recvfrom(1024)
cl2, addr2 = s.recvfrom(1024)

while True:
    msg1, addr1 = s.recvfrom(1024)
    msg1 = msg1.decode("utf-8")

    if msg1 != 'desconectar':
        s.sendto(msg1.encode("utf-8"), addr2)
        msg2, addr2 = s.recvfrom(1024)
        msg2 = msg2.decode("utf-8")
        if msg2 != 'desconectar':
            s.sendto(msg2.encode("utf-8"), addr1)
        else:
            s.sendto("El cliente 2 se ha desconectado".encode("utf-8"), addr1)
            msg1, addr1 = s.recvfrom(1024)
            msg1 = msg1.decode("utf-8")
            if msg1 == 'desconectar':
                break
    else:
        s.sendto("El cliente 1 se ha desconectado".encode("utf-8"), addr2)
        msg2, addr2 = s.recvfrom(1024)
        msg2 = msg2.decode("utf-8")
        if msg2 == 'desconectar':
            break


s.close()