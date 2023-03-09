def interseccion_lista(list1, list2):

    aux = []

    i = 0

    while i < len(list2):
        j = 0
        repeat = False
        while j < len(list1):
            if list1[j] == list2[i]:
                repeat = True
            j += 1
        if repeat == True and len(aux) == 0:
            aux.append(list2[i])
        if repeat == True:
            k = 0
            insertado = False
            while k < len(aux):
                if list2[i] == aux[k]:
                    insertado = True
                k += 1
            if insertado == False:
                aux.append(list2[i])
        i += 1

    print(aux)

list1 = [2,4,6,8]
list2 = [1,3,4,5,7,8,4]

interseccion_lista(list1, list2)
