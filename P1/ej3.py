import pathlib
import filecmp

f1 = pathlib.Path('./archivo.txt')
f2 = pathlib.Path('./archivo2.txt')

with open(f1, 'r') as f1, open(f2, 'w') as f2:
    for line in f1:
        f2.write(line)

if filecmp.cmp(f1,f2):
    print('Iguales')
else:
    print('Diferentes')
