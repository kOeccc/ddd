a = float(input())
b = float(input())
c = float(input())
d = (b * b) - (4 * a * c)
if d > 0:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    x1 = int(x1)
    if x1 < x2:
        x1 = x1
    elif x1 > x2:
        (x1, x2) = (x2, x1)
    print(int(x1), int(x2))
elif int(d) == 0:
    x1 = -b / (2 * a)
    print(x1)

