import math


def isPointArea(x, y):
    rx, ry = -1, 1  # координаты центра окр
    r = 2  # размер радиуса
    p = math.sqrt((rx - x)**2 - (ry - y)**2)  # расчет входит ли точка в круг

    return p <= r  # проверка на нахождение точки во всем круге


x = float(input())
y = float(input())
x1 = float(input())
y1 = float(input())
f = math.sqrt((x - x1)**2 - (y - y1)**2)
x3, y3 = -1, 0
print(f)
