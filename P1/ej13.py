def directorios():

    with open('/etc/passwd', 'r') as f:
        for line in f:
            x = line.split(':')
            print(x[0] + ':' + x[(len(x)-2)])
    

directorios()