def list_del (mylist, e):

    if type(e) is None:
        raise TypeError('Tipo erroneo')
    if len(mylist) == 0:
        raise TypeError('Lista vacia')
    else:
        mylist.remove(e)

    print(mylist)

list_del([5, 2, 4], 2)
