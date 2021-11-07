import math


def perm(x1, y1, x2, y2, x3, y3):
    dist1 = math.sqrt((x2 - x1)**2 + (y2 - y1))**2  # ab
    dist2 = math.sqrt((x3 - x1)**2 + (y3 - y1))**2  # ca
    dist3 = math.sqrt((x3 - x2)**2 + (y3 - y2))**2  # bc
    perimetr = dist1 + dist2 + dist3
    return perimetr


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())