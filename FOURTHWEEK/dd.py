from math import sqrt


def IsPrime(n):
    i = 2
    while n % i != 0:
        if sqrt(n) >= i:
            i += 1
            print(n)
        else:
            return i != n
    return i == n


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
