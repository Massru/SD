def accum(x, y, z):

    total = 0

    if not type(x) is int:
        raise TypeError("Solo permitidos enteros")
    if not type(y) is int:
        raise TypeError("Solo permitidos enteros")
    if not type(z) is int:
        raise TypeError("Solo permitidos enteros")
    else:

        if x % 2 == 0:
            total += x
        if y % 2 == 0:
            total += y
        if z % 2 == 0:
            total += z
    return total

print(accum(2, 3, 4))
