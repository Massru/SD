import socket

direccion_servidor = ('localhost', 1024)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ss.bind(direccion_servidor)
ss.listen(5)

s1, addr1 = ss.accept()
s2, addr2 = ss.accept()

while True:

    msg1 = s1.recv(1024).decode("utf-8")

    if msg1 != 'desconectar':
        s2.sendall(msg1.encode("utf-8"))
        msg2 = s2.recv(1024).decode("utf-8")
        if msg2 != 'desconectar':
            s1.sendall(msg2.encode("utf-8"))
        else:
            s1.sendall("El cliente 2 se ha desconectado".encode("utf-8"))
            s2.close()
            msg1 = s1.recv(1024).decode("utf-8")
            if msg1 == 'desconectar':
                s1.close()
                break
    else:
        s2.sendall("El cliente 1 se ha deconectado".encode("utf-8"))
        s1.close()
        msg2 = s2.recv(1024).decode("utf-8")
        if msg2 == 'desconectar':
            s2.close()
            break

ss.close()
