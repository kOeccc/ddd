a = int(input())
b = int(input())
c = int(input())
a1 = int(input())
b1 = int(input())
c1 = int(input())
if a > b:
    (a, b) = (b, a)
if b > c:
    (b, c) = (c, b)
if a > b:
    (a, b) = (b, a)
if a1 > b1:
    (a1, b1) = (b1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if a < c1:
    print('0')
else:
    print((a // a1) * (b // b1) * (c // c1))
