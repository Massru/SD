def union_lista(list1, list2):

    i = 0

    while i < len(list2):
        j = 0
        repeat = False
        while j < len(list1):
            if list1[j] == list2[i]:
                repeat = True
            j += 1
        if repeat == False:
            list1.append(list2[i])
        i += 1

    print(list1)



list1 = [2,4,6,8]
list2 = [1,3,4,5,7,8]

union_lista(list1, list2)
