import socket
import argparse
import os

def main(host, port):

    ficheros = os.listdir()

    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_udp.bind((host, port))

    print("Me quedo a la espera")
    mensaje, addr = s_udp.recvfrom(1024)
    print(str(mensaje.decode("utf-8")))

    archivo, addr = s_udp.recvfrom(1024)
    print("Nombre del archivo para enviar: " + archivo.decode("utf-8"))

    archivoin = archivo.decode("utf-8")

    i = 0
    existe = False
    while i < len(ficheros):
        if archivoin == ficheros[i]:
            existe = True
        i += 1
    
    if existe == True:
        s_udp.sendto("Archivo existente, ¿desea sobreescribir?".encode("utf-8"), (host, port))
    else:
        print("El archivo existe")

    s_udp.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1025, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    args = parser.parse_args()

    main(args.host, args.port)