a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= b:
    (a, b) = (b, a)
if b <= c:
    (b, c) = (c, b)
if c <= a:
    (c, a) = (a, c)
if a <= d and a <= e:
    print('YES')
else:
    print('NO')
