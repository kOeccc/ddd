a = float(input())
b = float(input())
c = float(input())
d = (b * b) - (4 * a * c)
if d > 0:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    if x1 > x2:
        (x1, x2) = (x2, x1)
    print('2', x1, x2)
elif d == 0:
    x1 = -b / (2 * a)
    print('1', x1)
else:
    print('0')
