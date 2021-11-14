import math


def pifa(x, y, xc, yc, r):
    p = math.sqrt((x - xc)**2 + (y - yc)**2)
    return p


def IsPointInCircle(x, y, xc, yc, r):
    return pifa(x, y, xc, yc, r) <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
