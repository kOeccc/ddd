import math


def distance(x1, x2, y1, y2):
    dist1 = (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return dist1


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print('{0:.5f}'.format(distance(x1, x2, y1, y2)))
