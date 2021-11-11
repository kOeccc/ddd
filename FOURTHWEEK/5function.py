def sred(a, b):
    if a < b:
        return a
    return b


def sred3(a, b, c):
    return sred(sred(a, b), c)


a = int(input())
b = int(input())
c = int(input())

print(sred(a, b), sred3(a, b, c))
