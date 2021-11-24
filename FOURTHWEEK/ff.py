import math
x, y = (float(input()), float(input()))
if(math.sqrt((x + 1) ** 2 + (y - 1) ** 2) <= 2 and
        2 * x + 2 <= y >= -x):
    print('YES')
