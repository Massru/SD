def prime(a, b):
    if type(a) is not int:
        raise TypeError('No es entero')
    if type(b) is not int:
        raise TypeError('No es entero')
    else:
        vector = []
        while a <= b:
            i = a-1
            primo = True
            while i > 1:
                if a%i == 0:
                    primo = False
                i -= 1
            if primo == True:
                vector.append(a)
            a += 1

        print(vector)

prime(2, 100)