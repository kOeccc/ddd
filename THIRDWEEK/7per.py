import math
p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
while i <= k:
    itog = (x * 100 + y) * (100 + p) / 100
    i += 1
    x = int(itog // 100)
    y = int(itog % 100)
print(x, y)
