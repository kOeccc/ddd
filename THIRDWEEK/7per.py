import math
p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
m = 0
a = 1
itog = x + y / 100
while i <= k:
    a = itog * (1 + p / 100) 
    i += 1
    itog = a
    print(a)
print(a)
