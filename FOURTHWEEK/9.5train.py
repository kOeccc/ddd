def xor(x, y):
    if x == y == 0:
        return(x)
    elif x != y:
        return(1)
    else:
        return(0)


x, y = int(input()), int(input())
print(xor(x, y))
