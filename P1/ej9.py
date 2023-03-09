import os

def get_file_info(filename):

    f = open(filename, 'r')

    if type(filename) is None:
        raise TypeError('Archivo nulo')
    if os.path.isfile(filename) is None:
        raise OSError('Archivo no encontrado')
    else:
    
        Tamanno = os.stat(filename).st_size
        Palabras = []

    lista = f.read()
    aux = ' '

    for n in lista:
        if(n!=' '):
            aux += n
        elif(n == ' ' and aux[-1] == 's'):
            Palabras.append(aux)
            aux = ''
        else:
            aux = ''
    if (aux != ' ' and aux[-1] == 's'):
        Palabras.append(aux)

    f.close()

    print(Tamanno, Palabras)

get_file_info('mifichero.txt')