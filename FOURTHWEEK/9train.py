import math


def isPointArea(x, y):  # координаты центра окр
    return upperFunction(x, y) or downFunction(x, y)


def upperFunction(x, y):
    line2 = 2 * x + 2
    p = math.sqrt((x + 1) ** 2 + (y - 1) ** 2)\
        <= 2
    return p and line2 <= y >= -x


def downFunction(x, y):
    line2 = 2 * x + 2
    p = math.sqrt((x + 1) ** 2 + (y - 1) ** 2)\
        >= 2
    return p and line2 >= y <= -x


x = float(input())  # левая верхняя линия = 0,0 и -1, 1 = 0.0
y = float(input())  # правая линия = -1, 0 и 0, 2
if isPointArea(x, y):
    print("YES")
else:
    print('NO')
