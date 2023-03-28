import socket
from _thread import *

direccion_servidor = ('127.0.0.1', 1024)
contadorhebras = 0

ss = socket.socket()

try:
    ss.bind(direccion_servidor)
except socket.error as e:
    print(str(e))

ss.listen(5)

def hebra_cliente(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says - Hola: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    client, address = ss.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(hebra_cliente, (client, ))
    contadorhebras += 1
    print('Thread Number: ' + str(contadorhebras))
    
serverSocket.close()
