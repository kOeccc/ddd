from math import sqrt


import math


def IsPrime(n):
    i = 2
    while n % i != 0:
        if math.sqrt(n) >= i:
            i += 1
        else:
            return i != n
    return n == i


n = int(input())
if IsPrime(n):
    print("YES")
else:
    print('NO')
