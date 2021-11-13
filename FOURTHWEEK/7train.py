import math


def modul4(x):
    return (x * x)**0.5


def IsPointInSquare(x, y):
    return modul4(x) + modul4(y) <= 1\
         and modul4(y) + modul4(x) >= -1


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
