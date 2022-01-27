def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif b != 0 and a != 0:
        return gcd(b, a % b)


def RuduceFraction(a, b):
    return a // gcd(a, b), b // gcd(a, b)


a = int(input())
b = int(input())
print(*RuduceFraction(a, b))
