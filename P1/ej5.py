def list_add(mylist, e):

    if type(e) is None:
        raise TypeError('Tipo erroneo')
    else:
        mylist.append(e)

    print(mylist)

list_add([5, 2], 4)