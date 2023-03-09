import os

directorio = os.getcwd()
ficheros = os.listdir()

i = 0
while i < len(ficheros):
    print(ficheros[i] + ': ' + str(os.stat(ficheros[i]).st_size) + ' Bytes')
    i += 1

j = 0
suma = 0
while j < len(ficheros):
    suma += os.stat(ficheros[j]).st_size
    j += 1

print(str(suma) + ' Bytes')
