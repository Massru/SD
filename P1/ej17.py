import os

ficheros = os.listdir()

for fichero in ficheros:
    if fichero.endswith(".txt") and fichero != 'union.txt':
        with open(fichero, 'r') as f:
            content = f.read()
        print(fichero)
        with open('union.txt', 'a') as union:
            union.write("\n" + content)
