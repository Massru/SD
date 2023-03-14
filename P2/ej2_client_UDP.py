import socket
import argparse

def main(host, port, filein):

    archivo = str(filein)

    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_udp.sendto("Soy el cliente".encode("utf-8"),(host, port))

    s_udp.sendto(archivo.encode("utf-8"), (host, port))

    mensaje, addr = s_udp.recvfrom(1024)
    print(mensaje.decode("utf-8"))

    s_udp.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1025, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--filein', default='file.pdf', help="file to be read")
    args = parser.parse_args()

    main(args.host, args.port, args.filein)