def dict_add(mydict, t):

    if type(t) is None or len(t) > 2:
        raise TypeError('Tipo erroneo')
    else:
        mydict.update(t)
    
    print(mydict)

dict_add({1: 'manzana'}, {2: 'fresa'})