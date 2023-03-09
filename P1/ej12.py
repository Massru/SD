def copiar(origen, destino):

    with open(origen, 'r') as file1:
        content = file1.read()

    file1.close()

    with open(destino, 'w') as file2:
        file2.write(content)

    file2.close()
    

copiar('archivo.txt', 'archivo2.txt')