import math
n = float(input())
a = math.floor(n)
b = (n - math.floor(n)) * 100
c = int(b)
print(a, '{0:.0f}'.format(b))
