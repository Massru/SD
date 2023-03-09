import os

directorio = os.getcwd()
print(directorio)
ficheros = os.listdir()
print(ficheros)

file = input('Archivo al que quieres cambiar el nombre: ')

i = 0
found = False
while i < len(ficheros):
    if file == ficheros[i]:
        found = True
    i +=1

if found == False:
    raise ValueError('Archivo no encontrado')
else:
    new_file = input('Nuevo nombre del archivo: ')

    j = 0
    duplicate = False
    while j < len(ficheros):
        if new_file == ficheros[j]:
            duplicate = True
        j += 1

    if duplicate == True:
        raise ValueError('Nombre de archivo duplicado')
    else:
        os.rename(file, new_file)
